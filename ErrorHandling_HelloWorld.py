def divideByZero(numerator, denominator):
    try:
        return numerator/denominator
    except:
        print('denominator is Zero. Cannot divide an number by 0')

print( divideByZero(100, 10) )
print( divideByZero(numerator=200, denominator=0) )
print( divideByZero(denominator=200, numerator=0) ) 
