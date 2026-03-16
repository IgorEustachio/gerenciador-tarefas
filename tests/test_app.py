from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


# Esse teste faz uma requisição GET no endpoint / e
# verifica se o código de status da resposta é 200 e
# se o conteúdo da resposta é {'message': 'Olá Mundo!'}.
def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
