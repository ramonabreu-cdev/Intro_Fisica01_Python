'''
 Um carro percorre  90km de Teresina até Altos em 1,5h e para por 1h .
 Em seguida, percorre 110 km em 2,5h até piripiri.
 Qual a Vm neste percurso?

'''
    #Definimos as variáveis para (d) e (t)

d = float(90 + 110) #Em KM 
t = float(1.5 + 1 + 2.5) #Em H , Lembrar que aqui se conta o tempo de repouso para o total

    #Definimos nossa equação vm , onde (d ) é a distância percorrida e (t) é o tempo gasto
vm = float(d / t) 
    #Exibimos o resultado
print("A Velocidade média neste percurso é de :Vm =", vm,"Km/h")


