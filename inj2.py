import os

s = input("Enter a phrase: ")
cmd = 'echo "' + s + '"'
print(cmd)
os.system(cmd)
