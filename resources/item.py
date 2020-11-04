from  resources.items import item_ascensions as ascensions
from  resources.items import items as items
from  resources.items import materials as common_materials
from  resources.items import uncommon_materials as uncommon_materials
from  resources.items import weapon_materials as weapon_materials

class Item():
    def __init__(self, name: str, ascension_lvl: int):
        if name.lower() not in items:
            exit(f"Item name not found, please check spelling of {name}")

        self.name = name.lower()
        self.ascension_lvl = ascension_lvl
        self.weapon_material = items[self.name]['weapon_material']
        self.uncommon_material = items[self.name]['uncommon_material']
        self.common_material = items[self.name]['common_material']
        self.cost_to_max = self.max_ascension_cost()

    def max_ascension_cost(self) -> dict:
        _current_lvl = self.ascension_lvl
        costs = {}
        while _current_lvl < 7:
            costs = add_to_dict(costs, 'mora', ascensions[str(_current_lvl)]['mora'])
            costs = add_to_dict(costs, weapon_materials[self.weapon_material][ascensions[str(_current_lvl)]['weapon_tier']], ascensions[str(_current_lvl)]['weapon_material'])
            costs = add_to_dict(costs, uncommon_materials[self.uncommon_material][ascensions[str(_current_lvl)]['uncommon_tier']], ascensions[str(_current_lvl)]['uncommon_material'])
            costs = add_to_dict(costs, common_materials[self.common_material][ascensions[str(_current_lvl)]['common_tier']], ascensions[str(_current_lvl)]['common_material'])
            _current_lvl += 1
        return costs


def add_to_dict(costs:dict, variable: str, increase: int) -> dict:
        if variable not in costs:
            costs[variable] = 0
        costs[variable] += increase
        return costs
