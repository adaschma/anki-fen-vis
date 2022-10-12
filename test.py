#!/usr/bin/env python

import sys
sys.path.append('..')
import anki_fen_vis

card_text = 'Hello, this is a test.\nThis is a board with white to move:\n[FEN]2r2rk1/1p1b1pb1/1q1p1n1p/2nPp1pP/p3P1P1/2N1BPN1/PP1QBK2/R6r w - - 0 1[/FEN]\n\nAnd here is another board with black to move:\n[fen]rnbqkb1r/pppp1ppp/5n2/4P3/2P5/8/PP2PPPP/RNBQKBNR b KQkq - 0 3[/fen].\n\nWhat do you think?\n'
card_text = anki_fen_vis.hook(card_text, None)

print(card_text)
#breakpoint()

