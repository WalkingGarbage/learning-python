import pygame
import os
import random

pygame.init()

print(os.getcwd())

sfondo1 = pygame.image.load('sfondo (2).png')
lancilrutto = pygame.image.load('lancilrutto (1).png')
lancilrutto2 = pygame.image.load('lancilrutto (2).png')
base1 = pygame.image.load('grass.png')
albero = pygame.image.load('albero.png')
SCHERMO = pygame.display.set_mode((1024,550))
mago = pygame.image.load('wizard_tower.png')
golem = pygame.image.load('golem.png')
goblin = pygame.image.load('goblin-door.png')
alfredo = pygame.image.load('alfredo.png')
grotta = pygame.image.load('grotta.png')
baseb = pygame.image.load('bg.png')
sasso = pygame.image.load('GrassLand_Stone_3.png')
finale1 = pygame.image.load('gameover-goblins.png')
finale3 = pygame.image.load('gameover-golem.png')
finale2 = pygame.image.load('win.png')

sfondo = sfondo1
base = base1

FONT_s = pygame.font.SysFont('Source Code Pro', 30, bold = True)
FONT = pygame.font.SysFont('Source Code Pro', 40, bold = True)
scritta = FONT.render('PRESS "F" TO INTERACT', 1, (255,0,0))

personaggi = [ [mago,[5000,210]] , [goblin,[100000,370]], [alfredo,[110000,450]], [golem,[205000,360]] ]
minigioco = False

dettagli = albero


############################################################carta forbice sasso
### 0=rock
### 1=scissors
### 2=paper
from random import randint
def check(x):
    
    if x==0:
        print("rock")
    elif x==1:
        print("scissors")
    elif x==2:
        print("paper")   
