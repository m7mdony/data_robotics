import os
import shutil
import random

def remove(file):
    try:
        shutil.rmtree(file)
    except:
        pass
    


remove("test")
remove("valid")
remove("train")

# Set the paths and percentages
images_path = "images"
labels_path = "labels"
output_root = ""

train_percentage=0.5
valid_percentage=0.2
test_percentage=0.3

if 0>train_percentage+test_percentage+valid_percentage or train_percentage+test_percentage+valid_percentage>1:
    print("percenteages are not correct")
else:   
    # Create the main folders
    for folder in ["train", "valid", "test"]:
        os.makedirs(os.path.join(output_root, folder, "images"))
        os.makedirs(os.path.join(output_root, folder, "labels"))

    # Get the list of images and labels
    image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
    label_files = [f for f in os.listdir(labels_path) if os.path.isfile(os.path.join(labels_path, f))]

    # Shuffle the files
    random.shuffle(image_files)
    random.shuffle(label_files)

    # Calculate the split points
    total_images = len(image_files)
    train_split = int(total_images * train_percentage)
    valid_split = int(total_images * valid_percentage)

    trainhash={}
    testhash={}
    validhash={}
    # Copy images to the respective folders
    for i, file in enumerate(image_files):
        source_path = os.path.join(images_path, file)
        if i < train_split:
            destination_path = os.path.join(output_root, "train", "images", file)
            trainhash[file[:-4]]=True
        elif i < train_split + valid_split:
            destination_path = os.path.join(output_root, "valid", "images", file)
            validhash[file[:-4]]=True
        else:
            destination_path = os.path.join(output_root, "test", "images", file)
            testhash[file[:-4]]=True
        shutil.copyfile(source_path, destination_path)
        

    # Copy labels to the respective folders
    for file in label_files:
        source_path = os.path.join(labels_path, file)
        destination_path=""
        if file[:-4] in trainhash:
            destination_path = os.path.join(output_root, "train", "labels", file)
        elif file[:-4] in testhash:
            destination_path = os.path.join(output_root, "test", "labels", file)
        elif file[:-4] in validhash:
            destination_path = os.path.join(output_root, "valid", "labels", file)
        shutil.copyfile(source_path, destination_path)    
        
        
            
