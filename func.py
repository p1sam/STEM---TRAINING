student_1 = [80, 89, 79, 85, 86]
student_2 = [56, 100, 81, 53, 78]

def total_marks(a):
    ttl = 0
    for i in a:
        ttl += i
    return ttl/len(a)

print("maen marks> ", total_marks(student_1))

