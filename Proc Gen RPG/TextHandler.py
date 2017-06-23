"""Procedural-Generated Dungeon RPG

textHandler.py
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

#global variables: Fixed
elements=('none', 'fire', 'water', 'air', 'earth')
  
def renameMonster(obj) :
    """This method changes the name of a Monster.
            It takes a Monster obj as argument.
            It returns a modified name string.
    """
    name=''
    if obj.getAttack() < obj.getLevel()*5 - (obj.getLevel()//2) : name='Weak '
    if obj.getAttack() > obj.getLevel()*10-(1+ obj.getLevel()//2): name='Strong '
    if obj.getDefence() < obj.getLevel()*5 - (obj.getLevel()//2) : name='Frail '
    if obj.getDefence() > obj.getLevel()*10- (1+obj.getLevel()//2) : name='Stalwart '
    name+= obj.getName()
    if obj.getElemental_aff() != 'none' : name+=' of {}'.format(obj.getElemental_aff())

    obj.changeName(name)
            
#####End Method
        
#GetResponse function
def getResponse(answ, *line) :
    """This function searches for a specific answer in the string.
        It takes a string argument. It may take another str(line) as an argument.
        It returns a boolean value.
    """
    if not len(line) >0 :
            #input line to search
            line=input("What do you do? : ")
            
    #search line
    if answ.lower() in line : return True
    else : return False
           
#search line function
def searchLine(*objs) :
    """This function searches a line input from the user for keywords.
        It contains lists with keywords.
        It may take a list as an extra argument.
        It returns a dictionary of '3' keywords.
    """
    #keyword lists
    actions=['move', 'use', 'search', 'show', 'cast',  'open', 'touch']
    directions=['up','down','right','left']
    lists=['action', 'inventory', 'status', 'pet']
    trivia=['dance', 'feel', 'maim', 'sing', 'write on', 'creep', 'sneak', 'eat', 'laugh', 'lol' ]
    return_dic={'action' : 'X' ,'direction': 'X' ,'object': 'X' }
    ###
    ##print("Objs is:", objs)
    ###
    #getLine and list
    line=input("What do you do? ")
    line_list=line.split()    

    for word in line_list :
        for action in actions :
            if getResponse(word, action)== True: return_dic['action']=action
        for direction in directions :
            if getResponse(word, direction)== True: return_dic['direction']=direction
        if len(objs)>0 :
            for tpl in objs :
                for obj in tpl :
                    if getResponse(word, obj)==True: return_dic['object']=obj
                
    #set for show            
    if return_dic['action']=='show' :
        for word in line_list :
            for alist in lists :
                if getResponse(word, alist)== True : return_dic['object']=alist
    #set for trivia
    if return_dic['action']=='X' :
        for word in line_list :
            for action in trivia :
                if getResponse(word, action)== True: return_dic['action']=action
    return return_dic
#####END FUNCTION        

def completeLine(dic):
    """This function completes the line from analizeResponse()
        It takes a dic obj as an argument;
        It returns a string.
    """
    line=""
    #for move
    if dic['action']=='move' :
        if dic['direction']=='X' :
                line+="towards the "
                if not dic['object']=='X' :
                    line+=dic['object'] + " "
        else : line+=dic['direction'] + "."
            
    #for cast or use or open
    if dic['action']in ['cast', 'use', 'open'] :
        line+=dic['object'] + "."
            
            
    return line

#####END FUNCTION
        
    
        
