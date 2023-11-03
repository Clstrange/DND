
new_spell = input("Which spell would you like to cast?: ")

def test(spell):
    converted_spell = ''
    i = 1
    for x in spell:
        
        converted_spell = converted_spell + spell[len(spell) - i]
        i = i + 1
    
    return converted_spell




print("Incantation: ", test(new_spell))