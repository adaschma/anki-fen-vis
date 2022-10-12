import re
import sys

# import bundled chess package
from . import chess
from .chess import svg

def qt_breakpoint():
    from PyQt5.QtCore import pyqtRemoveInputHook
    pyqtRemoveInputHook()
    import pdb
    pdb.set_trace()

def fen2svg(m):
    # m: re.Match
    fen = m.group(1)
    board = chess.Board()
    board.set_fen(fen)
    svg = chess.svg.board(board)
    return svg

def hook(txt, editor):
    # txt: str
    # editor: aqt.editor
    result = re.sub(r'\[FEN\](.*?)\[\/FEN\]', fen2svg, txt, flags=re.IGNORECASE)
    return result

if sys.executable.endswith('anki'):
    print('anki_fen_vis: executing from ANKI gui')
    from aqt import gui_hooks
    gui_hooks.editor_will_munge_html.append(hook)
elif sys.executable.endswith('python'):
    print('anki_fen_vis: executing in command-line')
else:
    print('anki_fen_vis: executing ???')

