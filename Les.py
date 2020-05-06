class Les():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.quant = 0

    def getQuant(self):
        return self.quant

    def estaCheia(self):
        #if self.quant == 5:
        #    return True
        #else:
        #    return False

              #Ou
        
        return self.quant == 5

              #Ou

        #if self.quant == 5:
        #    return True
        #return False

    def estaVazia(self):
        return self.quant == 0

    def inserirFim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
        
    def show(self):
        i = 0
        while i < self.quant:
            print(self.vetor[i])
            i += 1

    def removerFim(self):
        self.quant -= 1

    def inserirInicio(self, valor):
        i = self.quant
        while i > 0:
            self.vetor[i] = self.vetor[i-1]
            i -= 1
        self.vetor[0] = valor
        self.quant += 1

    def removerInicio(self):
        i = 0
        while self.quant -1 > i:
            self.vetor[i] = self.vetor[i+1]
            i += 1
        self.quant -= 1

    def inserirAposDeterminado(self, valor1, valor2):
        posicao = 0
        for i in self.vetor:
            if self.vetor[i] == valor2:
                posicao = self.quant[i]
            
        
        while posicao < self.quant:
            self.vetor[self.quant] = self.vetor[self.quant -1]
            self.quant -= 1
        self.vetor[quant] = valor1
        self.quant += 1
                
        










        
