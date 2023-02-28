from pytoolsbrunojatoba.spam.enviador_de_email import Enviador
from pytoolsbrunojatoba.spam.main import EnviadorDeSpam
from pytoolsbrunojatoba.spam.modelos import Usuario
import pytest

@pytest.mark.parametrize(
        'usuarios',
        [
            [
                Usuario(nome='Bruno', email='brjatoba92@djangosolutions.com'), 
                Usuario(nome='Isabella', email='bellaragao@gmail.com')
            ],
            [
                Usuario(nome='Bruno', email='brjatoba92@djangosolutions.com'), 
            ]
        ]
)

def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'brjatoba92@djangosolutions.com',
        'DevPro Course',
        'Check the amazings modules'
    )
    assert len(usuarios) == enviador.qtd_email_enviados

class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Bruno', email='brjatoba92@djangosolutions.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bellaragao@google.com',
        'DevPro Course',
        'Check the amazings modules'
    )
    assert enviador.parametros_de_envio == (
        'bellaragao@google.com',
        'brjatoba92@djangosolutions.com',
        'DevPro Course',
        'Check the amazings modules'
    )
