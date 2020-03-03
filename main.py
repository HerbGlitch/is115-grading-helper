import os
import time

os.chdir("c:/users/heber/downloads")

running = True

old_dir = os.listdir()

os.system("cls")

while(running):
    new_in_dir = [item for item in os.listdir() if item not in old_dir]
    if any(".ipynb" in d for d in new_in_dir):
        ipynb_file = ""
        for d in os.listdir():
            if(".ipynb" in d):
                ipynb_file = d
        if(input("Want grade " + ipynb_file + " (y/n): ").lower() == "y"):   
            name = ipynb_file.split(".")[0]
            os.system("ipynb-py-convert " + ipynb_file + " " + name + ".py")
            os.system("del " + ipynb_file)
            # os.system("code " + name + ".py")
            # input("continue: ")
            os.system("vim " + name + ".py")
            os.system("python " + name + ".py")
            while(input("Run again (y/n): ").lower() == "y"):
                os.system("python " + name + ".py")
            os.system("del " + name + ".py")
            os.system("cls")
        else:
            old_dir.append(ipynb_file)
    time.sleep(2)
