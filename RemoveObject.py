import os

def RemoveObject(obj, os=os):
    print ('The passed object is {}'.format(obj)) 
    print ('What is os is {}'.format(os)) 
    print ('Calling as {}'.format(os.remove))
    os.remove(obj)
