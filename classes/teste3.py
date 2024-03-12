from num2word import word

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
        a, b, c = 1

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

        while counter < posicao:
            if(word(counter, lang = 'pt-BR')[0] == "d"):
                ultimo = counter 
                counter += 1

        return ultimo