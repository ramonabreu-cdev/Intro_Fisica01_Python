'''
Em carro anda a 72 km/h por 10s e , em seguida,
passa 20s em 5 m/s . 
Qual é a sua Velocidade Média ? 

'''
    # o primeiro a ser feito é transformar o primeiro tempo de km/h para m/s
vm1 = float(72 / 3.6) #de km/h para m/s
    # Definimos o primeiro tempo, de acordo com o problema
t1 = float(10) #tempo em segundos
    # Se em cada Segundo ando o valor de (vm1) , então em 10 segundo ando (t1) vezes (vm1)
d1 = float(vm1 * t1)
    # Em seguida definimos (vm2), de acordo com o problema
vm2 = float(5) # Em m/s
    # E se o tempo seguinte é : (t2)
t2 = float(20) #tempo em segundoss
    #Então, se em 1s anda 5m , então em (t2)s vai andar :
d2 = float( vm2 * t2) 
    #Então (vm) Velocidade Média é :
vm =float((d1 + d2) / (t1 + t2))
    
    #Então Exibimos o Valor da velocidade Média :
print( "A velocidade média Total é: ",vm, "m/s")

