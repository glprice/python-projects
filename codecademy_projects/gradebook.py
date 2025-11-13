last_semester_gradebook = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65],
]

# Your code below:

# list of subjects taken and list of corresponing grades in order
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# combined list of "subjects" and "grades"
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# prints gradebook in terminal
print("Semester Final Scores: \n" + str(gradebook))

# adds "computer science" and the corresponding grade to the lists
subjects.append("computer science")
grades.append(100)
gradebook.append(["computer science", 100])

# adds "visual arts" and the corresponding grade to the lists
subjects.append("visual arts")
grades.append(93)
gradebook.append(["visual arts", 93])

# modifies grade of visual arts in "grades" and "gradebook"
grades[-1] = 98
gradebook[-1][1] = 98

# removes numerical grade from list and then replaces it using .remove and .append (as per instructions)
gradebook[2].remove(85)
gradebook[2].append("Pass")

# combines" gradebook" and "last_semster_gradebook" into one list in order
full_gradebook = last_semester_gradebook + gradebook
print("\n End of Year Results:\n" + str(full_gradebook))
