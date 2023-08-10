# 시간 초과
# n = int(input())
# students = []
# for _ in range (n):
#     name, kor, eng, math = map(str, input().split())
#     students.append([name, int(kor) * (-1), int(eng), int(math) * (-1)])

# students = sorted(students, key = lambda x: (x[1], x[2], x[3], x[0])) 
# for student in students:
#     print(student[0])

n = int(input())
students = []
for _ in range (n):
    name, kor, eng, math = map(str, input().split())
    students.append([int(kor) * (-1), int(eng), int(math) * (-1), name])

students.sort()
for student in students:
    print(student[-1])