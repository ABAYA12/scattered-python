import matplotlib.pyplot as plt
# A representation of students performance

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
students = [0, 0, 10, 22, 70, 33, 55, 100, 9, 4]
# plot the graph
plt.scatter(students, marks)
# give the graph a title
plt.title("Grade distribution of students | ABAYA University", fontsize=14)
# lable the x and y axis
plt.xlabel("Students")
plt.ylabel("Marks of students")
plt.yticks([10, 22, 70, 33, 55, 100, 9, 4], [
           10, 22, 70, 33, 55, 100, 9, 4])
plt.savefig('studentreport.png', bbox_inches='tight')
