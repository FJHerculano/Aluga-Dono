class Pessoa():
     nome = ""
     sobrenome = ""
     data_nasci=""
     cep = ""
     cidade = ""
     rua = ""
     bairro = ""
     num_casa = ""
     estado = ""
     celular = ""
     ponto_refere = ""
     email= ""
     email_recupe = ""
     senha = ""

     def __init__(self,nome,sobrenome,data_nasci,cep, cidade, rua, bairro,num_casa, estado, celular,ponto_refere,email, email_recupe,senha):
         self.nome = nome
         self.sobrenome = sobrenome
         self.data_nasci =data_nasci
         self.cep = cep
         self.cidade = cidade
         self.rua = rua
         self.bairro = bairro
         self.num_casa = num_casa
         self.estado = estado
         self.celular = celular
         self.ponto_refere = ponto_refere
         self.email = email
         self.email_recupe = email_recupe
         self.senha = senha

         def setNome(self,nome):
             self.nome = nome

         def getNome(self):
            return self.nome

         def setSobreNome(self,sobrenome):
             self.sobrenome = sobrenome

         def getSobreNome(self):
            return self.sobrenome   

         def setData-nasci(self,data_nasci):
             self.data_nasci = data_nasci

         def getSobreNome(self):
            return self.data_nasci
        
         def setCep(self,cep):
             self.cep = cep

         def getSobreNome(self):
            return self.cep
        
         def setCidade(self,cidade):
             self.cidade = cidade
         def getSobreNome(self):
            return self.cidade
        
         def setRua(self,rua):
             self.rua = rua
         def getSobreNome(self):
            return self.rua
            
        def setBairro(self,bairro):
             self.bairro = bairro
        def getSobreNome(self):
            return self.bairro

        def setNum_casa(self,num_casa):
             self.num_casa = num_casa
        def getSobreNome(self):
            return self.num_casa
        
        def setEstado(self,estado):
             self.estado = estado
        def getSobreNome(self):
            return self.estado

        def setCelular(self,celular):
             self.celular = celular
        def getSobreNome(self):
            return self.celular
        
        def setPonto_refere(self,ponto_refere):
             self.ponto_refere=ponto_refere
        def getSobreNome(self):
            return self.ponto_refere
        
        
        def setEmail(self,email):
             self.email = email
        def getSobreNome(self):
            return self.email
        
        def setEmail_recupe(self,email_recupe):
             self.email_recupe = email_recupe
        def getSobreNome(self):
            return self.email-recupe

        def setSenha(self,senha):
             self.senha = senha
        def getSobreNome(self):
            return self.senha

