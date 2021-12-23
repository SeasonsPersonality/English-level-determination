# English level determination
# The test does not have a negative score.
#

from Question import Question
# questions
question_prompts = [
    "\n1. What ___ when i called?\n(a) Was you doing\n(b) was you do\n(c) Were you doing\n(d) You were doing\n",
    "\n2. Wich word from is not correct?\n(a) Clotheful\n(b) Clothing\n(c) Clothed\n(d) Clothe\n",
    "\n3. Nothing ___ done when the boss is away.\n(a) Becomes\n(b) Gets\n(c) Been\n(d) Got\n",
    "\n4. You can use my car ___ tomorrow.\n(a) Yet\n(b) Since\n(c) Until\n(d) Around\n",
    "\n5. What ___ your favorite food as a child?\n(a) Will\n(b) Were\n(c) Would\n(d) is\n",
    "\n6. ___ you like?i like Grapes and Mango.\n(a) What kind of fruit\n(b) What type of fruit do\n(c) How many fruit do\n(d) Types of fruit do\n",
    "\n7. I will talk ___ Pual when i find him.\n(a) Around\n(b) To\n(c) At\n(d) Towards\n",
    "\n8. ____? Adolph Hitler did.\n(a) Who start World War ||\n(b) Who started the Second World War\n(c) Who caused World War ||\n(d) Who did World War ||\n",
    "\n9. I never have ___ such a boring book!\n(a) Saw\n(b) Red\n(c) Read\n(d) Readen\n",
    "\n10. Please, let me ___!\n(a) Think\n(b) Have\n(c) Make\n(d) Put\n",
]

# prompt & answer(Question and answer number)
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a"),

]
# colored text and background
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def run_test(question):
    score = 0
    for question in questions:

        # Check
        # If the user does not enter the correct input, she\he will enter again
        while True:
            answer = input(f"{question.prompt}\n>").lower()
            if answer not in ["a", "b", "c", "d"]:
                prRed("something wrong")
            else:
                break
        # in the following...
        if answer == question.answer:
            score += 1

        # grade
    if 8 <= score <= 10:
        print("\nYour level is: Advanced")
    elif 6 <= score < 8:
        print("\nYour level is: Intermediate")
    elif 4 <= score < 6:
        print("\nYour level is: Pre intermediate")
    elif 2 <= score < 4:
        print("\nYour level is: Elementary")
    else:
        print("\nYour level is: Starter")

    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")
# run_code
run_test(question_prompts)