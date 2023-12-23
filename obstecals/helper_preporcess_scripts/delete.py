import os

def delete_last_n_files(directory, n):
    files = os.listdir(directory)
    files.sort()  # Sort the files alphabetically or based on your requirements

    # Make sure to handle the case where there are fewer than n files
    if len(files) <= n:
        print(f"There are fewer than {n} files in the directory. Nothing to delete.")
        return

    files_to_delete = files[-n:]

    for file_name in files_to_delete:
        file_path = os.path.join(directory, file_name)
        os.remove(file_path)
        print(f"Deleted: {file_path}")

# Replace 'your_directory_path' with the actual path to your input directory
directory_path = 'images'
delete_last_n_files(directory_path, 400)
