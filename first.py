'''
user = 'mohamed'
password = '123'

if user == 'mohamed' and password == '123':
    print('Login Succesfull, Welcome Mohamed :)')
elif user == 'ahmed' or password == '123' :
    print ('hello dear :) :)')
if not user == 'ali' or password == '123':
    print ('welcome again mohamed')
else:
    print('Invalid username or password please check the validaty')
    
'''


x = 0

while x < 5 :
    y = 0
    print (x +1 , 'iteration')
    while y < 3:
        print( 'X = ', x , 'Y = ' , y)
        y += 1 
    x +=1 
