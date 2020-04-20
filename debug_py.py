# import pdb #import pdb module
# module - python file contains usefull classes and functions wrote by developer

# according to wikipedia - Debuggin is the process of finding and resolving defects or probles within a computer program that prevent correct operation of computer software or a system

# why debuggin
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not worknig the same way we want/.



# steps for debuggin
# 1.) set trace
# 2.) execute code line by line




# pdb.set_trace()


name = input("Enter your name:")
age = input("Enter your age")

print(f"hello {name} your age is {age}")

age2 = age + 5

print(f"{name} you will be {age2} in next five years")