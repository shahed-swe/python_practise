from csv import writer,DictWriter

with open('file.csv','a', newline='') as f:
    csv_writer = writer(f)
    # methods -- writerow, writerows
    # writerow
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['shahed','bd'])
    # csv_writer.writerow(['azad','bd'])
    # csv_writer.writerow(['ashik','bd'])
    # csv_writer.writerow(['rajib','bd'])
    # csv_writer.writerow(['atik','bd'])
    # writerows
    csv_writer.writerows([
        ['name','countries'],
        ['Shahed','bd'],
        ['Ashik','bd'],
        ['Azad','bd'],
        ['Rajib','bd'],
        ['Atik','bd']
    ])
# import python_ascii
# print(python_ascii.__package__)

with open('final.csv','w',newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
    # csv_writer.writerow({
    #     'first_name':'Shahed',
    #     'last_name':'Talukder',
    #     'age':'22'
    # })
    # csv_writer.writerow({
    #     'first_name':'Ashik',
    #     'last_name':'Mia',
    #     'age':'22'
    # })
    # csv_writer.writerow({
    #     'first_name':'Azad',
    #     'last_name':'Mia',
    #     'age':'22'
    # })
    csv_writer.writerows([
        {
            'first_name':'Shahed',
            'last_name':'Talukder',
            'age':'22'
        },
        {
            'first_name':'Ashik',
            'last_name':'Mia',
            'age':'22'
        },
        {
            'first_name':'Azad',
            'last_name':'Mia',
            'age':'22'
        },
        {
            'first_name':'Rajib',
            'last_name':'Mia',
            'age':'22'
        }
    ])


from csv import DictReader,DictWriter


with open('final.csv','r') as rf:
    with open('file.csv','w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['first_name','last_name','salary'])
        csv_writer.writeheader()
        for row in csv_reader:
            if int(row['age']) > 20:
                fname,lname,salary = row['first_name'],row['last_name'],21000
            else:
                fname,lname,salary = row['first_name'],row['last_name'],19500
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'salary': salary
            })
