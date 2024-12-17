try:
    val1=int(input('Please enter a INTEGER: '))
    val2=int(input('Please enter another INTEGER: '))
    result=val1/val2
    print(result)
    pr('hi')
except ZeroDivisionError as ex:
    print('A number cannot be divided by zero!\nI got this:',ex)
except ValueError as ex:
    print('WHY DID YOU NOT WRITE AN INTEGER!\nI GOT THIS: ',ex)
except:
    print('THERE IS AN ERROR!!!SAVE THIS PROGRAM!!!')