#Setting up empty wordl for the game and next generation
dim = 15
world = [[0 for i in range(dim)]for j in range(dim)]
newW = [[0 for i in range(dim)]for j in range(dim)]
#Input for starting of the world
start_string = \
'\
OOOOOOOOOOOOOOOn\
OOOXOOOOOOOOOOOn\
OOOOXOOOOOOOOOOn\
OOXXXOOOOOOOOOOn\
OOOOOOOOOOOOOOOn\
OOOOOXOOOXOOOOOn\
OOOOOOOXOOOOOOOn\
OOOOOOXXXOOOOOOn\
OOOOOOOXOOOOOOOn\
OOOOOXOOOOOOOOOn\
OOOOOXOOOOOOOOOn\
OOOOOXOOOOOOOOOn\
OOOOOOOOOOOOOOOn\
OOOOOOOOOOOOOOOn\
OOOOOOOOOOOOOOOn\
'
#option for custom start from text file 
inp = ''
inp = input('Type yes if you have custom start position in a text file (if you enter any differend input starting position will be taken from code): ')
if inp == 'yes':
    inp = input('type in adress of the text file(if this fails start from code will be used):')
    try:
        file = open(inp,"r")
        start_string = file.read()
        file.close()
    except:
        print('file could',inp ,' not be found')
  

#Reading the start
a=0
b=0
for letter in start_string:
    try:
        if letter == 'X' :
            world[b][a] = 1
        elif letter == 'O':
            world[b][a] = 0
        a = a+1
        if letter == 'n':
            a = 0
            b = b+1
    except:
        print('Cell (', a ,',',b,'is out of bounds')

# Function for evolution.
# Implementign all rules of game of life in a way that allways rewrites the whole next generation
def evol(y,x):
    life = 0
    for aa in range(3):
        for bb in range(3):
            if y+bb-1 in range(dim) and x+aa-1 in range(dim):
                if aa != 1 or bb !=1:
                    life = life + world[y+bb-1][x+aa-1]


    if world[y][x] == 0:
            if life == 3:
                newW[y][x] = 1
            else:
                newW[y][x] = 0
    else:
            if life == 2 or life == 3:
                newW[y][x] = 1
            else:
                newW[y][x] = 0

#Generating and printing of the next generation
while(True):
    line = ''
    for i in range(dim):
        for j in range(dim):
            evol(i,j)
            if world[i][j] == 1:
                line = line + 'X'
            else:
                line = line + ' '
        print(line)
        line = ''
    world = newW
    newW = [[0 for i in range(dim)]for j in range(dim)]

    inp = ''
    inp = input('Type "end" to end the game:')
    if inp == 'end':
        break

