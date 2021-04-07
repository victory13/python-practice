# create a new file - x
# f = open("file_1","x")
# f.write("new file")
# f.close()

# f = open("file_1","r")
# print(f.read(3))
# f.close()

# f = open("file_1","w")
# f.write("new file new")
# f.close()

# f = open("file_1","a")
# f.truncate(10)
# f.write("appended 1")
# f.close()

f = open("file_1","r")
# f.seek(4)
# print(f.read())
# print(f.tell())
# f.close()

#f = open("file_1","a")
# f.write("New file 1-1 \n new line 2 \n new line 3")
#f.close()

print(f.readlines())