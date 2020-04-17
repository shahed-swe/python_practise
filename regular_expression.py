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

