import Maps


new_map=Maps.Maps("first", 10)
new_map.Create('forrest')

events=0
for i in range (0, new_map.getSize()) :
    line=""
    for j in range(0, new_map.getSize()) :
        try: line+=new_map.grid[i][j].getGraphic()
        except: line+= new_map.grid[i][j]
    line+=" @endline"
        
    if len(line)<new_map.getSize() : print("Line Length error.", end="")

    print(line)
    
input("This is the map.")