def rps():
    p=0
    o=0
    print(f'''
                 _                                         _                    
                | |                                       (_)                   
  _ __ ___   ___| | ___ __   __ _ _ __   ___ _ __ ___  ___ _ ___ ___  ___  _ __ 
 | '__/ _ \ / __| |/ | '_ \ / _` | '_ \ / _ | '__/ __|/ __| / __/ __|/ _ \| '__|
 | | | (_) | (__|   <| |_) | (_| | |_) |  __| |  \__ | (__| \__ \__ | (_) | |   
 |_|  \___/ \___|_|\_| .__/ \__,_| .__/ \___|_|  |___/\___|_|___|___/\___/|_|   
                     | |         | |                                            
                     |_|         |_|                                            ''')
    print("""\nAt the end of the cave there is a goblin to protect the exit.
It will only let you pass if you beat it at rock, scissors and paper
    
    0 = rock
    1 = scissors
    2 = paper
    """)
    while (p<2 and o<2):
        a=int(input("Your move:"))
        check(a)
        b=randint(0,2)
        print("Opponent:")
        check(b)
        if (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
            print("You Won!\n")
            p=p+1
        elif a==b:
            print("Spare!\n")
        elif (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1):
            print("You Lost!\n")
            o=o+1
    if p>=2:
        print("GOBLIN:  I'm no match against you!")
        input('press enter to continue')
        return True
    else:
        print("GOBLIN:  Wohoo! I'm the best!")
        input('press enter to continue')
        return False
    
#########################################################impiccato###################################################################


    
from string import ascii_lowercase
def hm(parola):
    global vuota_l
    global parola_l
    parola_l = [lettera for lettera in parola]
    vuota_l = ['_']* len(parola)
    #print (parola)
    #print (vuota_l)
    if corpo_hm(parola):
        return True
    else: return False
    
    
            
    
def hangman():
    global vinto
    global perso
    print(f'''
  __    __       __      _____  ___    _______   ___      ___       __      _____  ___   
 /" |  | "\     /""\    (\"   \|"   \  /" _   "| |"  \    /"  |     /""\    (\"   \|"   \  
(:  (__)  :)   /    \   |.\    \    |(: ( \___)  \   \  //   |    /    \   |.\    \    | 
 \/      \/   /' /\  \  |: \.   \   | \/ \       /\   \/.    |   /' /\  \  |: \.   \   | 
 //  __   \  //  __'  \ |.  \    \. | //  \ ___ |: \.        |  //  __'  \ |.  \    \. | 
(:  (  )  :)/   /  \   \|    \    \ |(:   _(  _||.  \    /:  | /   /  \   \|    \    \ | 
 \__|  |__/(___/    \___)\___|\____\) \_______) |___|\__/|___|(___/    \___)\___|\____\) 
                                                                                         ''')
    print('\n\n\nFinally, arrived at the last challenge \nthe knight must solve the hangman proposed by the protector of the elixir,\nwhich is a huge Golem, \nif not you will be eliminated')
    vinto = False
    perso = False
    parole = ['python', 'techcamp', 'elisir', 'champion', 'adventure', 'python', 'techcamp', 'elisir', 'champion', 'adventure', 'lancilrutto']
    parola = random.choice(parole)
    if hm(parola):
        return True
    else: return False

    
    
def corpo_hm(parola):
    punti = 0
    errori = 0
    while (not vinto) and (not perso):
        vuota = ' '.join(vuota_l)
        print(vuota)
        scelta = (input('insert a letter ')).lower()
        if scelta in set(ascii_lowercase) - {' '}:
            x=0
            for lettera1 in parola_l:
                x+=1
                #print(lettera1)
                if scelta == lettera1:
                    #print('yes')
                    vuota_l[x-1] = scelta.upper()
                    punti += 1
            if scelta not in parola_l:
                errori+=1
            if errori == 0:
                 print (''' \n\n\n\n\n\n''')
            if errori == 1:
                print ('''          

                                    
                                    
                                    
                                    
                                ------------''')
            if errori == 7:
                print ('''
                                   ________
                                    |   |
                                    |   \\0 
                                    |  /[]\\ 
                                    |   ll 
                                    |
                                ------------''')
                print('you lost, the word was'+ parola)
                input('press enter to continue')
                return False
                

            if errori == 2:
                print ('''         
                                    |  
                                    |  
                                    |  
                                    |   
                                    |
                                ------------''')
            if errori == 3:
                print ('''
                                   ________
                                    |  
                                    |  
                                    |  
                                    |   
                                    |
                                ------------''')
            if errori == 4:
                print ('''
                                   ________
                                    |   | 
                                    |   \ 
                                    |  
                                    |   
                                    |
                                ------------''')
            if errori == 5:
                print ('''      
                                   ________
                                    |   | 
                                    |   \\0
                                    |  
                                    |   
                                    |
                                ------------''')
            if errori == 6:
                print ('''
                                   ________            
                                    |   |              
                                    |   \\0              
                                    |  /[]\\                           
                                    |                       
                                    |                                 
                                ------------''')
                
        else: print('insert a valid letter')

        if punti == len (parola_l):
            print('you won')
            input('press enter to continue')
            return True
            

        
        
############################################enigma##################################################################################


        
def riddle(q,w1,w2,w3,p):
    print(f'''
    ____  _     __    ____   
   / __ \(_)___/ /___/ / /__ 
  / /_/ / / __  / __  / / _ \.
 / _, _/ / /_/ / /_/ / /  __/ 
/_/ |_/_/\__,_/\__,_/_/\___/ 
                             ''')
    print('\n\nyou have been kidnapped by Alfredo, an evil unicorn... answer the question correctly and he will free you\n\n')
    win=False
    print(q)
    print('1: '+w1)
    print('2: '+w2)
    print('3: '+w3)
    while(win==False):
        a=int(input("What is the right answer? "))
        if a-1==p:
            print("Oh Yes, I got it right! Maybe I should quit doing the knight and start programming...\n\nYou managed to escape and returned to the crossroads")
            input('press enter to continue')
            win=True
        else:
            print("I don't think that's the right answer, maybe I should think again...")


            
###############################àTRISSSSSS#######################################################################################


            
def drawBoard(board): 
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if not (letter == 'X' or letter == 'O'):
            print("Please type X or O(letter)!")

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Don Chosciotte'
    else:
        return 'Don Chosciotte'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('I think thats enough... Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Mumble muble... what should I do next? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def tris():
    print(f'''
___________.__             __                      __                 
\__    ___/|__| ____     _/  |______    ____     _/  |_  ____   ____  
  |    |   |  |/ ___\    \   __\__  \ _/ ___\    \   __\/  _ \_/ __ \ 
  |    |   |  \  \___     |  |  / __ \|  \___     |  | (  <_> )  ___/ 
  |____|   |__|\___  >    |__| (____  /\___  >    |__|  \____/ \___  >
                   \/               \/     \/                      \/ ''')
    print('Chosciotte reaches the wizard to ask him some informations. \nHowever he will give you the information, only if you win to a tic tac toe match!')
    print("""
     7 | 8 | 9
    -----------
     4 | 5 | 6
    -----------
     1 | 2 | 3
     """)
    loss=0
    win=False
    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print(turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'Don Chosciotte':
                # Player's turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Oh Yeah! Take that, you useless wizard!\n\nthe magician teleported you to a cave and you are in front of a crossroads\n\n')
                    win=True
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Oh crap! The game is a tie! I shold ask for another chance...')
                        loss=loss+1
                        break
                    else:
                        turn = 'Wizard'

            else:
                # Computer's turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('Oh no, I lost to that stupid wizard! I shold ask for another chance...')
                    loss=loss+1
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Oh crap! The game is a tie! I shold ask for another chance...')
                        loss=loss+1
                        break
                    else:
                        turn = 'Don Chosciotte'

        if loss>=3 or win==True:
            if not playAgain():
                break



            ##################################TRISSSS###############################################################

def rigiocare():
    global minigioco1, minigioco2, passaggio1, passaggio2, posizione, p, sfondo, base, dettagli,h
    scelta = input('\n\ndo you want to play again? (yes/no)')
    if scelta == 'yes':
        minigioco1 = False
        minigioco2 = False
        passaggio1 = False
        passaggio2 = False
        sfondo = sfondo1
        base = base1
        dettagli = albero
        h = 324
        posizione = 0
        p = True
    elif scelta == 'no':
        print('\n\nThanks for playing\n\nWhit love\nDario Malici \nFrancesco Lanza \nIlaria Montanaro \nRiccardo Pasquotti \nTommaso Meucci')
        while True:
            x=0



def fine(n):
    global posizione
    pygame.init()
    SCHERMO = pygame.display.set_mode((1024,550))
    posizione = -15000
    x=0
    while x==0:
        
        SCHERMO.blit(n, (0,0))
        aggiorna()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                x=1
                break
    rigiocare()
    



            
h = 324
k = 0
FPS = 60

class alberi_classe:
    def __init__(self):
        self.x= (random.randint(-40,50)*100)
        self.y= h
        #print(self.x)
    def disegna_e_avanza(self):
        if p:
            self.x -= velx
        SCHERMO.blit(dettagli,(self.x,self.y))
        
def nuovo_albero():
    alberi.append(alberi_classe())

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def genera_alberi():
    for x in range(20):
        nuovo_albero()

def inizializza():
    global lanx, lany, velx, vely
    global basex
    global alberi
    alberi = []
    alberi.append(alberi_classe())
    alberi.append(alberi_classe())
    alberi.append(alberi_classe())
    alberi.append(alberi_classe())
    alberi.append(alberi_classe())
    alberi.append(alberi_classe())
    basex = -100
    lanx = 200
    lany = 420
    velx = 0
    vely = 0

inizio1 = FONT_s.render('''Don Chosciotte is a valorous knight, and is the last descendant ''', 1, (255,0,0))
inizio1bis = FONT_s.render('''of the noble Wessex family''', 1, (255,0,0))
inizio2 = FONT_s.render('His people are dying  for a huge drought that started 1 year before. ', 1, (255,0,0))
inizio2bis = FONT_s.render('Don Chosciotte is watching his people suffering and he can’t handle it anymore', 1, (255,0,0))
inizio3 = FONT_s.render('When he was just a little boy his father told him a story about ', 1, (255,0,0))
inizio3bis = FONT_s.render('a holy elixir, which makes every kind of land fertilized', 1, (255,0,0))
inizio4 = FONT_s.render('So he begins his journey', 1, (255,0,0))


def storia():
    if 100<posizione<900:
        SCHERMO.blit(inizio1, (100,40))
        SCHERMO.blit(inizio1bis, (100,80))
    if 1000<posizione<1900:
        SCHERMO.blit(inizio2, (60,40))
        SCHERMO.blit(inizio2bis, (60,80))
    if 2000<posizione<2900:
        SCHERMO.blit(inizio3, (100,40))
        SCHERMO.blit(inizio3bis, (100,80))
    if 3000<posizione<3900:
        SCHERMO.blit(inizio4,(100,40))
        
def disegna_oggetti():
    global minigioco
    SCHERMO.blit(sfondo, (0,0))
    for albero in alberi:
        albero.disegna_e_avanza()
    
   
    for personaggio in personaggi:
        if -2000<personaggio[1][0]-posizione<2000:
            #print('si')
            #print(personaggio)
            SCHERMO.blit(personaggio[0],(personaggio[1][0]-posizione,personaggio[1][1]))
        if -500< personaggio[1][0] - posizione <700:
            if not 105000<posizione<115000 :
                SCHERMO.blit(scritta, (300,40))
            #print('ciao')
            #print(posizione)
            minigioco = True
    storia()
            
    SCHERMO.blit(base, (basex-100,460))
    if velx >= 0:
        SCHERMO.blit(lancilrutto, (lanx,lany))
    elif velx < 0:
        SCHERMO.blit(lancilrutto2, (lanx,lany)) 
   

    aggiorna()

def verifica_posizione():
    global posizione
    global velx
    global p
    if passaggio1 == True:
        if passaggio2 == True:
            posizione += velx
            p= True
        elif passaggio2 == False:
            if posizione > 99500 or velx > 0:
                posizione += velx
                p = True
            else:
                basex= 0
                p = False
    elif passaggio1 == False:
        if posizione < 5500 or velx<0:
            posizione += velx
            p = True
        else:
            basex = 0
            p = False
    
minigioco1 = False
minigioco2 = False
passaggio1 = False
passaggio2 = False
posizione = 0
p = True

def gioco():
    global velx
    global vely
    global posizione
    global basex
    global lany
    global lanx
    global minigioco1
    global minigioco
    global p
    global alberi
    global SCHERMO
    global passaggio1,passaggio2
    global sfondo
    global grotta
    global minigioco2
    global passaggio2
    global base
    global albero
    global h
    global minigioco2
    global dettagli
    inizializza()
    #print (posizione)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    genera_alberi()
    #for albero in alberi:
     #   print(albero.x)
    
    while True:
        if velx > 30:
            velx -= 2
        elif velx < -30:
            velx += 2
        minigioco = False
        disegna_oggetti()

            
        vely += 15
        for event in pygame.event.get():
            ##print (event)
            if event.type == pygame.KEYDOWN  and  event.key == pygame.K_RIGHT and not (minigioco1 or minigioco2) :
                velx = 30
            if event.type == pygame.KEYUP  and  event.key == pygame.K_RIGHT and not (minigioco1 or minigioco2):
                velx = 0
            if event.type == pygame.KEYUP  and  event.key == pygame.K_LEFT and not (minigioco1 or minigioco2):
                velx = 0
            if event.type == pygame.KEYDOWN  and  event.key == pygame.K_LEFT and not (minigioco1 or minigioco2):
                velx = -30
            if event.type == pygame.KEYDOWN  and  event.key == pygame.K_UP and lany==420:
                vely = -42
                if velx > 0:
                    velx += 16
                elif velx < 0:
                    velx -= 16
            if event.type == pygame.QUIT:
                pygame.quit()
            if minigioco and 105000<posizione<115000:
                pygame.quit()
                minigioco1 = True
                riddle('''If you break me, I’ll not stop working.
If you can touch me, my work is done.
If you lose me, you must find me with a ring soon after.
What am I?''','gold' ,'heart','fame', 1)
                minigioco1= False
                posizione = 105000
                pygame.init()
                SCHERMO = pygame.display.set_mode((1024,550))   
                gioco()
                
            if event.type == pygame.KEYDOWN  and  event.key == pygame.K_f and minigioco:
                pygame.quit()
                if 1000<posizione< 6000:
                    minigioco1 = True
                    tris()
                    passaggio1 = True
                    minigioco1 = False
                    sfondo = grotta
                    posizione += 102000
                    base = baseb
                    dettagli = sasso
                    h= 444
                if 90000<posizione<102000:
                    minigioco2 = True
                    if rps():
                        passaggio2 = True
                        minigioco2 = False
                        sfondo = sfondo1
                        base = base1
                        posizione = 200000
                        h = 470
                    else:
                        fine(finale1)
                    
                if posizione > 200000:
                    minigioco1 = True
                    if hangman():
                        fine(finale2)
                    else:
                        fine(finale3)
                    minigioco1 = False
                    
                
                        
                pygame.init()
                SCHERMO = pygame.display.set_mode((1024,550))   
                gioco()
        if p:
            basex -= velx
            #print (basex)
        if basex < -90 or basex > 90:
            basex = 0
        

        lany += vely
        #print (vely)
        if lany > 420:
            lany = 420
            vely = 0

        
        verifica_posizione()
        
gioco()
