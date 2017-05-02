def eggs(someParameter):
    print('Value of spam is [' + someParameter + '] and address of spam is {}'.format(id(someParameter)))
    someParameter = someParameter + 'Hi'
    print('Value of spam is [' + someParameter + '] and address of spam is {}'.format(id(someParameter)))
    twice = someParameter * 2
    print('Value of spam is [' + twice + '] and address of spam is {}'.format(id(twice)))

spam = 'Hello!'
print('Value of spam is [' + spam + '] and address of spam is {}'.format(id(spam)))
eggs(spam)
print('Value of spam after function call is [ ' + spam + ' ] and address of spam is {}'.format(id(spam)))