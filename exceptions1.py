#Dealing with with exceptions
x = -5 
if x < 0:
    raise Exception('x should be positive ')

# assert(x>=0), 'x is not positive'  Assertion error 
# a = 5/ 0  Zero division error

try: 
    a = 5 /0
except Exception as e:
    print('e')


try:
    a = 7 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as a:
    print(e)
else: 
    print('everything is fine')
finally:
    print('cleaning up ...')

    
