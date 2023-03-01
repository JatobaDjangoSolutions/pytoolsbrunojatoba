from unittest.mock import Mock
from pytoolsbrunojatoba import github_api
import pytest

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('brjatoba92')
    assert avatar_url == url

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/69490377?v=4'
    resp_mock.json.return_value = {
        'login': 'brjatoba92', 'id': 69490377,
        'avatar_url': url,
    }
    get_original = github_api.rq.get
    github_api.rq.get = Mock(return_value=resp_mock)
    yield url
    github_api.rq.get = get_original
    

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('brjatoba92')
    assert 'https://avatars.githubusercontent.com/u/69490377?v=4' == url