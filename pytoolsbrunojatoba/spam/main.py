class EnviadorDeSpam:
    
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.envidor = enviador
    
    def enviar_emails(self, remetente, assunto, corpo):
        for usuario in self.sessao.listar():
            self.envidor.enviar(
                remetente, 
                usuario.email, 
                assunto,
                corpo
            )
