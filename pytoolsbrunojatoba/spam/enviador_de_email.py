class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo_email):
        if '@' not in remetente:
            raise EmailInvalido('Email de remetente invalido: {remetente}')
        return remetente

class EmailInvalido(Exception):
    pass