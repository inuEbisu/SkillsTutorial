import os

for i in range(2):
    os.fork()
    print("hello")
