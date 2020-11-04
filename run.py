from resources.character import Character
from resources.item import Item

'''
Input: Character name and current ascension level
Output1: Item name and Quantity to increase to max ascension level to max
Output2: Item name and Quantity to increase to talent level to max

Input: Weapon name and current ascension level
Output: Item name and Quantity to increase to max ascension level to max
'''
def main():
    character_pool = {'qiqi': 1, 'ningguang': 6, 'fischl': 5, 'mona': 6, 'jean': 5, 'diluc': 4}
    character_reqs = {'mora': 0}
    #talent_reqs = {}

    item_pool = {'lost_prayer_to_the_sacred_winds': 6}
    item_reqs = {'mora': 0}
        
    for name, ascension_lvl in character_pool.items():
        character_reqs = merge_dicts(character_reqs, find_character_reqs(name, ascension_lvl))
    print("---Characters---")
    format_output(character_reqs)
    
    for name, ascension_lvl in item_pool.items():
        item_reqs = merge_dicts(item_reqs, find_item_reqs(name, ascension_lvl))
    print("---Items---")
    format_output(item_reqs)

def find_character_reqs(name: str, ascension_lvl: int) -> dict:
    character = Character(name, ascension_lvl)
    return character.cost_to_max
    

def find_talent_reqs():
    pass


def find_item_reqs(name: str, ascension_lvl: int) -> dict:
    item = Item(name, ascension_lvl)
    return item.cost_to_max


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    for k,v in dict2.items():
        if k not in dict1:
            dict1[k] = v
        else:
            dict1[k] = v + dict1[k]
    return dict1


def format_output(reqs: dict) -> None:
    for k,v in reqs.items():
        print(f'{k.replace("_", " ").title()}: {v:,}')


if __name__ == '__main__':
    main()
