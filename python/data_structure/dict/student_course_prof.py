course_professors = {'calculus' : 'Prof A', 'diff eq':'Prof. B', 'linear algebra':'Prof. C', 'real analysis':'Prof. D'}
student_courses = {'Student A':['calculus', 'diff eq'], 'Student B':['calculus', 'linear algebra'], 'Student C':['real analysis']}

#Output is like below
#student_professors = {'Student A': ['Prof A', 'Prof B'], 'Student B': ['Prof A', 'Prof C'], 'Student C':['Prof C']}

student_professors = {}

for student in student_courses:
	for course in student_courses[student]:
		if student not in student_professors:
			student_professors[student] = set()
		student_professors[student].add(course_professors[course])
print (student_professors)

