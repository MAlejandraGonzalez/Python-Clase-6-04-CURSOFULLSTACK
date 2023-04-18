#condicionales: simples y multiples


#OPERADORES LOGICOS 

#== #igual a: compara que ambos datos sean identicos en valor y tipo de dato 


#!= #diferentes a: compara ambos datos y se fija que sean distintos 

#operadores logicos numericos 

#>= , <= > , < 

#not #not es para asegurarse que algo no se encuentre 

#En este ejercicio si el usuario tiene 18 o mas años puede ingresar a nuestro sitio web


#edad= int(input("indique su uedad:")) 


#if edad >= 18:
   #print ("usted puede ingresar al sitio") 
   
#else:
    #print("acceso denegado") 
    
    #Es un edificio con 8 departamentos de los cuales estan ocupados 
    #depto 1 esta julian , depto 2 esta Alejandra , depto 3 esta Fernanda, depto 4 esta Maxi 
    #dependiendo el departamento que elija el usuario , mostrara el mensaje, "Llamando a..."nombre propietario"
    #Si elige otro numero se mostrara el mensaje... "llamando a porteria"
 
#while True:  
 #depto = int(input ("Con que depto desea comunicarse?: ")) 
#if depto ==1:
       #print("Llamando a julian")
#elif depto ==2:
       #print("Llamando a Alejandra") 
#elif depto ==3:
       #print("Llamando a Fernanda") 
#elif depto ==4:
       #print("Llamando a Maxi") 
#else:
       #print("Llamando a porteria") 
       
       #vamos a pedir un numero entero al usuario , y verificar si es multiplo de 2, si es multiplo de 4
       #(tambien nos diga)
while True:     
      numero = int(input("ingrese un NUMERO ENTERO: "))
      
      if numero % 2 != 0:
        print("no es multiplo de 2") 
      else:
        if numero % 4 == 0:
            print("es multiplo de 4(y ademas de 2)")
        else:
    
           print("Es multiplo de 2") 
    
    #match , nos permite segun la opcion , hacer una comparativa en nuestro programa , y evaluar una condicion ingresada
    #Practicar el condicional MATCH 
    
    #Nuestro programa es de una aerolinea :En nuestro menu, al inicio , 
    #lo que pregunta al usuario , es a que destino desea viajar .
    # Le mostrara en pantalla las siguientes opciones 
    
    #1) Europa 
    #2) Norteamerica
    #3)Asia 
    
    #El usuario ingresa un numero de opcion.SEGUN LA OPCION MOSTRARA DOS OPCIONES DE VIAJES DISPONIBLES 
    #POR EJ. SI ELIGE EUROPA MOSTRARA : ITALIA Y FRANCIA . el usuario elige un destino y luego el programa pregunta 
    #la cantidad de pasajeros , luego de que el usuario elija la cantidad de pasajeros le mostrara el importe a pagar
    #cada pasaje tiene un unico precio de $6000 
    
    
    
   


