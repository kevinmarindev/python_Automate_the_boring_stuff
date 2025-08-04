import pyperclip

text = pyperclip.paste()

# split string to array
list = text.split(".")
# print("DID TEXT GET MODIFIED", text)

for idx in range(len(list)):
    print(idx, list[idx])
    list[idx] = "*" + list[idx]

print("\n".join(list))  # Join the list back into a string with newlines

