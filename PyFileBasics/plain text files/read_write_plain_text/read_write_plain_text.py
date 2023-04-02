# sytnax for opening files: open(file path/name, mode)
# most used plain text modes: 'w' = write, 'r' = read, 'a' = append
file = open('plaintextfile.txt', 'r')  # open a file in read mode
quote = file.read()  # read the file
file.close()  # close the file

print(quote)

# opening a file using 'with open() as' automatically closes/flushes the file stream
with open('plaintextfile.txt', 'r') as f:
    contents = f.read()  # read the file

print(contents)

# writing into an already exsisting file (such as 'plaintextfile') will overwrite the file contents
with open('plaintextfile2.txt', 'w') as f:
    f.write("Tradition is the corpse of wisdom.\n")  # write into the file

# append into the file
with open('plaintextfile2.txt', 'a') as f:
    f.write("Do not fear the shrouded path.\n")  # append into the existing file using write method

with open('plaintextfile2.txt', 'r') as f:
    contents2 = f.read()

print(contents2)
