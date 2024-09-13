def fibonacci(num):
    A, B = 0, 1
    #Enquanto A for menor ou igual num...
    while A <= num:
    #Verificar se o valor A pertence à sequencia 
        if A == num:
            return True
        #Procedimento de soma 
        A, B = B, A + B
    return False

num = int(input("Degite um numero para verificação: "))

if fibonacci(num):
    print(f"O número {num} pertence a sequência Fibonacci!")
else:
    print(f"O número {num} não pertence a sequência Fibonacci!")
