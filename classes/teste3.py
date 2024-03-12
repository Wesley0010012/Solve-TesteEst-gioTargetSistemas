from num2words import num2words

class Teste3:
    def a(self, posicao):
        resultado = 1 + (posicao - 1) * 2
        return resultado
    
    def b(self, posicao):
        resultado = 2 ** posicao
        return resultado
    
    def c(self, posicao):
        resultado = (posicao - 1) ** 2
        return resultado

    def d(self, posicao):
        resultado = (posicao * 2) ** 2
        return resultado

    def e(self, posicao):
        a = 1
        b = 1
        c = 1

        if posicao == 1 or posicao == 2:
            return 1
        
        for i in range(2, posicao):
            c = a + b
            a = b
            b = c
        
        return c
    
    def f(self, posicao):
        counter = 0
        ultimo = 0
        number = 0

        while counter < posicao:
            if(num2words(number, lang = 'pt')[0] == 'd'):
                ultimo = number
                counter += 1
            number += 1
                

        return ultimo