import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '71f48e8b32aaf77930835f829308d382'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = 22771


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons' , params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Bulbasaur'