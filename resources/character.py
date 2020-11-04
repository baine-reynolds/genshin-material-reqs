from  resources.characters import character_ascensions as ascensions
from  resources.characters import characters as characters
from  resources.items import gem_suffix as gem_suffix
from  resources.items import elements as elements
from  resources.items import materials as materials

class Character():
    def __init__(self, name: str, ascension_lvl: int):
        if name.lower() not in characters:
            exit(f"Character name not found, please check spelling of {name}")

        self.name = name.lower()
        self.ascension_lvl = ascension_lvl
        self.element = characters[self.name]['element']
        self.special_material = characters[self.name]['special']
        self.common_material = characters[self.name]['common']
        self.gem = elements[self.element]['gem']
        self.core = elements[self.element]['core']
        self.cost_to_max = self.max_ascension_cost()

    def max_ascension_cost(self) -> dict:
        _current_lvl = self.ascension_lvl
        costs = {}
        while _current_lvl < 7:
            costs = add_to_dict(costs, 'mora', ascensions[str(_current_lvl)]['mora'])
            costs = add_to_dict(costs, f"{self.gem}{gem_suffix[ascensions[str(_current_lvl)]['gem_tier']]}", ascensions[str(_current_lvl)]['element_gem'])
            costs = add_to_dict(costs, self.core, ascensions[str(_current_lvl)]['core'])
            costs = add_to_dict(costs, self.special_material, ascensions[str(_current_lvl)]['specialty'])
            costs = add_to_dict(costs, materials[self.common_material][ascensions[str(_current_lvl)]['common_tier']], ascensions[str(_current_lvl)]['common'])
            _current_lvl += 1
        return costs
        

def add_to_dict(costs:dict, variable: str, increase: int) -> dict:
        if variable not in costs:
            costs[variable] = 0
        costs[variable] += increase
        return costs
