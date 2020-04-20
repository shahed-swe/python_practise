from csv import reader,DictReader

with open('basic_csv.csv', 'r') as f:
    csv_reader = reader(f)
    # reader() --> this return us an iterator so we can run loop only one times
    next(csv_reader)
    for i in csv_reader:
        print(i)


with open('basic_csv.csv','r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row['email'])



with open('basic_csv.csv','r') as f:
    csv_reader = DictReader(f, delimiter = '|')
    for row in csv_reader:
        print(row['email'])

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
