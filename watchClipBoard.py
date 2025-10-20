import pyperclip, time


print("Paste =========", pyperclip.paste())
print("yes", time.localtime())
upTop = ""
print("upto", upTop)

try:
    while True:
        if(pyperclip.paste() != upTop):
            print(pyperclip.paste())
            upTop = pyperclip.paste()

        time.sleep(0.5)

except KeyboardInterrupt:
    print("I stopped the proccess")