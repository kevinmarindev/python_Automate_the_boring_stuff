import sys, os, pyperclip

print(sys.argv)
print("Cat and dog")

print(os.getcwd())
if(len(sys.argv) > 1):
    print("yes has length")



if len(sys.argv) > 1:
    os.chdir(sys.argv[1])
pyperclip.copy(os.getcwd())