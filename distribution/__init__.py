import re
import sys
import json

# import bundled chess package
from . import chess
from .chess import svg

settings = {}

def qt_breakpoint():
    from PyQt5.QtCore import pyqtRemoveInputHook
    pyqtRemoveInputHook()
    import pdb
    pdb.set_trace()

def fen2svg(m):
    global config

    # m: re.Match
    fen = m.group(1)
    board = chess.Board()
    board.set_fen(fen)

    cmap = {'square light':config['square_light'], 'square dark':config['square_dark']}
    svg = chess.svg.board(board, orientation=board.turn, size=config['size'], coordinates=config['coordinates'], colors=cmap)
    return f'<!-- FEN:{fen} -->' + svg

def hook(txt, editor):
    # txt: str
    # editor: aqt.editor
    result = re.sub(r'\[FEN\](.*?)\[\/FEN\]', fen2svg, txt, flags=re.IGNORECASE)
    return result

if sys.executable.endswith('anki') or sys.executable.endswith('anki.exe'):
    print('anki_fen_vis: executing from ANKI gui')

    # read config
    from aqt import mw
    config = mw.addonManager.getConfig(__name__)
    print(f'anki_fen_vis: config {config}')

    # set hook
    from aqt import gui_hooks
    gui_hooks.editor_will_munge_html.append(hook)

elif sys.executable.endswith('python'):
    print('anki_fen_vis: executing from command-line')

    # read config
    import os
    import inspect
    this_file = inspect.stack()[0][1]
    this_dir = os.path.dirname(this_file)
    fpath_json = os.path.join(this_dir, "config.json")
    print(f'reading: {fpath_json}')
    with open(fpath_json) as fp:
        config = json.load(fp)
    print(f'config: {config}')

else:
    print('anki_fen_vis: executing ???')

