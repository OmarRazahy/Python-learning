file= open("note.txt","w")
file.write("This is a note. (duh) \n")
file.write("I am learning how to edit files in python.\n")
file.write("This is the first step of my journey to freelancing via python.\n")
file.close()

print("Part 1:file created")

file= open("note.txt","r")
content = file.read()
file.close()

print("Part 2:file content read:")
print(content)

file= open("note.txt","r")
lines = file.readlines()
file.close()

print("Part 3:file content read line by line:")
for line in lines:
    print(line.strip())

print("Part 4:appending to the file")

with open("note.txt","a") as file:
    file.write("this is an extra line added to the end of the file.\n")

print("Part 5:reading the file again to see the changes")

with open("note.txt","r") as file:
    print(file.read())

print("Day 3: complete.")
