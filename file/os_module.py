import os
import time
# f = os.getcwd()
# # os.mkdir('5555')
# for i in range(1,10000):
#     # os.mkdir(str(i)+"take")
#     # time.sleep(-50)
#     os.rmdir(str(i)+"take")
# # os.rmdir('5555')
# # if os.path.exists()

# # create file
# open('file.txt','a').close()

# command = f"touch shahed_{1}.txt"
# os.system(command)

for i in range(1,1000):
    command = f'echo "you have been hacked" > shahed_{i}.txt'
    os.system(command)

time.sleep(50)

for i in range(1,1000):
    command = f"rm shahed_{i}.txt"
    os.system(command)

# website = input("Enter your website name:")

# command = f"ping {website}"
# os.system(command)