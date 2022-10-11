import addon

card_text = 'Hello, this is a test.\nThis is a board:\n[FEN]2r2rk1/1p1b1pb1/1q1p1n1p/2nPp1pP/p3P1P1/2N1BPN1/PP1QBK2/R6r w - - 0 1[/FEN]\n\nAnd here is another board:\n[fen]2r2rk1/1p1b1pb1/1q1p1n1p/2nPp1pP/p3P1P1/2N1BPN1/PP1QBK2/R6r w - - 0 1[/fen].\n\nWhat do you think?\n'
card_text = addon.hook(card_text, None)

print(card_text)
#breakpoint()

