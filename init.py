import os
import tkinter as tk
from tkinter import colorchooser
from tkinter import *
from Pieces import *
from tkinter.ttk import *
dicx = {'p': [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]],
        'r': [[0, 0], [7, 0]],
        'k': [[1, 0], [6, 0]],
        'b': [[2, 0], [5, 0]],
        'q': [[3, 0]],
        'ki': [[4, 0]]
        }
dicy = {'p': [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]],
        'r': [[0, 7], [7, 7]],
        'k': [[1, 7], [6, 7]],
        'b': [[2, 7], [5, 7]],
        'ki': [[3, 7]],
        'q': [[4, 7]]

        }
counter = 0
selected = []
active_state = 0

geometry = '640x640'
root = tk.Tk()
queen = PhotoImage(file="Chess_Pieces_golden/queen.png")
queen = queen.subsample(3, 3)
pawn = PhotoImage(file="Chess_Pieces_golden/pawn.png")
pawn = pawn.subsample(4, 4)
knight = PhotoImage(file="Chess_Pieces_golden/knight.png")
knight = knight.subsample(4, 4)
rock = PhotoImage(file="Chess_Pieces_golden/rook.png")
rock = rock.subsample(4, 4)
bishop = PhotoImage(file="Chess_Pieces_golden/bishop.png")
bishop = bishop.subsample(4, 4)
king = PhotoImage(file="Chess_Pieces_golden/king.png")
king = king.subsample(4, 4)
trans = PhotoImage(file="Chess_Pieces_golden/lil.png")
path = "Chess_pieces_Green"
queeng = PhotoImage(file=os.path.join(path,'queen.png'))
queeng = queeng.subsample(3, 3)
pawng = PhotoImage(file=os.path.join(path,"pawn.png"))
pawng = pawng.subsample(4, 4)
knightg = PhotoImage(file=os.path.join(path,"knight.png"))
knightg = knightg.subsample(4, 4)
rockg = PhotoImage(file=os.path.join(path,"rook.png"))
rockg = rockg.subsample(4, 4)
bishopg = PhotoImage(file=os.path.join(path,"bishop.png"))
bishopg = bishopg.subsample(4, 4)
kingg = PhotoImage(file=os.path.join(path,"king.png"))
kingg = kingg.subsample(4, 4)
dica = {
    'q': queen,
    'p': pawn,
    'ki': king,
    'r': rock,
    'k': knight,
    'b': bishop,
    't': trans
}
dicb = {
    'q': queeng,
    'p': pawng,
    'ki': kingg,
    'r': rockg,
    'k': knightg,
    'b': bishopg,
    't': trans
}
