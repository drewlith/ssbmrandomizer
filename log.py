import characters, json, util

hitbox_elements = ["Normal", "Fire", "Electric", "Slash", "Coin", "Ice", "Sleep", "Sleep",
            "??????", "Grounded", "Cape", "Special", "Disable", "Dark", "Screw Attack",
            "Flower", "None"]
throw_elements = ["Normal", "Fire", "Electric", "Ice", "Darkness"]

def get_start_values():
    for fighter in characters.fighters:
        for attack in fighter.attacks:
            attack.original_values.append(attack.damage)
            attack.original_values.append(attack.angle)
            attack.original_values.append(attack.growth)
            attack.original_values.append(attack.set_kb)
            attack.original_values.append(attack.base)
            attack.original_values.append(attack.element)
            attack.original_values.append(attack.shield_damage)
            attack.original_values.append(attack.sfx)
            attack.original_values.append(attack.size)

        for throw in fighter.throws:
            throw.original_values.append(throw.damage)
            throw.original_values.append(throw.angle)
            throw.original_values.append(throw.growth)
            throw.original_values.append(throw.set_kb)
            throw.original_values.append(throw.base)
            throw.original_values.append(throw.element)

        for attribute in fighter.attributes:
            attribute.original_value = attribute.value

        for attribute in fighter.special_attributes:
            attribute.original_value = attribute.value

        for attribute in fighter.article_attributes:
            attribute.original_value = attribute.value
            
def create_log_dict(flags, output_json = True,  code = "", verbose = False):
    log_dict = {}
    general_dict = {}
    general_dict["Seed"] = util.get_flag(flags, "seed", True)
    general_dict["Flags"] = flags
    log_dict["General"] = general_dict
    for fighter in characters.fighters:
        fighter_dict = {}
        all_attacks_dict = {}
        all_throws_dict = {}
        all_attr_dict = {}
        all_special_dict = {}
        for attack in fighter.attacks:
            attack_dict = {}
            attack_dict["Tags"] = attack.tags
            attack_dict["Attack Rating"] = attack.strength
            damage_dict = {}
            damage_dict["Original"] = attack.original_values[0]
            damage_dict["New"] = attack.damage
            angle_dict = {}
            angle_dict["Original"] = attack.original_values[1]
            angle_dict["New"] = attack.angle
            growth_dict = {}
            growth_dict["Original"] = attack.original_values[2]
            growth_dict["New"] = attack.growth
            set_dict = {}
            set_dict["Original"] = attack.original_values[3]
            set_dict["New"] = attack.set_kb
            base_dict = {}
            base_dict["Original"] = attack.original_values[4]
            base_dict["New"] = attack.base
            element_dict = {}
            element_dict["Original"] = hitbox_elements[attack.original_values[5]]
            element_dict["New"] = hitbox_elements[attack.element]
            shield_dict = {}
            shield_dict["Original"] = attack.original_values[6]
            shield_dict["New"] = attack.shield_damage
            sfx_dict = {}
            sfx_dict["Original"] = attack.original_values[7]
            sfx_dict["New"] = attack.sfx
            size_dict = {}
            size_dict["Original"] = attack.original_values[8]
            size_dict["New"] = attack.size

            if verbose:
                damage_dict["Notes"] = attack.log_notes[0]
                angle_dict["Notes"] = attack.log_notes[1]
                growth_dict["Notes"] = attack.log_notes[2]
                set_dict["Notes"] = attack.log_notes[3]
                base_dict["Notes"] = attack.log_notes[4]
                element_dict["Notes"] = attack.log_notes[5]
                shield_dict["Notes"] = attack.log_notes[6]
                sfx_dict["Notes"] = attack.log_notes[7]
                size_dict["Notes"] = attack.log_notes[8]
                
            attack_dict["Damage"] = damage_dict
            attack_dict["Angle"] = angle_dict
            attack_dict["Knockback Growth"] = growth_dict
            attack_dict["Set Knockback"] = set_dict
            attack_dict["Base Knockback"] = base_dict
            attack_dict["Element"] = element_dict
            attack_dict["Shield Damage"] = shield_dict
            attack_dict["Sound Effect"] = sfx_dict
            attack_dict["Hitbox Size"] = size_dict
            
            all_attacks_dict[attack.name] = attack_dict

        for throw in fighter.throws:
            throw_dict = {}
            throw_dict["Tags"] = throw.tags
            damage_dict = {}
            damage_dict["Original"] = throw.original_values[0]
            damage_dict["New"] = throw.damage
            angle_dict = {}
            angle_dict["Original"] = throw.original_values[1]
            angle_dict["New"] = throw.angle
            growth_dict = {}
            growth_dict["Original"] = throw.original_values[2]
            growth_dict["New"] = throw.growth
            set_dict = {}
            set_dict["Original"] = throw.original_values[3]
            set_dict["New"] = throw.set_kb
            base_dict = {}
            base_dict["Original"] = throw.original_values[4]
            base_dict["New"] = throw.base
            element_dict = {}
            element_dict["Original"] = throw_elements[throw.original_values[5]]
            element_dict["New"] = throw_elements[throw.element]

            if verbose:
                damage_dict["Notes"] = throw.log_notes[0]
                angle_dict["Notes"] = throw.log_notes[1]
                growth_dict["Notes"] = throw.log_notes[2]
                set_dict["Notes"] = throw.log_notes[3]
                base_dict["Notes"] = throw.log_notes[4]
                element_dict["Notes"] = throw.log_notes[5]
                
            throw_dict["Damage"] = damage_dict
            throw_dict["Angle"] = angle_dict
            throw_dict["Knockback Growth"] = growth_dict
            throw_dict["Set Knockback"] = set_dict
            throw_dict["Base Knockback"] = base_dict
            throw_dict["Element"] = element_dict
            
            all_throws_dict[throw.name] = throw_dict

        for attribute in fighter.attributes:
            attribute_dict = {}
            attribute_dict["Tags"] = attribute.tags
            value_dict = {}
            value_dict["Original"] = round(attribute.original_value, 4)
            value_dict["New"] = round(attribute.value, 4)
            if verbose:
                value_dict["Notes"] = attribute.log_notes
            attribute_dict["Value"] = value_dict

            all_attr_dict[attribute.name] = attribute_dict

        for attribute in fighter.special_attributes:
            attribute_dict = {}
            attribute_dict["Tags"] = attribute.tags
            value_dict = {}
            value_dict["Original"] = round(attribute.original_value, 4)
            value_dict["New"] = round(attribute.value, 4)
            if verbose:
                value_dict["Notes"] = attribute.log_notes
            attribute_dict["Value"] = value_dict

            all_special_dict[attribute.name] = attribute_dict

        for attribute in fighter.article_attributes:
            attribute_dict = {}
            attribute_dict["Tags"] = attribute.tags
            value_dict = {}
            value_dict["Original"] = round(attribute.original_value, 4)
            value_dict["New"] = round(attribute.value, 4)
            if verbose:
                value_dict["Notes"] = attribute.log_notes
            attribute_dict["Value"] = value_dict

            all_special_dict[attribute.name] = attribute_dict
        fighter_dict["Attacks"] = all_attacks_dict
        fighter_dict["Throws"] = all_throws_dict
        fighter_dict["Attributes"] = all_attr_dict
        fighter_dict["Special"] = all_special_dict
        log_dict[fighter.name] = fighter_dict
    filename = ""
    if len(code) > 0:
        filename = code + ".json"
    else:
        filename = "output.json"
    with open('json/' + filename, 'w') as fp:
        json.dump(log_dict, fp, indent=6)










        
