Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # string a ser invertida
... string = "Hello, world!"
... # lista para armazenar os caracteres invertidos
... inverted = []
... # movimentando a string de trás pra frente
... for i in range(len(string)-1, -1, -1):
...     # inserindo os caracteres na lista 'inverted'
...     inverted.append(string[i])
... # unindo os caracteres invertidos em uma nova string
... inverted_string = "".join(inverted)
... # imprimindo a string invertida
... print(inverted_string)
