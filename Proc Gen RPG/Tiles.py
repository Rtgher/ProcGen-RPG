"""Procedural-Generated Dungeon RPG

Tiles.py
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

#This file contains the 'Tile' class and all its sub-classes:

class PlayerTile :
    """This Class holds the player Tile.
    """
    def __init__(self, Icon) :
        self.Graphic=Icon

#####END CLASS
        
class Tile :
    """This class is for game tiles; the equivalent of floors;
    It is a superclass.
    To be used in the map creation.
    It can be passable or not, with the values 'yes' or 'no'
    """
    def __init__(self, passability):
        self.Passability=passability

    #set/get Graphic
    def setGraphic(self, icon):
        self.Graphic=icon
    def getGraphic(self):
        return self.Graphic

    #set/get Description
    def setDesc(self, text):
        self.Desc=text
    def getDesc(self):
        return self.Desc

    #get Pasability
    def passable(self) :
        return self.Passability
    
#####END CLASS

class EventTile(Tile) :
    """This class is used for tiles with special events.
    It is a suclass of Tile.
    It has the following extra attributes:
    It has the following extra Methods:
    """
        
    #set Choices
    def setChoice1(self, text):
        self.Choice1=text
    def getChoice1(self):
        return self.Choice1
    def setChoice2(self,text):
        self.Choice2=text
    def getChoice2(self):
        return self.Choice2
    def setChoice3(self,text):
        self.Choice3=text
    def getChoice3(self):
        return self.Choice3

    #set/get Reward
    def setReward(self, amount):
        self.Reward=amount
    def getReward(self):
        return self.Reward

#####END CLASS
