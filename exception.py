try:
    user=int(input('Please enter a INTEGER:  '))
    print('Thank you!')
except ValueError as error:
    print('WHY did YOU NOT input an INTEGER!\nI got this error: ',error)

