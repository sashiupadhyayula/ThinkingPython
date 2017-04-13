import string

print('Enter a sentence that you wish to modify:')

#Global Variables
_inputString = input()
_delimiter1 = ''
_delimiter2 = ''
_alphabetsCharArray = list(string.ascii_lowercase) + list(string.ascii_uppercase)
_finalOutput = []
_tempCharArray = []

print('You entered : ' + _inputString)

def evaluateSlice(slice):
    print('slice is: ' + ''.join(str(i) for i in slice))

    _subSlice = slice[1:-1]
    _distinctCharCountSet = set()
    _result = []
    for i in _subSlice:
        _distinctCharCountSet.add(str(i))

    _result.append(slice[0])
    _result.append(str(len(_distinctCharCountSet)))
    _result.append(slice[-1])
    print('evaluateSlice resulting value is: ' + str(_result))
    return _result

for _inputIterator in _inputString:
    if _inputIterator in _alphabetsCharArray:
        _tempCharArray.append(_inputIterator)
    else:                                                               #This means _inputIterator character is a delimitor
        if len(_tempCharArray) > 0 and len(_tempCharArray) < 3:
            _finalOutput.append(''.join(str(i) for i in _tempCharArray))
            _finalOutput.append(''.join(_inputIterator))
            _tempCharArray = []
        else:
            if len(_tempCharArray) == 0:
                _finalOutput.append(''.join(_inputIterator))
            else:
                _finalOutput.append(''.join(str(i) for i in evaluateSlice(_tempCharArray)))
                _finalOutput.append(''.join(_inputIterator))
                _tempCharArray = []

if len(_tempCharArray) > 3:                 #This is for only one word with more than two characters.
    _finalOutput.append(''.join(str(i) for i in evaluateSlice(_tempCharArray)))
elif len(_tempCharArray) > 0 and len(_tempCharArray) < 3:
    _finalOutput.append(''.join(str(i) for i in _tempCharArray))

#I am very happppy that th!s pr@graaaam is workiiiing grrrrre@t
print('Modified String is: ' + ''.join(str(i) for i in _finalOutput))
print('program is complete')