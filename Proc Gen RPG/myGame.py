"""Procedural-Generated Dungeon RPG

mygame.py
this is a prototype for a procedural-generated dungeon RPG
has bare-minimum graphics
created by rtgher 26/11/2014->
"""
__version__=0.2
__status__="Prototype"
__author__="traghera@gmail.com"

#License
""" The software itself is a free product. Anyone can download and install it on their own machine, without
having to pay anything for it. Anyone can dustribute the product and make copies of it as they wish.

    The source code is available for view to anyone, wheter it is an individual or corporation.
    Anyone can distribute and post the source code on the internet or classrooms.
    Anyone can modify the source code as they will however:
       #Credit must be given to the original author;
       #Any software that uses this source code, or any modified verion of this source code must
       be made available for free unrestricted download, unless if otherwise specified by the author.
       #Any software that uses this source code, or any portions of it cannot be used in comercial products
       except with the aproval of the author. (contact on e-mail).
    Anyone can buy rights to use the source code in any commercial products by messaging the author;
"""

#Import section
import Actors
import Actions 
from time import sleep
from random import randrange

from TextHandler import getResponse
from TextHandler import searchLine
from TextHandler import completeLine
from TextHandler import renameMonster

#Globals Variable
player=None

#Globals Fixed
elements=('none', 'fire', 'water', 'air', 'earth')


#####END FUNCTION

#DrawElement function
def drawElement(item) :
    """This function draws an ASCII image on the screen.
    May be upgraded to proper graphics eventually.
    It takes one item as an optional argument, and draws it.
    It prints an image.
    """
    #Door
    if item == 'door' :
        text="""
..................____................
.................|   ,|................
.................|___.|................"""

    print(text)

#####END FUNCTION
           
def analiseResponse(*objs) :
    """This function analises the player's input.
    It prints out a message of what the player is doing.
    It analizes the input through searchLine().
    It may take a list of objs as an argument, to pass it on.
    It returns a dictionary obj.
    """
    objs=tuple(objs) #delete if buggs normal start_game
    dic=searchLine(objs)
    line="You "
    line+=dic['action']+" "
    if dic['action'] in ['move', 'cast', 'use', 'open'] : line+=completeLine(dic)
    if dic['action']=='show':
        if dic['object']=='inventory': print(player.getInventory())
        elif dic['object']=='action' : print(player.getAction())
        elif dic['object']=='status' : print(player.getStatus())
        elif dic['object']=='pet' : print(player.Pet().getAll())
        else : print("Cannot show that.")
    if line!="You " :
        print(line)
    
    return dic

#####END FUNCTION
    
