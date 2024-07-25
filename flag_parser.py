import characters
from util import percent_chance
from random import randint as rng
from random import uniform as rng_f
                                  
def percent_range(value, low, high):
    is_float = True
    if low > high:
        low, high = high, low
    if value == 0:
        return value
    if type(value) == int:
        value = float(value)
        is_float = False
    low = low * 0.01
    high = high * 0.01
    value = value * rng_f(low, high)
    if value < 0.0001 and value > 0:
        value = 0.0001
    if not is_float:
        value = round(value)
        value = int(value)
    return value

def is_character(string):
    character_list = characters.ALL_CHARACTERS
    for character_name in character_list:
        if string == character_name:
            return True
    return False

def is_attack(string):
    tag_list = characters.attack_tags
    for tag in tag_list:
        if string == tag:
            return True
    return False

def is_throw(string):
    tag_list = characters.throw_tags
    for tag in tag_list:
        if string == tag:
            return True
    return False

def is_attribute(string):
    tag_list = characters.attribute_tags
    for tag in tag_list:
        if string == tag:
            return True
    return False

def is_tag(string):
    tag_list = characters.ALL_TAGS
    for tag in tag_list:
        if string == tag:
            return True
    return False

def create_flag(flag):
    bowser = characters.find_fighter("Bowser")
    falcon = characters.find_fighter("Captain Falcon")
    dk = characters.find_fighter("Donkey Kong")
    dr = characters.find_fighter("Dr. Mario")
    falco = characters.find_fighter("Falco")
    fox = characters.find_fighter("Fox")
    ganon = characters.find_fighter("Ganondorf")
    popo = characters.find_fighter("Popo")
    nana = characters.find_fighter("Nana")
    puff = characters.find_fighter("Jigglypuff")
    kirby = characters.find_fighter("Kirby")
    link = characters.find_fighter("Link")
    luigi = characters.find_fighter("Luigi")
    mario = characters.find_fighter("Mario")
    marth = characters.find_fighter("Marth")
    mewtwo = characters.find_fighter("Mewtwo")
    gnw = characters.find_fighter("Mr. Game & Watch")
    ness = characters.find_fighter("Ness")
    peach = characters.find_fighter("Peach")
    pichu = characters.find_fighter("Pichu")
    pikachu = characters.find_fighter("Pikachu")
    roy = characters.find_fighter("Roy")
    samus = characters.find_fighter("Samus")
    sheik = characters.find_fighter("Sheik")
    yoshi = characters.find_fighter("Yoshi")
    young_link = characters.find_fighter("Young Link")
    zelda = characters.find_fighter("Zelda")
    
    key_phrases = []
    current_phrase = ""
    parameter_string = ""
    parameter_a = 0
    parameter_b = 0
    flag += " "
    for char in flag:
        if char == "_":
            key_phrases.append(current_phrase)
            current_phrase = ""
        elif char == " ":
            key_phrases.append(current_phrase)
            parameter_string = flag[flag.index(char)+1:]
            break
        else:
            current_phrase += char
        
    if ":" in parameter_string:
        a = ""
        b = ""
        for char in parameter_string:
            if char == ":":
                b = parameter_string[parameter_string.index(char)+1:]
                if "." in a:
                    parameter_a = float(a)
                    parameter_b = float(b)
                else:
                    parameter_a = int(a)
                    parameter_b = int(b)
            else:
                a += char
    else:
        if len(parameter_string) > 0:   
            parameter_a = int(parameter_string)

    # Percent Range
    if key_phrases[0] == "randomize%":
        # Global
        if key_phrases[1] == "attributes":
            for fighter in characters.fighters:
                for attribute in fighter.attributes:
                    attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.special_attributes:
                    attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.article_attributes:
                    attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
        # Global Attacks/Throws
        elif not is_character(key_phrases[1]) and not is_tag(key_phrases[1]) and not is_attack(key_phrases[1]) and not is_throw(key_phrases[1]):
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    value = percent_range(getattr(attack, key_phrases[1]), parameter_a, parameter_b)
                    setattr(attack, key_phrases[1], value)
                for throw in fighter.throws:
                    value = percent_range(getattr(throw, key_phrases[1]), parameter_a, parameter_b)
                    setattr(throw, key_phrases[1], value)
        # Global Attributes by name
        if is_attribute(key_phrases[1]):
            for fighter in characters.fighters:
                for attribute in fighter.attributes:
                    for tag in attribute.tags:
                        if key_phrases[1] == tag:
                            attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.special_attributes:
                    for tag in attribute.tags:
                        if key_phrases[1] == tag:
                            attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.article_attributes:
                   for tag in attribute.tags:
                        if key_phrases[1] == tag:
                            attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
        # Global Tags
        if is_tag(key_phrases[1]):
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    for tag in attack.tags:
                        if key_phrases[1] == tag:
                            value = percent_range(getattr(attack, key_phrases[2]), parameter_a, parameter_b)
                            setattr(attack, key_phrases[2], value)
                for throw in fighter.throws:
                    for tag in throw.tags:
                        if key_phrases[1] == tag:
                            value = percent_range(getattr(throw, key_phrases[2]), parameter_a, parameter_b)
                            setattr(throw, key_phrases[2], value)
        # Character Global
        if is_character(key_phrases[1]):
            fighter = eval(key_phrases[1])
            if key_phrases[2] == "attributes":
                for attribute in fighter.attributes:
                    attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.special_attributes:
                    attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.article_attributes:
                    attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
            elif not is_tag(key_phrases[2]) and not is_attribute(key_phrases[2]) and not is_attack(key_phrases[2] and not is_throw(key_phrases[2])):
                for attack in fighter.attacks:
                    value = percent_range(getattr(attack, key_phrases[2]), parameter_a, parameter_b)
                    setattr(attack, key_phrases[2], value)
                for throw in fighter.throws:
                    value = percent_range(getattr(throw, key_phrases[2]), parameter_a, parameter_b)
                    setattr(throw, key_phrases[2], value)
            # Character Specific
            # Attributes
            if is_attribute(key_phrases[2]):
                for attribute in fighter.attributes:
                    for tag in attribute.tags:
                        if key_phrases[2] == tag:
                            attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.special_attributes:
                    for tag in attribute.tags:
                        if key_phrases[2] == tag:
                            attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
                for attribute in fighter.article_attributes:
                    for tag in attribute.tags:
                        if key_phrases[2] == tag:
                            attribute.value = percent_range(attribute.value, parameter_a, parameter_b)
            # Throws/Attacks
            if is_tag(key_phrases[2]) or is_attack(key_phrases[2]) or is_throw(key_phrases[2]):
                for attack in fighter.attacks:
                    for tag in attack.tags:
                        if key_phrases[2] == tag:
                            value = percent_range(getattr(attack, key_phrases[3]), parameter_a, parameter_b)
                            setattr(attack, key_phrases[3], value)
                for throw in fighter.throws:
                    for tag in throw.tags:
                        if key_phrases[2] == tag:
                            value = percent_range(getattr(throw, key_phrases[3]), parameter_a, parameter_b)
                            setattr(throw, key_phrases[3], value)
    # Normal Range
    if key_phrases[0] == "randomize":
        # Global First
        if not is_character(key_phrases[1]) and not is_tag(key_phrases[1]) and not is_attribute(key_phrases[1]) and not is_attack(key_phrases[1]) and not is_throw(key_phrases[1]):
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    setattr(attack, key_phrases[1], rng(parameter_a, parameter_b))
                for throw in fighter.throws:
                    setattr(throw, key_phrases[1], rng(parameter_a, parameter_b))
        # Global Attributes by name
        if is_attribute(key_phrases[1]):
            for fighter in characters.fighters:
                for attribute in fighter.attributes:
                    for tag in attribute.tags:
                        if tag == key_phrases[1]:
                            if attribute.integer:
                                attribute.value = rng(parameter_a, parameter_b)
                            else:
                                attribute.value = rng_f(parameter_a, parameter_b)
                for attribute in fighter.special_attributes:
                    for tag in attribute.tags:
                        if tag == key_phrases[1]:
                            if attribute.integer:
                                attribute.value = rng(parameter_a, parameter_b)
                            else:
                                attribute.value = rng_f(parameter_a, parameter_b)
                for attribute in fighter.article_attributes:
                    for tag in attribute.tags:
                        if tag == key_phrases[1]:
                            if attribute.integer:
                                attribute.value = rng(parameter_a, parameter_b)
                            else:
                                attribute.value = rng_f(parameter_a, parameter_b)
        # Global Tags
        if is_tag(key_phrases[1]):
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    for tag in attack.tags:
                        if key_phrases[1] == tag:
                            setattr(attack, key_phrases[2], rng(parameter_a, parameter_b))
                for throw in fighter.throws:
                    for tag in throw.tags:
                        if key_phrases[1] == tag:
                            setattr(throw, key_phrases[2], rng(parameter_a, parameter_b))
        # Character Global
        if is_character(key_phrases[1]):
            fighter = eval(key_phrases[1])
            if not is_tag(key_phrases[2]) and not is_attribute(key_phrases[2]) and not is_attack(key_phrases[2]) and not is_throw(key_phrases[2]):
                for attack in fighter.attacks:
                    setattr(attack, key_phrases[2], rng(parameter_a, parameter_b))
                for throw in fighter.throws:
                    setattr(throw, key_phrases[2], rng(parameter_a, parameter_b))
        # Character Specific
        # Character Attributes by Name
            if is_attribute(key_phrases[2]):
                for attribute in fighter.attributes:
                    for tag in attribute.tags:
                        if key_phrases[2] == tag:
                            if attribute.integer:
                                attribute.value = rng(parameter_a, parameter_b)
                            else:
                                attribute.value = rng_f(parameter_a, parameter_b)
                for attribute in fighter.special_attributes:
                    for tag in attribute.tags:
                        if key_phrases[2] == tag:
                            if attribute.integer:
                                attribute.value = rng(parameter_a, parameter_b)
                            else:
                                attribute.value = rng_f(parameter_a, parameter_b)
                for attribute in fighter.article_attributes:
                    for tag in attribute.tags:
                        if key_phrases[2] == tag:
                            if attribute.integer:
                                attribute.value = rng(parameter_a, parameter_b)
                            else:
                                attribute.value = rng_f(parameter_a, parameter_b)
        # Character Attacks/Throws by Tag
            if is_tag(key_phrases[2]) or is_attack(key_phrases[2]) or is_throw(key_phrases[2]):
                fighter = eval(key_phrases[1])
                for attack in fighter.attacks:
                    for tag in attack.tags:
                        if key_phrases[2] == tag:
                            setattr(attack, key_phrases[3], rng(parameter_a, parameter_b))
                for throw in fighter.throws:
                    for tag in throw.tags:
                        if key_phrases[2] == tag:
                            setattr(throw, key_phrases[3], rng(parameter_a, parameter_b))

    # Global Set
    if is_tag(key_phrases[0]) or is_attack(key_phrases[0]) or is_throw(key_phrases[0]):
        for fighter in characters.fighters:
            for attack in fighter.attacks:
                for tag in attack.tags:
                    if key_phrases[0] == tag:
                        setattr(attack, key_phrases[1], parameter_a)
            for throw in fighter.throws:
                for tag in throw.tags:
                    if key_phrases[0] == tag:
                        setattr(throw, key_phrases[1], parameter_a)
    if is_attribute(key_phrases[0]):
        for fighter in characters.fighters:
            for attribute in fighter.attributes:
                for tag in attribute.tags:
                    if key_phrases[0] == tag:
                        attribute.value = parameter_a
            for attribute in fighter.special_attributes:
                for tag in attribute.tags:
                    if key_phrases[0] == tag:
                        attribute.value = parameter_a
            for attribute in fighter.article_attributes:
                for tag in attribute.tags:
                    if key_phrases[0] == tag:
                        attribute.value = parameter_a
    # Character Global Set
    if is_character(key_phrases[0]):
        fighter = eval(key_phrases[0])
        if is_tag(key_phrases[1]) or is_attack(key_phrases[1]) or is_throw(key_phrases[1]):
            for attack in fighter.attacks:
                for tag in attack.tags:
                    if key_phrases[1] == tag:
                        setattr(attack, key_phrases[2], parameter_a)
            for throw in fighter.throws:
                for tag in throw.tags:
                    if key_phrases[1] == tag:
                        setattr(throw, key_phrases[2], parameter_a)
        if is_attribute(key_phrases[1]):
            for attribute in fighter.attributes:
                for tag in attribute.tags:
                    if key_phrases[1] == tag:
                        attribute.value = parameter_a
            for attribute in fighter.special_attributes:
                for tag in attribute.tags:
                    if key_phrases[1] == tag:
                        attribute.value = parameter_a
            for attribute in fighter.article_attributes:
                for tag in attribute.tags:
                    if key_phrases[1] == tag:
                        attribute.value = parameter_a
        
def start(flags):
    # Divide flag string into individual flags
    flags = flags[1:]
    flags += "-"
    current_flag = ""
    flag_array = []
    for char in flags:
        if char == "-":
            # Delimit certain flags
            if char == "&":
                current_flag = ""
            elif "seed " in current_flag:
                current_flag = ""
            else:
                flag_array.append(current_flag)
                current_flag = ""
        else:
            current_flag += char
    for flag in flag_array:
        create_flag(flag)
            
    #print("End randomizing")
