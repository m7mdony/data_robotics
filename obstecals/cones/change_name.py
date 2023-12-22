import os

input_dir = "labels"

# Ensure the input directory exists
if not os.path.exists(input_dir):
    print(f"Error: The specified input directory '{input_dir}' does not exist.")
else:
    # Get a list of all JPG files in the directory
    jpg_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".txt")]

    # Rename the files with sequential numbers
    for i, jpg_file in enumerate(jpg_files, start=1):
        old_path = os.path.join(input_dir, jpg_file)
        new_name = f"{i}.txt"
        new_path = os.path.join(input_dir, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {jpg_file} to {new_name}")
