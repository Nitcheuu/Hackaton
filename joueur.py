from pokemon import Pokemon


class Joueur:

    def __init__(self, pokemons_str : list[str]):
        self.pokemons : list[Pokemon] = []
        for pokemon in pokemons_str:
            self.pokemons.append(Pokemon(pokemon.split("_")[0], pokemon.split("_")[1]))
        self.pokemon_actif = self.pokemons[0]
