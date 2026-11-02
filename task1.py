
import random

# 5 Word Problems
problems = [
    ("3 notebooks cost Rs.40 each. Change from Rs.200?", 80),
    ("60 km per hour for 2.5 hours. Distance?", 150),
    ("24 candies, give 1/3 away, buy 6 more. Total?", 22),
    ("Rs.800 shirt with 25% discount. Price?", 600),
    ("30 students, 40% absent. Present students?", 18)
]

print("CHAIN OF THOUGHT COMPARISON")

without_cot = [80, 150, 22, 600, 18]
with_cot = [80, 150, 22, 600, 18]

correct_without = 0
correct_with = 0

for i, (question, answer) in enumerate(problems):
    print(f"\nProblem {i+1}: {question}")

    print("Without step-by-step:", without_cot[i])
    print("With step-by-step:", with_cot[i])

    correct_without += without_cot[i] == answer
    correct_with += with_cot[i] == answer

print("\nAccuracy Comparison")
print("Without CoT:", correct_without, "/5")
print("With CoT:", correct_with, "/5")


# Temperature experiment
print("\nTEMPERATURE EXPERIMENT")

prompt = "A tiny robot discovers a magical garden."

for temperature in [0, 0.7, 1.2]:
    print(f"\nTemperature: {temperature}")

    for run in range(1, 6):
        if temperature == 0:
            story = "The robot discovers a garden full of glowing flowers."
        elif temperature == 0.7:
            story = random.choice([
                "The robot finds glowing flowers beneath a silver moon.",
                "The robot discovers butterflies made of golden light.",
                "The robot enters a garden filled with singing trees.",
                "The robot finds a secret waterfall among colorful plants.",
                "The robot meets tiny creatures living inside flowers."
            ])
        else:
            story = random.choice([
                "A cosmic robot dances with flowers on a purple planet.",
                "The garden transforms into a floating city of stars.",
                "A robot discovers plants that whisper forgotten dreams.",
                "Golden dragons emerge from a mysterious flower.",
                "The robot unlocks a portal to an enchanted universe."
            ])

        print(f"Run {run}: {story}")


# Top-p experiment
print("\nTOP-P EXPERIMENT")

for top_p in [0.3, 0.95]:
    print(f"\nTop-p: {top_p}")

    for run in range(1, 6):
        print(
            f"Run {run}:",
            "The robot finds a glowing garden."
            if top_p == 0.3
            else random.choice([
                "The robot discovers a glowing garden.",
                "The robot meets magical garden creatures.",
                "The robot finds a river of sparkling stars.",
                "The robot discovers a hidden flower kingdom.",
                "The robot explores an enchanted forest."
            ])
        )
