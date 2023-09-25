import os

def clear_directory(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    try:
        # Get a list of files in the directory
        files = os.listdir(directory_path)

        # Delete each file in the directory
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

        print(f"'{directory_path}' directory has been cleaned.")
    except Exception as e:
        print(f"An error occurred while clearing the directory: {e}")

# Specify the directory to clear
directory_to_clear = 'out'

# Call the function to clear the directory
clear_directory(directory_to_clear)

