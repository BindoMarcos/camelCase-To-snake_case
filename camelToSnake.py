import os    

def iterateFiles():
    directory = input("Type the root directory: ");

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r+") as f:
                for line in f:
                    #add condition to check if line contains camelCase
    print("Files changed");


iterateFiles()