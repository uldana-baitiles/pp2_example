# Read and print file contents

with open("sample.txt", "r") as f:
    aaaa = f.read()

print(aaaa)

# Append new line to file

with open("sample.txt", "a") as f:
    f.write("New line added.\n")

print("Line appended.")