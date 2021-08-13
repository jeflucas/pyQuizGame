points = 0

print('Welcome to capital game:')

playing = input("Do you wwant to play this game? (y/n) ")

if playing.lower() != 'y':
    quit()

print('Lets play!')

answer = input('What is the capital of Brazil? ')
if answer == 'brasilia':
    print('Excellent!')
    points = points + 1 
    
else: 
    print('Incorrect!')

answer = input('What is the capital of Argentina? ')
if answer == 'Buenos Aires':
    print('Excellent!')
else: 
    print('Incorrect!')

answer = input('What is the capital of Canada? ')
if answer == 'Otawa':
    print('Excellent!')
else: 
    print('Incorrect!')

answer = input('What is the capital of Englad? ')
if answer == 'London':
    print('Excellent!')
else: 
    print('Incorrect!')