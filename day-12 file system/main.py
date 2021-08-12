file = open("main.txt",mode="w")
file.write("hello my name is og")
file.close()

file = open("main.txt",mode="a")
file.write("\nhlo")
file.close()

file = open("main.txt",mode="r")
print(file.read())
file.close()
