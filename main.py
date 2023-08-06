
def sum_odd_indexes():
    arr = [3, 5, 9, 7, 7, 7, 8]
    result = 0
    for i in range(len(arr)):
        m = i
        while m < len(arr):
            result += sum(arr[i: m + 1])
            m += 2
    return result


print(sum_odd_indexes())

sum_odd_indexes()


def matrix():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = []
    c = []
    for i in range(len(a)):
        for j in range(len(a)):
            b.append(a[j][i])
        b.reverse()

        c.append(b)
        b = []
    return c


print(matrix())
matrix()
