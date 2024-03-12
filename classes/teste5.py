

class Teste5:
    def executar(self, texto):
        tamanhoTexto = len(texto)
        resultado = ""

        for i in range(1, tamanhoTexto + 1):
            resultado += texto[tamanhoTexto - i]

        return resultado