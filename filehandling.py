f=open("file1.txt","a")
f.write(" I am 22 years old")
f.close()
f=open("file1.txt","r")
print(f.read())

# -- delete of file --
import os
os.remove("file1.txt")

import os
if os.path.exists("file1.txt"):
    os.remove("file1.txt")
else:
    print("file deleted")

