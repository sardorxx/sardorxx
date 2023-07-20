
def find_min_moves():
    seats = [2, 2, 6, 6]
    students = [1, 3, 2, 6]
    seats = sorted(seats)
    students = sorted(students)
    counter = 0
    for x in range(len(seats)):
        counter += abs(seats[x] - students[x])
        print(seats[x], students[x], counter)


find_min_moves()

