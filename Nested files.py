import os


def func():
    count = 1
    for i in range(5):
        os.mkdir(os.path.join(os.getcwd(), f'Sardor{i}'))
        os.chdir(os.path.join(os.getcwd(), f'Sardor{i}'))
        count += 1
        for b in range(count):
            os.mkdir(os.path.join(os.getcwd(), f'Sardor{b}'))
        os.chdir(os.path.join(os.getcwd(), f'Sardor{i}'))


func()
