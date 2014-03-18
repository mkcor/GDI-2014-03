age = raw_input('What is your age? ')
age = int(age)
place = raw_input('What is your place? (Capitalize) ')

legal18 = ['AB', 'MB', 'QC']
legal19 = ['BC', 'ON', 'SK']
legal21 = ['MA', 'NY', 'VT']

if place not in legal18 + legal19 + legal21:
    print('This location is not supported')
else:
    if age >= 21:
        print('You are allowed to drink alcohol')
    elif age >= 19 and place in legal19:
        print 'You are allowed to drink alcohol in', place
    elif age >= 18 and place in legal18:
        print 'You are allowed to drink alcohol in', place
    else:
        print('You are not allowed to drink alcohol')
