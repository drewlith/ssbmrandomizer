import characters

def start():
    char_num = 0
    last_name = characters.fighters[0].name
    for fighter in characters.fighters:
        print()
        if fighter.name != last_name:
            char_num += 1
            last_name = fighter.name
        print(characters.ALL_CHARACTERS[char_num] + ' = characters.find_fighter("' + characters.fighters[char_num].name + '")')
        for attribute in fighter.special_attributes:
            if attribute.integer:
                print(characters.ALL_CHARACTERS[char_num] + '.find_attribute("' + attribute.name + '").value = rng(' + str(round(attribute.value, 4)) + ' - ' +
                      str(round(attribute.value * 0.25)) + ' * mod, ' + str(round(attribute.value)) + ' + ' + str(round(attribute.value * 0.25)) + ' * mod)')
            else:
                print(characters.ALL_CHARACTERS[char_num] + '.find_attribute("' + attribute.name + '").value = rng_f(' + str(round(attribute.value, 4)) + ' - ' +
                      str(round(attribute.value * 0.25, 4)) + ' * mod, ' + str(round(attribute.value, 4)) + ' + ' + str(round(attribute.value * 0.5, 4)) + ' * mod)')
        for attribute in fighter.article_attributes:
            if attribute.integer:
                print(characters.ALL_CHARACTERS[char_num] + '.find_attribute("' + attribute.name + '").value = rng(' + str(round(attribute.value, 4)) + ' - ' +
                      str(round(attribute.value * 0.25)) + ' * mod, ' + str(round(attribute.value)) + ' + ' + str(round(attribute.value * 0.25)) + ' * mod)')
            else:
                print(characters.ALL_CHARACTERS[char_num] + '.find_attribute("' + attribute.name + '").value = rng_f(' + str(round(attribute.value, 4)) + ' - ' +
                      str(round(attribute.value * 0.25, 4)) + ' * mod, ' + str(round(attribute.value, 4)) + ' + ' + str(round(attribute.value * 0.5, 4)) + ' * mod)')

    

