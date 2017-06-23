"""Procedural-Generated Dungeon RPG

Maps.py
this is a prototype for a procedural-generated dungeon RPG
has bare-minimum graphics
created by rtgher 26/11/2014->
"""
__version__=0.2
__status__="Prototype"
__author__="traghera@gmail.com"

#License
""" The software itself is a free product. Anyone can download and install it on their own machine, without
having to pay anything for it. Anyone can distribute the product and make copies of it as they wish.

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
import Tiles
from time import sleep
from random import choice
from random import randrange


#global variables:
        #Tiles:
player=Tiles.PlayerTile('8')
grass=Tiles.Tile(True)
grass.setGraphic('"')
wall=Tiles.Tile(False)
wall.setGraphic('[]')
water=Tiles.Tile(False)
water.setGraphic('~')
road=Tiles.Tile(True)
road.setGraphic('::')
start=Tiles.EventTile(True)
start.setGraphic('E')
end=Tiles.EventTile(False)
end.setGraphic('|=|')
tree=Tiles.Tile(False)
tree.setGraphic(chr(134))
grate=Tiles.Tile(False)
grate.setGraphic('#')
event=Tiles.EventTile(False)
event.setGraphic('$')

class Maps :
    """This class contains the Map Generation tools.
    It creates a 'map' on init.
    It has a grid[size][size] in it.
    """

    def __init__(self, Name, size) :
        self.grid=[ (['.'] * size) for i in range(size) ]
        self.size=size
        event_nr=size- randrange(2, size//1.50)
        self.event_list=[]
        for i in range(0, event_nr) :
            self.event_list.append(event)

    def getSize(self) :
        return self.size

   
    
#####END Function
    def Find(self, tile) :
        """This function returns the grid position of the first occurence of 'tile' on the grid.
        Return is a touple.
        """
        for i in range (self.getSize()-1) :
            for j in range(self.getSize()-1) :
                if self.grid[i][j]==tile :
                    return (i,j)
            
#####End Function
            
    def Near(self, pos) :
        """This function returns a list of tiles around the
    specified tile (by grid position).
    It takes a touple (i,j) as argument.
    """
        tiles=[]
        #set rowstart
        if pos[0]>0 : rowstart=pos[0]-1
        else : rowstart=pos[0]
        
        #set rowend
        if pos[0]== self.getSize()-1 : rowend=pos[0]
        else : rowend=pos[0]+1
        
        #set colstart
        if pos[1]>0 : colstart=pos[1]-1
        else : colstart=pos[1]
        
        #set colend
        if pos[1]< self.getSize()-1 : colend=pos[1]+1
        else : colend=pos[1]

        for i in range(rowstart, rowend+1) :
            for j in range(colstart, colend+1) :
                if (i,j) != pos : tiles.append(self.grid[i][j])

        
        return tiles

#####END Function

    def Towards(self, y, x, desy, desx) :
        """This function moves towards the destination from the starting (y,x).
    This function takes 4 arguments: the two coordonates of the starting pos, and those of the dest.
    returns a touple of two coordonates.
    """
        sy=y
        sx=x
        
        nr=randrange(10)
        while (sy,sx)==(y,x) :
            
            if nr %2==0 :
               #mod y
                if y<desy : y+=1
                elif y>desy :  y-=1
                else :
                    y=y
                    nr+=1
            else :
                #mod x
                if x<desx: x+=1
                elif x>desx: x-=1
                else :
                    x=x
                    nr+=1
                    
            nexttile=(y,x)
        
        return nexttile

#####End Function
    
    def DistTo(self, y, x, desy, desx) :
        """This recursive function returns the distance from the target x,y obj to the
    desy,desx object on the grid using the Near function.
    It returns an integer of type int.
    """
        switch=True
        distance=0
        while switch :
            if self.grid[desy][desx] in self.Near((y,x)) :
                switch= False
                return distance+1
            else :
                #mod y
                if y<desy: y+=1
                elif y>desy: y-=1
                else : y=y
                #mod x
                if x<desx: x+=1
                elif x>desx: x-=1
                else : x=x
                distance+=1
                
                if distance>1000 :
                    print(" Invalid Distance.")
                    return -1
                    
            
        
            

#####END Function
    
    def CountTIle(self, y,x ,tile):
        """This function counts how many tiles of type 'tile'
    there are near the tile on the .grid[y][x] position.
    """
        count=0
        pos=(y,x)
        near=Near(pos)
        for each in near :
            if each==tile : count+=1

        return count
    
#####END Function

    def Fill(self, tile, *pos) :
        """This function fills the selected range on the grid with the specified tile.
        It takes a tile, and a list of 4 row/column positions as arguments.
        """
    
        #return if invalid
        if len(pos)==0 :
            print("Invalid row/column declaration")
            return
    
        if pos[0]==pos[1] :
            i= pos[0]
            for j in range(pos[2],pos[3]+1) :
                self.grid[i][j]=tile
        else:
            for i in range(pos[0],pos[1]+1) :
                if pos[2]==pos[3] :
                    j=pos[2]
                    self.grid[i][j]=tile
                else:
                    for j in range(pos[2],pos[3]+1) :
                        self.grid[i][j]=tile

#####End Function

    def PathTo(self, tile, y,x ,end_y, end_x) :
        """This function creates a path from coordonates y,x to end_y, end_x.
    It takes 5 arguments, mainly the tile to fill in and the pairs of coordonates between the two points.
    """
        #actual pathwaycreate loop
        while y!=end_y or x!=end_x :
            nexttile=self.Towards(y,x,end_y,end_x)
            y=nexttile[0]
            x=nexttile[1]
            if self.grid[y][x] not in [start, end, event]:
                self.grid[y][x]=tile

#####End Function
                
    def tieEvent(self, y, x, path) :
        """This function creates a path from an event to the main 'road'
    """
        pathtile=choice(path)
        size=self.getSize()
        spec_tile= [start, end, event]
        
        sy=randrange(0, size) 
        sx=randrange(0, size) 
        while self.grid[sy][sx] not in path or self.grid[sy][sx] in spec_tile :
            sy=randrange(0, size) 
            sx=randrange(0, size)
        self.PathTo(pathtile,  sy,sx, y, x)

        #Debug
        print("Event path created.")
        

            
######End Function                    

    def Create(self, kind) :
        """This function randomly generates the actual map.
    It takes a kind attribute deffining what tileset it is.
    """
        global event
        size=self.getSize()
        #init kind list and kind
        kinds=['forrest','dungeon','cave', 'village','other']
        if kind not in kinds: kind='other'
        self.kind=kind
        events=[start,end, event]
        if kind=='forrest' :
            barriers=[tree, water]
            path=[grass,road]
        if kind=='dungeon' :
            barriers=[wall,grate]
            path=[grass,road]
        if kind=='other' :
            barriers=[tree,water,grate,wall]
            path=[grass,road]

        #fill borders
        self.Fill(barriers[0], 0, 0, 0, size-1)
        self.Fill(barriers[0], size-1, 0, 0, 0)
        self.Fill(barriers[0], size-1, size-1, 0, size-1)
        self.Fill(barriers[0], size-1, 0, size-1, size-1)

        #set entrance
        entrance_y= choice([0,size-1])
        entrance_x= size- randrange(1,size)
        self.grid[entrance_y][entrance_x]=start

        #debug
        print("Entrance set.")
        
        #set exit
        
        for y in range(size) :
            x=randrange(0,size-2)
            if self.DistTo(y, x, entrance_y, entrance_x) > self.getSize()//1.5:
                self.grid[y][x]= end
                end_y=y
                end_x=x
                break

        #debug
        print("Exit set.")

        #set special tiles list
        spec_tiles=[start, end, event]

        #create first pathway towards exit.
        pathtile=choice(path)
        y=entrance_y
        x=entrance_x
        #actual pathwaycreate loop
        self.PathTo(pathtile, y,x, end_y, end_x)

        #debug
        print("Exit pathway created.")
        print("There are ", len(self.event_list),"events.")
        

        #add events
        for event in self.event_list :
            y=randrange(1,size-1)
            x=randrange(1,size-1)
            count=0
            while self.grid[y][x] in spec_tiles :
                y=randrange(1,size-1)
                x=randrange(1,size-1)
                
            
            self.grid[y][x]=event
            indexy=y
            indexx=x

            #debug
            print("Event Created")
            self.tieEvent(y,x,path)
            
                                    
        #debug
        print("Added events.")

        #fill rest of map;
        size=self.getSize()
        for i in range (0, size) :
            tile=choice(barriers)
            for j in range(0, size) :
                ij=self.grid[i][j]
                if (ij not in spec_tiles) and (ij not in barriers) and (ij not in path) : self.grid[i][j]=tile
                
        #debug
        print("Map Created.")
            
#####End Function

        
                        
            
        

    
