from pokemon import Pokemon


class Joueur:

    def __init__(self, pokemons_str : list[str], attaques_str):
        self.pokemons : list[Pokemon] = []
        i  = 0
        for pokemon in pokemons_str:
            self.pokemons.append(Pokemon(pokemon.split("_")[0], pokemon.split("_")[1], attaques_str[i]))
            i += 1
        self.pokemon_actif = self.pokemons[0]
