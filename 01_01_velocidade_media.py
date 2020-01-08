#Velocidade Média aula 01 #

'''
- Velocidade média = vm
    -Variação de Distâcia = d
    -Variação do Tempo = t
        - Então temos a seguinte fórmula : vm = d / t

            A unidade padrão para a vm = metros por segundo ou : vm = m/s .
            Porém a mais ultilizado no dia dia é o Quilômetros por Hora ou vm = km/h 

'''
# Temos algumas Regras de converssão :
print(" EP01) quanto é  20 m/s em km/h ? (Transformação de m/s para Km/h)")

    #primeiro defino minha primeira variável de velocidade em m/s
vms = float(20) 
    # Depois defino minha constante de transformação que é 3.6 
ct =float(3.6) 
    # Para transformar de m/s para kmn/h multiplica-se m/s pela nossa constante que é 3.6
vkh = float(vms*ct)
    # Agora Exibimos na Tela o resultado obtido
print ("20 m/s em km/h é: ",vkh ," km/h")

print(" EP02) quanto é  20 k/h em m/s ? (Transformação de  Km/h para m/s) " )

    #primeiro defino minha primeira variável de velocidade em k/h
kh = float(20)
    # Depois defino minha constante de transformação que é 3.6 
c = float(3.6)
    # Para transformar de  kmn/h para m/s divide-se k/h pela nossa constante que é 3.6
ms = float(kh / c)
    # Agora Exibimos na Tela o resultado obtido
print ("20 KM/H em M/S é: ",ms ," M/S")

print("-------------------------------------------------------------------")

print("OBS >>>> Quando se Fala de velocidades muito pequenas e de tempos muito rápidos temos a velocidade instantânea")

print("-------------------------------------------------------------------")








