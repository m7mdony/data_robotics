import os

def change(folder_path):
    files=os.listdir(folder_path)
    
    for txt_file in files:
        filename = os.path.join(folder_path, txt_file)
        text=""
        with open(filename,"r") as file:
            lines=file.readlines()       
            for line in lines:
                line=list(map(float,line.split()))

               
                classname=line[0]
                cords=line[1:]
                
                max_x=float("inf")*-1
                max_y=float("inf")*-1
                min_x=float("inf")
                min_y=float("inf")
                for i in range(0,len(cords)-1,2):
                    max_x=max(max_x,cords[i])
                    min_x=min(min_x,cords[i])
                for i in range(1,len(cords),2):
                    max_y=max(max_y,cords[i])
                    min_y=min(min_y,cords[i])
                x,y=min_x,min_y
                w=max_x-min_x
                h=max_y-min_y   
                text+=str(classname)+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n"   
        with open(filename,"w") as file:
            file.write(text)            


folder_path="labels"

change(folder_path)