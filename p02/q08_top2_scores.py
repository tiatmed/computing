number_students = int(input("Enter number of students: "))

studentname = []

studentscore = []

x = 1

for i in range(1, number_students+1):
	studentname.append(input("Enter student's name: "))
	studentscore.append(input("Enter student's score: "))
	number_students -= 1

highestscore = max(studentscore)

#finds the index position of the name student with the highest score using the index position of the highest score
print(studentname[studentscore.index(highestscore)], "had the highest score of", highestscore)

studentname.pop(studentscore.index(highestscore))

studentscore.pop(studentscore.index(highestscore))

secondhighestscore = max(studentscore)

print(studentname[studentscore.index(secondhighestscore)], "had the second highest score of", secondhighestscore)
