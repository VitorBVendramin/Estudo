from data.races_data import get_race

class Character:
    def __init__(self, nome: str, race_key: str):
        self.nome = nome
        self.race = get_race(race_key)
        
        # pega os atributos da raça como ponto de partida
        self.atributos = self.race.to_dict()