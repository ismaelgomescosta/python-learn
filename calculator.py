import re

print("My Calculator ")
print("Type 'kit' to exit \n ")

previous = ''
run = True

def performMath():
    global run
    global previous
    
    if previous == '':
        equation = input("Enter equation ")
    else:
        equation = input(str(previous))
    
    if equation == 'kit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if equation != '':
            previous = eval(str(previous)+str(equation))
            print("You typed", previous)
        
    
while run:
    try:
        performMath()
    except:        
        previous = ''
        run = True
        performMath()
    