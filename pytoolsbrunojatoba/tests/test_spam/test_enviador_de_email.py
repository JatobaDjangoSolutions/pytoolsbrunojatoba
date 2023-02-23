from pytoolsbrunojatoba.spam.enviador_de_email import Enviador, EmailInvalido

import pytest

def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

@pytest.mark.parametrize('destinatario', ['bellaragao@gmail.com', 'revphilippe@outlook.com']
)
def test_remetente(destinatario):
    enviador=Enviador()
    resultado = enviador.enviar( 
        destinatario,
        'brjatoba@djangosolutions.com',
        'DevPro Alert',
        'The DevPro Course is with subscribed open. Enjoy now !!!'
        )
    assert destinatario in resultado


@pytest.mark.parametrize('destinatario', ['', 'revphilippe']
)
def test_remetente_invalido(destinatario):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar( 
            destinatario,
            'brjatoba@djangosolutions.com',
            'DevPro Alert',
            'The DevPro Course is with subscribed open. Enjoy now !!!'
            )
