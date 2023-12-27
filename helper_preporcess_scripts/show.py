import cv2

def read_annotations(annotation_file):
    with open(annotation_file, 'r') as file:
        lines = file.readlines()
    
    annotations = []
    for line in lines:
        values = line.strip().split()
        class_id = int(values[0])
        x, y, w, h = map(float, values[1:])
        annotations.append((class_id, x, y, w, h))
    
    return annotations

def display_annotations(image, annotations):
    for annotation in annotations:
        class_id, x, y, w, h = annotation
        
        height, width, _ = image.shape
        x_min = int((x - w / 2) * width)
        y_min = int((y - h / 2) * height)
        x_max = int((x + w / 2) * width)
        y_max = int((y + h / 2) * height)
        print(x_min,y_min,x_max,y_max)
        color = (0, 255, 0)  # Green color for bounding boxes
        thickness = 2
        image = cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)
    
    return image

# Example usage
annotation_file = "labels/1117.txt"
image_file = "images/1117.jpg"

annotations = read_annotations(annotation_file)
image = cv2.imread(image_file)

if annotations and image is not None:
    image_with_annotations = display_annotations(image.copy(), annotations)

    cv2.imshow("Image with Annotations", image_with_annotations)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No annotations or image not found.")
