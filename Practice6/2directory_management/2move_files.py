import os
import shutil

# create folder where files will be moved
os.makedirs("Practice6/moved_files", exist_ok=True)

# find txt files inside Practice6
for file in os.listdir("Practice6"):
    if file.endswith(".txt"):
        print("Found txt file:", file)

# copy sample.txt to new folder
shutil.copy("Practice6/sample.txt", "Practice6/moved_files/sample_copy.txt")
print("File copied")

# move file
shutil.move("Practice6/moved_files/sample_copy.txt",
            "Practice6/moved_files/sample_moved.txt")

print("File moved")
