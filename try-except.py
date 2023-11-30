try: 
    x = int(input('Input an integer :'))
    print(x)
except :
    print('value not an integer')

#? when to use try except in real world projects : 
#>>> user input validation : allows you to catch errors if the input is not in the expected format.
#>>> file operation: files might encounter issues like the file not existing, permission errors or unexpected file format
#>>> invalid mathematical operations 
#>>> multi threading operations 

