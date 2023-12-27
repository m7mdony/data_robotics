import os

def isinside(box1, box2):
    # Extract coordinates of boxes
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    # Calculate half-width and half-height for each box
    w1_half, h1_half = w1 / 2, h1 / 2
    w2_half, h2_half = w2 / 2, h2 / 2

    # Calculate box coordinates
    x1_min, y1_min, x1_max, y1_max = x1 - w1_half, y1 - h1_half, x1 + w1_half, y1 + h1_half
    x2_min, y2_min, x2_max, y2_max = x2 - w2_half, y2 - h2_half, x2 + w2_half, y2 + h2_half

    # Calculate intersection coordinates
    inter_x_min, inter_y_min = max(x1_min, x2_min), max(y1_min, y2_min)
    inter_x_max, inter_y_max = min(x1_max, x2_max), min(y1_max, y2_max)

    # Calculate intersection area
    inter_area = max(0, inter_x_max - inter_x_min) * max(0, inter_y_max - inter_y_min)

    # Calculate areas of each box
    area1 = w1 * h1
    area2 = w2 * h2

    # Check if at least 90% of one box is inside the other
    return inter_area >= 0.85 * min(area1, area2)




def change(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Read bounding box annotations from the file
        annotations = []
        with open(file_path, "r") as file:
            for line in file:
                annotation = list(map(float, line.split()))
                annotation[0]=int(annotation[0])
                annotations.append(annotation)

        # Identify and delete overlapping boxes with smaller area
        boxes_to_delete = set()
        for i in range(len(annotations)):
            for j in range(i + 1, len(annotations)):
                box1 = annotations[i][1:]  # Exclude the object class
                box2 = annotations[j][1:]  # Exclude the object class
                inside1 = isinside(box1, box2) 
                print(f"IoU between box {i+1} and box {j+1}: {inside1} ")
                
                if inside1:
                    # If there is an overlap, compare areas and mark the box with smaller area for deletion
                    area1 = box1[2] * box1[3]
                    area2 = box2[2] * box2[3]
                    
                    if area1 < area2:
                        boxes_to_delete.add(i)
                    else:
                        boxes_to_delete.add(j)

        # Delete boxes with smaller area
        annotations_after_deletion = [annotations[i] for i in range(len(annotations)) if i not in boxes_to_delete]

        # Save the modified annotations back to the file
        with open(file_path, "w") as file:
            for annotation in annotations_after_deletion:
                line = " ".join(map(str, annotation)) + "\n"
                file.write(line)

# Replace "labels" with the actual path to your folder containing annotation files
folder_path = "labels"
change(folder_path)
