#using all parameter type
#we have to maintain parameter serial
#normal parameter
#args param
#default param
#kwargs
def cont(name,*args,last_name = 'unknown',**kwargs):
  print(name)
  print(args)
  print(last_name)
  print(kwargs)
  
if __name__ == '__main__':
  cont("shahed",2,3,4,"talukder",age = 23,address = 'khagan')