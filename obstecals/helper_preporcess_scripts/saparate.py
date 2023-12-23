import os
import shutil

def organize_files(src_dir, images_dir, labels_dir):
    # Create the target directories if they don't exist
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    if not os.path.exists(labels_dir):
        os.makedirs(labels_dir)

    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)

        # Check if the file is an image (you can adjust the conditions as needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Move image to the images directory
            shutil.move(src_path, os.path.join(images_dir, filename))
            print(f'Moved {filename} to {images_dir}')
        elif filename.lower().endswith('.txt'):
            # Move text file to the labels directory
            shutil.move(src_path, os.path.join(labels_dir, filename))
            print(f'Moved {filename} to {labels_dir}')

# Example usage:
src_directory = 'train'
images_directory = 'images'
labels_directory = 'labels'

organize_files(src_directory, images_directory, labels_directory)
