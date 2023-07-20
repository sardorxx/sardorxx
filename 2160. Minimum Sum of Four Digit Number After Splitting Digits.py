def minimum_sum():
    num = 2932
    a = sorted(str(num))
    return int(a[0] + a[2]) + int(a[1] + a[3])


minimum_sum()
