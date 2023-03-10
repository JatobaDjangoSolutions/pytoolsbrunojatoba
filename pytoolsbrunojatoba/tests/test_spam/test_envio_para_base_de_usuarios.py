from pytoolsbrunojatoba.spam.main import EnviadorDeSpam
from pytoolsbrunojatoba.spam.modelos import Usuario
import pytest
from unittest.mock import Mock


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'brjatoba92@djangosolutions.com',
        'DevPro Course',
        'Check the amazings modules'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Bruno', email='brjatoba92@djangosolutions.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bellaragao@google.com',
        'DevPro Course',
        'Check the amazings modules'
    )
    enviador.enviar.assert_called_once_with == (
        'bellaragao@google.com',
        'brjatoba92@djangosolutions.com',
        'DevPro Course',
        'Check the amazings modules'
    )
