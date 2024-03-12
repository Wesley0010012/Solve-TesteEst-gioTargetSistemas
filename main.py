from classes.teste1 import Teste1
from classes.teste2 import Teste2
from classes.teste3 import Teste3
from classes.teste5 import Teste5

teste1 = Teste1()
teste2 = Teste2()
teste3 = Teste3()
teste5 = Teste5()

print(f"Resposta do teste 1: A soma para o indice {13} é: {teste1.executar(13)}.")

print("Respostas do teste 2:")
print(f"Caso 1: para {5} é {teste2.executar(5)}")
print(f"Caso 1: para {25} é {teste2.executar(25)}")

print("Respostas do teste 3:")
print(f"A -> {teste3.a(5)}")
print(f"B -> {teste3.b(7)}")
print(f"C -> {teste3.c(8)}")
print(f"D -> {teste3.d(5)}")
print(f"E -> {teste3.e(7)}")
print(f"F -> {teste3.f(8)}")