#newGame Function
def startGame() :
    """This function starts a new game.
    It generates a new character;
    It resets all attributes/actions/statuses...etc...
    It controlls most other functions.
    """
    #Intro
    print("You are alone.")
    input("...")
    print("You are in something that looks like a room... or a mirror... or a lake...\
It does not matter. All you have now is your keyboard. You can see no limit, no end... no purpouse. \n \
Silence... Deafening silence... ")
    sleep(1)
    print("...but it breaks by the sound of a voice: ")
    print(" 'Hey, you!' ")
    sleep(2)
    print(" 'Yeah, you!' ")
    input("Type something: ")
    print(" 'Hah! Glad you can speak!' ...", end=" ")
    sleep(2)
    print("... 'You have no ideea what's going on, do you...?' ")
    input("Yes/No? ")
    print(" 'Doesn't really matter anyway... ", end=" ")
    sleep(1)
    print("... and to tell the truth I don't really know either. All I know is... ")
    print("You are here.' ")
    input("...")
    print("...")
    Defence=randrange(3,11)
    
    #get Player Name
    print(" 'So, anyway, since you are going to be here a while, what's your name?' :")
    name=input("My name is: ")
    while len(name)<2 :name=input(" 'C'moon, I know you can remember!' : ")
    name=name[0].upper()+name[1:]
    print(" 'Ah, so your name is {0}, is it? \n Very well then.' ".format(name))
    #Create player
    global player
    player= Actors.Player(name)
    
    #enter through door.
    print(" 'Ah, look, something is happening!' ")
    sleep(1)
    drawElement('door')
    print(" 'Look! It looks like a door!' ....")
    print(" ''Well, don't just stand there! Open it!' ")
    while not getResponse("Open") : print("You cannot do that here. \n All you can see is the door.")
    print("You open the door.")
    sleep(2)

    #box handle
    print(" You enter a poorly lit room. You find yourself shrouded in pitch-black darkness.\n... \
Right in the middle of the room you see a small, jewel-box like object. You are too far from it to make out exactly \
what it is. \nThe light in the room is way too dark to make out anything but the table in the apparent middle. ")
    moved=False
    while not moved :
        playeraction=analiseResponse('table','box','center','jewel-box', 'it')
        if playeraction['action']!='move' : print ("You can't do that in this darkness\.\n\
It might be best to move to the table. ")
        else :
           if playeraction['object']== 'X' :
               print("You can't see anything but the table with the box.\n")
           else : moved=True
    print(" As you near the table it becomes obvious that the item on the table is not a box. \
Actually, it looks more like a well. Or a hole. Deep. Dark. You are intrigued by it.")
    sleep(1)
    print(" You think you may be able to 'open' it somehow by touching it? ")
    playeraction=analiseResponse('box', 'hole', 'jewel-box', 'well', 'it')
    while not playeraction['action'] in ['open', 'touch', 'use'] :
        print("You can fool around all you want, but I'd open the box. ")
        playeraction=analiseResponse('box', 'hole', 'jewel-box', 'well', 'it')
    while not (playeraction['object'] in ['box', 'hole', 'jewel-box', 'well'] and playeraction['action'] in ['open', 'touch', 'use']):
        print("The box!... or hole... or jewel-box thinggye... let's just call it a well! ")
        playeraction=analiseResponse('box', 'hole', 'jewel-box', 'well', 'it')
    print(" All of a sudden the part you were touching the thing with starts morphing. It changes shape. \
You see it spiralling out into a vortex. The whole room spins with it. You are getting sucked in the well.\n \
You blank out.")
    input("...")

    #pet gain
    print("...")
    sleep(1)
    Attack=randrange(3,11)
    print(" Darkness. ")
    sleep(1)
    print("The room you wake up in is dark. Too dark. You cannot see anything. And what's worse, you\
feel that you are not alone in this room.")
    sleep(1)
    print("Growls... low, humming, growls... or are they spoken words?... In any case...")
    print("You are not alone.")
    sleep(1)
    print("You can feel something behind you. Your senses tell you to turn around.")
    times=0
    while not getResponse('turn around') and times<6:
        print("There is no such thing. You can only turn around.")
        times+=1
    print("Fear or not, you are doing this. You turn around to find...")
    #create pet
    sleep(1)
    pet=Actors.Pet('Unnamed', 1, Attack, Defence )
    player.setPet(pet)
    player.Pet().findElemental_aff()
    print("... a {0}".format(player.Pet().getRace() ))
    #get desc: #######
    print("... And somehow it seems friendly.")
    print(" 'Ah! There you are! I lost you there for a second when you went in through that door!.\
Hmm? What's this?...\n Oh! You got yourself a pet! I think it likes you... kinda.' ")
    sleep(1)
    print("The creature looks at you. It looks... happy?")
    sleep(1)
    #showstats
    print(" 'Anyway, I think It can fight! Try to see its stats! You can still type, right? Try typing 'show pet'. ' ")
    playeraction=analiseResponse()
    while playeraction['action'] != 'show' and playeraction['object']!= 'pet' : playeraction=analiseResponse()
    print(" 'I was right! See? It has an attack and a defence stat!... But it doesn't have a name yet.' ")
    sleep(1)
    print(" 'Well, don't just stand there, name your pet!' ")
    name=input("His name will be: ")
    while len(name)<2 : name=input(" Nah, I don't think that will work... \nHis name will be: ")
    name=name.capitalize()
    player.Pet().changeName(name)
    renameMonster(player.Pet())
    print(" 'Good job! Now we can go and explore! Oh, by the way, whenever you go into a room I can't see you, \
or any progress you may have made. Try not to break your keyboard where I can't see you!' ")
    print(" 'See you soon!' ")
    input("...")
    print("You fall.")
    new_map=Maps(first, 10)
    new_map.Create()
    for i in range (0, 10) :
        for j in range(0, 10) :
            print(new_map.grid[i][j], end="")
        print("\n")
    input("This is the map.")
             
               
startGame()            
        


    



    
    
    
    
    
