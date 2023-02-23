from pytoolsbrunojatoba.spam.enviador_de_email import Enviador

def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

def test_remetente():
    enviador=Enviador()
    resultado = enviador.enviar(
        'brjatoba@djangosolutions.com', 
        'bellaragao@gmail.com', 
        'DevPro Alert',
        'The DevPro Course is with subscribed open. Enjoy now !!!'
        )
    
    assert 'brjatoba@djangosolutions.com' in resultado
