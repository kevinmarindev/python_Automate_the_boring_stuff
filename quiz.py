import pathlib
import random
from quizData import capitals
print("starting program")
print("=======================")
print(capitals)

# print(pathlib.Path().cwd())
p = pathlib.Path("files/")
print("my path", pathlib.Path().cwd() / p)
if p.exists():
    print('yes valid')

for i in range(1):
    quiz = open(f"files/quiz_{i}", "w", encoding="utf-8")
    answer_sheet = open(f"files/answer_{i}", "w", encoding="utf-8")
    ##header for quiz file
    quiz.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz.write((' ' * 20) + f'State Capitals Quiz {i}')
    quiz.write('\n\n')

    ##capitals
    states = list(capitals.keys())
    print("random:", states)
    random.shuffle(states)

    ##get correct answer and 3 wrong answers for the quiz
    for i in range(5):
        correct_answer = capitals[states[i]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        sample = random.sample(wrong_answers, 3)
        all_options = sample + [correct_answer]
        print(all_options)

        ## write to file
        quiz.write(f"\n{i + 1}. Capital of {states[i]}? \n")
        options = ["a","b","c", "d"]
        for j in range(4):
            quiz.write(f"{options[j]}. {all_options[j]} \n")
        # quiz.close()
        ##answer key
        answer_sheet.write(f"{i + 1}. {correct_answer} \n")