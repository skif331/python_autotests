import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '71f48e8b32aaf77930835f829308d382'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}

create_data = {
    "name": "Pikachu",
    "photo_id": 1
}

create_response = requests.post(f'{URL}/pokemons', headers = HEADER, json=create_data)
print("Создание покемона:", create_response.json())

pokemon_id = create_response.json().get('id')

update_data = {
    "pokemon_id": pokemon_id,
    "name": "Bulbasaur",
    "photo_id": 2
}

update_response = requests.put(f'{URL}/pokemons', headers = HEADER, json=update_data)
print("Смена имени покемона:", update_response.json())


catch_data = {
    "pokemon_id": pokemon_id
}

catch_response = requests.post(f'{URL}/trainers/add_pokeball', headers = HEADER, json=catch_data)
print("Поймать покемона в покебол:", catch_response.json())

