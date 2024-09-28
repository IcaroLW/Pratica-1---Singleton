class FabricaDeChocolate:
    def __init__(self):
        self.caldeira = FabricaDeChocolate.getInstancia()

    def testar(self):
        self.caldeira.encher() 
        self.caldeira.encher()  

        self.caldeira.ferver()  
        self.caldeira.ferver() 

        self.caldeira.drenar()  
        self.caldeira.drenar() 
        self.caldeira.ferver()  

        self.caldeira.encher()  
        self.caldeira.ferver()  
        self.caldeira.drenar()  

fabrica = FabricaDeChocolate()
fabrica.testar()
