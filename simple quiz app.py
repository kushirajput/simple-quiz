# Simple Quiz App in Python

score = 0

print("Welcome to the Python Quiz!\n")

questions = [
    ("What is the correct extension for Python files?", "a", ["a) .py", "b) .java", "c) .txt", "d) .html"]),
    ("Which keyword is used to define a function?", "b", ["a) function", "b) def", "c) fun", "d) define"]),
    ("What is the output of 2 + 3 * 4?", "c", ["a) 20", "b) 10", "c) 14", "d) 24"]),
    ("Which function is used to display output?", "a", ["a) print()", "b) show()", "c) echo()", "d) output()"])
]

for q, ans, opts in questions:
    print(q)
    for o in opts:
        print(o)
    user_ans = input("Enter your answer (a/b/c/d): ").lower()

    if user_ans == ans:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("Quiz Completed")
print("Your Score:", score, "/", len(questions))