class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'went to party', self.x, 'times')
    
    def __del__(self):
        print(self.name, 'is destructed with', self.x, 'parties')

emi = PartyAnimal("Emilio")
joti = PartyAnimal("Jotadé")

emi.party()
joti.party()
emi.party()

# We are going to extend the PartyAnimal class

class PokemonFan(PartyAnimal):
    pokedex = 0
    def catch_a_pokemon(self):
        self.pokedex = self.pokedex + 1
        self.party()
        print(self.name, 'has', self.pokedex, 'pokemons in the pokedex')

paco = PokemonFan("Paco")
paco.party()
paco.catch_a_pokemon()