import os

def check(images):
    file_map={}
    # Get the list of files in the input path
    files = os.listdir(images)
    for filename in files:
        name=filename[:-4]

        if name not in file_map:
            file_map[name]=True
    
    return file_map    


def deletetxt(file_map,labels):

    files = os.listdir(labels)
    for filename in files:
        file_path=os.path.join(labels,filename)
        name=filename[:-4]
        
        if name not in file_map:

            os.remove(file_path)
            print("deleted ",file_path)
images="images"
labels="labels"
file_map=check(images)

deletetxt(file_map,labels)
