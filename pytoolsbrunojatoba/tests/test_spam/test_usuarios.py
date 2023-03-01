from pytoolsbrunojatoba.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Bruno', email='brjatoba92@djangosolutions.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Bruno', email='brjatoba92@djangosolutions.com'),
        Usuario(nome='Isabella', email='bellaragao@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
