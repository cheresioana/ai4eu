from typing import Optional, List
import os
import logging
import json
import time
import fastapi
import fastapi.templating
import pydantic
import queue
import grpc
import concurrent.futures
import sys
import traceback

sys.path.append('../protobuf/')
import sudoku_gui_pb2_grpc
import sudoku_gui_pb2

logger = logging.getLogger(__name__)
# set logging level in uvicorn!

class FieldSpec(pydantic.BaseModel):

    x: int
    y: int
    content: Optional[int]
    cssclass: Optional[str]

class GUIUpdate(pydantic.BaseModel):

    statusbar: str
    field: List[FieldSpec]


class GRPCRequestDataBroker(sudoku_gui_pb2_grpc.SudokuDesignEvaluationRequestDataBrokerServicer):
    def __init__(self, to_protobuf_queue):
        self.to_protobuf_queue = to_protobuf_queue

    def requestSudokuEvaluation(self, request, context):
        logging.info("requesting sudoku evaluation")

        ret = sudoku_gui_pb2.SudokuDesignEvaluationJob()

        try:
            ret = self.to_protobuf_queue.get(block=True)
        except:
            logging.warning("got exception %s", traceback.format_exc())
            time.sleep(1)
            pass

        return ret

class GRPCResultProcessor(sudoku_gui_pb2_grpc.SudokuDesignEvaluationResultProcessorServicer):
    def __init__(self, to_js_queue):
        self.to_js_queue = to_js_queue

    def processEvaluationResult(self, request, context):
        logging.info("received evaluation result with status %d and solution of size %d", request.status, len(request.solution))

        # pass this to javascript to send it to the GUI
        statusstr = {
            0: 'Sudoku has no solution',
            1: 'Sudoku has a unique solution',
            2: 'Sudoku has multiple solutions'
        }[request.status]
        fields = []
        if request.status in [1,2]:
            for v, xy in zip(request.solution, [ (col,row) for row in range(1,10)  for col in range(1,10)]):
                #logging.info("v %d xy %s", v, xy)
                if v in range(1,10):
                    fields.append(FieldSpec(x=xy[0], y=xy[1], content=v, cssclass='solution'))

        gu = GUIUpdate(statusbar=statusstr, field=fields)
        self.to_js_queue.put(gu)

        # dummy return
        return sudoku_gui_pb2.Empty(empty=0)

field = {}
def reset_field():
    field = {}

def create_app() -> fastapi.FastAPI:

    app = fastapi.FastAPI(title='SudokuGUIServer', debug=True)
    app.logger = logger
    reset_field()
    return app

app = create_app()

configfile = os.environ['CONFIG'] if 'CONFIG' in os.environ else "../config.json"
logging.info("loading config from %s", configfile)
config = json.load(open(configfile, 'rt'))
protobuf_to_js_queue = queue.Queue()
js_to_protobuf_queue = queue.Queue()
templates = fastapi.templating.Jinja2Templates(directory='templates')

grpcserver = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
sudoku_gui_pb2_grpc.add_SudokuDesignEvaluationRequestDataBrokerServicer_to_server(GRPCRequestDataBroker(js_to_protobuf_queue), grpcserver)
sudoku_gui_pb2_grpc.add_SudokuDesignEvaluationResultProcessorServicer_to_server(GRPCResultProcessor(protobuf_to_js_queue), grpcserver)
grpcport = config['gui-grpcport']
grpcserver.add_insecure_port('localhost:'+str(grpcport))
logging.info("starting grpc server at port %d", grpcport)
grpcserver.start()

@app.get('/')
def serve_website(request: fastapi.Request):
    return templates.TemplateResponse("gui.html", { 'request': request }, headers={'Cache-Control': 'no-cache'})

@app.get('/gui.js')
def serve_js(request: fastapi.Request):
    return fastapi.responses.FileResponse("gui.js", headers={'Cache-Control': 'no-cache'})

@app.get('/gui.css')
def serve_css(request: fastapi.Request):
    return fastapi.responses.FileResponse("gui.css", headers={'Cache-Control': 'no-cache'})

@app.put('/reset', response_model=None)
def reset() -> None:
    '''
    Startup the GUI = set all fields to "uninitialized"
    This is a single-user server!
    '''
    reset_field()

@app.put('/user_setcell', response_model=None)
def setcell(x: int, y: int, value: Optional[int] = None) -> None:
    '''
    If the user changes a cell value in the GUI,
    this PUT request is sent.
    '''
    logging.info("user_setcell(%d,%d,%s)", x, y, value)

    # 0-based indexing
    x = x - 1
    y = y - 1
    
    key = (x,y)
    if value is not None:
        field[key] = value
    else:
        if key in field:
            del(field[key])

    # return design evaluation job from requestSudokuEvaluation()
    ret = sudoku_gui_pb2.SudokuDesignEvaluationJob()
    ret.field.extend([ 0 for x in range(0,81) ])

    for k, v in field.items():
        x, y = k
        ret.field[x+9*y] = v

    js_to_protobuf_queue.put(ret)

    return None

@app.get('/wait_update', response_model=Optional[GUIUpdate])
def wait_update(timeout_ms: int):
    '''
    The GUI periodically calls this method to wait for a new
    update to the GUI. Ideally the GUI calls this each <timeout_ms>
    milliseconds.
    '''
    logging.info("wait_update(%d)", timeout_ms)

    ret = None

    try:
        ret = protobuf_to_js_queue.get(block=True, timeout=timeout_ms/1000.0)
    except queue.Empty:
        pass

    logging.info("wait_update returns (%s)", ret)
    return ret
