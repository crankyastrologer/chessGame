
def pawnMove(Current, Next,x):
    y = False
    if x==0:
        if (Current[0] - Next[0]) == 0 and (Current[1] - Next[1]) == -1:

            y= True
        elif Current[1]==1 and Current[1]-Next[1]==-2:
            if (Current[0] - Next[0]) == 0:
                y=True
        else:
            print('pawn move')

            y =False
    else:
        if (Current[0] - Next[0]) == 0 and (Current[1] - Next[1]) == 1:

            y= True
        elif Current[1]==6 and Current[1]-Next[1]==2:
            if (Current[0] - Next[0]) == 0:
                y=True
        else:
            print('pawn move')

            y= False
    return y



def kingMove(Current, Next):
    if Next[0] - Current[0] < 2 and Next[1] - Current[1] < 2:
        return True
    else:
        return False


def rockMove(Current, Next):
    if Current[0] - Next[0] == 0:
        return True
    elif Current[1] - Next[1] == 0:
        return True
    else:
        return False


def bishopMove(Current, Next):
    if abs(Current[0] - Next[0] )== abs(Current[1] - Next[1]):
        return True
    else:
        return False


def queenMove(Current, Next):
    if Current[0] - Next[0] == 0:
        return True
    elif Current[1] - Next[1] == 0:
        return True
    elif abs(Current[0] - Next[0]) == abs(Current[1] - Next[1]):
        return True
    else:
        return False


def knightMove(Current, Next):
    if abs(Current[0] - Next[0]) == 2 and abs(Current[1] - Next[1]) == 1:
        return True
    elif abs(Current[0] - Next[0]) == 1 and abs(Current[1] - Next[1]) == 2:
        return True
    else:
        return False
