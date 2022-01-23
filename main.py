import random


def grid_const(position):
    grid_fn = f" {position[0]} | {position[1]} | {position[2]} \n" \
           "____________\n" \
           f" {position[3]} | {position[4]} | {position[5]} \n" \
           "____________\n" \
           f" {position[6]} | {position[7]} | {position[8]} \n"
    return grid_fn


def check_index():
    user = []
    pc = []
    i = 0
    t = 0
    for item in pos:
        if item == x:
            user.append(pos.index(x, i, 10))
        elif item == o:
            pc.append(pos.index(o, t, 10))
        i += 1
        t += 1
    win_chek(user, pc)


def win_chek(user, pc):
    global game_on
    if (user == [0, 1, 2]) or (user == [3, 4, 5]) or (user == [6, 7, 8]) or (user == [0, 3, 6]) or (user == [1, 4, 7]) \
            or (user == [2, 5, 8]) or (user == [2, 4, 6]) or (user == [0, 4, 8]):
        print("The winner is User")
        game_on = False
    elif (pc == [0, 1, 2]) or (pc == [3, 4, 5]) or (pc == [6, 7, 8]) or (pc == [0, 3, 6]) or (pc == [1, 4, 7]) \
            or (pc == [2, 5, 8]) or (pc == [2, 4, 6]) or (pc == [0, 4, 8]):
        print("The winner is User")
        game_on = False


x = "❌"
o = "⭕"

pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print("Welcome to Tic Tac Toe Game")
grid = grid_const(pos)
print(grid)

game_on = True
while game_on:
    user_choice = int(input("Choose position by number: "))
    if user_choice > 8 or user_choice < 0:
        print("The position you entered is out of range")
    else:
        if user_choice in options:
            pos[user_choice] = x
            options.remove(user_choice)
            if len(options) != 0:
                pc_choice = random.choice(options)
                pos[pc_choice] = o
                options.remove(pc_choice)
                grid = grid_const(pos)
                print(grid)
                check_index()
            else:
                grid = grid_const(pos)
                print(grid)
                print("Game Over! it was a draw!")
                game_on = False
        else:
            print("the position you entered is already occupied")
