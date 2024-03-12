

class Teste2:
    def executar(self, numero):
        a = 1
        b = 1
        c = 1

        while(True):
            c = a + b
            a = b
            b = c

            if(b > numero):
                return False

            if(b == numero):
                return True
