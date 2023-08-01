import csv
import pandas as pd
old_ = []
middle_ = []
youth_ = []
with open('people-100000.csv', 'r') as csv_file:
    dict_reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')


    for row in dict_reader:
        a = int(row['Date of birth'][:-6])
        b0 = row['Index']
        b = row['User Id']
        b1 = row['First Name']
        b2 = row['Last Name']
        b3 = row['Sex']
        b4 = row['Email']
        b5 = row['Phone']
        b6 = row['Date of birth']
        b7 = row['Job Title']
        o = ([b0]+[b]+[b1]+[b2]+[b3]+[b4]+[b5]+[b6]+[b7])


        if a <= 1945 and a >= 1906: #[Index,User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title]
            old_.append(o)

        elif a > 1945 and a <= 1983:
            middle_.append(o)
        elif a > 1983 and a <= 2022:
            youth_.append(o)
        else:
            print(a)

df = pd.DataFrame(old_, columns=['Index', 'User ID', 'Name', 'LastName', 'Sex', 'Email',
                                               'Phone', 'Date of birth', 'Job Title'])
df.to_csv('OldPeoples.csv')
df = pd.DataFrame(middle_, columns=['Index', 'User ID', 'Name', 'LastName', 'Sex', 'Email',
                                               'Phone', 'Date of birth', 'Job Title'])
df.to_csv('MiddleAgePeoples.csv')

df = pd.DataFrame(youth_, columns=['Index', 'User ID', 'Name', 'LastName', 'Sex', 'Email',
                                               'Phone', 'Date of birth', 'Job Title'])
df.to_csv('YouthPeople.csv')


