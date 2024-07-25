import characters, json
ALL_ATTACK_TAGS = ["Attack", "Normal", "Special", "Shine", "Recovery", "Up B", "Down B", "Side B", "Neutral B", "N-Air", "F-Air", "B-Air", "D-Air", "Up Air", "Z-Air",
            "Pummel", "Jab", "F-Tilt", "Up-Tilt", "Down-Tilt", "Dash Attack", "Up Smash",
            "Down Smash", "Forward Smash", "Projectile", "Multi-hit", "Spike", "Meteor",
            "Sweet Spot", "Sour Spot", "Weak Hit", "Strong Hit", "Late Hit", ]
ALL_THROW_TAGS = ["Throw", "Normal", "Special", "Kill Throw", "Forward Throw",
            "Down Throw", "Up Throw", "Back Throw", "Combo Throw", "Command Throw"]
ALL_ATTRIBUTE_TAGS = ["Attribute", "Article", "Special", "Common", "Movement", "Animation", "Frames", "Scale",
                  "Projectile", "Etc", "Property"]
def start():
    adv_dict = {}
    adv_dict["All Attacks"] = ALL_ATTACK_TAGS
    adv_dict["All Throws"] = ALL_THROW_TAGS
    adv_dict["All Attributes"] = ALL_ATTRIBUTE_TAGS
    
    for fighter in characters.fighters:
        fighter_dict = {}
        attacks = []
        throws = []
        attributes = []
        for attack in fighter.attacks:
            attacks.append(attack.name)
        for throw in fighter.throws:
            throws.append(throw.name)
        for attribute in fighter.attributes:
            attributes.append(attribute.name)
        for attribute in fighter.special_attributes:
            attributes.append(attribute.name)
        for attribute in fighter.article_attributes:
            attributes.append(attribute.name)
        fighter_dict["Attacks"] = attacks
        fighter_dict["Throws"] = throws
        fighter_dict["Attributes"] = attributes
        adv_dict[fighter.name] = fighter_dict

    with open("adv.json", "w") as output:
        json.dump(adv_dict, output)

