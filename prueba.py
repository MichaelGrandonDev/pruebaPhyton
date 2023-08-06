nombre = input('ingrese nombre:')
edad = int(input('cuantos años tenes?'))

version='1.1'
print(f'inicio del programa: {version}')

array = {1, 2, 3, 4}

print(f'hola {nombre}')
print(f'edad: {edad}')

if(edad > 18):
    print(f'{nombre} sos mayor de edad')
else:
    print(f'{nombre} sos menor de edad')
    
    
for item in array:
    print(item)
    
var = 0
while(var < 10):
    print(f'var: {var}')
    var = var + 1