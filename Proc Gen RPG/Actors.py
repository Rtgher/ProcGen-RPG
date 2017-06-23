"""Procedural-Generated Dungeon RPG

Actors.py
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
#import section
from random import choice
from random import randrange as random

#global variables (immutable) declaration:
elements=('none', 'fire', 'water', 'air', 'earth')
race=('Nephilim', 'Dragon', 'Behemoth', 'Demi-God', 'Spirit', 'Chimera', 'Giant', 'Enigma')

#This file contains the 'Actor' class and all of its sub-clases:

class Actor:
    """
    #Actor class for all Actors within the game;
    # Is superclass
    """
    def __init__(self, Name, level) :
        self.Name=Name
        self.level=level
        self.action_list= []
        self.status_list=[]
        self.desc=""
        
    def getLevel(self):
        return self.level
    
    #Get/Change Name
    def getName(self):
        return self.Name
    def changeName(self, Name) :
        self.Name=Name
    
    #Add/Get Attack
    def defAttack(self, Attack) :
        self.Attack=Attack
    def getAttack(self) :
        return self.Attack
    
    #Add/Remove/Get Action:
    def addAction(self, Action):
        self.action_list.append(Action)
    def removeAction(self,Action):
        self.action_list.remove(Action)
    def getAction(self):
        return self.action_list
        
    #Add and get status effect list
    def addStatus(self, status):
        self.status_list.append(status)
    def removeStatus(self, status):
        self.status_list.remove(status)
    def getStatus(self):
        return self.status

    #set and get description
    def setDesc(self, text):
        self.desc=text
    def getDesc(self):
        return self.desc
    
#####END CLASS
        
class Player(Actor):
    """This class represents the player
    It is a subclass of Actor.
    It has the following Attributes, plus those of Actor class: Inventory, Defence, Attack, Position(x,y),
    It has the following Methods, plus those of the Actor class: initInventory ; addInventory; removeInventory;
    printInventory; addAttack;getAttack; addDefence;getDefence; setPosition;getPosition;
    """
    def __init__(self, Name):
        Actor.__init__(self, Name, 0)
        self.Inventory= []
        self.Attack=1
        self.Defence=1
        self.position={'x':0, 'y':0}
        self.desc="You. Yourself, and none other. You, and your keyboard."

        
    #add Inventory and relevant Inventory functions:
    def addInventory(self, item):
        self.Inventory.append(item)
    def removeInventory(self, item):
        self.Inventory.remove(item)
    def getInventory(self):
        return self.Inventory
            
    #Add and get Attack
    def addAttack(self, Attack):
        self.Attack+=Attack
    def getAttack(self):
        return self.Attack
    
    #Add and get Defence
    def addDefence(self,Defence):
        self.Defence+=Defence
    def getDefence(self):
        return self.Defence

    #Add and Get position
    def setPosition(self,x,y):
        self.position['x']=x
        self.position['y']=y
    def getPosition(self):
        return (self.position['x'],self.position['y'])

    #Init and Get Pet
    def setPet(self, pet):
        self.pet=pet
    def Pet(self):
        return self.pet

    
#####END CLASS

class Monster(Actor):
    """This class is for combatants
    It is a subclass of Actor.
    It has the following attributes beside those of Actor:  Attack, Defence, Elemental_aff, Elemental_deff(elements),
    Health
    It has the following extra methods:addAttack/getAttack; addDefence/getDefence; set/find/getElemental_aff; 
    """
    def __init__(self, Name, level, Attack, Defence):
        Actor.__init__(self, Name, level)
        self.Attack=Attack
        self.Defence=Defence
        self.Elemental_def={'fire': 0, 'water': 0, 'air': 0, 'earth':0 }
        self.Health=10
        if random (0,8)%2==0 : self.findElemental_aff(self)

    #Add and get health
    def addHealth(self, amount):
        self.Health+=amount
    def getHealth(self):
        return self.Health

    #Add and get Attack
    def addAttack(self, Attack):
        self.Attack+=Attack
    def getAttack(self):
        return self.Attack
    
    #Add and get Defence
    def addDefence(self,Defence):
        self.Defence+=Defence
    def getDefence(self):
        return self.Defence

    #set and get Elemental affinity
    def findElemental_aff(self):
        self.Elemental_aff=choice(elements)
        if random(0,10) %2==0:
            self.Elemental_aff='none'
    def setElemental_aff(self,element):
        self.Elemental_aff=element
    def getElemental_aff(self):
        return self.Elemental_aff
    
   #Add and Get Elemental Resistance         
    def addElemental_def(self, element, nr):
        self.Elemental_def[element]+=nr
    def getElemental_def(self, element):
        return self.Elemental_def[element]

    #Get a text full of stats
    def getAll(self) :
        text="""Name:{0}
Health:{1}; Attack: {2} ; Defence:{3} ;
Elemental Affinity:{4};
Description:{5}
 """.format(self.getName(), self.getHealth(), self.getAttack(), self.getDefence(), self.getElemental_aff(), self.getDesc())
        return text

#####END CLASS
    
class Pet(Monster):
    """This class is for the player's pet
    Is a subclass of Monster.
    It has the following extra Attributes: Race, Loyalty
    It has the following extra methods: getRace; add/getLoyalty;
    """
    def __init__(self, Name, level, Attack, Defence):
        Monster.__init__(self, Name, level, Attack, Defence)
        self.nickname=self.Name
        self.race=choice(race)
        self.Name=self.race[0].upper+self.race[1:]
        self.Loyalty=10
        self.findElemental_aff(self)
        

    #getRace
    def getRace(self):
        return self.race

    #add/get Loyalty
    def addLoyalty(self, nr):
        self.Loyalty+=nr
    def getLoyalty(self):
        return self.Loyalty

    #get All stats
    def getAll(self) :
        text=Monster.getAll(self)
        text+="""Race:{0}; Loyalty:{1}""".format(self.getRace(),self.getLoyalty())
        return text
    
#####END CLASS
