from classes.teste1 import Teste1
from classes.teste2 import Teste2
from classes.teste3 import Teste3
from classes.teste5 import Teste5

teste1 = Teste1()
teste2 = Teste2()
teste3 = Teste3()
teste5 = Teste5()

print(f"Resposta do teste 1: A soma para o indice {13} é: {teste1.executar(13)}.")

print("Resposta do teste 2: ")
print(f"Caso 1: para {5} é {teste2.executar(5)}")
print(f"Caso 1: para {25} é {teste2.executar(25)}")