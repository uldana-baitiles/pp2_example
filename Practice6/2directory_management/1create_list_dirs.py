import os

# create directory
os.makedirs("Practice6/test_folder", exist_ok=True)

# create nested directories Создаёт вложенные папки
os.makedirs("Practice6/test_folder/inner_folder", exist_ok=True)

print("Directories created")

# show current directory в какой папке сейчас работает Python
print("Current directory:")
print(os.getcwd())

# list files and folders inside Practice6 
# Показывает все файлы и папки внутри директории
print("Files in Practice6:")
print(os.listdir("Practice6"))