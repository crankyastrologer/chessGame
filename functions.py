from init import *
def askcol1():
    mycolor = colorchooser.askcolor()[1]
    global black
    black = mycolor
def askcol2():
    mycolor = colorchooser.askcolor()[1]
    global white
    white = mycolor

def pawncond(Current, Next, x):
    y = check_piece(Next[0], Next[1])
    if y[1] != x and y[0] != "":
        if abs(Current[0] - Next[0]) == abs(Current[1] - Next[1]) == 1:
            return True
        else: return False
    else: return False


def open_popup():
    top = Toplevel(root)
    top.geometry("750x250")
    top.title("Child Window")
    Label(top, text="Game Ended!", font=('Mistral 18 bold')).place(x=200, y=80)
    button = tk.Button(top, text="close", command=root.destroy)
    button.place(x=375,y=125)


def endgame():
    if len(dicx['ki']) == 0 or len(dicy['ki']) == 0:
        return True
    else:
        return False


def check_collision(a, b):
    Curr = a[0]
    Curr1 = a[1]
    Next = b[0]
    Next1 = b[1]
    if Curr1 == Next1:
        if Curr > Next:
            while Curr > Next:
                Curr = Curr - 1
                x = check_piece(Curr, Curr1)
                if x[0] != "":
                    return False


        elif Curr < Next:
            while Curr < Next:
                Curr = Curr + 1
                x = check_piece(Curr, Curr1)
                if x[0] != "":
                    return False


    elif Curr == Next:
        if Curr1 > Next1:
            while Curr1 > Next1:
                Curr1 = Curr1 - 1
                x = check_piece(Curr, Curr1)
                if x[0] != "":
                    return False


        elif Curr1 < Next1:
            while Curr1 < Next1:
                Curr1 = Curr1 + 1
                x = check_piece(Curr, Curr1)
                if x[0] != "":
                    return False


    else:
        return True
    return True


def check_piece(row, column):
    x = ["", 0]
    for vale in dicx.values():
        for i in vale:
            if i[0] == row and i[1] == column:
                x[0] = get_key(vale)
                x[1] = 0
    for val in dicy.values():
        for i in val:
            if i[0] == row and i[1] == column:
                x[0] = get_key(val)
                x[1] = 1
    return x


def returnImage(row, column):
    x = check_piece(row, column)
    if x[0] != "":
        if x[1] == 0:

            return dica[x[0]]
        else:

            return dicb[x[0]]
    else:
        return dica['t']


def get_key(val):
    for key, value in dicx.items():
        if val == value:
            return key
    for key, value in dicy.items():
        if val == value:
            return key


def remove(a, b, c):
    if c == 0:
        dicx[a].remove(b)
    else:
        dicy[a].remove(b)


def append(a, b, c):
    if c == 0:
        dicx[a].append(b)
    else:
        dicy[a].append(b)


def prin(row, column):
    print(f'{row} {column}')

    x = check_piece(row, column)
    if (x[0] != ""):
        global selected
        selected = [row, column]
        global active_state
        active_state = 1

        check()


def pri(row, column):
    global active_state
    active_state = 0
    global selected
    x = check_piece(selected[0], selected[1])
    global counter
    if x[1] == counter:
        y = check_piece(row, column)
        print(f'asdf{selected}')
        t = False
        a = selected
        z = True
        z = check_collision(a, [row, column])
        print(f'{z}z')
        if x[0] == 'p':

            t = pawnMove(a, [row, column], x[1])
            if (t != True):
                t = pawncond(a, [row, column], x[1])
                print("ye")
            print("ii")
        elif x[0] == "k":
            t = knightMove(selected, [row, column])
            z = True
        elif x[0] == 'b':
            t = bishopMove(selected, [row, column])
        elif x[0] == 'r':
            t = rockMove(selected, [row, column])
        elif x[0] == 'ki':
            t = kingMove(selected, [row, column])
        else:
            t = queenMove(selected, [row, column])

        print(x)
        print(f's{selected}')
        print(f'{t}t')
        ls = [row, column]
        if y[0] == '' and t == z == True:
            remove(x[0], selected, x[1])
            append(x[0], ls, x[1])

            if counter == 1:
                counter = 0
            else:
                counter = 1
        elif t == z == True and y[1] != counter:
            remove(x[0], selected, x[1])
            append(x[0], ls, x[1])

            if y[1] == 0:
                ls = [row, column]
                dicx[y[0]].remove(ls)
            else:
                ls = [row, column]
                dicy[y[0]].remove(ls)
            if counter == 1:
                counter = 0
            else:
                counter = 1

    check()

black = "black"
white = "White"
def check():
    a = endgame()
    if a == False:
        if active_state == 0:
            print("lol")
            for i in range(0, 8):
                for j in range(0, 8):
                    if (i + j) % 2 == 0:
                        color = black
                    else:
                        color = white
                    returnImage(i, j)
                    button = tk.Button(root, width=80, height=80, command=lambda row=i, column=j: prin(row, column),
                                       background=color, image=returnImage(i, j))
                    button.grid(row=i, column=j)
            button1 = tk.Button(root,width=10,height = 1,command=askcol1,text = "color2")
            button1.place(x=700,y=700)
            button2 = tk.Button(root, width=10, height=1, command=askcol2,text="color1")
            button2.place(x=700,y=750)

        else:
            print("jii")
            for i in range(0, 8):
                for j in range(0, 8):
                    if (i + j) % 2 == 0:
                        color = black
                    else:
                        color = white
                    returnImage(i, j)
                    button = tk.Button(root, width=80, height=80, command=lambda row=i, column=j: pri(row, column),
                                       background=color, image=returnImage(i, j))
                    button.grid(row=i, column=j)


    else:
        open_popup()
