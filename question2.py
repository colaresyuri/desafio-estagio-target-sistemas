def fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Teste com um número informado

n = int(input("Informe um número: "))
print(fibonacci(n))
