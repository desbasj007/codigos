"""
Função de entrada, no qual o usuario deve entrar 5 numeros inteiros separados por espaço
"""
def entrada():
    """ arr = [] é a declaração do array (vetor) que receberá so valores de entrados,
com a restrição 1 ≤ arr [i] ≥ 10⁹, mas o python ja resolve os parametros de limite"""
    arr = []
    while len(arr) <= 5: #Condição de loop de entrada é inferior ou igual a 5.
        arr = list(map(int,input("\nEntre 5 numeros inteiros separados por espaço : ").strip().split()))[:5]
        if len(arr) != 5: # verificação do numero de inteiro digitado
            print(" Lista de numero diferente de 5 ")#mensagem de erro, caso o # de entrada for < 5
    
        else: 
            return arr
            

"""FUnção que chama a função de entrada, fazer as somas e identificar o menor e o maior soma possivel
"""
def miniMaxSum():
    arr = entrada () # variavel arr  recebe a chamada da função de entrada.
    minimo = -1 #inicializando as variaveis com -1
    maximo = -1 # "  "  "  "  "    "    "    "   "
    for i in range (len(arr)): 
       soma = 0 #inicializando a variavel soma com 0.
       
       for j in range (len(arr)):# loop para percorer o array 
           if (j != i): # condição que permite pular um valor do array
               soma = soma + arr[j] # soma dos elemento do array
         
       if (soma > maximo):                # verificação dos valores maximo e minimo.
         maximo = soma
       if (soma < minimo or minimo < 0):
         minimo = soma
      
    print(minimo,' ', maximo) #saida da função miniMaxSum()


miniMaxSum() # Chamada da função miniMaxSum.
