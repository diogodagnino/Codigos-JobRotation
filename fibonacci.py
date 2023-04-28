Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Função para o cálculo de Fibonacci
... def fibonacci(n):
...     # Variáveis com os dois primeiros termos da sequência
...     a, b = 0, 1
...     # Loop while até atingir o número informado
...     while b < n:
...         # Sobrepõem os valores da sequência
...         a, b = b, a + b
...     # Retorna o resultado
...     return b
... # Inserção de número pelo usuário
... num = int(input("Digite um número: "))
... # Verificação de pertencimento à sequência de Fibonacci
... if fibonacci(num) == num:
...     print(num, "pertence à sequência de Fibonacci.")
... else:
...     print(num, "não pertence à sequência de Fibonacci.")
