from pytoolsbrunojatoba.spam.db import Conexao
from pytoolsbrunojatoba.spam.modelos import Usuario
import pytest

@pytest.fixture
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Bruno')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    

def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Bruno'), Usuario(nome='Isabella')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
