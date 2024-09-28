class CaldeiraChocolate:
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super(CaldeiraChocolate, cls).__new__(cls)
            cls.instancia.vazia = True
            cls.instancia.fervida = False
        return cls.instancia

    def encher(self):
        if self.vazia:
            self.vazia = False
            self.fervida = False  # Reseta fervida ao encher
            print("A caldeira foi preenchida com chocolate e leite.")
        else:
            print("A caldeira já está cheia. Não é possível preencher novamente.")

    def ferver(self):
        if not self.vazia and not self.fervida:
            self.fervida = True
            print("A mistura de chocolate e leite está fervendo.")
        elif self.vazia:
            print("A caldeira está vazia. Não é possível ferver.")
        else:
            print("A mistura já foi fervida. Não é possível ferver novamente.")

    def drenar(self):
        if self.fervida:
            self.vazia = True
            self.fervida = False  # Reseta fervida ao drenar
            print("A mistura foi drenada da caldeira.")
        elif self.vazia:
            print("A caldeira está vazia. Não é possível drenar.")
        else:
            print("A mistura ainda não foi fervida. Não é possível drenar.")

