from pytoolsbrunojatoba.spam.enviador_de_email import Enviador
from pytoolsbrunojatoba.spam.main import EnviadorDeSpam

def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'brjatoba@djangosolutions.com',
        'DevPro Course',
        'Check the amazings modules'
    )
