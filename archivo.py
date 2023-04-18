print("Hola mundo")

    #comentario por  linea 
    
    #Este es un coemntario por bloque
    #todo lo que esta aca adentro se encuentra comentado
    
    
    
    #errores al declarar variables
    #No inicializar con numeros
    #No utilizar caracteres especiales, salvo el guion_bajo:
    
    #operadores 
    
    #variable1 = 10
    #variable2 = 3
    
    #print(variable1 + variable2) #equivale al console.log en Javascript  
    
    #NO PODEMOS CONCATENAR Strings con Integers/Float
    #La multiplicacion SI ES UN OPERADOR SOPORTADO Entre strings y Integers (NO ASI CON FLOAT)
    #Entre Strings podemos concatenar nuestras variables 
    
    #como se piden datos y se muestran en Python 
    
    #nombre = input("Digame su nombre: ") 
    #opcion 1: CONCATENAR 
    #print("Hola"+nombre) 
    
    #opcion 2: separdor por comas 
    #print("Hola",nombre) 
    
    #opcion 3 metodo f-string 
    #print(f"Hola {nombre}")
    
    #ejemplos
    
    nombre = input("Ingrese su año de nacimiento: ")
    anio_nacimiento = input("Ingrese su nombre: ")
    #La variable de nacimiento es de tipo string , por lo tanto debemos convertirla a integer
    
    edad=2023-int(anio_nacimiento)
    
    #opcion 1: CONCATENAR 
    print("Hola "+nombre+" tu edad es de "+str(edad)) 
    
    #opcion 2: separar por comas 
    print("Hola",nombre,"tu edad es de",edad)
    
    #opcion 3: metodo f-string 
    print(f"Hola {nombre} tu edad es de {edad}") 