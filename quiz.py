import pathlib
from quizData import capitals
## loop 35 times to create 35 quizes
# for i in range(5):
#     print(i)

print(pathlib.Path().cwd())
p = pathlib.Path("files/file_one.txt")
print(p.suffix)
if p.exists():
    print('yes valid')

for i in range(1):
    file = open(p, "a", encoding="utf-8")
    file.write("\n new line")
    file.close()