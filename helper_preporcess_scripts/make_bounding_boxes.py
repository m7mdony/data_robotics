import os

def change(folder_path):
    files=os.listdir(folder_path)
    
    for txt_file in files:
        filename = os.path.join(folder_path, txt_file)
        text=""
        with open(filename,"r") as file:
            lines=file.readlines()       
            for line in lines:
                line = list(map(float, line.split()))

                classname = int(line[0])  # Assuming class label is an integer
                cords = line[1:]

                min_x = min(cords[0::2])
                min_y = min(cords[1::2])
                max_x = max(cords[0::2])
                max_y = max(cords[1::2])
                w = max_x - min_x
                h = max_y - min_y
                x = min_x+(w/2)
                y = min_y+(h/2)
                
                text+=str(classname)+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n"   
        with open(filename,"w") as file:
            file.write(text)            


folder_path="labels"

change(folder_path)