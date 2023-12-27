import cv2
import numpy as np
import os
def draw_annotations(image_path, annotation_file, current_index, image_file, total, display_scale=0.5):
    end = False

    # Load the image
    image = cv2.imread(image_path)
    print(image_path)
    # Resize the image for display
    display_height = int(image.shape[0] * display_scale)
    display_width = int(image.shape[1] * display_scale)
    resized_image = cv2.resize(image, (display_width, display_height))

    # Read annotations from the file
    try:
        with open(annotation_file, 'r') as file:
            annotations_list = [list(map(float, line.split())) for line in file]
    except Exception as e:
        print(f"Error reading annotations from file: {e}")
        return

    # Iterate through each set of annotations
    for annotations in annotations_list:
        try:
            for i in range(1, len(annotations)-3, 2):
                start_x = int(annotations[i] * display_width)
                start_y = int(annotations[i + 1] * display_height)
                end_x = int(annotations[i + 2] * display_width)
                end_y = int(annotations[i + 3] * display_height)
                cv2.line(resized_image, (start_x, start_y), (end_x, end_y), color=(0, 255, 0), thickness=2)

            with open("save.txt", "w") as file:
                file.write(image_file)
        except Exception as e:
            print(f"Error processing annotations: {e}")

    # Display the resized image
    print(image_path, "current index ", current_index, "/", total)
    cv2.imshow('Annotated Image', resized_image)
    key = cv2.waitKey(0)

    # Check if the user pressed 'q' to stop
    if key == ord('q'):
        cv2.destroyAllWindows()
        exit()
    # Check if the user wants to delete the image
    elif key == ord('d'):
        # Delete both the image and annotation file
        os.remove(image_path)
        os.remove(annotation_file)
        print(f"Image and annotation deleted: {image_path}")
        cv2.destroyAllWindows()
        return 'next'  # Continue to the next image
    elif key == ord('b'):
        cv2.destroyAllWindows()
        return 'prev'  # Go back to the previous image
    else:
        return 'next'  # Continue to the next image

# Example usage
images_path="images"
labels_path="labels"
def displayer(images_path, labels_path):
    # Get a list of all image files in the images_path directory
    image_files = [f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    current_index=0
    # with open("save.txt","r")as file:
    #     for line in file:
    #         image_name=line
    # while current_index<len(image_files):
    #     image_file = image_files[current_index]
    #     if image_file==image_name:
    #         break
    #     current_index+=1
        

    while current_index < len(image_files):
        # Construct the full path to the image and its corresponding annotation file
        image_file = image_files[current_index]
        image_path = os.path.join(images_path, image_file)
        annotation_file = os.path.join(labels_path, f"{os.path.splitext(image_file)[0]}.txt")

        # Call draw_annotations function and get the action
        action = draw_annotations(image_path, annotation_file,current_index,image_file,len(image_files))

        if action == 'next':
            # Continue to the next image
            current_index += 1
        elif action == 'prev':
            # Go back to the previous image
            current_index = max(0, current_index - 1)

displayer(images_path,labels_path)
