import random

CELLS = [(0,0),(0,1),(0,2),(0,3),(0,4),
         (1,0),(1,1),(1,2),(1,3),(1,4),
         (2,0),(2,1),(2,2),(2,3),(2,4),
         (3,0),(3,1),(3,2),(3,3),(3,4),
         (4,0),(4,1),(4,2),(4,3),(4,4),]


def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or door == start or monster == start:
        return get_locations()

    # monster = random
    # door = random
    # start = random

    #if monster, door, or start are the same, do it again

    #return monster door start
    return monster, door, start

def move_player(player,move):
    #get player's current location
    x,y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    #if move is LEFT, y - 1
    #if move is RIGHT, y + 1
    #if move is UP, x -1
    #if move is DOWN, x + 1
    return x,y

def get_moves(player):
    moves = ['LEFT','RIGHT','UP','DOWN']
    # player = (x,y)


    # if player's y in 0, remove LEFT
    # if player's x in 0, remove UP
    # if player's y in 4, remove RIGHT
    # if player's x in 4, remove DOWN

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 4:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 4:
        moves.remove('DOWN')


    return moves

monster, door, player = get_locations()

while True:
    moves = get_moves(player)
    print "Welcome to the dungeon!"
    print "You're currently in room {}".format(player)
    print 'You can move {}'.format(moves)
    print 'Enter QUIT to quit'

    move = raw_input('> ')
    move = move.upper()

    if move =='QUIT':
        break

    if move in moves:
        player = move_player(player,move)
    else:
        print "** Walls are hard stop walking into them! **"
        continue

    if player == door:
        print 'You Escaped!'
        break
    elif player == monster:
        print 'You were eaten by the GRU!'
        break
