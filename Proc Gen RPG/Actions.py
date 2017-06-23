"""Procedural-Generated Dungeon RPG

Actions.py
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

#This file contains the Action class and all its sub-classes:
class Action:
    """This class is for actions that can be performed by actors
     It is a superclass.
    """
    def __init__(self, Name, cost, element):
        self.Name=Name
        self.cost=cost
        self.element=element
        
    #set/get Description(Desc)
    def setDesc(self, text):
        self.Desc=text
    def getDesc(self):
        return self.Desc

    #getName/getCost/getElement
    def getName(self):
        return self.Name
    def getCost(self):
        return self.cost
    def getElement(self):
        return self.element

#####END CLASS

class Magic(Action):
    """This class is for atk/def magic actions.
    It is a subclass of Actions
    It has these extra Atributes: mtype, amount
    It has these extra methods: cast(self, obj, attribute, amount); 
    """
    def __init__(self, Name, cost, element, mtype, nr):
        Action.__init__(self, Name, cost, element)
        self.mtype=mtype
        self.amount=nr
        
    #Cast method
    def cast(self, obj, attribute, amount, **statuses):
        if self.mtype=='damage' :
            obj.addHealth(-amount)
        if self.mtype=='heal':
            obj.addHealth(amount)
        obj.addStatus(statuses)

#####END CLASS
        
class Status:
    """This class is for statuses.
    It is a class subordinate to Magic, and related to Magic, but does not inherit from it.
    The magic class can add a status to an obj.
    """
    def __init__(self, Name, stype, amount, turn_duration, **Attribute):
        self.Name=Name
        self.stype=stype
        self.amount=amount
        self.turn_duration=turn_duration
        self.Attribute=Attribute

    #Set/Get Desc
    def setDesc(self, text):
        self.Desc=text
    def getDesc(self):
        return self.Desc

    #Get duration
    def getDuration(self):
        return self.turn_duration

    #Execute method
    def Execute(self, obj, attribute):
        if self.mtype=='damage' :
            obj.addHealth(-amount)
        if self.mtype=='heal':
            obj.addHealth(amount)
        if self.mtype=='buff':
            att="add"+self.Attribute
            obj.att(self.amount)
            
#####END CLASS
