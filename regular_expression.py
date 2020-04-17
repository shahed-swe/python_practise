import re

a = "My name is Shahed and i am a student"

# re.search(pattern, string, flags<optional>)
# (.*---.*)
# . --> means match any charecter
# * --> zero or more character
# flags <optional>
# re.I means case insensative

p = re.search('.*and.*', a) #without flags case sensetive

p1 = re.search('.*Is.*',a,re.I)
if p:
    print('Found')
else:
    print('Not Found')

if p1:
    print("String has found")
else:
    print("String not found")

# re.group() --> print the string we just make match

if p1:
    print("String has found")
    print(p1.group())
else:
    print("String not found")

new_string = "hello, How are you? Are you there?"

regex = re.search('(.*)are(.*)', new_string, re.I)
if regex:
    print("Found")
    print(regex.group())
    print(regex.group(1))
    print(regex.group(2))
    
else:
    print("Not Found")

print(regex.group().capitalize())
print(regex.group().title())
print(regex.group().upper())

# here we will discuss about regular expression match

p = re.match('My.*', a,re.I)
p2 = re.match('(My.*) (and) (.*student)',a,re.I)

if p:
    print('Match')
    print(p.group())
else:
    print('Not match')


if p2:
    print("Match")
    print(f"{p2.group()}")
    print(f"{p2.group(1)}")
    print(f"{p2.group(2)}")
    print(f"{p2.group(3)}")
else:
    print("Not match")


# regular expression substitution
# \d means digit
# \D means nondigit

new_string2 = 'This is 1234 to 4567 haha'
p = re.match('.*(\d).*', new_string2) #find integer number inside string
if p:
    print(p.group())
    print(p.group(1))
else:
    print("Not match")


p = re.sub('\d','0',new_string2)
print(p)
p = re.sub('\d*','0',new_string2)
print(p)
p = re.sub('\d.*','0',new_string2)
print(p)
p = re.sub('.*\d','0',new_string2)
print(p)

# regular expression gmail
# /w --> word character
# + --> one or more
# . --> any character
# * --> zero or more

a = 'shahed.talukder51@hotmailemail.com'
# p = re.search('\w+\.*\w+@\w+.com',a,re.I)
p = re.search('\w+\.*\w+@\w+.\w+',a,re.I)
# p = re.search('\w+\.*\w+@gmail.com',a,re.I)


if p:
    print("found")
else:
    print("not found")