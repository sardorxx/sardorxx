import csv
import pandas as pd
organization_small = []
organization_medium = []
organization_large = []
with open('organizations-100000.csv', 'r') as csv_file:
    dict_reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')


    for row in dict_reader:
        if row['Number of employees'].isdigit():
            a = int(row['Number of employees'])
            if a <= 500:
                organization_small.append(row)
            elif a > 500 and a <= 1000:
                organization_medium.append(row)
            elif a > 1000 and a < 9999:
                organization_large.append(row)
            else:
                print(a)

df = pd.DataFrame(organization_large, columns=['Index', 'Org ID', 'Name', 'Website', 'Country', 'Description',
                                               'Founded', 'Industry', 'Num of employees'])
df.to_csv('LargeOrganization.csv')
df = pd.DataFrame(organization_small, columns=['Index', 'Org ID', 'Name', 'Website', 'Country', 'Description',
                                               'Founded', 'Industry', 'Num of employees'])
df.to_csv('SmallOrganization.csv')
df = pd.DataFrame(organization_medium, columns=['Index', 'Org ID', 'Name', 'Website', 'Country', 'Description',
                                               'Founded', 'Industry', 'Num of employees'])
df.to_csv('MediumOrganization.csv')


