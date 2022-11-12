print('This program converts a temperature from celcius degree to fahreneit degree and vic versal \n1. Celcius to Fahrenheit \n2. Fahrenheit to celcius')

choice = int(input('Choose 1 or 2 :'))



def cf():
    c = int(input('Enter the temperature in celcius degree : '))
    f= ((9*c)/5) +32
    print('Temperature in Fahreneit degree : ' ,f,'°F')
    
    
    
def fc():
    f = int(input('Enter the temperature in celcius degree : '))
    c= (5/9)*(f-32)
    print('Temperature in Celcius degree : ' ,c,'°C')
    
if choice ==1:
      cf()
elif choice ==2:
      fc()
      