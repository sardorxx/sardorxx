import csv
import pandas as pd
transaction = []
rows = []
date = []
res = []
c = 0.0



with open('electronic-card-transactions-june-2023-csv-tables.csv', 'r') as csv_files:
    reader = csv.DictReader(csv_files, delimiter=',', quotechar='|')
    for row in reader:
        rows.append(row)
        date.append(row['Period'])
    dates = (list(set(date)))
    for i in dates:
        i = str(i)
        c = 0.0
        res = {}
        for r in rows:
            a = r['Period']
            if i == a:
                b = (r['Data_value'])
                if b.isdigit():
                    b = float(b)
                    c += b
        res = [i, c]
        transaction.append(res)

df = pd.DataFrame(transaction, columns=['Year', 'Date_Value'])
df.to_csv('Daily_Transaction.csv')

