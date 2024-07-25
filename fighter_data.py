import characters
# Script pulls data from subactions and attribute data and aims to abstract them to make each item
# Easier to work with later.
def attack_from_subaction(subactions, action_id):
    hitboxes = []
    if len(subactions[action_id].hitboxes) < 1:
        return []
    for hitbox in subactions[action_id].hitboxes:
        hitboxes.append(hitbox)
    return hitboxes

def merge_from_subactions(subactions, action_ids):
    hitboxes = []
    for i in range(len(action_ids)):
        for hitbox in attack_from_subaction(subactions, action_ids[i]):
            hitboxes.append(hitbox)
    return hitboxes

def add_all(files):
    add_common_hitboxes()
    add_special_data(files)

def add_common_hitboxes():
    for fighter in characters.fighters:
        actions = fighter.subactions
        # Normals
        fighter.add_attack(attack_from_subaction(actions, 46), "Jab 1", 0, ["normal", "jab"])
        fighter.add_attack(attack_from_subaction(actions, 47), "Jab 2", 0, ["normal", "jab"])
        fighter.add_attack(attack_from_subaction(actions, 48), "Jab 3", 0, ["normal", "jab"])
        fighter.add_attack(attack_from_subaction(actions, 52), "Dash Attack", 0, ["normal", "dashattack"])
        fighter.add_attack(merge_from_subactions(actions, [53,54,55,56,57]), "Forward Tilt", 0, ["normal", "ftilt"])
        fighter.add_attack(attack_from_subaction(actions, 58), "Up Tilt", 0, ["normal", "uptilt"])
        fighter.add_attack(attack_from_subaction(actions, 59), "Down Tilt", 0, ["normal", "dtilt"])
        fighter.add_attack(merge_from_subactions(actions, [60,61,62,63,64]), "Forward Smash", 0, ["normal", "fsmash"])
        fighter.add_attack(attack_from_subaction(actions, 66), "Up Smash", 0, ["normal", "upsmash"])
        fighter.add_attack(attack_from_subaction(actions, 67), "Down Smash", 0, ["normal", "downsmash"])
        fighter.add_attack(attack_from_subaction(actions, 68), "Neutral Aerial", 0, ["normal", "nair"])
        fighter.add_attack(attack_from_subaction(actions, 69), "Forward Aerial", 0, ["normal", "fair"])
        fighter.add_attack(attack_from_subaction(actions, 70), "Back Aerial", 0, ["normal", "bair"])
        fighter.add_attack(attack_from_subaction(actions, 70), "Up Aerial", 0, ["normal", "upair"])
        fighter.add_attack(attack_from_subaction(actions, 72), "Down Aerial", 0, ["normal", "dair"])
        fighter.add_attack(attack_from_subaction(actions, 187), "Get-Up Attack Up", 4, ["normal", "recovery"])
        fighter.add_attack(attack_from_subaction(actions, 195), "Get-Up Attack Down", 4, ["normal", "recovery"])
        fighter.add_attack(attack_from_subaction(actions, 221), "Ledge Attack Slow", 4, ["normal", "recovery"])
        fighter.add_attack(attack_from_subaction(actions, 222), "Ledge Attack Fast", 4, ["normal", "recovery"])
        fighter.add_attack(attack_from_subaction(actions, 245), "Pummel", 2, ["normal", "pummel"])
        # Throws
        fighter.add_throw(actions[247].throws[0], "Forward Throw", ["fthrow"])
        fighter.add_throw(actions[248].throws[0], "Back Throw", ["bthrow"])
        fighter.add_throw(actions[249].throws[0], "Up Throw", ["upthrow"])
        fighter.add_throw(actions[250].throws[0], "Down Throw", ["downthrow"])
        # items
        fighter.add_item(attack_from_subaction(actions, 108), "Beam Sword Neutral", 4, ["item"])
        fighter.add_item(attack_from_subaction(actions, 109), "Beam Sword Tilt", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 110), "Beam Sword Smash", 8, ["item"])
        fighter.add_item(attack_from_subaction(actions, 111), "Beam Sword Dash", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 112), "Home-run Bat Neutral", 4, ["item"])
        fighter.add_item(attack_from_subaction(actions, 113), "Home-run Bat Tilt", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 114), "Home-run Bat Smash", 10, ["item"])
        fighter.add_item(attack_from_subaction(actions, 115), "Home-run Bat Dash", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 116), "Parasol Neutral", 4, ["item"])
        fighter.add_item(attack_from_subaction(actions, 117), "Parasol Tilt", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 118), "Parasol Smash", 8, ["item"])
        fighter.add_item(attack_from_subaction(actions, 119), "Parasol Dash", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 120), "Fan Neutral", 4, ["item"])
        fighter.add_item(attack_from_subaction(actions, 121), "Fan Tilt", 6, ["item"])
        fighter.add_item(attack_from_subaction(actions, 122), "Fan Smash", 9, ["item"])
        fighter.add_item(attack_from_subaction(actions, 123), "Fan Dash", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 124), "Star Rod Neutral", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 125), "Star Rod Tilt", 6, ["item"])
        fighter.add_item(attack_from_subaction(actions, 126), "Star Rod Smash", 8, ["item"])
        fighter.add_item(attack_from_subaction(actions, 127), "Star Rod Dash", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 128), "Lip's Stick Neutral", 5, ["item"])
        fighter.add_item(attack_from_subaction(actions, 129), "Lip's Stick Tilt", 6, ["item"])
        fighter.add_item(attack_from_subaction(actions, 130), "Lip's Stick Smash", 8, ["item"])
        fighter.add_item(attack_from_subaction(actions, 131), "Lip's Stick Dash", 5, ["item"])
        fighter.add_item(merge_from_subactions(actions, [144, 145]), "Screw Attack", 2, ["item"])

def add_special_data(files):
    # Bowser
    bowser = characters.find_fighter("Bowser")
    # Special Attacks
    bowser.add_attack(attack_from_subaction(bowser.subactions, 301), "Koopa Klaw")
    bowser.add_attack(attack_from_subaction(bowser.subactions, 311), "Whirling Fortress")
    bowser.add_attack(attack_from_subaction(bowser.subactions, 312), "Aerial Whirling Fortress")
    bowser.add_attack(merge_from_subactions(bowser.subactions, [313, 314]), "Bowser Bomb")
    bowser.add_throw(bowser.subactions[304].throws[0], "Koopa Klaw Forward Throw")
    bowser.add_throw(bowser.subactions[305].throws[0], "Koopa Klaw Back Throw")
    bowser.add_throw(bowser.subactions[309].throws[0], "Aerial Koopa Klaw Forward Throw")
    bowser.add_throw(bowser.subactions[310].throws[0], "Aerial Koopa Klaw Back Throw")
    
    # Special Attributes
    attribute_data = bowser.special_attribute_data
    bowser.add_attribute_special(attribute_data, 0x00, "Passive Super Armor")
    bowser.add_attribute_special(attribute_data, 0x08, "Flame Breath Recharge Rate: Fuel")
    bowser.add_attribute_special(attribute_data, 0x0C, "Flame Breath Recharge Rate: Flame Size")
    bowser.add_attribute_special(attribute_data, 0x10, "Flame Breath Max Fuel")
    bowser.add_attribute_special(attribute_data, 0x2C, "Koopa Klaw Bite Damage", True)
    bowser.add_attribute_special(attribute_data, 0x4C, "Koopa Klaw Grab Duration")
    bowser.add_attribute_special(attribute_data, 0x54, "Whirling Fortress Aerial Vertical Momentum")
    bowser.add_attribute_special(attribute_data, 0x58, "Whirling Fortress Gravity")
    bowser.add_attribute_special(attribute_data, 0x5C, "Whirling Fortress Aerial Vertical Momentum 2nd Half")
    bowser.add_attribute_special(attribute_data, 0x60, "Whirling Fortress Ground Speed")
    bowser.add_attribute_special(attribute_data, 0x64, "Whirling Fortress Momentum Preservation")
    bowser.add_attribute_special(attribute_data, 0x68, "Whirling Fortress Grounded Turning Speed")
    bowser.add_attribute_special(attribute_data, 0x6C, "Whirling Fortress Aerial Mobility")
    bowser.add_attribute_special(attribute_data, 0x7C, "Whirling Fortress Landing Lag")
    bowser.add_attribute_special(attribute_data, 0x80, "Bowser Bomb Aerial Horizontal Momentum Multiplier")
    bowser.add_attribute_special(attribute_data, 0x84, "Bowser Bomb Initial Aerial Vertical Momentum")
    bowser.add_attribute_special(attribute_data, 0x88, "Bowser Bomb Horizontal Momentum Preservation")
    bowser.add_attribute_special(attribute_data, 0x8C, "Bowser Bomb Vertical Momentum Deceleration Rate")
    bowser.add_attribute_special(attribute_data, 0x90, "Bowser Bomb Gravity Scale")
    bowser.add_attribute_special(attribute_data, 0x94, "Bowser Bomb Descent Speed")
    # Articles
    flame_data = bowser.articles_datas[0]
    bowser.add_attribute_article(flame_data, 0x08, "Flame Velocity")
    bowser.add_attribute_article(flame_data, 0x0C, "Flame Acceleration")
    bowser.add_attribute_article(flame_data, 0x10, "Flame Min. Angle")
    bowser.add_attribute_article(flame_data, 0x14, "Flame Max Angle")
    # Captain Falcon
    falcon = characters.find_fighter("Captain Falcon")
    falcon.add_attack(merge_from_subactions(falcon.subactions, [301, 302]), "Falcon Punch")
    falcon.add_attack(attack_from_subaction(falcon.subactions, 304), "Raptor Boost (Ground)")
    falcon.add_attack(attack_from_subaction(falcon.subactions, 306), "Raptor Boost (Air)")
    falcon.add_attack(attack_from_subaction(falcon.subactions, 309), "Falcon Dive")
    falcon.add_attack(merge_from_subactions(falcon.subactions, [311, 313]), "Falcon Kick")
    falcon.add_attack(attack_from_subaction(falcon.subactions, 314), "Falcon Kick Landing")
    attribute_data = falcon.special_attribute_data
    falcon.add_attribute_special(attribute_data, 0x08, "Falcon Punch Momentum")
    falcon.add_attribute_special(attribute_data, 0x0C, "Aerial Falcon Punch Angle Difference")
    falcon.add_attribute_special(attribute_data, 0x10, "Aerial Falcon Punch Vertical Momentum")
    falcon.add_attribute_special(attribute_data, 0x14, "Raptor Boost Gravity After Hit")
    falcon.add_attribute_special(attribute_data, 0x18, "Raptor Boost Gravity After Whiff A")
    falcon.add_attribute_special(attribute_data, 0x1C, "Raptor Boost Gravity After Whiff B")
    falcon.add_attribute_special(attribute_data, 0x38, "Raptor Boost Whiff Landing Lag")
    falcon.add_attribute_special(attribute_data, 0x3C, "Raptor Boost Success Landing Lag")
    falcon.add_attribute_special(attribute_data, 0x40, "Falcon Dive Air Friction Multiplier")
    falcon.add_attribute_special(attribute_data, 0x44, "Falcon Dive Horizontal Momentum")
    falcon.add_attribute_special(attribute_data, 0x48, "Falcon Dive Freefall Speed Multiplier")
    falcon.add_attribute_special(attribute_data, 0x4C, "Falcon Dive Landing Lag")
    falcon.add_attribute_special(attribute_data, 0x60, "Falcon Dive Gravity During Throw")
    falcon.add_attribute_special(attribute_data, 0x74, "Falcon Kick Speed Modifier After Hit")
    falcon.add_attribute_special(attribute_data, 0x7C, "Falcon Kick Ground Lag Multiplier")
    falcon.add_attribute_special(attribute_data, 0x80, "Falcon Kick Landing Lag Multiplier")
    falcon.add_attribute_special(attribute_data, 0x84, "Falcon Kick Ground Traction")
    falcon.add_attribute_special(attribute_data, 0x88, "Falcon Kick Landing Traction")
    
    # Donkey Kong
    dk = characters.find_fighter("Donkey Kong")
    dk.add_attack(merge_from_subactions(dk.subactions, [322, 327]), "Giant Punch (No Charge)")
    dk.add_attack(merge_from_subactions(dk.subactions, [323, 328]), "Giant Punch (Charged)")
    dk.add_attack(attack_from_subaction(dk.subactions, 329), "Headbutt (Ground)")
    dk.add_attack(attack_from_subaction(dk.subactions, 330), "Headbutt (Air)")
    dk.add_attack(attack_from_subaction(dk.subactions, 331), "Spinning Kong (Ground)")
    dk.add_attack(attack_from_subaction(dk.subactions, 332), "Spinning Kong (Air)")
    dk.add_attack(attack_from_subaction(dk.subactions, 334), "Hand Slap")
    attribute_data = dk.special_attribute_data
    dk.add_attribute_special(attribute_data, 0x20, "Cargo Hold Turn Speed")
    dk.add_attribute_special(attribute_data, 0x24, "Cargo Hold Jump Startup")
    dk.add_attribute_special(attribute_data, 0x28, "Cargo Hold Jump Landing Lag")
    dk.add_attribute_special(attribute_data, 0x2C, "Giant Punch Arm Swings Needed To Full Charge", True)
    dk.add_attribute_special(attribute_data, 0x30, "Giant Punch Damage Increase Per Swing", True)
    dk.add_attribute_special(attribute_data, 0x34, "Giant Punch Grounded Forward Velocity (Charged)")
    dk.add_attribute_special(attribute_data, 0x38, "Giant Punch Landing Lag")
    dk.add_attribute_special(attribute_data, 0x40, "Headbutt Momentum Transfer Modifier")
    dk.add_attribute_special(attribute_data, 0x44, "Headbutt Gravity")
    dk.add_attribute_special(attribute_data, 0x4C, "Spinning Kong Aerial Vertical Velocity")
    dk.add_attribute_special(attribute_data, 0x50, "Spinning Kong Aerial Gravity")
    dk.add_attribute_special(attribute_data, 0x54, "Spinning Kong Grounded Horizontal Velocity")
    dk.add_attribute_special(attribute_data, 0x58, "Spinning Kong Aerial Horizontal Velocity")
    dk.add_attribute_special(attribute_data, 0x5C, "Spinning Kong Grounded Mobility")
    dk.add_attribute_special(attribute_data, 0x60, "Spinning Kong Aerial Mobility")
    dk.add_attribute_special(attribute_data, 0x64, "Spinning Kong Landing Lag")
    dk.add_attribute_special(attribute_data, 0x68, "Hand Slap Hitbox X Offset 1")
    dk.add_attribute_special(attribute_data, 0x6C, "Hand Slap Hitbox X Offset 2")

    # Dr. Mario
    dr = characters.find_fighter("Dr. Mario")
    dr.add_attack(attack_from_subaction(dr.subactions, 297), "Super Sheet")
    dr.add_attack(merge_from_subactions(dr.subactions, [299, 300]), "Super Jump Punch")
    dr.add_attack(merge_from_subactions(dr.subactions, [301, 302]), "Dr. Tornado")
    # Special Attributes
    attribute_data = dr.special_attribute_data
    dr.add_attribute_special(attribute_data, 0x00, "Super Sheet Horizontal Momentum")
    dr.add_attribute_special(attribute_data, 0x04, "Super Sheet Horizontal Velocity")
    dr.add_attribute_special(attribute_data, 0x08, "Super Sheet Vertical Momentum")
    dr.add_attribute_special(attribute_data, 0x0C, "Super Sheet Gravity")
    dr.add_attribute_special(attribute_data, 0x10, "Super Sheet Max Falling Speed")
    dr.add_attribute_special(attribute_data, 0x74, "Super Sheet Reflection Bubble Size")
    dr.add_attribute_special(attribute_data, 0x78, "Super Sheet Reflection Damage Multiplier")
    dr.add_attribute_special(attribute_data, 0x7C, "Super Sheet Projectile Reflection Speed Multiplier")
    dr.add_attribute_special(attribute_data, 0x18, "Super Jump Punch Freefall Mobility")
    dr.add_attribute_special(attribute_data, 0x1C, "Super Jump Punch Landing Lag")
    dr.add_attribute_special(attribute_data, 0x28, "Super Jump Punch Max Angle Change")
    dr.add_attribute_special(attribute_data, 0x2C, "Super Jump Punch Initial Horizontal Momentum")
    dr.add_attribute_special(attribute_data, 0x30, "Super Jump Punch Initial Gravity")
    dr.add_attribute_special(attribute_data, 0x34, "Super Jump Punch Initial Vertical Momentum")
    dr.add_attribute_special(attribute_data, 0x38, "Dr. Tornado Grounded Rise Resistance")
    dr.add_attribute_special(attribute_data, 0x3C, "Dr. Tornado Base Air Speed")
    dr.add_attribute_special(attribute_data, 0x40, "Dr. Tornado Horizontal Velocity Limit")
    dr.add_attribute_special(attribute_data, 0x44, "Dr. Tornado Horizontal Acceleration")
    dr.add_attribute_special(attribute_data, 0x48, "Dr. Tornado Horizontal Drift")
    dr.add_attribute_special(attribute_data, 0x4C, "Dr. Tornado Deceleration Rate")
    dr.add_attribute_special(attribute_data, 0x54, "Dr. Tornado Velocity Gain From B Press")
    dr.add_attribute_special(attribute_data, 0x58, "Dr. Tornado Terminal Velocity")
    dr.add_attribute_special(attribute_data, 0x5C, "Dr. Tornado Landing Lag", True)
    # Articles
    megavitamin_data = dr.articles_datas[0]
    dr.add_attribute_article(megavitamin_data, 0x00, "Megavitamin Initial Velocity")
    dr.add_attribute_article(megavitamin_data, 0x04, "Megavitamin Angle")
    dr.add_attribute_article(megavitamin_data, 0x08, "Megavitamin Duration")
    dr.add_attribute_article(megavitamin_data, 0x10, "Megavitamin Bounce Height")
    
    # Falco
    falco = characters.find_fighter("Falco")
    falco.add_attack(merge_from_subactions(falco.subactions, [308, 309]), "Fire Bird")
    falco.add_attack(attack_from_subaction(falco.subactions, 313), "Shine")
    attribute_data = falco.special_attribute_data
    # Special Attributes
    falco.add_attribute_special(attribute_data, 0x10, "Blaster Launch Angle")
    falco.add_attribute_special(attribute_data, 0x14, "Blaster Launch Speed")
    falco.add_attribute_special(attribute_data, 0x18, "Blaster Landing Lag")
    falco.add_attribute_special(attribute_data, 0x24, "Phantasm Gravity Frame Delay")
    falco.add_attribute_special(attribute_data, 0x28, "Phantasm Initial Horizontal Momentum")
    falco.add_attribute_special(attribute_data, 0x38, "Phantasm Ground Friction")
    falco.add_attribute_special(attribute_data, 0x3C, "Phantasm Air Dash Speed")
    falco.add_attribute_special(attribute_data, 0x40, "Phantasm Air Dash Momentum")
    falco.add_attribute_special(attribute_data, 0x44, "Phantasm Air Dash Vertical Deceleration")
    falco.add_attribute_special(attribute_data, 0x48, "Phantasm Ending Gravity")
    falco.add_attribute_special(attribute_data, 0x50, "Phantasm Landing Lag")
    falco.add_attribute_special(attribute_data, 0x54, "Fire Bird Gravity Frame Delay")
    falco.add_attribute_special(attribute_data, 0x58, "Fire Bird Startup Horizontal Momentum")
    falco.add_attribute_special(attribute_data, 0x5C, "Fire Bird Startup Aerial Momentum Preservation")
    falco.add_attribute_special(attribute_data, 0x60, "Fire Bird Fall Acceleration")
    falco.add_attribute_special(attribute_data, 0x68, "Fire Bird Frames of Travel")
    falco.add_attribute_special(attribute_data, 0x70, "Fire Bird Aerial Ending Momentum")
    falco.add_attribute_special(attribute_data, 0x74, "Fire Bird Travel Speed")
    falco.add_attribute_special(attribute_data, 0x78, "Fire Bird Reverse Acceleration")
    falco.add_attribute_special(attribute_data, 0x7C, "Fire Bird Grounded Ending Momentum")
    falco.add_attribute_special(attribute_data, 0x84, "Fire Bird Bounce Horizontal Velocity")
    falco.add_attribute_special(attribute_data, 0x90, "Fire Bird Landing Lag")
    falco.add_attribute_special(attribute_data, 0x94, "Fire Bird Landing Lag After Bounce")
    falco.add_attribute_special(attribute_data, 0x98, "Reflector Release Frames")
    falco.add_attribute_special(attribute_data, 0x9C, "Reflector Turn Animation Frames")
    falco.add_attribute_special(attribute_data, 0xA4, "Reflector Gravity Frame Delay")
    falco.add_attribute_special(attribute_data, 0xA8, "Reflector Momentum Preservation")
    falco.add_attribute_special(attribute_data, 0xAC, "Reflector Fall Acceleration")
    falco.add_attribute_special(attribute_data, 0xB0, "Reflector Max Damage Reflectable", True)
    falco.add_attribute_special(attribute_data, 0xC8, "Reflector Reflection Damage Multiplier")
    falco.add_attribute_special(attribute_data, 0xCC, "Reflector Reflection Speed Multiplier")
    # Articles
    # Laser
    laser_data = falco.articles_datas[0]
    falco.add_attribute_article(laser_data, 0x0, "Laser Duration")
    falco.add_attribute_article(laser_data, 0x4, "Laser Max Horizontal Stretch")
    # Phantasm
    phantasm_data = falco.articles_datas[1]
    falco.add_attribute_article(laser_data, 0x0, "Phantasm Duration of After Image", 1)

    # Fox
    fox = characters.find_fighter("Fox")
    fox.add_attack(attack_from_subaction(fox.subactions, 307), "Fire Fox (Start)")
    fox.add_attack(merge_from_subactions(fox.subactions, [308, 309]), "Fire Fox")
    fox.add_attack(attack_from_subaction(fox.subactions, 313), "Shine")
    attribute_data = fox.special_attribute_data
    fox.add_attribute_special(attribute_data, 0x10, "Blaster Launch Angle")
    fox.add_attribute_special(attribute_data, 0x14, "Blaster Launch Speed")
    fox.add_attribute_special(attribute_data, 0x18, "Blaster Landing Lag")
    fox.add_attribute_special(attribute_data, 0x24, "Illusion Gravity Frame Delay")
    fox.add_attribute_special(attribute_data, 0x28, "Illusion Initial Horizontal Momentum")
    fox.add_attribute_special(attribute_data, 0x38, "Illusion Ground Friction")
    fox.add_attribute_special(attribute_data, 0x3C, "Illusion Air Dash Speed")
    fox.add_attribute_special(attribute_data, 0x40, "Illusion Air Dash Momentum")
    fox.add_attribute_special(attribute_data, 0x44, "Illusion Air Dash Vertical Deceleration")
    fox.add_attribute_special(attribute_data, 0x48, "Illusion Ending Gravity")
    fox.add_attribute_special(attribute_data, 0x50, "Illusion Landing Lag")
    fox.add_attribute_special(attribute_data, 0x54, "Fire Fox Gravity Frame Delay")
    fox.add_attribute_special(attribute_data, 0x58, "Fire Fox Startup Horizontal Momentum")
    fox.add_attribute_special(attribute_data, 0x5C, "Fire Fox Startup Aerial Momentum Preservation")
    fox.add_attribute_special(attribute_data, 0x60, "Fire Fox Fall Acceleration")
    fox.add_attribute_special(attribute_data, 0x68, "Fire Fox Frames of Travel")
    fox.add_attribute_special(attribute_data, 0x70, "Fire Fox Aerial Ending Momentum")
    fox.add_attribute_special(attribute_data, 0x74, "Fire Fox Travel Speed")
    fox.add_attribute_special(attribute_data, 0x78, "Fire Fox Reverse Acceleration")
    fox.add_attribute_special(attribute_data, 0x7C, "Fire Fox Grounded Ending Momentum")
    fox.add_attribute_special(attribute_data, 0x84, "Fire Fox Bounce Horizontal Velocity")
    fox.add_attribute_special(attribute_data, 0x90, "Fire Fox Landing Lag")
    fox.add_attribute_special(attribute_data, 0x94, "Fire Fox Landing Lag After Bounce")
    fox.add_attribute_special(attribute_data, 0x98, "Reflector Release Frames")
    fox.add_attribute_special(attribute_data, 0x9C, "Reflector Turn Animation Frames")
    fox.add_attribute_special(attribute_data, 0xA4, "Reflector Gravity Frame Delay")
    fox.add_attribute_special(attribute_data, 0xA8, "Reflector Momentum Preservation")
    fox.add_attribute_special(attribute_data, 0xAC, "Reflector Fall Acceleration")
    fox.add_attribute_special(attribute_data, 0xB0, "Reflector Max Damage Reflectable", True)
    fox.add_attribute_special(attribute_data, 0xC8, "Reflector Reflection Damage Multiplier")
    fox.add_attribute_special(attribute_data, 0xCC, "Reflector Reflection Speed Multiplier")
    # Articles
    # Laser
    blaster_data = fox.articles_datas[0]
    fox.add_attribute_article(blaster_data, 0x0, "Laser Duration")
    fox.add_attribute_article(blaster_data, 0x4, "Laser Max Horizontal Stretch")
    # Phantasm
    illusion_data = falco.articles_datas[1]
    fox.add_attribute_article(laser_data, 0x0, "Illusion Duration of After Image", 1)

    # Ganondorf
    ganon = characters.find_fighter("Ganondorf")
    ganon.add_attack(merge_from_subactions(ganon.subactions, [301, 302]), "Warlock Punch")
    ganon.add_attack(attack_from_subaction(ganon.subactions, 304), "Gerudo Dragon (Ground)")
    ganon.add_attack(attack_from_subaction(ganon.subactions, 306), "Gerudo Dragon (Air)")
    ganon.add_attack(attack_from_subaction(ganon.subactions, 309), "Dark Dive")
    ganon.add_attack(merge_from_subactions(ganon.subactions, [311, 313]), "Wizard's Foot")
    ganon.add_attack(attack_from_subaction(ganon.subactions, 314), "Wizard's Foot Landing")
    attribute_data = ganon.special_attribute_data
    ganon.add_attribute_special(attribute_data, 0x08, "Warlock Punch Momentum")
    ganon.add_attribute_special(attribute_data, 0x0C, "Aerial Warlock Punch Angle Difference")
    ganon.add_attribute_special(attribute_data, 0x10, "Aerial Warlock Punch Vertical Momentum")
    ganon.add_attribute_special(attribute_data, 0x14, "Gerudo Dragon Gravity After Hit")
    ganon.add_attribute_special(attribute_data, 0x18, "Gerudo Dragon Gravity After Whiff A")
    ganon.add_attribute_special(attribute_data, 0x1C, "Gerudo Dragon Gravity After Whiff B")
    ganon.add_attribute_special(attribute_data, 0x38, "Gerudo Dragon Whiff Landing Lag")
    ganon.add_attribute_special(attribute_data, 0x3C, "Gerudo Dragon Success Landing Lag")
    ganon.add_attribute_special(attribute_data, 0x40, "Dark Dive Air Friction Multiplier")
    ganon.add_attribute_special(attribute_data, 0x44, "Dark Dive Horizontal Momentum")
    ganon.add_attribute_special(attribute_data, 0x48, "Dark Dive Freefall Speed Multiplier")
    ganon.add_attribute_special(attribute_data, 0x4C, "Dark Dive Landing Lag")
    ganon.add_attribute_special(attribute_data, 0x60, "Dark Dive Gravity During Throw")
    ganon.add_attribute_special(attribute_data, 0x74, "Wizard's Foot Speed Modifier After Hit")
    ganon.add_attribute_special(attribute_data, 0x7C, "Wizard's Foot Ground Lag Multiplier")
    ganon.add_attribute_special(attribute_data, 0x80, "Wizard's Foot Landing Lag Multiplier")
    ganon.add_attribute_special(attribute_data, 0x84, "Wizard's Foot Ground Traction")
    ganon.add_attribute_special(attribute_data, 0x88, "Wizard's Foot Landing Traction")
    
    # Popo
    popo = characters.find_fighter("Popo")
    popo.add_attack(attack_from_subaction(popo.subactions, 295), "Ice Shot")
    attribute_data = popo.special_attribute_data
    popo.add_attribute_special(attribute_data, 0x00, "Spawn Offset")
    popo.add_attribute_special(attribute_data, 0x04, "Ice Shot Aerial Vertical Momentum")
    popo.add_attribute_special(attribute_data, 0x08, "Ice Shot Landing Lag")
    popo.add_attribute_special(attribute_data, 0x0C, "Ice Shot Spawn X-Offset")
    popo.add_attribute_special(attribute_data, 0x10, "Ice Shot Spawn Y-Offset")
    popo.add_attribute_special(attribute_data, 0x20, "Squall Hammer Height Gain From B")
    popo.add_attribute_special(attribute_data, 0x24, "Squall Hammer Base Vertical Velocity")
    popo.add_attribute_special(attribute_data, 0x2C, "Squall Hammer Initial Horizontal Velocity")
    popo.add_attribute_special(attribute_data, 0x30, "Squall Hammer Slope Angle Modifier")
    popo.add_attribute_special(attribute_data, 0x34, "Squall Hammer Aerial Horizontal Mobility")
    popo.add_attribute_special(attribute_data, 0x38, "Squall Hammer Ground Horizontal Mobility")
    popo.add_attribute_special(attribute_data, 0x3C, "Squall Hammer Momentum Gain From B")
    popo.add_attribute_special(attribute_data, 0x44, "Squall Hammer Horizontal Wall Bounce")
    popo.add_attribute_special(attribute_data, 0x48, "Squall Hammer Vertical Wall Bounce")
    popo.add_attribute_special(attribute_data, 0x4C, "Squall Hammer Solo Gravity")
    popo.add_attribute_special(attribute_data, 0x50, "Squall Hammer Duo Gravity")
    popo.add_attribute_special(attribute_data, 0x54, "Squall Hammer Solo Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0x58, "Squall Hammer Duo Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0x5C, "Squall Hammer Duration of Modified Gravity")
    popo.add_attribute_special(attribute_data, 0x60, "Squall Hammer Uphill Friction")
    popo.add_attribute_special(attribute_data, 0x64, "Squall Hammer Aerial Initial Horizontal Velocity")
    popo.add_attribute_special(attribute_data, 0x6C, "Squall Hammer Ground Friction")
    popo.add_attribute_special(attribute_data, 0x70, "Squall Hammer Landing Lag")
    popo.add_attribute_special(attribute_data, 0x74, "Belay Freefall Air Speed Multiplier")
    popo.add_attribute_special(attribute_data, 0x78, "Belay Landing Lag")
    popo.add_attribute_special(attribute_data, 0x84, "Belay Horizontal Velocity Deceleration")
    popo.add_attribute_special(attribute_data, 0x8C, "Belay Fall Acceleration")
    popo.add_attribute_special(attribute_data, 0x94, "Belay Duo Positive Vertical Momentum")
    popo.add_attribute_special(attribute_data, 0x98, "Belay Duo Negative Vertical Momentum")
    popo.add_attribute_special(attribute_data, 0x9C, "Belay Gravity")
    popo.add_attribute_special(attribute_data, 0xA0, "Belay Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0xA4, "Belay Solo Climber Vertical Momentum")
    popo.add_attribute_special(attribute_data, 0xA8, "Belay Solo Climber Gravity")
    popo.add_attribute_special(attribute_data, 0xAC, "Belay Solo Climber Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0xB0, "Belay Air Mobility Multiplier")
    popo.add_attribute_special(attribute_data, 0xB4, "Belay Air Speed Multiplier")
    popo.add_attribute_special(attribute_data, 0xB8, "Blizzard Delay Between Shots")
    popo.add_attribute_special(attribute_data, 0xBC, "Blizzard Hitboxes X Offset")
    popo.add_attribute_special(attribute_data, 0xC0, "Blizzard Hitboxes Y Offset")
    popo.add_attribute_special(attribute_data, 0xDC, "CPU Squall Hammer Height Gain From B")
    popo.add_attribute_special(attribute_data, 0xE0, "CPU Squall Hammer Base Vertical Velocity")
    popo.add_attribute_special(attribute_data, 0xE8, "CPU Squall Hammer Initial Horizontal Velocity")
    popo.add_attribute_special(attribute_data, 0xEC, "CPU Squall Hammer Slope Angle Modifier")
    popo.add_attribute_special(attribute_data, 0xF0, "CPU Squall Hammer Aerial Horizontal Mobility")
    popo.add_attribute_special(attribute_data, 0xF4, "CPU Squall Hammer Ground Horizontal Mobility")
    popo.add_attribute_special(attribute_data, 0xF8, "CPU Squall Hammer Momentum Gain From B")
    popo.add_attribute_special(attribute_data, 0x100, "CPU Squall Hammer Horizontal Wall Bounce")
    popo.add_attribute_special(attribute_data, 0x104, "CPU Squall Hammer Vertical Wall Bounce")
    popo.add_attribute_special(attribute_data, 0x108, "CPU Squall Hammer Solo Gravity")
    popo.add_attribute_special(attribute_data, 0x10C, "CPU Squall Hammer Duo Gravity")
    popo.add_attribute_special(attribute_data, 0x110, "CPU Squall Hammer Solo Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0x114, "CPU Squall Hammer Duo Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0x118, "CPU Squall Hammer Duration of Modified Gravity")
    popo.add_attribute_special(attribute_data, 0x11C, "CPU Squall Hammer Uphill Friction")
    popo.add_attribute_special(attribute_data, 0x120, "CPU Squall Hammer Aerial Initial Horizontal Velocity")
    popo.add_attribute_special(attribute_data, 0x128, "CPU Squall Hammer Traction")
    popo.add_attribute_special(attribute_data, 0x12C, "CPU Squall Hammer Landing Lag")
    popo.add_attribute_special(attribute_data, 0x130, "CPU Belay Freefall Air Speed Multiplier")
    popo.add_attribute_special(attribute_data, 0x134, "CPU Belay Landing Lag")
    popo.add_attribute_special(attribute_data, 0x13C, "CPU Belay Horizontal Velocity Deceleration")
    popo.add_attribute_special(attribute_data, 0x144, "CPU Belay Gravity")
    popo.add_attribute_special(attribute_data, 0x148, "CPU Belay Terminal Velocity")
    popo.add_attribute_special(attribute_data, 0x14C, "CPU Belay Solo Climber Vertical Momentum")
    # Articles
    ice_shot_data = popo.articles_datas[0]
    popo.add_attribute_article(ice_shot_data, 0x0, "Ice Shot Duration")
    popo.add_attribute_article(ice_shot_data, 0x10, "Ice Shot Speed")
    popo.add_attribute_article(ice_shot_data, 0x24, "Ice Shot Gravity")
    blizzard_data = popo.articles_datas[1]
    popo.add_attribute_article(blizzard_data, 0x0, "Blizzard Hitbox Duration", 1)
    popo.add_attribute_article(blizzard_data, 0x4, "Blizzard Hitbox Velocity", 1)
    popo.add_attribute_article(blizzard_data, 0x8, "Blizzard Hitbox Rise Acceleration", 1)
    popo.add_attribute_article(blizzard_data, 0xC, "Blizzard Minimum Angle of Hitbox Spread", 1)
    popo.add_attribute_article(blizzard_data, 0x10, "Blizzard Maximum Angle of Hitbox Spread", 1)
    belay_data = popo.articles_datas[2]
    popo.add_attribute_article(belay_data, 0x0, "Belay String Length", 2, True)
    popo.add_attribute_article(belay_data, 0x4, "Belay String Retraction Speed", 2, True)
    popo.add_attribute_article(belay_data, 0x14, "Belay String Gravity", 2)
    popo.add_attribute_article(belay_data, 0x1C, "Belay String Length 2", 2, True)
    popo.add_attribute_article(belay_data, 0x20, "Belay String Elasticity", 2, True)

    # Nana
    nana = characters.find_fighter("Nana")
    nana.add_attack(attack_from_subaction(nana.subactions, 295), "Ice Shot")
    nana.add_attack(attack_from_subaction(nana.subactions, 316), "Belay")

    # Jigglypuff
    puff = characters.find_fighter("Jigglypuff")
    puff.add_attack(merge_from_subactions(puff.subactions, [302, 303, 304, 310, 311, 312]), "Rollout")
    puff.add_attack(attack_from_subaction(puff.subactions, 317), "Pound")
    puff.add_attack(merge_from_subactions(puff.subactions, [321, 319]), "Sing")
    puff.add_attack(merge_from_subactions(puff.subactions, [320, 322, 323, 325]), "Rest")
    attribute_data = puff.special_attribute_data
    puff.add_attribute_special(attribute_data, 0x0, "Jumps Turn Duration", True)
    puff.add_attribute_special(attribute_data, 0x4, "Jumps Horizontal Momentum Backward")
    puff.add_attribute_special(attribute_data, 0x8, "Jumps Horizontal Momentum Forward")
    puff.add_attribute_special(attribute_data, 0xC, "Jumps Turn Momentum")
    puff.add_attribute_special(attribute_data, 0x10, "Jumps Horizontal Momentum Neutral")
    puff.add_attribute_special(attribute_data, 0x14, "Jump 1 Vertical Momentum")
    puff.add_attribute_special(attribute_data, 0x18, "Jump 2 Vertical Momentum")
    puff.add_attribute_special(attribute_data, 0x1C, "Jump 3 Vertical Momentum")
    puff.add_attribute_special(attribute_data, 0x20, "Jump 4 Vertical Momentum")
    puff.add_attribute_special(attribute_data, 0x24, "Jump 5 Vertical Momentum")
    puff.add_attribute_special(attribute_data, 0x28, "Number of Jumps", True)
    puff.add_attribute_special(attribute_data, 0x34, "Rollout Duration", True)
    puff.add_attribute_special(attribute_data, 0x3C, "Rollout Start Air Height Offset")
    puff.add_attribute_special(attribute_data, 0x40, "Rollout Bounciness")
    puff.add_attribute_special(attribute_data, 0x48, "Rollout Gravity During Roll")
    puff.add_attribute_special(attribute_data, 0x4C, "Rollout Base Rolling Speed")
    puff.add_attribute_special(attribute_data, 0x50, "Rollout Max Rolling Speed")
    puff.add_attribute_special(attribute_data, 0x5C, "Rollout Aerial X-Axis Momentum Forward")
    puff.add_attribute_special(attribute_data, 0x60, "Rollout Aerial Initial Momentum")
    puff.add_attribute_special(attribute_data, 0x64, "Rollout Max Momentum")
    puff.add_attribute_special(attribute_data, 0x68, "Rollout Spinning Speed")
    puff.add_attribute_special(attribute_data, 0x6C, "Rollout Spinning Turn Speed")
    puff.add_attribute_special(attribute_data, 0x78, "Rollout Bounciness A")
    puff.add_attribute_special(attribute_data, 0x7C, "Rollout Bounciness B")
    puff.add_attribute_special(attribute_data, 0x80, "Rollout Base Damage")
    puff.add_attribute_special(attribute_data, 0x84, "Rollout Damage Multiplier")
    puff.add_attribute_special(attribute_data, 0x88, "Rollout Horizontal Bounce On Hit")
    puff.add_attribute_special(attribute_data, 0x8C, "Rollout Vertical Bounce on Hit")
    puff.add_attribute_special(attribute_data, 0x90, "Rollout Input Modifier")
    puff.add_attribute_special(attribute_data, 0xA0, "Rollout Charge Rate")
    puff.add_attribute_special(attribute_data, 0xA4, "Rollout Charge Time")
    puff.add_attribute_special(attribute_data, 0xAC, "Rollout Spin Charge Animation")
    puff.add_attribute_special(attribute_data, 0xB8, "Rollout Speed Variable")
    puff.add_attribute_special(attribute_data, 0xBC, "Rollout Spin Animation Post Hit")
    puff.add_attribute_special(attribute_data, 0xC0, "Rollout Air Speed")
    puff.add_attribute_special(attribute_data, 0xC4, "Rollout Turn Rate Variable")
    puff.add_attribute_special(attribute_data, 0xD8, "Rollout Landing Lag")
    puff.add_attribute_special(attribute_data, 0xE4, "Pound Angled Directional Difference")
    puff.add_attribute_special(attribute_data, 0xF0, "Pound Air Travel Distance")
    puff.add_attribute_special(attribute_data, 0xF4, "Pound Air Deceleration Rate")

    # Kirby
    kirby = characters.find_fighter("Kirby")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 322), "Hammer (Ground)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 323), "Hammer (Air)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 325), "Final Cutter")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 336), "Stone")
    kirby.add_attack(merge_from_subactions(kirby.subactions, [368, 369]), "Falcon Punch (Copy)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 388), "Ice Shot (Copy)")
    kirby.add_attack(merge_from_subactions(kirby.subactions, [393, 398]), "Giant Punch (Copy, Uncharged)")
    kirby.add_attack(merge_from_subactions(kirby.subactions, [394, 399]), "Giant Punch (Copy, Charged)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 400), "Nayru's Love (Copy)")
    kirby.add_attack(merge_from_subactions(kirby.subactions, [412, 413, 414, 420, 421, 422]), "Rollout (Copy)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 429), "Shield Breaker (Copy, Uncharged)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 430), "Shield Breaker (Copy, Charged)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 436), "Shadow Ball (Copy, Loop)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 445), "Sausage (Copy)")
    kirby.add_attack(merge_from_subactions(kirby.subactions, [463, 464]), "Warlock Punch (Copy)")
    kirby.add_attack(attack_from_subaction(kirby.subactions, 467), "Flare Blade? (Copy, Uncharged)") # Does a lot of shield damage similar to Marth's
    kirby.add_attack(attack_from_subaction(kirby.subactions, 468), "Flare Blade? (Copy, Charged)")
    attribute_data = kirby.special_attribute_data
    kirby.add_attribute_special(attribute_data, 0x0, "Jumps Turn Duration", True)
    kirby.add_attribute_special(attribute_data, 0x4, "Jumps Horizontal Momentum Backward")
    kirby.add_attribute_special(attribute_data, 0x8, "Jumps Horizontal Momentum Forward")
    kirby.add_attribute_special(attribute_data, 0xC, "Jumps Turn Momentum")
    kirby.add_attribute_special(attribute_data, 0x10, "Jumps Horizontal Momentum Neutral")
    kirby.add_attribute_special(attribute_data, 0x14, "Jump 1 Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x18, "Jump 2 Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x1C, "Jump 3 Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x20, "Jump 4 Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x24, "Jump 5 Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x28, "Number of Jumps", True)
    kirby.add_attribute_special(attribute_data, 0x44, "Inhale Gravity of Inhaled Player")
    kirby.add_attribute_special(attribute_data, 0x48, "Inhale Velocity of Outer Grab Box")
    kirby.add_attribute_special(attribute_data, 0x4C, "Inhale Velocity of Inner Grab Box")
    kirby.add_attribute_special(attribute_data, 0x50, "Inhale Speed")
    kirby.add_attribute_special(attribute_data, 0x54, "Inhale Breakout Resistance")
    kirby.add_attribute_special(attribute_data, 0x58, "Inhale Duration Divisor")
    kirby.add_attribute_special(attribute_data, 0x5C, "Inhale Base Duration")
    kirby.add_attribute_special(attribute_data, 0x60, "Inhale Star Deceleration Rate")
    kirby.add_attribute_special(attribute_data, 0x64, "Inhale Star Duration Divisor")
    kirby.add_attribute_special(attribute_data, 0x68, "Inhale Star Base Duration")
    kirby.add_attribute_special(attribute_data, 0x6C, "Inhale Star Swallow Duration")
    kirby.add_attribute_special(attribute_data, 0x70, "Inhale Star Spin Animation Duration")
    kirby.add_attribute_special(attribute_data, 0x7C, "Inhale Walk Speed")
    kirby.add_attribute_special(attribute_data, 0x80, "Inhale Jump Height")
    kirby.add_attribute_special(attribute_data, 0x84, "Inhale Stop Momentum")
    kirby.add_attribute_special(attribute_data, 0x88, "Inhale Spit Horizontal Velocity")
    kirby.add_attribute_special(attribute_data, 0x8C, "Inhale Spit Velocity Deceleration Rate")
    kirby.add_attribute_special(attribute_data, 0x90, "Inhale Spit Release Angle")
    kirby.add_attribute_special(attribute_data, 0x94, "Inhale Swallow Star Vertical Velocity")
    kirby.add_attribute_special(attribute_data, 0x98, "Inhale Swallow Star Gravity")
    kirby.add_attribute_special(attribute_data, 0x9C, "Inhale Spit Star Release Opponent Horizontal Velocity")
    kirby.add_attribute_special(attribute_data, 0xA0, "Inhale Spit Star Release Opponent Vertical Velocity")
    kirby.add_attribute_special(attribute_data, 0xB0, "Inhale Copy Ability Lose Odds")
    kirby.add_attribute_special(attribute_data, 0xCC, "Hammer Aerial Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0xD0, "Hammer Landing Lag")
    kirby.add_attribute_special(attribute_data, 0xD4, "Final Cutter Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0xD8, "Final Cutter Horizontal Momentum")
    kirby.add_attribute_special(attribute_data, 0xDC, "Final Cutter X-Offset of Projectile")
    kirby.add_attribute_special(attribute_data, 0xE0, "Final Cutter Y-Offset of Projectile")
    kirby.add_attribute_special(attribute_data, 0xEC, "Stone Max Duration", True)
    kirby.add_attribute_special(attribute_data, 0xF0, "Stone Minimum Duration", True)
    kirby.add_attribute_special(attribute_data, 0xFC, "Stone Slide Acceleration")
    kirby.add_attribute_special(attribute_data, 0x100, "Stone Slide Max Speed")
    kirby.add_attribute_special(attribute_data, 0x104, "Stone Gravity")
    kirby.add_attribute_special(attribute_data, 0x108, "Stone HP")
    kirby.add_attribute_special(attribute_data, 0x10C, "Stone Resistance")
    kirby.add_attribute_special(attribute_data, 0x114, "Stone Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x11C, "Flame Breath Recharge Rate: Fuel")
    kirby.add_attribute_special(attribute_data, 0x120, "Flame Breath Recharge Rate: Flame Size")
    kirby.add_attribute_special(attribute_data, 0x124, "Flame Breath Max Fuel")
    kirby.add_attribute_special(attribute_data, 0x168, "Charge Shot Charge Time")
    kirby.add_attribute_special(attribute_data, 0x16C, "Charge Shot Recoil")
    kirby.add_attribute_special(attribute_data, 0x170, "Charge Shot Frames Per Charge Level", True)
    kirby.add_attribute_special(attribute_data, 0x174, "Charge Shot Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x180, "Toad Aerial Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x184, "Toad Fall Acceleration")
    kirby.add_attribute_special(attribute_data, 0x3FC, "Toad Detection Bubble Size")
    kirby.add_attribute_special(attribute_data, 0x190, "Giant Punch Swings to Fully Charge", True)
    kirby.add_attribute_special(attribute_data, 0x194, "Giant Punch Damage Increase Per Swing", True)
    kirby.add_attribute_special(attribute_data, 0x198, "Giant Punch Grounded Horizontal Velocity")
    kirby.add_attribute_special(attribute_data, 0x19C, "Giant Punch Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x1A0, "PK Flash Grounded Animation Loop Frames", True)
    kirby.add_attribute_special(attribute_data, 0x1A4, "PK Flash Air Animation Loop Frames", True)
    kirby.add_attribute_special(attribute_data, 0x1A8, "PK Flash Falling Acceleration Delay", True)
    kirby.add_attribute_special(attribute_data, 0x1AC, "PK Flash Charge Release Delay", True)
    kirby.add_attribute_special(attribute_data, 0x1B4, "PK Flash Gravity")
    kirby.add_attribute_special(attribute_data, 0x1BC, "PK Flash Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x1C0, "Pikachu Thunder Jolt Ground Spawn X-Offset")
    kirby.add_attribute_special(attribute_data, 0x1C4, "Pikachu Thunder Jolt Ground Spawn Y-Offset")
    kirby.add_attribute_special(attribute_data, 0x1C8, "Pikachu Thunder Jolt Air Spawn X-Offset")
    kirby.add_attribute_special(attribute_data, 0x1CC, "Pikachu Thunder Jolt Air Spawn Y-Offset")
    kirby.add_attribute_special(attribute_data, 0x1D0, "Pikachu Thunder Jolt Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x1C0, "Pichu Thunder Jolt Ground Spawn X-Offset")
    kirby.add_attribute_special(attribute_data, 0x1C4, "Pichu Jolt Ground Spawn Y-Offset")
    kirby.add_attribute_special(attribute_data, 0x1C8, "Pichu Jolt Air Spawn X-Offset")
    kirby.add_attribute_special(attribute_data, 0x1CC, "Pichu Jolt Air Spawn Y-Offset")
    kirby.add_attribute_special(attribute_data, 0x1D0, "Pichu Jolt Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x200, "Falcon Punch Momentum")
    kirby.add_attribute_special(attribute_data, 0x204, "Aerial Falcon Punch Angle Difference")
    kirby.add_attribute_special(attribute_data, 0x208, "Aerial Falcon Punch Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x214, "Warlock Punch Momentum")
    kirby.add_attribute_special(attribute_data, 0x218, "Aerial Warlock Punch Angle Difference")
    kirby.add_attribute_special(attribute_data, 0x21C, "Aerial Warlock Punch Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x230, "Fox Blaster Launch Angle")
    kirby.add_attribute_special(attribute_data, 0x234, "Fox Blaster Launch Speed")
    kirby.add_attribute_special(attribute_data, 0x238, "Fox Blaster Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x254, "Falco Blaster Launch Angle")
    kirby.add_attribute_special(attribute_data, 0x258, "Falco Blaster Launch Speed")
    kirby.add_attribute_special(attribute_data, 0x25C, "Falco Blaster Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x268, "Bow Frames For Max Charge")
    kirby.add_attribute_special(attribute_data, 0x26C, "Bow Charge Speed")
    kirby.add_attribute_special(attribute_data, 0x270, "Bow Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x2A8, "Nayru's Love Gravity Delay", True)
    kirby.add_attribute_special(attribute_data, 0x2AC, "Nayru's Love Momentum Preservation")
    kirby.add_attribute_special(attribute_data, 0x2B0, "Nayru's Love Fall Acceleration")
    kirby.add_attribute_special(attribute_data, 0x404, "Nayru's Love Max Damage Reflectable", True)
    kirby.add_attribute_special(attribute_data, 0x404, "Nayru's Love Reflection Bubble Size")
    kirby.add_attribute_special(attribute_data, 0x404, "Nayru's Love Reflection Damage Multiplier")
    kirby.add_attribute_special(attribute_data, 0x404, "Nayru's Love Reflection Speed Multiplier")
    kirby.add_attribute_special(attribute_data, 0x2B4, "Rollout Duration", True)
    kirby.add_attribute_special(attribute_data, 0x2BC, "Rollout Start Air Height Offset")
    kirby.add_attribute_special(attribute_data, 0x2C0, "Rollout Bounciness")
    kirby.add_attribute_special(attribute_data, 0x2C8, "Rollout Gravity During Roll")
    kirby.add_attribute_special(attribute_data, 0x2CC, "Rollout Base Rolling Speed")
    kirby.add_attribute_special(attribute_data, 0x2D0, "Rollout Max Rolling Speed")
    kirby.add_attribute_special(attribute_data, 0x2D8, "Rollout Aerial X-Axis Momentum Forward")
    kirby.add_attribute_special(attribute_data, 0x2E0, "Rollout Aerial Initial Momentum")
    kirby.add_attribute_special(attribute_data, 0x2E4, "Rollout Max Momentum")
    kirby.add_attribute_special(attribute_data, 0x2E8, "Rollout Spinning Speed")
    kirby.add_attribute_special(attribute_data, 0x2EC, "Rollout Spinning Turn Speed")
    kirby.add_attribute_special(attribute_data, 0x2F8, "Rollout Bounciness A")
    kirby.add_attribute_special(attribute_data, 0x2FC, "Rollout Bounciness B")
    kirby.add_attribute_special(attribute_data, 0x300, "Rollout Base Damage")
    kirby.add_attribute_special(attribute_data, 0x304, "Rollout Damage Multiplier")
    kirby.add_attribute_special(attribute_data, 0x308, "Rollout Horizontal Bounce On Hit")
    kirby.add_attribute_special(attribute_data, 0x30C, "Rollout Vertical Bounce on Hit")
    kirby.add_attribute_special(attribute_data, 0x310, "Rollout Input Modifier")
    kirby.add_attribute_special(attribute_data, 0x320, "Rollout Charge Rate")
    kirby.add_attribute_special(attribute_data, 0x324, "Rollout Charge Time")
    kirby.add_attribute_special(attribute_data, 0x32C, "Rollout Spin Charge Animation")
    kirby.add_attribute_special(attribute_data, 0x338, "Rollout Speed Variable")
    kirby.add_attribute_special(attribute_data, 0x33C, "Rollout Spin Animation Post Hit")
    kirby.add_attribute_special(attribute_data, 0x340, "Rollout Air Speed")
    kirby.add_attribute_special(attribute_data, 0x344, "Rollout Turn Rate Variable")
    kirby.add_attribute_special(attribute_data, 0x358, "Rollout Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x35C, "Shield Breaker Loops For Full Charge", True)
    kirby.add_attribute_special(attribute_data, 0x360, "Shield Breaker Base Damage", True)
    kirby.add_attribute_special(attribute_data, 0x364, "Shield Breaker Damage Per Loop", True)
    kirby.add_attribute_special(attribute_data, 0x36C, "Shield Breaker Momentum Preservation")
    kirby.add_attribute_special(attribute_data, 0x36C, "Shield Breaker Deceleration Rate")
    kirby.add_attribute_special(attribute_data, 0x370, "Flare Blade Loops For Full Charge", True)
    kirby.add_attribute_special(attribute_data, 0x374, "Flare Blade Base Damage", True)
    kirby.add_attribute_special(attribute_data, 0x378, "Flare Blade Damage Per Loop", True)
    kirby.add_attribute_special(attribute_data, 0x37C, "Flare Blade Momentum Preservation")
    kirby.add_attribute_special(attribute_data, 0x380, "Flare Blade Deceleration Rate")
    kirby.add_attribute_special(attribute_data, 0x384, "Shadow Ball Charge Increment")
    kirby.add_attribute_special(attribute_data, 0x388, "Shadow Ball Release Momentum Grounded")
    kirby.add_attribute_special(attribute_data, 0x38C, "Shadow Ball Release Momentum Air")
    kirby.add_attribute_special(attribute_data, 0x390, "Shadow Ball Loops For Full Charge", True)
    kirby.add_attribute_special(attribute_data, 0x398, "Shadow Ball Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x39C, "Ice Shot Aerial Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x3A0, "Ice Shot Landing Lag")
    kirby.add_attribute_special(attribute_data, 0x3A4, "Ice Shot Spawn X-Offset")
    kirby.add_attribute_special(attribute_data, 0x3A8, "Ice Shot Spawn Y-Offset")
    kirby.add_attribute_special(attribute_data, 0x3AC, "Egg Lay Horizontal Momentum")
    kirby.add_attribute_special(attribute_data, 0x3B0, "Egg Lay Vertical Momentum")
    kirby.add_attribute_special(attribute_data, 0x3B4, "Egg Lay Damage Multiplier")
    kirby.add_attribute_special(attribute_data, 0x3BC, "Egg Lay Growth Time")
    kirby.add_attribute_special(attribute_data, 0x3C0, "Egg Lay Base Duration")
    kirby.add_attribute_special(attribute_data, 0x3C4, "Egg Lay Breakout Resistance")
    kirby.add_attribute_special(attribute_data, 0x3C8, "Egg Lay Wiggle Out")
    kirby.add_attribute_special(attribute_data, 0x3D4, "Egg Lay Release Intangibility", True)
    kirby.add_attribute_special(attribute_data, 0x3D8, "Egg Lay Break Out Horizontal Velocity")
    kirby.add_attribute_special(attribute_data, 0x3DC, "Egg Lay Break Out Vertical Velocity")
    kirby.add_attribute_special(attribute_data, 0x3E4, "Chef Multi Hit Begin Frame")
    kirby.add_attribute_special(attribute_data, 0x3E8, "Chef Max Sausages")
    # Articles
    final_cutter_data = kirby.articles_datas[0]
    kirby.add_attribute_article(final_cutter_data, 0x0, "Final Cutter Velocity")
    kirby.add_attribute_article(final_cutter_data, 0x8, "Final Cutter Duration")
    kirby.add_attribute_article(final_cutter_data, 0xC, "Final Cutter Deceleration Rate")
    
    # Link
    link = characters.find_fighter("Link")
    link.add_attack(attack_from_subaction(link.subactions, 295), "Forward Smash (Second Hit)")
    link.add_attack(attack_from_subaction(link.subactions, 308), "Spin Attack (Ground)")
    link.add_attack(attack_from_subaction(link.subactions, 309), "Spin Attack (Air)")
    link.add_attack(attack_from_subaction(link.subactions, 312), "Hookshot (Air)")
    attribute_data = link.special_attribute_data
    link.add_attribute_special(attribute_data, 0x0, "Bow Frames For Max Charge")
    link.add_attribute_special(attribute_data, 0x4, "Bow Charge Speed")
    link.add_attribute_special(attribute_data, 0x8, "Bow Landing Lag")
    link.add_attribute_special(attribute_data, 0x18, "Boomerang Launch Angle")
    link.add_attribute_special(attribute_data, 0x20, "Boomerang Smash Launch Velocity")
    link.add_attribute_special(attribute_data, 0x24, "Boomerang Tilt Launch Velocity")
    link.add_attribute_special(attribute_data, 0x30, "Spin Attack Landing Lag")
    link.add_attribute_special(attribute_data, 0x34, "Spin Attack Horizontal Momentum")
    link.add_attribute_special(attribute_data, 0x38, "Spin Attack Aerial Mobility")
    link.add_attribute_special(attribute_data, 0x3C, "Spin Attack Momentum Preservation")
    link.add_attribute_special(attribute_data, 0x40, "Spin Attack Vertical Momentum")
    link.add_attribute_special(attribute_data, 0x44, "Spin Attack Landing Gravity")
    link.add_attribute_special(attribute_data, 0x4C, "Down Aerial Bounce Momentum")
    link.add_attribute_special(attribute_data, 0x50, "Down Aerial Hitbox Reapply Rate")
    link.add_attribute_special(attribute_data, 0x58, "Down Aerial Hitbox 0 Damage On Rehit", True)
    link.add_attribute_special(attribute_data, 0x5C, "Down Aerial Hitbox 1 Damage On Rehit", True)
    link.add_attribute_special(attribute_data, 0x60, "Down Aerial Hitbox 2 Damage On Rehit", True)
    #link.add_attribute_special(attribute_data, 0x6C, "Sword Trail Colors 1 - Do not modify")
    #link.add_attribute_special(attribute_data, 0x70, "Sword Trail Colors 2 - Do not modify")
    #link.add_attribute_special(attribute_data, 0x74, "Sword Trail Colors 3 - Do not modify")
    link.add_attribute_special(attribute_data, 0x7C, "Sword Trail Width")
    link.add_attribute_special(attribute_data, 0x7C, "Sword Trail Height")
    link.add_attribute_special(attribute_data, 0x84, "Hookshot Grab Delay", True)
    link.add_attribute_special(attribute_data, 0x88, "Hookshot Grab Chain Release Begin", True)
    link.add_attribute_special(attribute_data, 0x8C, "Hookshot Grab Chain Retract Begin", True)
    link.add_attribute_special(attribute_data, 0x90, "Hookshot Grab Chain Retract Finish", True)
    link.add_attribute_special(attribute_data, 0x94, "Hookshot Dash Grab Delay", True)
    link.add_attribute_special(attribute_data, 0x98, "Hookshot Dash Grab Chain Release Begin", True)
    link.add_attribute_special(attribute_data, 0x9C, "Hookshot Dash Grab Chain Retract Begin", True)
    link.add_attribute_special(attribute_data, 0xA0, "Hookshot Dash Grab Chain Retract Finish", True)
    link.add_attribute_special(attribute_data, 0xA4, "Hookshot Air Delay", True)
    link.add_attribute_special(attribute_data, 0xA8, "Hookshot Air Chain Release Begin", True)
    link.add_attribute_special(attribute_data, 0xAC, "Hookshot Air Chain Retract Begin", True)
    link.add_attribute_special(attribute_data, 0xB0, "Hookshot Air Chain Retract Finish", True)
    link.add_attribute_special(attribute_data, 0xB4, "Hookshot Wall Release Jump Height")
    link.add_attribute_special(attribute_data, 0xB8, "Hookshot Hang Duration", True)
    link.add_attribute_special(attribute_data, 0xD4, "Hylian Shield Collision Bubble Size")
    link.add_attribute_special(attribute_data, 0xD8, "Hylian Shield Impact Momentum Multiplier")
    # Articles
    bomb_data = link.articles_datas[0]
    link.add_attribute_article(bomb_data, 0x0, "Bomb Duration", 0, True)
    link.add_attribute_article(bomb_data, 0x4, "Bomb Max Bounces", 0, True)
    link.add_attribute_article(bomb_data, 0x8, "Bomb Bounce Rehit Rate", 0, True)
    link.add_attribute_article(bomb_data, 0xC, "Bomb Explosion Flash Frames", 0, True)
    link.add_attribute_article(bomb_data, 0x10, "Bomb HP", 0, True)
    link.add_attribute_article(bomb_data, 0x24, "Bomb Horizontal Velocity to Detonate")
    link.add_attribute_article(bomb_data, 0x2C, "Bomb Base Launch Speed on Hit")
    link.add_attribute_article(bomb_data, 0x30, "Bomb Launch Speed Multiplier on Hit")
    boomerang_data = link.articles_datas[1]
    link.add_attribute_article(boomerang_data, 0x0, "Boomerang Tilt Duration", 1, True)
    link.add_attribute_article(boomerang_data, 0x4, "Boomerang Smash Duration", 1, True)
    link.add_attribute_article(boomerang_data, 0xC, "Boomerang Launch Velocity", 1)
    link.add_attribute_article(boomerang_data, 0x14, "Boomerang Release Angle Multiplier", 1)
    link.add_attribute_article(boomerang_data, 0x18, "Boomerang Return Transition Smoothness", 1)
    link.add_attribute_article(boomerang_data, 0x1C, "Boomerang Return Angle Modifier", 1)
    link.add_attribute_article(boomerang_data, 0x20, "Boomerang Return Homing Accuracy 1", 1)
    link.add_attribute_article(boomerang_data, 0x24, "Boomerang Return Homing Accuracy 2", 1)
    link.add_attribute_article(boomerang_data, 0x28, "Boomerang Rebound Angle Modifier", 1)
    link.add_attribute_article(boomerang_data, 0x2C, "Boomerang Return Acceleration", 1)
    link.add_attribute_article(boomerang_data, 0x30, "Boomerang Spin Speed", 1)
    link.add_attribute_article(boomerang_data, 0x38, "Boomerang Frame Delay Between SFX", 1)
    link.add_attribute_article(boomerang_data, 0x3C, "Boomerang Trail Effect 1 Delay", 1)
    link.add_attribute_article(boomerang_data, 0x40, "Boomerang Trail Effect 2 Delay", 1)
    hookshot_data = link.articles_datas[2]
    link.add_attribute_article(hookshot_data, 0xC, "Hookshot Number of Chains", 2, True)
    link.add_attribute_article(hookshot_data, 0x10, "Hookshot Distance Between Chains", 2)
    link.add_attribute_article(hookshot_data, 0x18, "Hookshot Chain Launch Speed", 2)
    link.add_attribute_article(hookshot_data, 0x1C, "Hookshot Chain Gravity", 2)
    link.add_attribute_article(hookshot_data, 0x20, "Hookshot Chain Retraction Speed", 2)
    link.add_attribute_article(hookshot_data, 0x4C, "Hookshot Ground Length Modifier", 2)
    link.add_attribute_article(hookshot_data, 0x50, "Hookshot Air Length Modifier", 2)
    arrow_data = link.articles_datas[3]
    link.add_attribute_article(arrow_data, 0x0, "Arrow Duration (Air)", 3)
    link.add_attribute_article(arrow_data, 0x4, "Arrow Uncharged Velocity", 3)
    link.add_attribute_article(arrow_data, 0x8, "Arrow Charged Velocity Multiplier", 3)
    link.add_attribute_article(arrow_data, 0xC, "Arrow Uncharged Damage", 3)
    link.add_attribute_article(arrow_data, 0x10, "Arrow Full Charge Damage", 3)
    link.add_attribute_article(arrow_data, 0x18, "Arrow Duration (Ground)", 3)
    link.add_attribute_article(arrow_data, 0x1C, "Arrow Gravity", 3)
    link.add_attribute_article(arrow_data, 0x20, "Arrow Arc Modifier (Cosmetic only)", 3)

    # Luigi
    luigi = characters.find_fighter("Luigi")
    luigi.add_attack(attack_from_subaction(luigi.subactions, 239), "Appeal")
    luigi.add_attack(attack_from_subaction(luigi.subactions, 299), "Green Missile (Uncharged)")
    luigi.add_attack(attack_from_subaction(luigi.subactions, 300), "Green Missile (Charged, Misfire)")
    luigi.add_attack(attack_from_subaction(luigi.subactions, 308), "Super Jump Punch (Ground)")
    luigi.add_attack(attack_from_subaction(luigi.subactions, 309), "Super Jump Punch (Air)")
    luigi.add_attack(merge_from_subactions(luigi.subactions, [310, 311]), "Cyclone")
    attribute_data = luigi.special_attribute_data
    luigi.add_attribute_special(attribute_data, 0x8, "Green Missile Charge Rate")
    luigi.add_attribute_special(attribute_data, 0xC, "Green Missile Frames to Fully Charge")
    luigi.add_attribute_special(attribute_data, 0x10, "Green Missile Tilt Damage")
    luigi.add_attribute_special(attribute_data, 0x18, "Green Missile Traction Multiplier")
    luigi.add_attribute_special(attribute_data, 0x24, "Green Missile Horizontal Momentum")
    luigi.add_attribute_special(attribute_data, 0x28, "Green Missile Horizontal Momentum Multiplier")
    luigi.add_attribute_special(attribute_data, 0x2C, "Green Missile Vertical Momentum")
    luigi.add_attribute_special(attribute_data, 0x30, "Green Missile Vertical Momentum Multiplier")
    luigi.add_attribute_special(attribute_data, 0x34, "Green Missile Gravity on Launch")
    luigi.add_attribute_special(attribute_data, 0x38, "Green Missile Ending Friction Modifier")
    luigi.add_attribute_special(attribute_data, 0x3C, "Green Missile Launch End Horizontal Deceleration")
    luigi.add_attribute_special(attribute_data, 0x40, "Green Missile Launch End Gravity Multiplier")
    luigi.add_attribute_special(attribute_data, 0x44, "Green Missile Misfire Chance")
    luigi.add_attribute_special(attribute_data, 0x48, "Green Missile Misfire Horizontal Momentum")
    luigi.add_attribute_special(attribute_data, 0x4C, "Green Missile Misfire Vertical Momentum")
    luigi.add_attribute_special(attribute_data, 0x50, "Super Jump Punch Freefall Mobility")
    luigi.add_attribute_special(attribute_data, 0x54, "Super Jump Punch Landing Lag")
    luigi.add_attribute_special(attribute_data, 0x60, "Super Jump Punch Air Control During Up B")
    luigi.add_attribute_special(attribute_data, 0x64, "Super Jump Punch Air Control Input Modifier")
    luigi.add_attribute_special(attribute_data, 0x68, "Super Jump Punch Gravity")
    luigi.add_attribute_special(attribute_data, 0x6C, "Super Jump Punch Air Vertical Momentum")
    luigi.add_attribute_special(attribute_data, 0x70, "Cyclone Momentum From Initial B Tap")
    luigi.add_attribute_special(attribute_data, 0x74, "Cyclone Grounded Horizontal Momentum")
    luigi.add_attribute_special(attribute_data, 0x78, "Cyclone Aerial Horizontal Momentum")
    luigi.add_attribute_special(attribute_data, 0x7C, "Cyclone Grounded Momentum Modifier")
    luigi.add_attribute_special(attribute_data, 0x80, "Cyclone Aerial Momentum Modifier")
    luigi.add_attribute_special(attribute_data, 0x84, "Cyclone Ending Friction")
    luigi.add_attribute_special(attribute_data, 0x8C, "Cyclone Max Vertical Momentum From B Tap")
    luigi.add_attribute_special(attribute_data, 0x90, "Cyclone Gravity Modifier During B Tap")
    # Articles
    fireball_data = luigi.articles_datas[0]
    luigi.add_attribute_article(fireball_data, 0xC, "Fireball Spin Animation Speed")
    luigi.add_attribute_article(fireball_data, 0x10, "Fireball Gravity")
    luigi.add_attribute_article(fireball_data, 0x14, "Fireball Terminal Velocity")
    fireball_data_b = luigi.articles_datas[1]
    luigi.add_attribute_article(fireball_data_b, 0x0, "Fireball Initial Velocity", 1)
    luigi.add_attribute_article(fireball_data_b, 0x4, "Fireball Duration", 1)
    luigi.add_attribute_article(fireball_data_b, 0xC, "Fireball Bounce Multiplier", 1)

    # Mario
    mario = characters.find_fighter("Mario")
    mario.add_attack(merge_from_subactions(mario.subactions, [297, 298]), "Cape")
    mario.add_attack(merge_from_subactions(mario.subactions, [299, 300]), "Super Jump Punch")
    mario.add_attack(merge_from_subactions(mario.subactions, [301, 302]), "Tornado")
    attribute_data = mario.special_attribute_data
    mario.add_attribute_special(attribute_data, 0x00, "Cape Horizontal Momentum")
    mario.add_attribute_special(attribute_data, 0x04, "Cape Horizontal Velocity")
    mario.add_attribute_special(attribute_data, 0x08, "Cape Vertical Momentum")
    mario.add_attribute_special(attribute_data, 0x0C, "Cape Gravity")
    mario.add_attribute_special(attribute_data, 0x10, "Cape Max Falling Speed")
    mario.add_attribute_special(attribute_data, 0x74, "Cape Reflection Bubble Size")
    mario.add_attribute_special(attribute_data, 0x78, "Cape Reflection Damage Multiplier")
    mario.add_attribute_special(attribute_data, 0x7C, "Cape Projectile Reflection Speed Multiplier")
    mario.add_attribute_special(attribute_data, 0x18, "Super Jump Punch Freefall Mobility")
    mario.add_attribute_special(attribute_data, 0x1C, "Super Jump Punch Landing Lag")
    mario.add_attribute_special(attribute_data, 0x28, "Super Jump Punch Max Angle Change")
    mario.add_attribute_special(attribute_data, 0x2C, "Super Jump Punch Initial Horizontal Momentum")
    mario.add_attribute_special(attribute_data, 0x30, "Super Jump Punch Initial Gravity")
    mario.add_attribute_special(attribute_data, 0x34, "Super Jump Punch Initial Vertical Momentum")
    mario.add_attribute_special(attribute_data, 0x38, "Tornado Grounded Rise Resistance")
    mario.add_attribute_special(attribute_data, 0x3C, "Tornado Base Air Speed")
    mario.add_attribute_special(attribute_data, 0x40, "Tornado Horizontal Velocity Limit")
    mario.add_attribute_special(attribute_data, 0x44, "Tornado Horizontal Acceleration")
    mario.add_attribute_special(attribute_data, 0x48, "Tornado Horizontal marioift")
    mario.add_attribute_special(attribute_data, 0x4C, "Tornado Deceleration Rate")
    mario.add_attribute_special(attribute_data, 0x54, "Tornado Velocity Gain From B Press")
    mario.add_attribute_special(attribute_data, 0x58, "Tornado Terminal Velocity")
    mario.add_attribute_special(attribute_data, 0x5C, "Tornado Landing Lag", True)
    # Articles
    mfireball_data = mario.articles_datas[0]
    mario.add_attribute_article(mfireball_data, 0x0, "Fireball Initial Velocity")
    mario.add_attribute_article(mfireball_data, 0x4, "Fireball Initial Angle")
    mario.add_attribute_article(mfireball_data, 0x8, "Fireball Duration")
    mario.add_attribute_article(mfireball_data, 0x10, "Fireball Bounce Muliplier")
    

    # Marth
    marth = characters.find_fighter("Marth")
    marth.add_attack(merge_from_subactions(marth.subactions, [296, 297, 299, 300, 301, 302]), "Shield Breaker (Uncharged)")
    marth.add_attack(attack_from_subaction(marth.subactions, 298), "Shield Breaker (Charged)")
    marth.add_attack(merge_from_subactions(marth.subactions, [303, 312]), "Dancing Blade (1st)")
    marth.add_attack(merge_from_subactions(marth.subactions, [304, 313]), "Dancing Blade (2nd, Up)")
    marth.add_attack(merge_from_subactions(marth.subactions, [305, 314]), "Dancing Blade (2nd, Down)")
    marth.add_attack(merge_from_subactions(marth.subactions, [306, 315]), "Dancing Blade (3rd, Up)")
    marth.add_attack(merge_from_subactions(marth.subactions, [307, 316]), "Dancing Blade (3rd, Side)")
    marth.add_attack(merge_from_subactions(marth.subactions, [308, 317]), "Dancing Blade (3rd, Down)")
    marth.add_attack(merge_from_subactions(marth.subactions, [309, 318]), "Dancing Blade (4th, Up)")
    marth.add_attack(merge_from_subactions(marth.subactions, [310, 319]), "Dancing Blade (4th, Side)")
    marth.add_attack(merge_from_subactions(marth.subactions, [311, 320]), "Dancing Blade (4th, Down)")
    marth.add_attack(attack_from_subaction(marth.subactions, 321), "Dolphin Slash")
    marth.add_attack(attack_from_subaction(marth.subactions, 324), "Counter")
    attribute_data = marth.special_attribute_data 
    marth.add_attribute_special(attribute_data, 0x0, "Shield Breaker Loops For Full Charge", True)
    marth.add_attribute_special(attribute_data, 0x4, "Shield Breaker Base Damage", True)
    marth.add_attribute_special(attribute_data, 0x8, "Shield Breaker Damage Per Loop", True)
    marth.add_attribute_special(attribute_data, 0xC, "Shield Breaker Momentum Preservation")
    marth.add_attribute_special(attribute_data, 0x10, "Shield Breaker Deceleration Rate")
    marth.add_attribute_special(attribute_data, 0x14, "Dancing Blade Aerial Horizontal Momentum Preservation")
    marth.add_attribute_special(attribute_data, 0x18, "Dancing Blade Aerial Horizontal Deceleration")
    marth.add_attribute_special(attribute_data, 0x1C, "Dancing Blade Aerial Vertical Boost")
    marth.add_attribute_special(attribute_data, 0x20, "Dancing Blade Aerial Vertical Deceleration")
    marth.add_attribute_special(attribute_data, 0x24, "Dancing Blade Gravity")
    marth.add_attribute_special(attribute_data, 0x28, "Dolphin Slash Freefall Mobility")
    marth.add_attribute_special(attribute_data, 0x2C, "Dolphin Slash Landing Lag")
    marth.add_attribute_special(attribute_data, 0x3C, "Dolphin Slash Displacement From Input")
    marth.add_attribute_special(attribute_data, 0x40, "Dolphin Slash Aerial Height Ratio")
    marth.add_attribute_special(attribute_data, 0x44, "Dolphin Slash Gravity After Use")
    marth.add_attribute_special(attribute_data, 0x48, "Dolphin Slash Max Fall Speed After Use")
    marth.add_attribute_special(attribute_data, 0x4C, "Counter Horizontal Momentum")
    marth.add_attribute_special(attribute_data, 0x50, "Counter Horizontal Deceleration")
    marth.add_attribute_special(attribute_data, 0x54, "Counter Gravity")
    marth.add_attribute_special(attribute_data, 0x58, "Counter Maximum Falling Speed")
    marth.add_attribute_special(attribute_data, 0x5C, "Counter Damage Multiplier")
    marth.add_attribute_special(attribute_data, 0x60, "Counter Hitlag")
    marth.add_attribute_special(attribute_data, 0x74, "Counter Detection Bubble Size")
    marth.add_attribute_special(attribute_data, 0x78, "Sword Trail Fade")
    marth.add_attribute_special(attribute_data, 0x7C, "Sword Trail Length")
    #marth.add_attribute_special(attribute_data, 0x80, "Sword Trail Color 1 - Don't Modify")
    #marth.add_attribute_special(attribute_data, 0x84, "Sword Trail Color 2 - Don't Modify")
    #marth.add_attribute_special(attribute_data, 0x88, "Sword Trail Color 3 - Don't Modify")
    marth.add_attribute_special(attribute_data, 0x90, "Sword Trail Width")
    marth.add_attribute_special(attribute_data, 0x94, "Sword Trail Height")

    # Mewtwo
    mewtwo = characters.find_fighter("Mewtwo")
    mewtwo.add_attack(merge_from_subactions(mewtwo.subactions, [296, 297]), "Shadow Ball (Loop)")
    attribute_data = mewtwo.special_attribute_data
    mewtwo.add_attribute_special(attribute_data, 0x0, "Shadow Ball Charge Increment")
    mewtwo.add_attribute_special(attribute_data, 0x4, "Shadow Ball Release Momentum Grounded")
    mewtwo.add_attribute_special(attribute_data, 0x8, "Shadow Ball Release Momentum Air")
    mewtwo.add_attribute_special(attribute_data, 0xC, "Shadow Ball Loops For Full Charge", True)
    mewtwo.add_attribute_special(attribute_data, 0x14, "Shadow Ball Landing Lag")
    mewtwo.add_attribute_special(attribute_data, 0x18, "Confusion Aerial Vertical Lift")
    mewtwo.add_attribute_special(attribute_data, 0x20, "Confusion Max Damage Reflectable")
    mewtwo.add_attribute_special(attribute_data, 0x30, "Confusion Reflection Bubble Size")
    mewtwo.add_attribute_special(attribute_data, 0x34, "Confusion Reflection Damage Multiplier")
    mewtwo.add_attribute_special(attribute_data, 0x38, "Confusion Reflection Speed Multiplier")
    mewtwo.add_attribute_special(attribute_data, 0x50, "Teleport Travel Time", True)
    mewtwo.add_attribute_special(attribute_data, 0x5C, "Teleport Initial Momentum 1")
    mewtwo.add_attribute_special(attribute_data, 0x60, "Teleport Initial Momentum 2")
    mewtwo.add_attribute_special(attribute_data, 0x64, "Teleport Ending Momentum")
    mewtwo.add_attribute_special(attribute_data, 0x6C, "Teleport Ending Momentum Multiplier")
    mewtwo.add_attribute_special(attribute_data, 0x74, "Teleport Landing Lag")
    mewtwo.add_attribute_special(attribute_data, 0x78, "Disable Base Falling Acceleration")
    mewtwo.add_attribute_special(attribute_data, 0x7C, "Disable Falling Acceleration Multiplier")
    mewtwo.add_attribute_special(attribute_data, 0x80, "Disable X-Offset")
    mewtwo.add_attribute_special(attribute_data, 0x84, "Disable Y-Offset")
    # Articles
    disable_data = mewtwo.articles_datas[0]
    mewtwo.add_attribute_article(disable_data, 0x0, "Disable Duration")
    mewtwo.add_attribute_article(disable_data, 0x4, "Disable Travel Speed")
    shadow_ball_data = mewtwo.articles_datas[1]
    mewtwo.add_attribute_article(shadow_ball_data, 0x0, "Shadow Ball Duration", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x4, "Shadow Ball Launch Angle", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x8, "Shadow Ball Uncharged Speed", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0xC, "Shadow Ball Charged Speed", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x10, "Shadow Ball Uncharged Damage", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x14, "Shadow Ball Full Charge Damage", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x18, "Shadow Ball Uncharged Size", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x1C, "Shadow Ball Full Charge Size", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x20, "Shadow Ball Wiggle Intensity", 1, True)
    mewtwo.add_attribute_article(shadow_ball_data, 0x28, "Shadow Ball Wiggle Modifier", 1)
    mewtwo.add_attribute_article(shadow_ball_data, 0x2C, "Shadow Ball Wiggle Smoothness", 1)

    # Game & Watch
    gnw = characters.find_fighter("Mr. Game & Watch")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [295, 296]), "Sausage (Pan Hit)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [297, 306]), "Judgment (1)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [298, 307]), "Judgment (2)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [299, 308]), "Judgment (3)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [300, 309]), "Judgment (4)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [301, 310]), "Judgment (5)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [302, 311]), "Judgment (6)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [303, 312]), "Judgment (7)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [304, 313]), "Judgment (8)")
    gnw.add_attack(merge_from_subactions(gnw.subactions, [305, 314]), "Judgment (9)")
    gnw.add_attack(attack_from_subaction(gnw.subactions, 315), "Fire!")
    attribute_data = gnw.special_attribute_data
    gnw.add_attribute_special(attribute_data, 0x0, "Model Width")
    gnw.add_attribute_special(attribute_data, 0x18, "Chef Multi Hit Begin Frame")
    gnw.add_attribute_special(attribute_data, 0x1C, "Chef Max Sausages")
    gnw.add_attribute_special(attribute_data, 0x20, "Judgment Momentum Preservation")
    gnw.add_attribute_special(attribute_data, 0x24, "Judgment Momentum Preservation Modifier")
    gnw.add_attribute_special(attribute_data, 0x58, "Fire! Launch Angle Modifier")
    gnw.add_attribute_special(attribute_data, 0x5C, "Fire! Launch Angle Max Difference")
    gnw.add_attribute_special(attribute_data, 0x60, "Fire! Landing Lag")
    gnw.add_attribute_special(attribute_data, 0x64, "Oil Panic Momentum Preservation")
    gnw.add_attribute_special(attribute_data, 0x68, "Oil Panic Momentum Preservation Modifier")
    gnw.add_attribute_special(attribute_data, 0x6C, "Oil Panic Fall acceleration")
    gnw.add_attribute_special(attribute_data, 0x74, "Oil Panic Base Damage")
    gnw.add_attribute_special(attribute_data, 0x78, "Oil Panic Damage Multiplier")
    gnw.add_attribute_special(attribute_data, 0x90, "Oil Panic Absorption Bubble Size")
    # Articles
    sausage_data = gnw.articles_datas[0]
    gnw.add_attribute_article(sausage_data, 0x4, "Sausage Wall Bounce Multiplier")
    gnw.add_attribute_article(sausage_data, 0x8, "Sausage Duration")
    gnw.add_attribute_article(sausage_data, 0x10, "Sausage 1 Horizontal Velocity")
    gnw.add_attribute_article(sausage_data, 0x14, "Sausage 1 Vertical Velocity")
    gnw.add_attribute_article(sausage_data, 0x18, "Sausage 1 Gravity Velocity")
    gnw.add_attribute_article(sausage_data, 0x1C, "Sausage 1 Spin Intensity")
    gnw.add_attribute_article(sausage_data, 0x20, "Sausage 1 Spin Intensity Multiplier")
    gnw.add_attribute_article(sausage_data, 0x24, "Sausage 2 Horizontal Velocity")
    gnw.add_attribute_article(sausage_data, 0x28, "Sausage 2 Vertical Velocity")
    gnw.add_attribute_article(sausage_data, 0x2C, "Sausage 2 Gravity Velocity")
    gnw.add_attribute_article(sausage_data, 0x30, "Sausage 2 Spin Intensity")
    gnw.add_attribute_article(sausage_data, 0x34, "Sausage 2 Spin Intensity Multiplier")
    gnw.add_attribute_article(sausage_data, 0x38, "Sausage 3 Horizontal Velocity")
    gnw.add_attribute_article(sausage_data, 0x3C, "Sausage 3 Vertical Velocity")
    gnw.add_attribute_article(sausage_data, 0x40, "Sausage 3 Gravity Velocity")
    gnw.add_attribute_article(sausage_data, 0x44, "Sausage 3 Spin Intensity")
    gnw.add_attribute_article(sausage_data, 0x48, "Sausage 3 Spin Intensity Multiplier")
    gnw.add_attribute_article(sausage_data, 0x4C, "Sausage 4 Horizontal Velocity")
    gnw.add_attribute_article(sausage_data, 0x50, "Sausage 4 Vertical Velocity")
    gnw.add_attribute_article(sausage_data, 0x54, "Sausage 4 Gravity Velocity")
    gnw.add_attribute_article(sausage_data, 0x58, "Sausage 4 Spin Intensity")
    gnw.add_attribute_article(sausage_data, 0x5C, "Sausage 4 Spin Intensity Multiplier")
    gnw.add_attribute_article(sausage_data, 0x60, "Sausage 5 Horizontal Velocity")
    gnw.add_attribute_article(sausage_data, 0x64, "Sausage 5 Vertical Velocity")
    gnw.add_attribute_article(sausage_data, 0x68, "Sausage 5 Gravity Velocity")
    gnw.add_attribute_article(sausage_data, 0x6C, "Sausage 5 Spin Intensity")
    gnw.add_attribute_article(sausage_data, 0x70, "Sausage 5 Spin Intensity Multiplier")
    
    # Ness
    ness = characters.find_fighter("Ness")
    ness.add_attack(merge_from_subactions(ness.subactions, [295, 296]), "Up Smash (Hold)")
    ness.add_attack(attack_from_subaction(ness.subactions, 298), "Down Smash (2)")
    ness.add_attack(attack_from_subaction(ness.subactions, 312), "PK Thunder (Bolt hits Ness)")
    attribute_data = ness.special_attribute_data
    ness.add_attribute_special(attribute_data, 0x0, "PK Flash Grounded Animation Loop Frames", True)
    ness.add_attribute_special(attribute_data, 0x4, "PK Flash Air Animation Loop Frames", True)
    ness.add_attribute_special(attribute_data, 0x8, "PK Flash Falling Acceleration Delay", True)
    ness.add_attribute_special(attribute_data, 0xC, "PK Flash Charge Release Delay", True)
    ness.add_attribute_special(attribute_data, 0x14, "PK Flash Gravity")
    ness.add_attribute_special(attribute_data, 0x1C, "PK Flash Landing Lag")
    ness.add_attribute_special(attribute_data, 0x20, "PK Fire Air Launch Trajectory")
    ness.add_attribute_special(attribute_data, 0x24, "PK Fire Aerial Velocity")
    ness.add_attribute_special(attribute_data, 0x28, "PK Fire Ground Launch Trajectory")
    ness.add_attribute_special(attribute_data, 0x2C, "PK Fire Ground Velocity")
    ness.add_attribute_special(attribute_data, 0x30, "PK Fire Spawn X-Offset")
    ness.add_attribute_special(attribute_data, 0x34, "PK Fire Spawn Y-Offset")
    ness.add_attribute_special(attribute_data, 0x38, "PK Fire Landing Lag")
    ness.add_attribute_special(attribute_data, 0x44, "PK Thunder Animation Timer On Hit", True)
    ness.add_attribute_special(attribute_data, 0x48, "PK Thunder Fall Delay", True)
    ness.add_attribute_special(attribute_data, 0x50, "PK Thunder Fall Acceleration")
    ness.add_attribute_special(attribute_data, 0x54, "PK Thunder 2 Momentum")
    ness.add_attribute_special(attribute_data, 0x5C, "PK Thunder 2 Deceleration Rate")
    ness.add_attribute_special(attribute_data, 0x70, "PK Thunder 2 Landing Lag")
    ness.add_attribute_special(attribute_data, 0x74, "PK Magnet Initial Cooldown")
    ness.add_attribute_special(attribute_data, 0x84, "PK Magnet Fall Delay", True)
    ness.add_attribute_special(attribute_data, 0x88, "PK Magnet Momentum Preservation")
    ness.add_attribute_special(attribute_data, 0x8C, "PK Magnet Fall Acceleration")
    ness.add_attribute_special(attribute_data, 0x94, "PK Magnet Healing Multiplier")
    ness.add_attribute_special(attribute_data, 0xA8, "PK Magnet Absorption Bubble Size")
    ness.add_attribute_special(attribute_data, 0xAC, "Yo-Yo Smash Charge Duration")
    ness.add_attribute_special(attribute_data, 0xB0, "Yo-Yo Smash Charge Damage Multiplier")
    ness.add_attribute_special(attribute_data, 0xB4, "Yo-Yo Smash Charge Hitbox Rehit Rate")
    ness.add_attribute_special(attribute_data, 0xB8, "Baseball Bat Max Damage Reflectable", True)
    ness.add_attribute_special(attribute_data, 0xB8, "Baseball Bat Reflection Damage Multiplier")
    ness.add_attribute_special(attribute_data, 0xB8, "Baseball Bat Reflection Speed Multiplier")
    # Articles
    pkfire_spark_data = ness.articles_datas[0]
    ness.add_attribute_article(pkfire_spark_data, 0x0, "PK Fire Spark Duration")
    ness.add_attribute_article(pkfire_spark_data, 0x4, "PK Fire Spark Y Offset")
    pkfire_pillar_data = ness.articles_datas[1]
    ness.add_attribute_article(pkfire_pillar_data, 0x0, "PK Fire Pillar Duration", 1)
    ness.add_attribute_article(pkfire_pillar_data, 0x4, "PK Fire Pillar Hurtbox Resistance", 1)
    ness.add_attribute_article(pkfire_pillar_data, 0x8, "PK Fire Pillar Size Decay Multiplier", 1)
    pkflash_charge_data = ness.articles_datas[2]
    ness.add_attribute_article(pkflash_charge_data, 0x0, "PK Flash Charge Duration", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x4, "PK Flash Charge Hitbox Size Modifier", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x8, "PK Flash Charge Initial Graphic Size Multiplier", 2)
    ness.add_attribute_article(pkflash_charge_data, 0xC, "PK Flash Charge Graphic Growth Multiplier", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x10, "PK Flash Charge Horizontal Momentum", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x14, "PK Flash Charge Peak Rising Height", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x18, "PK Flash Charge Control Sensitivity", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x1C, "PK Flash Charge Projectile Gravity", 2)
    ness.add_attribute_article(pkflash_charge_data, 0x28, "PK Flash Charge Detonation Delay", 2)
    pkthunder_data = ness.articles_datas[3]
    ness.add_attribute_article(pkthunder_data, 0x0, "PK Thunder Duration", 3)
    ness.add_attribute_article(pkthunder_data, 0x4, "PK Thunder Speed", 3)
    ness.add_attribute_article(pkthunder_data, 0x8, "PK Thunder Initial Angle", 3)
    ness.add_attribute_article(pkthunder_data, 0xC, "PK Thunder Turning Sensitivity", 3)
    ness.add_attribute_article(pkthunder_data, 0x10, "PK Thunder Turning Radius", 3)
    pkflash_data = ness.articles_datas[4]
    ness.add_attribute_article(pkflash_data, 0x00, "PK Flash 2 Hitbox Size Modifier", 4)
    ness.add_attribute_article(pkflash_data, 0x04, "PK Flash 2 Graphic Size Multiplier", 4)
    ness.add_attribute_article(pkflash_data, 0x08, "PK Flash 2 Graphic Growth Multiplier", 4)
    ness.add_attribute_article(pkflash_data, 0x0C, "PK Flash 2 Base Damage", 4)
    ness.add_attribute_article(pkflash_data, 0x10, "PK Flash 2 Damage Multiplier", 4)
    yoyo_data = ness.articles_datas[5]
    ness.add_attribute_article(yoyo_data, 0x00, "Yo-Yo Number of String Segments", 5, True)
    ness.add_attribute_article(yoyo_data, 0x04, "Yo-Yo Number of Up-Smash String Segments", 5, True)
    ness.add_attribute_article(yoyo_data, 0x08, "Yo-Yo Number of Down-Smash String Segments", 5, True)
    ness.add_attribute_article(yoyo_data, 0x0C, "Yo-Yo String Size", 5)
    ness.add_attribute_article(yoyo_data, 0x18, "Yo-Yo Spin Animation Speed", 5)
    ness.add_attribute_article(yoyo_data, 0x1C, "Yo-Yo Charge Spin Animation Speed", 5)
    ness.add_attribute_article(yoyo_data, 0x20, "Yo-Yo Charge Spin Animation Speed Modifier", 5)
    ness.add_attribute_article(yoyo_data, 0x24, "Yo-Yo Charge Horizontal Release Velocity", 5)
    ness.add_attribute_article(yoyo_data, 0x28, "Yo-Yo Charge Pull Acceleration", 5)
    ness.add_attribute_article(yoyo_data, 0x2C, "Yo-Yo Max Charge Horizontal Velocity", 5)
    ness.add_attribute_article(yoyo_data, 0x30, "Yo-Yo Charge Vertical Release Velocity", 5)
    ness.add_attribute_article(yoyo_data, 0x34, "Yo-Yo Charge Base Gravity", 5)
    ness.add_attribute_article(yoyo_data, 0x38, "Yo-Yo Charge Terminal Velocity", 5)
    ness.add_attribute_article(yoyo_data, 0x3C, "Yo-Yo Charge Horizontal Pull Strength", 5)
    ness.add_attribute_article(yoyo_data, 0x40, "Yo-Yo Frame for Up Smash Model Rotation Change", 5, True)
    ness.add_attribute_article(yoyo_data, 0x44, "Yo-Yo Frame for Up Smash Snap to Palm", 5, True)
    ness.add_attribute_article(yoyo_data, 0x48, "Yo-Yo Frame for Down Smash Model Rotation Change", 5, True)
    ness.add_attribute_article(yoyo_data, 0x4C, "Yo-Yo Frame for Down Smash Snap to Palm", 5, True)
    
    # Peach
    peach = characters.find_fighter("Peach")
    peach.add_attack(attack_from_subaction(peach.subactions, 298), "Tennis Racket")
    peach.add_attack(attack_from_subaction(peach.subactions, 299), "Golf Club")
    peach.add_attack(attack_from_subaction(peach.subactions, 300), "Frying Pan")
    peach.add_attack(attack_from_subaction(peach.subactions, 308), "Parasol")
    peach.add_attack(attack_from_subaction(peach.subactions, 316), "Parasol (Reopen)")
    attribute_data = peach.special_attribute_data
    peach.add_attribute_special(attribute_data, 0xC, "Float Duration")
    peach.add_attribute_special(attribute_data, 0x14, "Vegetable Base Odds (1/X)", True)
    peach.add_attribute_special(attribute_data, 0x18, "Vegetable Item 1 Odds (Y/X)", True)
    peach.add_attribute_special(attribute_data, 0x1C, "Vegetable Item 1 ID", True)
    peach.add_attribute_special(attribute_data, 0x20, "Vegetable Item 2 Odds (Y/X)", True)
    peach.add_attribute_special(attribute_data, 0x24, "Vegetable Item 2 ID", True)
    peach.add_attribute_special(attribute_data, 0x28, "Vegetable Item 3 Odds (Y/X)", True)
    peach.add_attribute_special(attribute_data, 0x2C, "Vegetable Item 3 ID", True)
    peach.add_attribute_special(attribute_data, 0x44, "Peach Bomber Tilt Horizontal Momentum")
    peach.add_attribute_special(attribute_data, 0x48, "Peach Bomber Smash Horizontal Momentum")
    peach.add_attribute_special(attribute_data, 0x4C, "Peach Bomber Vertical Momentum")
    peach.add_attribute_special(attribute_data, 0x64, "Peach Bomber Vertical Recoil")
    peach.add_attribute_special(attribute_data, 0x74, "Peach Parasol Landing Lag")
    peach.add_attribute_special(attribute_data, 0x80, "Peach Parasol Launch Control Modifier")
    peach.add_attribute_special(attribute_data, 0x9C, "Toad Aerial Vertical Momentum")
    peach.add_attribute_special(attribute_data, 0xA0, "Toad Fall Acceleration")
    peach.add_attribute_special(attribute_data, 0xBC, "Toad Detection Bubble Size")
    # Articles
    turnip_data = peach.articles_datas[0]
    peach.add_attribute_article(turnip_data, 0x0, "Turnip Duration")
    peach.add_attribute_article(turnip_data, 0x8, "Turnip #1 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0xC, "Turnip #1 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x10, "Turnip #2 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x14, "Turnip #2 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x18, "Turnip #3 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x1C, "Turnip #3 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x20, "Turnip #4 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x24, "Turnip #4 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x28, "Turnip #5 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x2C, "Turnip #5 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x30, "Turnip #6 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x34, "Turnip #6 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x38, "Turnip #7 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x3C, "Turnip #7 Damage", 0, True)
    peach.add_attribute_article(turnip_data, 0x40, "Turnip #8 Odds", 0, True)
    peach.add_attribute_article(turnip_data, 0x44, "Turnip #8 Damage", 0, True)
    toad_data = peach.articles_datas[1]
    peach.add_attribute_article(toad_data, 0x0, "Toad Counter Velocity", 1)
    peach.add_attribute_article(toad_data, 0x4, "Toad Counter Distance Modifier", 1)
    peach.add_attribute_article(toad_data, 0x8, "Toad Counter Scatter Modifier", 1)
    peach.add_attribute_article(toad_data, 0xC, "Toad Counter Angle", 1)

    # Pichu
    pichu = characters.find_fighter("Pichu")
    pichu.add_attack(merge_from_subactions(pichu.subactions, [298, 299]), "Skull Bash")
    pichu.add_attack(attack_from_subaction(pichu.subactions, 314), "Thunder")
    attribute_data = pichu.special_attribute_data
    pichu.add_attribute_special(attribute_data, 0x0, "Thunder Jolt Ground Spawn X-Offset")
    pichu.add_attribute_special(attribute_data, 0x4, "Thunder Jolt Ground Spawn Y-Offset")
    pichu.add_attribute_special(attribute_data, 0x8, "Thunder Jolt Air Spawn X-Offset")
    pichu.add_attribute_special(attribute_data, 0xC, "Thunder Jolt Air Spawn Y-Offset")
    pichu.add_attribute_special(attribute_data, 0x10, "Thunder Jolt Landing Lag")
    pichu.add_attribute_special(attribute_data, 0x1C, "Skull Bash Smash Window")
    pichu.add_attribute_special(attribute_data, 0x20, "Skull Bash Charge Rate")
    pichu.add_attribute_special(attribute_data, 0x24, "Skull Bash Max Charge Duration")
    pichu.add_attribute_special(attribute_data, 0x28, "Skull Bash Tilt Damage")
    pichu.add_attribute_special(attribute_data, 0x30, "Skull Bash Traction Multiplier")
    pichu.add_attribute_special(attribute_data, 0x38, "Skull Bash Falling Speed")
    pichu.add_attribute_special(attribute_data, 0x3C, "Skull Bash Horizontal Launch Momentum")
    pichu.add_attribute_special(attribute_data, 0x40, "Skull Bash Horizontal Momentum Multiplier")
    pichu.add_attribute_special(attribute_data, 0x44, "Skull Bash Vertical Launch Momentum")
    pichu.add_attribute_special(attribute_data, 0x48, "Skull Bash Vertical Momentum Multiplier")
    pichu.add_attribute_special(attribute_data, 0x4C, "Skull Bash Gravity During Launch Animation")
    pichu.add_attribute_special(attribute_data, 0x50, "Skull Bash Ending Friction Modifier")
    pichu.add_attribute_special(attribute_data, 0x54, "Skull Bash Horizontal Deceleration")
    pichu.add_attribute_special(attribute_data, 0x58, "Skull Bash Gravity During End of Launch")
    pichu.add_attribute_special(attribute_data, 0x60, "Agility Travel Distance", True)
    pichu.add_attribute_special(attribute_data, 0x64, "Agility Momentum Variable")
    pichu.add_attribute_special(attribute_data, 0x68, "Agility Grounded Model Rotation")
    pichu.add_attribute_special(attribute_data, 0x6C, "Agility Grounded Model Width Multiplier")
    pichu.add_attribute_special(attribute_data, 0x70, "Agility Grounded Model Height Multiplier")
    pichu.add_attribute_special(attribute_data, 0x74, "Agility Air Model Length Multiplier")
    pichu.add_attribute_special(attribute_data, 0x78, "Agility Air Model Rotation")
    pichu.add_attribute_special(attribute_data, 0x7C, "Agility Air Model Width Multiplier")
    pichu.add_attribute_special(attribute_data, 0x80, "Agility Air Model Height Multiplier")
    pichu.add_attribute_special(attribute_data, 0x84, "Agility Air Model Length Multiplier")
    pichu.add_attribute_special(attribute_data, 0x90, "Agility Base Dash Momentum")
    pichu.add_attribute_special(attribute_data, 0x94, "Agility Start Momentum Boost")
    pichu.add_attribute_special(attribute_data, 0x98, "Agility Second Dash Length Multiplier")
    pichu.add_attribute_special(attribute_data, 0x9C, "Agility Momentum Preservation")
    pichu.add_attribute_special(attribute_data, 0xA4, "Agility Momentum Variable 2")
    pichu.add_attribute_special(attribute_data, 0xB0, "Agility Landing Lag")
    pichu.add_attribute_special(attribute_data, 0xB4, "Thunder Vertical Momentum Gain on Strike")
    pichu.add_attribute_special(attribute_data, 0xB8, "Thunder Fall Acceleration on Strike")
    pichu.add_attribute_special(attribute_data, 0xC0, "Thunder Travel Speed")
    pichu.add_attribute_special(attribute_data, 0xCC, "Thunder Displacement of Thunder Cloud")
    pichu.add_attribute_special(attribute_data, 0xD0, "Thunder Spawn Y-Offset")
    pichu.add_attribute_special(attribute_data, 0xD4, "Thunder Number of Bursts", True)
    pichu.add_attribute_special(attribute_data, 0xD8, "Thunder Delay Between Bursts", True)
    # Articles
    thunder_data = pichu.articles_datas[0]
    pichu.add_attribute_article(thunder_data, 0x0, "Thunder Maximum Travel Distance")
    pichu.add_attribute_article(thunder_data, 0x4, "Thunder Vertical Collision Detection")
    pichu.add_attribute_article(thunder_data, 0x8, "Thunder Size of Self-hit Collision Detection")
    jolt_data = pichu.articles_datas[1]
    pichu.add_attribute_article(jolt_data, 0x0, "Thunder Jolt Duration", 1)
    pichu.add_attribute_article(jolt_data, 0x4, "Thunder Jolt Launch Angle", 1)
    pichu.add_attribute_article(jolt_data, 0x8, "Thunder Jolt Aerial Launch Velocity", 1)

    # Pikachu
    pikachu = characters.find_fighter("Pikachu")
    pikachu.add_attack(merge_from_subactions(pikachu.subactions, [298, 299]), "Skull Bash")
    pikachu.add_attack(merge_from_subactions(pikachu.subactions, [306, 307]), "Quick Attack")
    pikachu.add_attack(attack_from_subaction(pikachu.subactions, 314), "Thunder")
    attribute_data = pikachu.special_attribute_data
    pikachu.add_attribute_special(attribute_data, 0x0, "Thunder Jolt Ground Spawn X-Offset")
    pikachu.add_attribute_special(attribute_data, 0x4, "Thunder Jolt Ground Spawn Y-Offset")
    pikachu.add_attribute_special(attribute_data, 0x8, "Thunder Jolt Air Spawn X-Offset")
    pikachu.add_attribute_special(attribute_data, 0xC, "Thunder Jolt Air Spawn Y-Offset")
    pikachu.add_attribute_special(attribute_data, 0x10, "Thunder Jolt Landing Lag")
    pikachu.add_attribute_special(attribute_data, 0x1C, "Skull Bash Smash Window")
    pikachu.add_attribute_special(attribute_data, 0x20, "Skull Bash Charge Rate")
    pikachu.add_attribute_special(attribute_data, 0x24, "Skull Bash Max Charge Duration")
    pikachu.add_attribute_special(attribute_data, 0x28, "Skull Bash Tilt Damage")
    pikachu.add_attribute_special(attribute_data, 0x30, "Skull Bash Traction Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x38, "Skull Bash Falling Speed")
    pikachu.add_attribute_special(attribute_data, 0x3C, "Skull Bash Horizontal Launch Momentum")
    pikachu.add_attribute_special(attribute_data, 0x40, "Skull Bash Horizontal Momentum Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x44, "Skull Bash Vertical Launch Momentum")
    pikachu.add_attribute_special(attribute_data, 0x48, "Skull Bash Vertical Momentum Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x4C, "Skull Bash Gravity During Launch Animation")
    pikachu.add_attribute_special(attribute_data, 0x50, "Skull Bash Ending Friction Modifier")
    pikachu.add_attribute_special(attribute_data, 0x54, "Skull Bash Horizontal Deceleration")
    pikachu.add_attribute_special(attribute_data, 0x58, "Skull Bash Gravity During End of Launch")
    pikachu.add_attribute_special(attribute_data, 0x60, "Quick Attack Travel Distance", True)
    pikachu.add_attribute_special(attribute_data, 0x64, "Quick Attack Momentum Variable")
    pikachu.add_attribute_special(attribute_data, 0x68, "Quick Attack Grounded Model Rotation")
    pikachu.add_attribute_special(attribute_data, 0x6C, "Quick Attack Grounded Model Width Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x70, "Quick Attack Grounded Model Height Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x74, "Quick Attack Air Model Length Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x78, "Quick Attack Air Model Rotation")
    pikachu.add_attribute_special(attribute_data, 0x7C, "Quick Attack Air Model Width Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x80, "Quick Attack Air Model Height Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x84, "Quick Attack Air Model Length Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x90, "Quick Attack Base Dash Momentum")
    pikachu.add_attribute_special(attribute_data, 0x94, "Quick Attack Start Momentum Boost")
    pikachu.add_attribute_special(attribute_data, 0x98, "Quick Attack Second Dash Length Multiplier")
    pikachu.add_attribute_special(attribute_data, 0x9C, "Quick Attack Momentum Preservation")
    pikachu.add_attribute_special(attribute_data, 0xA4, "Quick Attack Momentum Variable 2")
    pikachu.add_attribute_special(attribute_data, 0xB0, "Quick Attack Landing Lag")
    pikachu.add_attribute_special(attribute_data, 0xB4, "Thunder Vertical Momentum Gain on Strike")
    pikachu.add_attribute_special(attribute_data, 0xB8, "Thunder Fall Acceleration on Strike")
    pikachu.add_attribute_special(attribute_data, 0xC0, "Thunder Travel Speed")
    pikachu.add_attribute_special(attribute_data, 0xCC, "Thunder Displacement of Thunder Cloud")
    pikachu.add_attribute_special(attribute_data, 0xD0, "Thunder Spawn Y-Offset")
    pikachu.add_attribute_special(attribute_data, 0xD4, "Thunder Number of Bursts", True)
    pikachu.add_attribute_special(attribute_data, 0xD8, "Thunder Delay Between Bursts", True)
    # Articles
    thunder_data_b = pikachu.articles_datas[0]
    pikachu.add_attribute_article(thunder_data_b, 0x0, "Thunder Maximum Travel Distance")
    pikachu.add_attribute_article(thunder_data_b, 0x4, "Thunder Vertical Collision Detection")
    pikachu.add_attribute_article(thunder_data_b, 0x8, "Thunder Size of Self-hit Collision Detection")
    jolt_data_b = pikachu.articles_datas[1]
    pikachu.add_attribute_article(jolt_data_b, 0x0, "Thunder Jolt Duration", 1)
    pikachu.add_attribute_article(jolt_data_b, 0x4, "Thunder Jolt Launch Angle", 1)
    pikachu.add_attribute_article(jolt_data_b, 0x8, "Thunder Jolt Aerial Launch Velocity", 1)

    # Roy
    roy = characters.find_fighter("Roy")
    roy.add_attack(merge_from_subactions(roy.subactions, [296, 297, 299, 300, 301, 302]), "Flare Blade (Uncharged)")
    roy.add_attack(attack_from_subaction(roy.subactions, 298), "Flare Blade (Charged)")
    roy.add_attack(merge_from_subactions(roy.subactions, [303, 312]), "Double-Edge Dance (1st)")
    roy.add_attack(merge_from_subactions(roy.subactions, [304, 313]), "Double-Edge Dance (2nd, Up)")
    roy.add_attack(merge_from_subactions(roy.subactions, [305, 314]), "Double-Edge Dance (2nd, Down)")
    roy.add_attack(merge_from_subactions(roy.subactions, [306, 315]), "Double-Edge Dance (3rd, Up)")
    roy.add_attack(merge_from_subactions(roy.subactions, [307, 316]), "Double-Edge Dance (3rd, Side)")
    roy.add_attack(merge_from_subactions(roy.subactions, [308, 317]), "Double-Edge Dance (3rd, Down)")
    roy.add_attack(merge_from_subactions(roy.subactions, [309, 318]), "Double-Edge Dance (4th, Up)")
    roy.add_attack(merge_from_subactions(roy.subactions, [310, 319]), "Double-Edge Dance (4th, Side)")
    roy.add_attack(merge_from_subactions(roy.subactions, [311, 320]), "Double-Edge Dance (4th, Down)")
    roy.add_attack(attack_from_subaction(roy.subactions, 321), "Blazer")
    roy.add_attack(attack_from_subaction(roy.subactions, 324), "Counter")
    attribute_data = roy.special_attribute_data 
    roy.add_attribute_special(attribute_data, 0x0, "Flare Blade Loops For Full Charge", True)
    roy.add_attribute_special(attribute_data, 0x4, "Flare Blade Base Damage", True)
    roy.add_attribute_special(attribute_data, 0x8, "Flare Blade Damage Per Loop", True)
    roy.add_attribute_special(attribute_data, 0xC, "Flare Blade Momentum Preservation")
    roy.add_attribute_special(attribute_data, 0x10, "Flare Blade Deceleration Rate")
    roy.add_attribute_special(attribute_data, 0x14, "Double-Edge Dance Aerial Horizontal Momentum Preservation")
    roy.add_attribute_special(attribute_data, 0x18, "Double-Edge Dance Aerial Horizontal Deceleration")
    roy.add_attribute_special(attribute_data, 0x1C, "Double-Edge Dance Aerial Vertical Boost")
    roy.add_attribute_special(attribute_data, 0x20, "Double-Edge Dance Aerial Vertical Deceleration")
    roy.add_attribute_special(attribute_data, 0x24, "Double-Edge Dance Gravity")
    roy.add_attribute_special(attribute_data, 0x28, "Blazer Freefall Mobility")
    roy.add_attribute_special(attribute_data, 0x2C, "Blazer Landing Lag")
    roy.add_attribute_special(attribute_data, 0x3C, "Blazer Displacement From Input")
    roy.add_attribute_special(attribute_data, 0x40, "Blazer Aerial Height Ratio")
    roy.add_attribute_special(attribute_data, 0x44, "Blazer Gravity After Use")
    roy.add_attribute_special(attribute_data, 0x48, "Blazer Max Fall Speed After Use")
    roy.add_attribute_special(attribute_data, 0x4C, "Counter Horizontal Momentum")
    roy.add_attribute_special(attribute_data, 0x50, "Counter Horizontal Deceleration")
    roy.add_attribute_special(attribute_data, 0x54, "Counter Gravity")
    roy.add_attribute_special(attribute_data, 0x58, "Counter Maximum Falling Speed")
    roy.add_attribute_special(attribute_data, 0x5C, "Counter Damage Multiplier")
    roy.add_attribute_special(attribute_data, 0x60, "Counter Hitlag")
    roy.add_attribute_special(attribute_data, 0x74, "Counter Detection Bubble Size")
    roy.add_attribute_special(attribute_data, 0x78, "Sword Trail Fade")
    roy.add_attribute_special(attribute_data, 0x7C, "Sword Trail Length")
    #roy.add_attribute_special(attribute_data, 0x80, "Sword Trail Color 1 - Don't Modify")
    #roy.add_attribute_special(attribute_data, 0x84, "Sword Trail Color 2 - Don't Modify")
    #roy.add_attribute_special(attribute_data, 0x88, "Sword Trail Color 3 - Don't Modify")
    roy.add_attribute_special(attribute_data, 0x90, "Sword Trail Width")
    roy.add_attribute_special(attribute_data, 0x94, "Sword Trail Height")

    # Samus
    samus = characters.find_fighter("Samus")
    samus.add_attack(merge_from_subactions(samus.subactions, [307, 308]), "Screw Attack")
    samus.add_attack(attack_from_subaction(samus.subactions, 311), "Grapple Beam (Air)")
    attribute_data = samus.special_attribute_data
    samus.add_attribute_special(attribute_data, 0x0, "Bomb Self-Hit Animation Delay")
    samus.add_attribute_special(attribute_data, 0x4, "Bomb Self-Hit Grounded Launch Angle")
    samus.add_attribute_special(attribute_data, 0x8, "Bomb Self-Hit Momentum")
    samus.add_attribute_special(attribute_data, 0x10, "Bomb Self-Hit Horizontal Velocity Multiplier")
    samus.add_attribute_special(attribute_data, 0x18, "Charge Shot Charge Time")
    samus.add_attribute_special(attribute_data, 0x1C, "Charge Shot Recoil")
    samus.add_attribute_special(attribute_data, 0x20, "Charge Shot Frames Per Charge Level", True)
    samus.add_attribute_special(attribute_data, 0x24, "Charge Shot Landing Lag")
    samus.add_attribute_special(attribute_data, 0x28, "Missile Smash Window")
    samus.add_attribute_special(attribute_data, 0x2C, "Missile Momentum Preservation")
    samus.add_attribute_special(attribute_data, 0x30, "Missile Momentum Preservation Multiplier")
    samus.add_attribute_special(attribute_data, 0x34, "Missile Spawn X-Offset")
    samus.add_attribute_special(attribute_data, 0x38, "Screw Attack Grounded Start Horizontal Momentum")
    samus.add_attribute_special(attribute_data, 0x3C, "Screw Attack Control Variable")
    samus.add_attribute_special(attribute_data, 0x40, "Screw Attack Air Friction")
    samus.add_attribute_special(attribute_data, 0x44, "Screw Attack Aerial Vertical Momentum")
    samus.add_attribute_special(attribute_data, 0x50, "Screw Attack Landing Lag")
    samus.add_attribute_special(attribute_data, 0x54, "Morph Ball Bomb Ground Vertical Momentum")
    samus.add_attribute_special(attribute_data, 0x58, "Morph Ball Bomb Air Vertical Momentum")
    samus.add_attribute_special(attribute_data, 0x5C, "Morph Ball Bomb Ground Mobility")
    samus.add_attribute_special(attribute_data, 0x60, "Morph Ball Bomb Air Mobility")
    samus.add_attribute_special(attribute_data, 0x64, "Morph Ball Bomb Ground Acceleration Multiplier")
    samus.add_attribute_special(attribute_data, 0x68, "Morph Ball Bomb Air Acceleration Multiplier")
    samus.add_attribute_special(attribute_data, 0x6C, "Morph Ball Bomb Ground Speed Multiplier")
    samus.add_attribute_special(attribute_data, 0x70, "Morph Ball Bomb Air Speed Multiplier")
    samus.add_attribute_special(attribute_data, 0x74, "Morph Ball Bomb X-Offset")
    samus.add_attribute_special(attribute_data, 0x78, "Morph Ball Bomb Y-Offset")
    samus.add_attribute_special(attribute_data, 0x9C, "Grapple Beam Grab Delay", True)
    samus.add_attribute_special(attribute_data, 0xA0, "Grapple Beam Grab Chain Release Begin", True)
    samus.add_attribute_special(attribute_data, 0xA4, "Grapple Beam Grab Chain Retract Begin", True)
    samus.add_attribute_special(attribute_data, 0xA8, "Grapple Beam Grab Chain Retract Finish", True)
    samus.add_attribute_special(attribute_data, 0xAC, "Grapple Beam Dash Grab Delay", True)
    samus.add_attribute_special(attribute_data, 0xB0, "Grapple Beam Dash Grab Chain Release Begin", True)
    samus.add_attribute_special(attribute_data, 0xB4, "Grapple Beam Dash Grab Chain Retract Begin", True)
    samus.add_attribute_special(attribute_data, 0xB8, "Grapple Beam Dash Grab Chain Retract Finish", True)
    samus.add_attribute_special(attribute_data, 0xBC, "Grapple Beam Air Delay", True)
    samus.add_attribute_special(attribute_data, 0xC0, "Grapple Beam Air Chain Release Begin", True)
    samus.add_attribute_special(attribute_data, 0xC4, "Grapple Beam Air Chain Retract Begin", True)
    samus.add_attribute_special(attribute_data, 0xC8, "Grapple Beam Air Chain Retract Finish", True)
    samus.add_attribute_special(attribute_data, 0xCC, "Grapple Beam Wall Release Jump Height")
    samus.add_attribute_special(attribute_data, 0xD0, "Grapple Beam Hang Duration", True)
    # Articles
    mbomb_data = samus.articles_datas[0]
    samus.add_attribute_article(mbomb_data, 0x00, "Bomb Duration")
    beam_data = samus.articles_datas[1]
    samus.add_attribute_article(beam_data, 0x00, "Charge Shot Duration", 1)
    samus.add_attribute_article(beam_data, 0x04, "Charge Shot Angle", 1)
    samus.add_attribute_article(beam_data, 0x08, "Charge Shot Base Velocity", 1)
    samus.add_attribute_article(beam_data, 0x0C, "Charge Shot Charged Velocity", 1)
    samus.add_attribute_article(beam_data, 0x18, "Charge Shot Initial Size", 1)
    samus.add_attribute_article(beam_data, 0x1C, "Charge Shot Full Charge Graphic Size", 1)
    missile_data = samus.articles_datas[2]
    samus.add_attribute_article(missile_data, 0x04, "Missile Duration", 2)
    samus.add_attribute_article(missile_data, 0x08, "Missile Deceleration Frame", 2)
    samus.add_attribute_article(missile_data, 0x0C, "Missile Initial Velocity", 2)
    samus.add_attribute_article(missile_data, 0x10, "Missile Velocity After Deceleration", 2)
    samus.add_attribute_article(missile_data, 0x14, "Missile Deceleration Rate", 2)
    samus.add_attribute_article(missile_data, 0x18, "Missile Homing Accuracy", 2)
    samus.add_attribute_article(missile_data, 0x1C, "Missile Max Homing Angle", 2)
    samus.add_attribute_article(missile_data, 0x20, "Missile Homing Modifier", 2)
    samus.add_attribute_article(missile_data, 0x24, "Super Missile Duration", 2)
    samus.add_attribute_article(missile_data, 0x28, "Super Missile Acceleration Frame", 2)
    samus.add_attribute_article(missile_data, 0x2C, "Super Missile Initial Velocity", 2)
    samus.add_attribute_article(missile_data, 0x30, "Super Missile Acceleration Rate", 2)
    samus.add_attribute_article(missile_data, 0x34, "Super Missile Terminal Velocity", 2)
    grapple_data = samus.articles_datas[3]
    samus.add_attribute_article(grapple_data, 0x00, "Grapple Beam Recoil On Angled Surface", 3)
    samus.add_attribute_article(grapple_data, 0x0C, "Grapple Beam Number of Segments", 3)
    samus.add_attribute_article(grapple_data, 0x10, "Grapple Beam Distance Between Segments", 3)
    samus.add_attribute_article(grapple_data, 0x14, "Grapple Beam Elasticity", 3)
    samus.add_attribute_article(grapple_data, 0x18, "Grapple Beam Launch Speed", 3)
    samus.add_attribute_article(grapple_data, 0x1C, "Grapple Beam Gravity", 3)
    samus.add_attribute_article(grapple_data, 0x20, "Grapple Beam Retraction Speed", 3)
    samus.add_attribute_article(grapple_data, 0x24, "Grapple Beam End Retraction Speed", 3)
    samus.add_attribute_article(grapple_data, 0x5C, "Grapple Beam Ground Length Modifier", 3)
    samus.add_attribute_article(grapple_data, 0x60, "Grapple Beam Air Length Modifier", 3)

    # Sheik
    sheik = characters.find_fighter("Sheik")
    sheik.add_attack(attack_from_subaction(sheik.subactions, 303), "Chain Dance (Initial hit only?)")
    attribute_data = sheik.special_attribute_data
    sheik.add_attribute_special(attribute_data, 0x14, "Chain Dance Base Duration")
    sheik.add_attribute_special(attribute_data, 0x18, "Chain Dance Rehit Rate")
    sheik.add_attribute_special(attribute_data, 0x20, "Chain Dance Control Frame")
    sheik.add_attribute_special(attribute_data, 0x24, "Chain Dance Retraction Delay Frame")
    sheik.add_attribute_special(attribute_data, 0x28, "Chain Dance Retraction Begin Frame")
    sheik.add_attribute_special(attribute_data, 0x2C, "Vanish Vertical Momentum")
    sheik.add_attribute_special(attribute_data, 0x30, "Vanish Physics Variable")
    sheik.add_attribute_special(attribute_data, 0x34, "Vanish Fall Acceleration")
    sheik.add_attribute_special(attribute_data, 0x38, "Vanish Travel Distance", True)
    sheik.add_attribute_special(attribute_data, 0x44, "Vanish Base Momentum")
    sheik.add_attribute_special(attribute_data, 0x48, "Vanish Momentum Variable")
    sheik.add_attribute_special(attribute_data, 0x4C, "Vanish Momentum After Poof")
    sheik.add_attribute_special(attribute_data, 0x54, "Vanish Momentum After Poof 2")
    sheik.add_attribute_special(attribute_data, 0x5C, "Vanish Landing Lag")
    sheik.add_attribute_special(attribute_data, 0x60, "Transform Horizontal Momentum Preservation")
    sheik.add_attribute_special(attribute_data, 0x64, "Transform Vertical Momentum Preservation")
    # Articles
    needle_data = sheik.articles_datas[0]
    sheik.add_attribute_article(needle_data, 0x0, "Needles Air Duration")
    sheik.add_attribute_article(needle_data, 0x4, "Needles Ground Duration")
    sheik.add_attribute_article(needle_data, 0x8, "Needles Travel Speed")
    chain_data = sheik.articles_datas[1]
    sheik.add_attribute_article(chain_data, 0x0, "Chain Number of Segments", 1, True)
    sheik.add_attribute_article(chain_data, 0x4, "Chain Size", 1)
    sheik.add_attribute_article(chain_data, 0x10, "Chain Gravity/Elasticity", 1)
    sheik.add_attribute_article(chain_data, 0x14, "Chain Collision Sensitivity", 1)
    sheik.add_attribute_article(chain_data, 0x18, "Chain Gravity Modifier", 1)
    sheik.add_attribute_article(chain_data, 0x1C, "Chain Rebound Sensitivity", 1)
    sheik.add_attribute_article(chain_data, 0x20, "Chain Movement Modifier 2", 1)
    sheik.add_attribute_article(chain_data, 0x24, "Chain Mystery Value 1", 1)
    sheik.add_attribute_article(chain_data, 0x28, "Chain Mystery Value 2", 1)
    sheik.add_attribute_article(chain_data, 0x2C, "Chain Mystery Value 3", 1)
    sheik.add_attribute_article(chain_data, 0x30, "Chain Mystery Value 4", 1)
    sheik.add_attribute_article(chain_data, 0x34, "Chain Falling Speed", 1)
    sheik.add_attribute_article(chain_data, 0x38, "Chain Rebound Modifier 1", 1)
    sheik.add_attribute_article(chain_data, 0x3C, "Chain Rebound Modifier 2", 1)
    sheik.add_attribute_article(chain_data, 0x40, "Chain Delay Before Fall Acceleration", 1)
    sheik.add_attribute_article(chain_data, 0x44, "Chain Falling Mod", 1)
    sheik.add_attribute_article(chain_data, 0x48, "Chain Movement Modifier 2", 1)
    sheik.add_attribute_article(chain_data, 0x50, "Chain Spawn Position", 1)
    sheik.add_attribute_article(chain_data, 0x54, "Chain Movement Modifier 3", 1)
    sheik.add_attribute_article(chain_data, 0x58, "Chain Movement Modifier 4", 1)
    sheik.add_attribute_article(chain_data, 0x5C, "Chain Rebound from Collision", 1)
    sheik.add_attribute_article(chain_data, 0x60, "Chain Movement Modifier 5", 1)

    # Yoshi
    yoshi = characters.find_fighter("Yoshi")
    yoshi.add_attack(merge_from_subactions(yoshi.subactions, [302, 307]), "Egg Roll")
    yoshi.add_attack(merge_from_subactions(yoshi.subactions, [310, 311, 313]), "Ground Pound")
    attribute_data = yoshi.special_attribute_data
    yoshi.add_attribute_special(attribute_data, 0x0, "Flutter Jump Turn Duration", True)
    yoshi.add_attribute_special(attribute_data, 0x8, "Flutter Jump Super Armor")
    yoshi.add_attribute_special(attribute_data, 0x10, "Egg Lay Horizontal Momentum")
    yoshi.add_attribute_special(attribute_data, 0x14, "Egg Lay Vertical Momentum")
    yoshi.add_attribute_special(attribute_data, 0x18, "Egg Lay Damage Multiplier")
    yoshi.add_attribute_special(attribute_data, 0x20, "Egg Lay Growth Time")
    yoshi.add_attribute_special(attribute_data, 0x24, "Egg Lay Base Duration")
    yoshi.add_attribute_special(attribute_data, 0x28, "Egg Lay Breakout Resistance")
    yoshi.add_attribute_special(attribute_data, 0x2C, "Egg Lay Wiggle Out")
    yoshi.add_attribute_special(attribute_data, 0x38, "Egg Lay Release Intangibility", True)
    yoshi.add_attribute_special(attribute_data, 0x3C, "Egg Lay Break Out Horizontal Velocity")
    yoshi.add_attribute_special(attribute_data, 0x40, "Egg Lay Break Out Vertical Velocity")
    yoshi.add_attribute_special(attribute_data, 0x48, "Egg Roll Max Duration", True)
    yoshi.add_attribute_special(attribute_data, 0x4C, "Egg Roll Minimum Duration", True)
    yoshi.add_attribute_special(attribute_data, 0x50, "Egg Roll Duration Subtraction on Hit", True)
    yoshi.add_attribute_special(attribute_data, 0x58, "Egg Roll Horizontal Momentum")
    yoshi.add_attribute_special(attribute_data, 0x5C, "Egg Roll Vertical Momentum")
    yoshi.add_attribute_special(attribute_data, 0x60, "Egg Roll Spin Intensity")
    yoshi.add_attribute_special(attribute_data, 0x64, "Egg Roll First Land Momentum")
    yoshi.add_attribute_special(attribute_data, 0x68, "Egg Roll Smash Momentum Multiplier")
    yoshi.add_attribute_special(attribute_data, 0x6C, "Egg Roll Gravity")
    yoshi.add_attribute_special(attribute_data, 0x70, "Egg Roll Ending Gravity")
    yoshi.add_attribute_special(attribute_data, 0x74, "Egg Roll Accleration")
    yoshi.add_attribute_special(attribute_data, 0x7C, "Egg Roll Speed Modifier")
    yoshi.add_attribute_special(attribute_data, 0x8C, "Egg Roll Damage From Speed Modifier")
    yoshi.add_attribute_special(attribute_data, 0x90, "Egg Roll Air Acceleration")
    yoshi.add_attribute_special(attribute_data, 0x94, "Egg Roll Smash Window Ground")
    yoshi.add_attribute_special(attribute_data, 0x98, "Egg Roll Smash Window Air")
    yoshi.add_attribute_special(attribute_data, 0xA0, "Egg Roll Spin On Turn Modifier")
    yoshi.add_attribute_special(attribute_data, 0xAC, "Egg Roll Horizontal Recoil")
    yoshi.add_attribute_special(attribute_data, 0xB0, "Egg Roll Vertical Recoil")
    yoshi.add_attribute_special(attribute_data, 0xB4, "Egg Roll Velocity Mod On Recoil")
    yoshi.add_attribute_special(attribute_data, 0xB8, "Egg Roll Friction")
    yoshi.add_attribute_special(attribute_data, 0xBC, "Egg Roll Boost on Landing")
    yoshi.add_attribute_special(attribute_data, 0xC0, "Egg Roll Damage Modifier")
    yoshi.add_attribute_special(attribute_data, 0xC4, "Egg Roll Damage Ratio")
    yoshi.add_attribute_special(attribute_data, 0xCC, "Egg Roll Aerial Damage Reduction")
    yoshi.add_attribute_special(attribute_data, 0xD0, "Egg Roll Aerial Ending Acceleration")
    yoshi.add_attribute_special(attribute_data, 0xD4, "Egg Roll Acceleration Variable 1")
    yoshi.add_attribute_special(attribute_data, 0xD8, "Egg Roll Acceleration Variable 2")
    yoshi.add_attribute_special(attribute_data, 0xE0, "Egg Roll Ending Horizontal Velocity")
    yoshi.add_attribute_special(attribute_data, 0xE8, "Egg Roll Landing Lag")
    yoshi.add_attribute_special(attribute_data, 0xEC, "Egg Throw Angle Variable 1")
    yoshi.add_attribute_special(attribute_data, 0xF0, "Egg Throw Angle Variable 2")
    yoshi.add_attribute_special(attribute_data, 0xF4, "Egg Throw Angle Variable 3")
    yoshi.add_attribute_special(attribute_data, 0xF8, "Egg Throw Angle Variable 4")
    yoshi.add_attribute_special(attribute_data, 0xFC, "Egg Throw Base Launch Speed")
    yoshi.add_attribute_special(attribute_data, 0x100, "Egg Throw Launch Speed B Press Modifier")
    yoshi.add_attribute_special(attribute_data, 0x104, "Egg Throw X-Offset")
    yoshi.add_attribute_special(attribute_data, 0x108, "Egg Throw Y-Offset")
    yoshi.add_attribute_special(attribute_data, 0x110, "Egg Throw Spin Intensity")
    yoshi.add_attribute_special(attribute_data, 0x114, "Ground Pound Descent Speed")
    yoshi.add_attribute_special(attribute_data, 0x118, "Ground Pound Star X-Offset")
    yoshi.add_attribute_special(attribute_data, 0x11C, "Ground Pound Star Y-Offset")
    yoshi.add_attribute_special(attribute_data, 0x124, "Tongue Minimum Pull Speed")
    yoshi.add_attribute_special(attribute_data, 0x128, "Tongue Max Pull Speed")
    # Articles
    egg_data = yoshi.articles_datas[0]
    yoshi.add_attribute_article(egg_data, 0x00, "Egg Duration")
    star_data = yoshi.articles_datas[1]
    yoshi.add_attribute_article(star_data, 0x00, "Star Velocity", 1)
    yoshi.add_attribute_article(star_data, 0x04, "Star Acceleration", 1)

    # Young Link
    young_link = characters.find_fighter("Young Link")
    young_link.add_attack(attack_from_subaction(young_link.subactions, 295), "Forward Smash (Second Hit)")
    young_link.add_attack(attack_from_subaction(young_link.subactions, 308), "Spin Attack (Ground)")
    young_link.add_attack(attack_from_subaction(young_link.subactions, 309), "Spin Attack (Air)")
    young_link.add_attack(attack_from_subaction(young_link.subactions, 312), "Hookshot (Air)")
    attribute_data = young_link.special_attribute_data
    young_link.add_attribute_special(attribute_data, 0x0, "Bow Frames For Max Charge")
    young_link.add_attribute_special(attribute_data, 0x4, "Bow Charge Speed")
    young_link.add_attribute_special(attribute_data, 0x8, "Bow Landing Lag")
    young_link.add_attribute_special(attribute_data, 0x18, "Boomerang Launch Angle")
    young_link.add_attribute_special(attribute_data, 0x20, "Boomerang Smash Launch Velocity")
    young_link.add_attribute_special(attribute_data, 0x24, "Boomerang Tilt Launch Velocity")
    young_link.add_attribute_special(attribute_data, 0x30, "Spin Attack Landing Lag")
    young_link.add_attribute_special(attribute_data, 0x34, "Spin Attack Horizontal Momentum")
    young_link.add_attribute_special(attribute_data, 0x38, "Spin Attack Aerial Mobility")
    young_link.add_attribute_special(attribute_data, 0x3C, "Spin Attack Momentum Preservation")
    young_link.add_attribute_special(attribute_data, 0x40, "Spin Attack Vetical Momentum")
    young_link.add_attribute_special(attribute_data, 0x44, "Spin Attack Landing Gravity")
    young_link.add_attribute_special(attribute_data, 0x4C, "Down Aerial Bounce Momentum")
    young_link.add_attribute_special(attribute_data, 0x50, "Down Aerial Hitbox Reapply Rate")
    young_link.add_attribute_special(attribute_data, 0x58, "Down Aerial Hitbox 0 Damage On Rehit", True)
    young_link.add_attribute_special(attribute_data, 0x5C, "Down Aerial Hitbox 1 Damage On Rehit", True)
    young_link.add_attribute_special(attribute_data, 0x60, "Down Aerial Hitbox 2 Damage On Rehit", True)
    #young_link.add_attribute_special(attribute_data, 0x6C, "Sword Trail Colors 1 - Do not modify")
    #young_link.add_attribute_special(attribute_data, 0x70, "Sword Trail Colors 2 - Do not modify")
    #young_link.add_attribute_special(attribute_data, 0x74, "Sword Trail Colors 3 - Do not modify")
    young_link.add_attribute_special(attribute_data, 0x7C, "Sword Trail Width")
    young_link.add_attribute_special(attribute_data, 0x7C, "Sword Trail Height")
    young_link.add_attribute_special(attribute_data, 0x84, "Hookshot Grab Delay", True)
    young_link.add_attribute_special(attribute_data, 0x88, "Hookshot Grab Chain Release Begin", True)
    young_link.add_attribute_special(attribute_data, 0x8C, "Hookshot Grab Chain Retract Begin", True)
    young_link.add_attribute_special(attribute_data, 0x90, "Hookshot Grab Chain Retract Finish", True)
    young_link.add_attribute_special(attribute_data, 0x94, "Hookshot Dash Grab Delay", True)
    young_link.add_attribute_special(attribute_data, 0x98, "Hookshot Dash Grab Chain Release Begin", True)
    young_link.add_attribute_special(attribute_data, 0x9C, "Hookshot Dash Grab Chain Retract Begin", True)
    young_link.add_attribute_special(attribute_data, 0xA0, "Hookshot Dash Grab Chain Retract Finish", True)
    young_link.add_attribute_special(attribute_data, 0xA4, "Hookshot Air Delay", True)
    young_link.add_attribute_special(attribute_data, 0xA8, "Hookshot Air Chain Release Begin", True)
    young_link.add_attribute_special(attribute_data, 0xAC, "Hookshot Air Chain Retract Begin", True)
    young_link.add_attribute_special(attribute_data, 0xB0, "Hookshot Air Chain Retract Finish", True)
    young_link.add_attribute_special(attribute_data, 0xB4, "Hookshot Wall Release Jump Height")
    young_link.add_attribute_special(attribute_data, 0xB8, "Hookshot Hang Duration", True)
    young_link.add_attribute_special(attribute_data, 0xD4, "Deku Shield Collision Bubble Size")
    young_link.add_attribute_special(attribute_data, 0xD8, "Deku Shield Impact Momentum Multiplier")
    # Articles
    bomb_data = young_link.articles_datas[0]
    young_link.add_attribute_article(bomb_data, 0x0, "Bomb Duration", 0, True)
    young_link.add_attribute_article(bomb_data, 0x4, "Bomb Max Bounces", 0, True)
    young_link.add_attribute_article(bomb_data, 0x8, "Bomb Bounce Rehit Rate", 0, True)
    young_link.add_attribute_article(bomb_data, 0xC, "Bomb Explosion Flash Frames", 0, True)
    young_link.add_attribute_article(bomb_data, 0x10, "Bomb HP", 0, True)
    young_link.add_attribute_article(bomb_data, 0x24, "Bomb Horizontal Velocity to Detonate")
    young_link.add_attribute_article(bomb_data, 0x2C, "Bomb Base Launch Speed on Hit")
    young_link.add_attribute_article(bomb_data, 0x30, "Bomb Launch Speed Multiplier on Hit")
    boomerang_data = young_link.articles_datas[1]
    young_link.add_attribute_article(boomerang_data, 0x0, "Boomerang Tilt Duration", 1, True)
    young_link.add_attribute_article(boomerang_data, 0x4, "Boomerang Smash Duration", 1, True)
    young_link.add_attribute_article(boomerang_data, 0xC, "Boomerang Launch Velocity", 1)
    young_link.add_attribute_article(boomerang_data, 0x14, "Boomerang Release Angle Multiplier", 1)
    young_link.add_attribute_article(boomerang_data, 0x18, "Boomerang Return Transition Smoothness", 1)
    young_link.add_attribute_article(boomerang_data, 0x1C, "Boomerang Return Angle Modifier", 1)
    young_link.add_attribute_article(boomerang_data, 0x20, "Boomerang Return Homing Accuracy 1", 1)
    young_link.add_attribute_article(boomerang_data, 0x24, "Boomerang Return Homing Accuracy 2", 1)
    young_link.add_attribute_article(boomerang_data, 0x28, "Boomerang Rebound Angle Modifier", 1)
    young_link.add_attribute_article(boomerang_data, 0x2C, "Boomerang Return Acceleration", 1)
    young_link.add_attribute_article(boomerang_data, 0x30, "Boomerang Spin Speed", 1)
    young_link.add_attribute_article(boomerang_data, 0x38, "Boomerang Frame Delay Between SFX", 1)
    young_link.add_attribute_article(boomerang_data, 0x3C, "Boomerang Trail Effect 1 Delay", 1)
    young_link.add_attribute_article(boomerang_data, 0x40, "Boomerang Trail Effect 2 Delay", 1)
    hookshot_data = young_link.articles_datas[2]
    young_link.add_attribute_article(hookshot_data, 0xC, "Hookshot Number of Chains", 2, True)
    young_link.add_attribute_article(hookshot_data, 0x10, "Hookshot Distance Between Chains", 2)
    young_link.add_attribute_article(hookshot_data, 0x18, "Hookshot Chain Launch Speed", 2)
    young_link.add_attribute_article(hookshot_data, 0x1C, "Hookshot Chain Gravity", 2)
    young_link.add_attribute_article(hookshot_data, 0x20, "Hookshot Chain Retraction Speed", 2)
    young_link.add_attribute_article(hookshot_data, 0x4C, "Hookshot Ground Length Modifier", 2)
    young_link.add_attribute_article(hookshot_data, 0x50, "Hookshot Air Length Modifier", 2)
    arrow_data = young_link.articles_datas[3]
    young_link.add_attribute_article(arrow_data, 0x0, "Arrow Duration (Air)", 3)
    young_link.add_attribute_article(arrow_data, 0x4, "Arrow Uncharged Velocity", 3)
    young_link.add_attribute_article(arrow_data, 0x8, "Arrow Charged Velocity Multiplier", 3)
    young_link.add_attribute_article(arrow_data, 0xC, "Arrow Uncharged Damage", 3)
    young_link.add_attribute_article(arrow_data, 0x10, "Arrow Full Charge Damage", 3)
    young_link.add_attribute_article(arrow_data, 0x18, "Arrow Duration (Ground)", 3)
    young_link.add_attribute_article(arrow_data, 0x1C, "Arrow Gravity", 3)
    young_link.add_attribute_article(arrow_data, 0x20, "Arrow Arc Modifier (Cosmetic only)", 3)
    
    # Zelda
    zelda = characters.find_fighter("Zelda")
    zelda.add_attack(attack_from_subaction(zelda.subactions, 295), "Nayru's Love")
    zelda.add_attack(merge_from_subactions(zelda.subactions, [300, 301, 302]), "Din's Fire (?)")
    zelda.add_attack(merge_from_subactions(zelda.subactions, [303, 304, 305, 306]), "Farore's Wind (?)")
    attribute_data = zelda.special_attribute_data
    zelda.add_attribute_special(attribute_data, 0x4, "Nayru's Love Gravity Delay", True)
    zelda.add_attribute_special(attribute_data, 0x8, "Nayru's Love Momentum Preservation")
    zelda.add_attribute_special(attribute_data, 0xC, "Nayru's Love Fall Acceleration")
    zelda.add_attribute_special(attribute_data, 0x88, "Nayru's Love Max Damage Reflectable", True)
    zelda.add_attribute_special(attribute_data, 0x94, "Nayru's Love Reflection Bubble Size")
    zelda.add_attribute_special(attribute_data, 0x9C, "Nayru's Love Reflection Damage Multiplier")
    zelda.add_attribute_special(attribute_data, 0xA0, "Nayru's Love Reflection Speed Multiplier")
    zelda.add_attribute_special(attribute_data, 0x14, "Din's Fire Max Hold Time", True)
    zelda.add_attribute_special(attribute_data, 0x18, "Din's Fire Gravity Delay", True)
    zelda.add_attribute_special(attribute_data, 0x1C, "Din's Fire Frames for Auto Charge", True)
    zelda.add_attribute_special(attribute_data, 0x20, "Din's Fire X-Offset")
    zelda.add_attribute_special(attribute_data, 0x24, "Din's Fire Y-Offset")
    zelda.add_attribute_special(attribute_data, 0x2C, "Din's Fire Fall Acceleration")
    zelda.add_attribute_special(attribute_data, 0x34, "Din's Fire Landing Lag")
    zelda.add_attribute_special(attribute_data, 0x38, "Farore's Wind Horizontal Momentum Preservation")
    zelda.add_attribute_special(attribute_data, 0x3C, "Farore's Wind Vertical Momentum Preservation")
    zelda.add_attribute_special(attribute_data, 0x40, "Farore's Wind Fall Acceleration")
    zelda.add_attribute_special(attribute_data, 0x48, "Farore's Wind Travel Distance", True)
    zelda.add_attribute_special(attribute_data, 0x54, "Farore's Wind Base Momentum")
    zelda.add_attribute_special(attribute_data, 0x58, "Farore's Wind Momentum Variable")
    zelda.add_attribute_special(attribute_data, 0x5C, "Farore's Wind Momentum After Warp")
    zelda.add_attribute_special(attribute_data, 0x64, "Farore's Wind Momentum After Warp 2")
    zelda.add_attribute_special(attribute_data, 0x6C, "Farore's Wind Momentum Landing Lag")
    zelda.add_attribute_special(attribute_data, 0x70, "Farore's Wind Horizontal Momentum Modifier")
    zelda.add_attribute_special(attribute_data, 0x74, "Farore's Wind Vertical Momentum Modifier")
    # Articles
    dins_data_a = zelda.articles_datas[0]
    zelda.add_attribute_article(dins_data_a, 0x00, "Din's Fire Charge Maximum Duration")
    zelda.add_attribute_article(dins_data_a, 0x04, "Din's Fire Charge Damage Growth Window")
    zelda.add_attribute_article(dins_data_a, 0x10, "Din's Fire Charge Launch Angle")
    zelda.add_attribute_article(dins_data_a, 0x14, "Din's Fire Charge Initial Velocity")
    zelda.add_attribute_article(dins_data_a, 0x18, "Din's Fire Charge Acceleration")
    zelda.add_attribute_article(dins_data_a, 0x1C, "Din's Fire Charge Max Velocity")
    zelda.add_attribute_article(dins_data_a, 0x24, "Din's Fire Charge Vertical Meneuverability")
    zelda.add_attribute_article(dins_data_a, 0x28, "Din's Fire Charge Maximum Curve Angle")
    zelda.add_attribute_article(dins_data_a, 0x2C, "Din's Fire Charge Detonation Delay")
    dins_data_b = zelda.articles_datas[1]
    zelda.add_attribute_article(dins_data_b, 0x00, "Din's Fire Explosion Hitbox Size", 1)
    zelda.add_attribute_article(dins_data_b, 0x04, "Din's Fire Explosion Initial Graphic Size", 1)
    zelda.add_attribute_article(dins_data_b, 0x08, "Din's Fire Explosion Graphic Growth Multiplier", 1)
    zelda.add_attribute_article(dins_data_b, 0x0C, "Din's Fire Explosion Base Damage", 1)
    zelda.add_attribute_article(dins_data_b, 0x10, "Din's Fire Explosion Damage Multiplier", 1)
    
    
    
    ######################
    # This section is for creating sub attacks, tagging moves and attributes, giving them a flag-friendly name,
    # and rating their power level.

    def split_attack(fighter, attack, index, name_a, name_b):
        a = attack.hitboxes[0:index]        
        attack.name = name_a
        b = attack.hitboxes[index:]
        tags = []
        for tag in attack.tags:
            tags.append(tag)
        fighter.add_attack(b, name_b, attack.strength, tags, fighter.attacks.index(attack)+1)
        attack.hitboxes = a

    def split_attack_by_ids(fighter, attack, ids, name_a, name_b):
        a = []
        b = []
        for i in range(len(attack.hitboxes)):
            for id_ in ids:
                broke = False
                if i == id_:
                    a.append(attack.hitboxes[i])
                    broke = True
                    break
            if not broke:
                b.append(attack.hitboxes[i])
        tags = []
        for tag in attack.tags:
            tags.append(tag)
        fighter.add_attack(b, name_b, attack.strength, tags, fighter.attacks.index(attack)+1)
        attack.hitboxes = a
        attack.name = name_a
    
    bowser.find_attack("Jab 1").strength = 3
    bowser.find_attack("Jab 2").strength = 4
    bowser.find_attack("Dash Attack").strength = 6
    bowser.find_attack("Forward Tilt").strength = 6
    bowser.find_attack("Up Tilt").strength = 5
    bowser.find_attack("Down Tilt").strength = 5
    bowser.find_attack("Forward Smash").strength = 9
    split_attack(bowser, bowser.find_attack("Up Smash"), 2, "Up Smash (Start)", "Up Smash (End)")
    bowser.find_attack("Up Smash (Start)").strength = 8
    bowser.find_attack("Up Smash (End)").strength = 6
    split_attack(bowser, bowser.find_attack("Down Smash"), 4, "Down Smash (Spin)", "Down Smash (Final Hit)")
    bowser.find_attack("Down Smash (Spin)").strength = 2
    bowser.find_attack("Down Smash (Spin)").add_tag("multihit")
    bowser.find_attack("Down Smash (Final Hit)").strength = 7
    bowser.find_attack("Neutral Aerial").strength = 5
    bowser.find_attack("Forward Aerial").strength = 6
    bowser.find_attack("Back Aerial").strength = 6
    bowser.find_attack("Up Aerial").strength = 6
    bowser.find_attack("Down Aerial").strength = 2
    bowser.find_attack("Down Aerial").add_tag("multihit")
    bowser.find_attack("Koopa Klaw").strength = 5
    split_attack(bowser, bowser.find_attack("Whirling Fortress"), 2, "Whirling Fortress (Start)", "Whirling Fortress (Spin)")
    bowser.find_attack("Whirling Fortress (Start)").strength = 7
    bowser.find_attack("Whirling Fortress (Spin)").strength = 3
    split_attack(bowser, bowser.find_attack("Aerial Whirling Fortress"), 1, "Whirling Fortress (Start, Air)", "Whirling Fortress (Spin, Air)")
    bowser.find_attack("Whirling Fortress (Start, Air)").strength = 6
    bowser.find_attack("Whirling Fortress (Spin, Air)").strength = 2
    bowser.find_attack("Bowser Bomb").strength = 9

    falcon.find_attack("Jab 1").strength = 1
    falcon.find_attack("Jab 2").strength = 2
    falcon.find_attack("Jab 3").strength = 4
    split_attack(falcon, falcon.find_attack("Dash Attack"), 1, "Dash Attack", "Dash Attack (Late)")
    falcon.find_attack("Dash Attack").strength = 5
    falcon.find_attack("Dash Attack (Late)").strength = 3
    falcon.find_attack("Forward Tilt").strength = 5
    falcon.find_attack("Up Tilt").strength = 5
    falcon.find_attack("Down Tilt").strength = 6
    falcon.find_attack("Forward Smash").strength = 8
    split_attack(falcon, falcon.find_attack("Up Smash"), 2, "Up Smash (Start)", "Up Smash (Strong)")
    falcon.find_attack("Up Smash (Start)").strength = 4
    falcon.find_attack("Up Smash (Strong)").strength = 7
    falcon.find_attack("Down Smash").strength = 8
    split_attack(falcon, falcon.find_attack("Neutral Aerial"), 3, "Neutral Aerial (Hit 1)", "Neutral Aerial (Hit 2)")
    falcon.find_attack("Neutral Aerial (Hit 1)").strength = 2
    falcon.find_attack("Neutral Aerial (Hit 2)").strength = 4
    split_attack(falcon, falcon.find_attack("Forward Aerial"), 2, "Forward Aerial (Knee, Strong)", "Forward Aerial (Knee, Weak)")
    falcon.find_attack("Forward Aerial (Knee, Strong)").strength = 7
    falcon.find_attack("Forward Aerial (Knee, Weak)").strength = 4
    split_attack(falcon, falcon.find_attack("Back Aerial"), 3, "Back Aerial", "Back Aerial (Late)")
    falcon.find_attack("Back Aerial").strength = 6
    falcon.find_attack("Back Aerial (Late)").strength = 4
    split_attack(falcon, falcon.find_attack("Up Aerial"), 3, "Up Aerial", "Up Aerial (Late)")
    falcon.find_attack("Up Aerial").strength = 6
    falcon.find_attack("Up Aerial (Late)").strength = 4
    split_attack(falcon, falcon.find_attack("Down Aerial"), 2, "Down Aerial", "Down Aerial (Spike Hitbox)")
    falcon.find_attack("Down Aerial").strength = 6
    falcon.find_attack("Down Aerial (Spike Hitbox)").strength = 7
    falcon.find_attack("Falcon Punch").strength = 9
    falcon.find_attack("Raptor Boost (Ground)").strength = 6
    falcon.find_attack("Raptor Boost (Air)").strength = 5
    falcon.find_attack("Falcon Kick").strength = 7
    falcon.find_attack("Falcon Kick Landing").strength = 4

    dk.find_attack("Jab 1").strength = 2
    dk.find_attack("Jab 2").strength = 3
    dk.find_attack("Dash Attack").strength = 6
    dk.find_attack("Forward Tilt").strength = 5
    dk.find_attack("Up Tilt").strength = 5
    dk.find_attack("Down Tilt").strength = 4
    dk.find_attack("Forward Smash").strength = 8
    dk.find_attack("Up Smash").strength = 8
    dk.find_attack("Down Smash").strength = 7
    dk.find_attack("Neutral Aerial").strength = 5
    split_attack(dk, dk.find_attack("Forward Aerial"), 4, "Forward Aerial", "Forward Aerial (Spike)")
    dk.find_attack("Forward Aerial").strength = 7
    dk.find_attack("Forward Aerial (Spike)").strength = 7
    dk.find_attack("Back Aerial").strength = 6
    dk.find_attack("Up Aerial").strength = 6
    dk.find_attack("Down Aerial").strength = 6
    dk.find_attack("Giant Punch (No Charge)").strength = 5
    giant_punch = dk.find_attack("Giant Punch (Charged)")
    giant_punch.strength = 10
    giant_punch.damage = 30
    giant_punch.angle = 361
    giant_punch.base = 10
    dk.find_attack("Headbutt (Ground)").strength = 4
    dk.find_attack("Headbutt (Air)").strength = 6
    split_attack(dk, dk.find_attack("Spinning Kong"), 2, "Spinning Kong (Start)", "Spinning Kong (Loop)")
    dk.find_attack("Spinning Kong (Start)").strength = 6
    dk.find_attack("Spinning Kong (Loop)").strength = 3
    split_attack(dk, dk.find_attack("Spinning Kong (Air)"), 2, "Spinning Kong (Air, Start)", "Spinning Kong (Air, Loop)")
    dk.find_attack("Spinning Kong (Air, Start)").strength = 5
    dk.find_attack("Spinning Kong (Air, Loop)").strength = 3
    dk.find_attack("Hand Slap").strength = 6

    dr.find_attack("Jab 1").strength = 1
    dr.find_attack("Jab 2").strength = 2
    dr.find_attack("Jab 3").strength = 3
    dr.find_attack("Dash Attack").strength = 5
    dr.find_attack("Forward Tilt").strength = 4
    dr.find_attack("Up Tilt").strength = 5
    dr.find_attack("Down Tilt").strength = 4
    dr.find_attack("Forward Smash").strength = 8
    dr.find_attack("Up Smash").strength = 7
    dr.find_attack("Down Smash").strength = 8
    split_attack(dr, dr.find_attack("Neutral Aerial"), 2, "Neutral Aerial", "Neutral Aerial (Late)")
    dr.find_attack("Neutral Aerial").strength = 4
    dr.find_attack("Neutral Aerial (Late)").strength = 6
    dr.find_attack("Forward Aerial").strength = 7
    dr.find_attack("Back Aerial").strength = 5
    dr.find_attack("Up Aerial").strength = 5
    dr.find_attack("Down Aerial").strength = 2
    dr.find_attack("Super Sheet").strength = 4
    dr.find_attack("Super Jump Punch").strength = 3
    dr.find_attack("Dr. Tornado").strength = 3

    fox.find_attack("Jab 1").strength = 2
    fox.find_attack("Jab 2").strength = 2
    split_attack(fox, fox.find_attack("Dash Attack"), 2, "Dash Attack", "Dash Attack (Late)")
    fox.find_attack("Dash Attack").strength = 4
    fox.find_attack("Dash Attack (Late)").strength = 3
    fox.find_attack("Forward Tilt").strength = 4
    fox.find_attack("Up Tilt").strength = 5
    fox.find_attack("Down Tilt").strength = 5
    fox.find_attack("Forward Smash").strength = 7
    fox.find_attack("Up Smash").strength = 8
    fox.find_attack("Down Smash").strength = 7
    split_attack(fox, fox.find_attack("Neutral Aerial"), 3, "Neutral Aerial", "Neutral Aerial (Late)")
    fox.find_attack("Neutral Aerial").strength = 5
    fox.find_attack("Neutral Aerial (Late)").strength = 4
    fox.find_attack("Forward Aerial").strength = 5
    split_attack(fox, fox.find_attack("Back Aerial"), 2, "Back Aerial", "Back Aerial (Late)")
    fox.find_attack("Back Aerial").strength = 6
    fox.find_attack("Back Aerial (Late)").strength = 4
    split_attack(fox, fox.find_attack("Up Aerial"), 2, "Up Aerial", "Up Aerial (First Hit?)")
    fox.find_attack("Up Aerial").strength = 5
    fox.find_attack("Up Aerial (First Hit?)").strength = 3
    fox.find_attack("Down Aerial").strength = 2
    fox.find_attack("Fire Fox (Start)").strength = 1
    fox.find_attack("Fire Fox").strength = 6
    fox.find_attack("Shine").strength = 4

    ganon.find_attack("Jab 1").strength = 4
    split_attack(ganon, ganon.find_attack("Dash Attack"), 1, "Dash Attack", "Dash Attack (Late)")
    ganon.find_attack("Dash Attack").strength = 6
    ganon.find_attack("Dash Attack (Late)").strength = 4
    ganon.find_attack("Forward Tilt").strength = 6
    ganon.find_attack("Up Tilt").strength = 9
    ganon.find_attack("Down Tilt").strength = 6
    ganon.find_attack("Forward Smash").strength = 8
    ganon.find_attack("Up Smash").strength = 7
    split_attack(ganon, ganon.find_attack("Down Smash"), 2, "Down Smash (Start)", "Down Smash (Strong)")
    ganon.find_attack("Down Smash (Start)").strength = 4
    ganon.find_attack("Down Smash (Strong)").strength = 7
    ganon.find_attack("Neutral Aerial").strength = 5
    ganon.find_attack("Forward Aerial").strength = 7
    ganon.find_attack("Back Aerial").strength = 6
    ganon.find_attack("Up Aerial").strength = 6
    split_attack(ganon, ganon.find_attack("Down Aerial"), 2, "Down Aerial", "Down Aerial (Spike Hitbox)")
    ganon.find_attack("Down Aerial").strength = 7
    ganon.find_attack("Warlock Punch").strength = 10
    ganon.find_attack("Gerudo Dragon (Ground)").strength = 6
    ganon.find_attack("Gerudo Dragon (Air)").strength = 6
    split_attack(ganon, ganon.find_attack("Wizard's Foot"), 3, "Wizard's Foot", "Wizard's Foot (Air)")
    ganon.find_attack("Wizard's Foot").strength = 6
    ganon.find_attack("Wizard's Foot (Air)").strength = 7
    ganon.find_attack("Wizard's Foot Landing").strength = 5

    popo.find_attack("Jab 1").strength = 2
    popo.find_attack("Jab 2").strength = 3
    popo.find_attack("Dash Attack").strength = 5
    popo_ftilt = popo.find_attack("Forward Tilt")
    popo_ftilt.damage = 8
    popo_ftilt.angle = 361
    popo_ftilt.growth = 100
    popo_ftilt.base = 26
    popo.find_attack("Forward Tilt").strength = 4
    split_attack(popo, popo.find_attack("Up Tilt"), 2, "Up Tilt (Loop)", "Up Tilt (Strong)")
    popo.find_attack("Up Tilt (Loop)").strength = 1
    popo.find_attack("Up Tilt (Strong)").strength = 5
    popo.find_attack("Down Tilt").strength = 4
    popo.find_attack("Forward Smash").strength = 7
    popo.find_attack("Up Smash").strength = 7
    popo.find_attack("Down Smash").strength = 7
    popo.find_attack("Neutral Aerial").strength = 4
    split_attack(popo, popo.find_attack("Forward Aerial"), 1, "Forward Aerial (Spike)", "Forward Aerial")
    popo.find_attack("Forward Aerial (Spike)").strength = 7
    popo.find_attack("Forward Aerial").strength = 6
    popo.find_attack("Back Aerial").strength = 5
    popo.find_attack("Up Aerial").strength = 5
    popo.find_attack("Down Aerial").strength = 3
    popo.find_attack("Ice Shot").strength = 4

    nana.find_attack("Jab 1").strength = 2
    nana.find_attack("Jab 2").strength = 3
    nana.find_attack("Dash Attack").strength = 5
    nana_ftilt = nana.find_attack("Forward Tilt")
    nana_ftilt.damage = 8
    nana_ftilt.angle = 361
    nana_ftilt.growth = 100
    nana_ftilt.base = 26
    nana.find_attack("Forward Tilt").strength = 4
    split_attack(nana, nana.find_attack("Up Tilt"), 2, "Up Tilt (Loop)", "Up Tilt (Strong)")
    nana.find_attack("Up Tilt (Loop)").strength = 1
    nana.find_attack("Up Tilt (Strong)").strength = 5
    nana.find_attack("Down Tilt").strength = 4
    nana.find_attack("Forward Smash").strength = 7
    nana.find_attack("Up Smash").strength = 7
    nana.find_attack("Down Smash").strength = 7
    nana.find_attack("Neutral Aerial").strength = 4
    split_attack(nana, nana.find_attack("Forward Aerial"), 1, "Forward Aerial (Spike)", "Forward Aerial")
    nana.find_attack("Forward Aerial (Spike)").strength = 7
    nana.find_attack("Forward Aerial").strength = 6
    nana.find_attack("Back Aerial").strength = 5
    nana.find_attack("Up Aerial").strength = 5
    nana.find_attack("Down Aerial").strength = 3
    nana.find_attack("Ice Shot").strength = 4
    nana.find_attack("Belay").strength = 6

    puff.find_attack("Jab 1").strength = 2
    puff.find_attack("Jab 2").strength = 2
    puff.find_attack("Dash Attack").strength = 5
    puff.find_attack("Forward Tilt").strength = 4
    puff.find_attack("Up Tilt").strength = 5
    puff.find_attack("Down Tilt").strength = 4
    puff.find_attack("Forward Smash").strength = 7
    puff.find_attack("Up Smash").strength = 6
    puff.find_attack("Down Smash").strength = 6
    puff.find_attack("Neutral Aerial").strength = 5
    split_attack(puff, puff.find_attack("Forward Aerial"), 2, "Forward Aerial", "Forward Aerial (Late)")
    puff.find_attack("Forward Aerial").strength = 5
    puff.find_attack("Forward Aerial (Late)").strength = 4
    puff.find_attack("Back Aerial").strength = 6
    puff.find_attack("Up Aerial").strength = 6
    puff.find_attack("Down Aerial").strength = 1
    puff.find_attack("Rollout").strength = 6
    puff.find_attack("Pound").strength = 6
    puff.find_attack("Sing").strength = 9
    puff.find_attack("Rest").strength = 10

    kirby.find_attack("Jab 1").strength = 2
    kirby.find_attack("Jab 2").strength = 2
    kirby.find_attack("Dash Attack").strength = 5
    kirby.find_attack("Forward Tilt").strength = 5
    kirby.find_attack("Up Tilt").strength = 5
    kirby.find_attack("Down Tilt").strength = 5
    kirby.find_attack("Forward Smash").strength = 7
    kirby.find_attack("Up Smash").strength = 7
    kirby.find_attack("Down Smash").strength = 7
    kirby.find_attack("Neutral Aerial").strength = 5
    split_attack(kirby, kirby.find_attack("Forward Aerial"), 2, "Forward Aerial (Loop)", "Forward Aerial (Strong)")
    kirby.find_attack("Forward Aerial (Loop)").strength = 3
    kirby.find_attack("Forward Aerial (Strong)").strength = 5
    kirby.find_attack("Back Aerial").strength = 6
    kirby.find_attack("Up Aerial").strength = 6
    kirby.find_attack("Down Aerial").strength = 3
    kirby_hammer = kirby.find_attack("Hammer (Ground)")
    kirby_hammer.damage = 23
    kirby_hammer.growth = 76
    kirby_hammer.base = 65
    kirby_hammer.strength = 8
    kirby.find_attack("Hammer (Air)").strength = 3
    kirby.find_attack("Final Cutter").strength = 4
    kirby.find_attack("Stone").strength = 7
    kirby.find_attack("Falcon Punch (Copy)").strength = 8
    kirby.find_attack("Ice Shot (Copy)").strength = 5
    kirby.find_attack("Giant Punch (Copy, Uncharged)").strength = 5
    kirby_giant_punch = kirby.find_attack("Giant Punch (Copy, Charged)")
    kirby_giant_punch.damage = 30
    kirby_giant_punch.angle = 361
    kirby_giant_punch.base = 10
    kirby_giant_punch.strength = 10
    split_attack(kirby, kirby.find_attack("Nayru's Love (Copy)"), 2, "Nayru's Love (Copy, Loop)", "Nayru's Love (Copy, Strong)")
    kirby.find_attack("Nayru's Love (Copy, Loop)").strength = 1
    kirby.find_attack("Nayru's Love (Copy, Strong)").strength = 5
    kirby.find_attack("Rollout (Copy)").strength = 6
    kirby.find_attack("Shield Breaker (Copy, Uncharged)").strength = 5
    kirby.find_attack("Shield Breaker (Copy, Charged)").strength = 9
    kirby.find_attack("Shadow Ball (Copy, Loop)").strength = 2
    kirby.find_attack("Sausage (Copy)").strength = 4
    kirby.find_attack("Warlock Punch (Copy)").strength = 10
    kirby.find_attack("Flare Blade? (Copy, Uncharged)").strength = 5
    kirby.find_attack("Flare Blade? (Copy, Charged)").strength = 10

    link.find_attack("Jab 1").strength = 3
    link.find_attack("Jab 2").strength = 2
    link.find_attack("Jab 3").strength = 4
    link.find_attack("Dash Attack").strength = 5
    link.find_attack("Forward Tilt").strength = 6
    link.find_attack("Up Tilt").strength = 5
    link.find_attack("Down Tilt").strength = 6
    link.find_attack("Forward Smash").strength = 7
    split_attack(link, link.find_attack("Up Smash"), 8, "Up Smash (Loop)", "Up Smash (Strong)")
    link.find_attack("Up Smash (Loop)").strength = 3
    link.find_attack("Up Smash (Strong)").strength = 6
    link_downsmash = link.find_attack("Down Smash")
    link_downsmash.damage = 16
    link_downsmash.strength = 7
    link.find_attack("Neutral Aerial").strength = 5
    link.find_attack("Forward Aerial").strength = 6
    link.find_attack("Back Aerial").base = 15
    link.find_attack("Back Aerial").strength = 5
    link.find_attack("Up Aerial").base = 15
    link.find_attack("Up Aerial").strength = 6
    link.find_attack("Down Aerial").strength = 7
    link.find_attack("Forward Smash (Second Hit)").strength = 8
    split_attack(link, link.find_attack("Spin Attack (Ground)"), 4, "Spin Attack (Ground, Strong)", "Spin Attack (Ground, Loop)")
    link.find_attack("Spin Attack (Ground, Strong)").strength = 8
    link.find_attack("Spin Attack (Ground, Loop)").strength = 3
    link.find_attack("Spin Attack (Air)").strength = 3
    link.find_attack("Hookshot (Air)").strength = 5

    luigi.find_attack("Jab 1").strength = 2
    luigi.find_attack("Jab 2").strength = 2
    luigi.find_attack("Jab 3").strength = 3
    luigi.find_attack("Dash Attack").strength = 2
    luigi.find_attack("Forward Tilt").strength = 5
    luigi.find_attack("Up Tilt").strength = 5
    luigi.find_attack("Down Tilt").strength = 4
    luigi.find_attack("Forward Smash").strength = 7
    luigi.find_attack("Up Smash").strength = 7
    luigi.find_attack("Down Smash").strength = 7
    luigi.find_attack("Neutral Aerial").strength = 6
    luigi.find_attack("Forward Aerial").strength = 6
    luigi.find_attack("Back Aerial").strength = 5
    luigi.find_attack("Up Aerial").strength = 5
    luigi.find_attack("Down Aerial").strength = 6
    luigi.find_attack("Appeal").strength = 1
    luigi.find_attack("Green Missile (Uncharged)").strength = 5
    luigi.find_attack("Green Missile (Charged, Misfire)").strength = 9
    split_attack(luigi, luigi.find_attack("Super Jump Punch (Ground)"), 1, "Super Jump Punch (Ground, Strong)", "Super Jump Punch (Ground, Late)")
    luigi.find_attack("Super Jump Punch (Ground, Strong)").strength = 9
    luigi.find_attack("Super Jump Punch (Ground, Late)").strength = 1
    split_attack(luigi, luigi.find_attack("Super Jump Punch (Air)"), 1, "Super Jump Punch (Air, Strong)", "Super Jump Punch (Air, Late)")
    luigi.find_attack("Super Jump Punch (Air, Strong)").strength = 8
    luigi.find_attack("Super Jump Punch (Air, Late)").strength = 1
    luigi.find_attack("Cyclone").strength = 5

    mario.find_attack("Jab 1").strength = 1
    mario.find_attack("Jab 2").strength = 2
    mario.find_attack("Jab 3").strength = 3
    mario.find_attack("Dash Attack").strength = 5
    mario.find_attack("Forward Tilt").strength = 4
    mario.find_attack("Up Tilt").strength = 5
    mario.find_attack("Down Tilt").strength = 4
    mario.find_attack("Forward Smash").strength = 8
    mario.find_attack("Up Smash").strength = 7
    mario.find_attack("Down Smash").strength = 7
    split_attack(mario, mario.find_attack("Neutral Aerial"), 2, "Neutral Aerial", "Neutral Aerial (Late)")
    mario.find_attack("Neutral Aerial").strength = 5
    mario.find_attack("Neutral Aerial (Late)").strength = 4
    mario.find_attack("Forward Aerial").strength = 7
    mario.find_attack("Back Aerial").strength = 5
    mario.find_attack("Up Aerial").strength = 5
    mario.find_attack("Down Aerial").strength = 2
    mario.find_attack("Cape").strength = 4
    mario.find_attack("Super Jump Punch").strength = 3
    mario.find_attack("Tornado").strength = 3

    marth.find_attack("Jab 1").strength = 3
    marth.find_attack("Jab 2").strength = 3
    split_attack(marth, marth.find_attack("Dash Attack"), 3, "Dash Attack", "Dash Attack (Tipper)")
    marth.find_attack("Dash Attack").strength = 5
    marth.find_attack("Dash Attack (Tipper)").strength = 6
    split_attack(marth, marth.find_attack("Forward Tilt"), 3, "Forward Tilt", "Forward Tilt (Tipper)")
    marth.find_attack("Forward Tilt").strength = 4
    marth.find_attack("Forward Tilt (Tipper)").strength = 5
    split_attack_by_ids(marth, marth.find_attack("Up Tilt"), [3,7], "Up Tilt (Tipper)", "Up Tilt")
    marth.find_attack("Up Tilt").strength = 5
    marth.find_attack("Up Tilt (Tipper)").strength = 6
    split_attack(marth, marth.find_attack("Down Tilt"), 3, "Down Tilt", "Down Tilt (Tipper)")
    marth.find_attack("Down Tilt").strength = 4
    marth.find_attack("Down Tilt (Tipper)").strength = 5
    split_attack(marth, marth.find_attack("Forward Smash"), 3, "Forward Smash", "Forward Smash (Tipper)")
    marth.find_attack("Forward Smash").strength = 7
    marth.find_attack("Forward Smash (Tipper)").strength = 8
    split_attack(marth, marth.find_attack("Up Smash"), 3, "Up Smash", "Up Smash (Tipper)")
    marth.find_attack("Up Smash").strength = 5
    marth.find_attack("Up Smash (Tipper)").strength = 8
    split_attack_by_ids(marth, marth.find_attack("Down Smash"), [3,7], "Down Smash (Tipper)", "Down Smash")
    marth.find_attack("Down Smash").strength = 6
    marth.find_attack("Down Smash (Tipper)").strength = 8
    split_attack(marth, marth.find_attack("Neutral Aerial"), 4, "Neutral Aerial (First Hit)", "Neutral Aerial (Strong)")
    marth.find_attack("Neutral Aerial (First Hit)").strength = 2
    marth.find_attack("Neutral Aerial (Strong)").strength = 5
    split_attack(marth, marth.find_attack("Forward Aerial"), 3, "Forward Aerial", "Forward Aerial (Tipper)")
    marth.find_attack("Forward Aerial").strength = 5
    marth.find_attack("Forward Aerial (Tipper)").strength = 6
    split_attack(marth, marth.find_attack("Back Aerial"), 3, "Back Aerial", "Back Aerial (Tipper)")
    marth.find_attack("Back Aerial").strength = 5
    marth.find_attack("Back Aerial (Tipper)").strength = 6
    split_attack(marth, marth.find_attack("Up Aerial"), 3, "Up Aerial", "Up Aerial (Tipper)")
    marth.find_attack("Up Aerial").strength = 6
    marth.find_attack("Up Aerial (Tipper)").strength = 4
    split_attack(marth, marth.find_attack("Down Aerial"), 3, "Down Aerial", "Down Aerial (Tipper)")
    marth.find_attack("Down Aerial").strength = 5
    marth.find_attack("Down Aerial (Tipper)").strength = 7
    marth.find_attack("Shield Breaker (Uncharged)").strength = 4
    marth.find_attack("Shield Breaker (Charged)").strength = 10
    marth.find_attack("Dancing Blade (1st)").strength = 2
    marth.find_attack("Dancing Blade (2nd, Up)").strength = 3
    marth.find_attack("Dancing Blade (2nd, Down)").strength = 3
    marth.find_attack("Dancing Blade (3rd, Up)").strength = 5
    marth.find_attack("Dancing Blade (3rd, Side)").strength = 6
    marth.find_attack("Dancing Blade (3rd, Down)").strength = 6
    marth.find_attack("Dancing Blade (4th, Up)").strength = 7
    marth.find_attack("Dancing Blade (4th, Side)").strength = 7
    split_attack_by_ids(marth, marth.find_attack("Dancing Blade (4th, Down)"), [8,9,10], "Dancing Blade (4th, Down, Strong)", "Dancing Blade (4th, Down, Loop)")
    marth.find_attack("Dancing Blade (4th, Down, Strong)").strength = 6
    marth.find_attack("Dancing Blade (4th, Down, Loop)").strength = 3
    split_attack(marth, marth.find_attack("Dolphin Slash"), 3, "Dolphin Slash (Strong)", "Dolphin Slash")
    marth.find_attack("Dolphin Slash (Strong)").strength = 7
    marth.find_attack("Dolphin Slash").strength = 3
    marth.find_attack("Counter").strength = 5

    mewtwo.find_attack("Jab 1").strength = 3
    split_attack(mewtwo, mewtwo.find_attack("Dash Attack"), 3, "Dash Attack", "Dash Attack (Late)")
    mewtwo.find_attack("Dash Attack").strength = 5
    mewtwo.find_attack("Dash Attack (Late)").strength = 4
    mewtwo.find_attack("Forward Tilt").strength = 5
    mewtwo.find_attack("Up Tilt").strength = 5
    mewtwo.find_attack("Down Tilt").strength = 5
    mewtwo_fsmash = mewtwo.find_attack("Forward Smash")
    mewtwo_fsmash.damage = 20
    mewtwo_fsmash.growth = 75
    mewtwo_fsmash.base = 21
    mewtwo_fsmash.strength = 8
    split_attack(mewtwo, mewtwo.find_attack("Up Smash"), 4, "Up Smash (Loop)", "Up Smash")
    mewtwo.find_attack("Up Smash (Loop)").strength = 1
    mewtwo.find_attack("Up Smash").strength = 8
    mewtwo.find_attack("Down Smash").strength = 8
    split_attack(mewtwo, mewtwo.find_attack("Neutral Aerial"), 4, "Neutral Aerial (Loop)", "Neutral Aerial (Final)")
    mewtwo.find_attack("Neutral Aerial (Loop)").strength = 1
    mewtwo.find_attack("Neutral Aerial (Final)").strength = 5
    mewtwo.find_attack("Forward Aerial").strength = 6
    mewtwo.find_attack("Back Aerial").strength = 5
    mewtwo.find_attack("Up Aerial").strength = 5
    mewtwo.find_attack("Down Aerial").strength = 6
    mewtwo.find_attack("Shadow Ball (Loop)").strength = 1

    gnw.find_attack("Jab 1").strength = 2
    gnw.find_attack("Dash Attack").strength = 5
    gnw.find_attack("Forward Tilt").strength = 5
    gnw.find_attack("Up Tilt").strength = 5
    gnw.find_attack("Down Tilt").strength = 6
    gnw.find_attack("Forward Smash").strength = 8
    gnw.find_attack("Up Smash").strength = 7
    gnw_downsmash = gnw.find_attack("Down Smash")
    gnw_downsmash.damage = 16
    gnw_downsmash.angle = 80
    gnw_downsmash.growth = 90
    gnw_downsmash.base = 60
    gnw_downsmash.strength = 7
    gnw.find_attack("Neutral Aerial").strength = 7
    split_attack(gnw, gnw.find_attack("Forward Aerial"), 2, "Forward Aerial", "Forward Aerial (Late)")
    gnw.find_attack("Forward Aerial").strength = 6
    gnw.find_attack("Forward Aerial (Late)").strength = 3
    gnw.find_attack("Back Aerial").strength = 4
    gnw.find_attack("Up Aerial").strength = 4
    split_attack(gnw, gnw.find_attack("Down Aerial"), 1, "Down Aerial (Spike)", "Down Aerial")
    gnw.find_attack("Down Aerial (Spike)").strength = 7
    gnw.find_attack("Down Aerial").strength = 6
    gnw.find_attack("Sausage (Pan Hit)").strength = 4
    gnw.find_attack("Judgment (1)").strength = 1
    gnw.find_attack("Judgment (2)").strength = 2
    gnw.find_attack("Judgment (3)").strength = 3
    gnw.find_attack("Judgment (4)").strength = 4
    gnw.find_attack("Judgment (5)").strength = 5
    gnw.find_attack("Judgment (6)").strength = 5
    gnw.find_attack("Judgment (7)").strength = 6
    gnw.find_attack("Judgment (8)").strength = 4
    gnw.find_attack("Judgment (9)").strength = 10
    gnw.find_attack("Fire!").strength = 4

    ness.find_attack("Jab 1").strength = 2
    ness.find_attack("Jab 2").strength = 2
    ness.find_attack("Jab 3").strength = 3
    split_attack(ness, ness.find_attack("Dash Attack"), 4, "Dash Attack (Early)", "Dash Attack (Strong)")
    ness.find_attack("Dash Attack (Early)").strength = 3
    ness.find_attack("Dash Attack (Strong)").strength = 5
    ness.find_attack("Forward Tilt").strength = 5
    ness.find_attack("Up Tilt").strength = 5
    ness.find_attack("Down Tilt").strength = 2
    split_attack(ness, ness.find_attack("Forward Smash"), 2, "Forward Smash", "Forward Smash (Sweetspot)")
    ness.find_attack("Forward Smash").strength = 8
    ness.find_attack("Forward Smash (Sweetspot)").strength = 9
    ness.find_attack("Up Smash").strength = 6
    ness.find_attack("Down Smash").strength = 6
    ness.find_attack("Neutral Aerial").strength = 5
    split_attack(ness, ness.find_attack("Forward Aerial"), 2, "Forward Aerial (Loop)", "Forward Aerial")
    ness.find_attack("Forward Aerial (Loop)").strength = 2
    ness.find_attack("Forward Aerial").strength = 4
    split_attack(ness, ness.find_attack("Back Aerial"), 2, "Back Aerial", "Back Aerial (Late)")
    ness.find_attack("Back Aerial").strength = 6
    ness.find_attack("Back Aerial (Late)").strength = 4
    ness.find_attack("Up Aerial").strength = 5
    ness.find_attack("Down Aerial").strength = 6
    ness.find_attack("Up Smash (Hold)").strength = 3
    ness.find_attack("Down Smash (2)").strength = 5
    ness.find_attack("PK Thunder (Bolt hits Ness)").strength = 9

    peach.find_attack("Jab 1").strength = 2
    peach.find_attack("Jab 2").strength = 3
    split_attack(peach, peach.find_attack("Dash Attack"), 2, "Dash Attack", "Dash Attack (Late)")
    peach.find_attack("Dash Attack").strength = 6
    peach.find_attack("Dash Attack (Late)").strength = 4
    peach.find_attack("Forward Tilt").strength = 5
    peach.find_attack("Up Tilt").strength = 5
    peach.find_attack("Down Tilt").strength = 5
    peach.find_attack("Up Smash").strength = 7
    peach.find_attack("Down Smash").strength = 6
    peach.find_attack("Neutral Aerial").strength = 6
    peach.find_attack("Forward Aerial").strength = 7
    split_attack(peach, peach.find_attack("Back Aerial"), 1, "Back Aerial", "Back Aerial (Late)")
    peach.find_attack("Back Aerial").strength = 6
    peach.find_attack("Back Aerial (Late)").strength = 4
    peach.find_attack("Up Aerial").strength = 6
    peach.find_attack("Down Aerial").strength = 2
    tennis = peach.find_attack("Tennis Racket")
    tennis.strength = 7
    tennis.damage = 17
    tennis.angle = 45
    tennis.growth = 50
    tennis.base = 70
    peach.find_attack("Golf Club").strength = 7
    peach.find_attack("Frying Pan").strength = 7
    split_attack(peach, peach.find_attack("Parasol"), 1, "Parasol (First Hit)", "Parasol (Loop)")
    peach.find_attack("Parasol (First Hit)").strength = 4
    peach.find_attack("Parasol (Loop)").strength = 1
    peach.find_attack("Parasol (Reopen)").strength = 3

    pichu.find_attack("Jab 1").strength = 1
    pichu.find_attack("Dash Attack").strength = 5
    pichu.find_attack("Forward Tilt").strength = 4
    pichu.find_attack("Up Tilt").strength = 4
    pichu.find_attack("Down Tilt").strength = 4
    split_attack(pichu, pichu.find_attack("Forward Smash"), 3, "Forward Smash (Loop)", "Forward Smash")
    pichu.find_attack("Forward Smash (Loop)").strength = 2
    pichu.find_attack("Forward Smash").strength = 7
    pichu.find_attack("Up Smash").strength = 7
    pichu.find_attack("Down Smash").strength = 7
    split_attack(pichu, pichu.find_attack("Neutral Aerial"), 3, "Neutral Aerial", "Neutral Aerial (Late)")
    pichu.find_attack("Neutral Aerial").strength = 6
    pichu.find_attack("Neutral Aerial (Late)").strength = 4
    pichu.find_attack("Forward Aerial").strength = 2
    pichu.find_attack("Back Aerial").strength = 4
    pichu.find_attack("Up Aerial").strength = 4
    pichu.find_attack("Down Aerial").strength = 6
    pichu.find_attack("Skull Bash").strength = 3
    pichu.find_attack("Thunder").strength = 7

    pikachu.find_attack("Jab 1").strength = 1
    pikachu.find_attack("Dash Attack").strength = 5
    pikachu.find_attack("Forward Tilt").strength = 4
    pikachu.find_attack("Up Tilt").strength = 5
    pikachu.find_attack("Down Tilt").strength = 4
    pikachu.find_attack("Forward Smash").strength = 8
    split_attack(pikachu, pikachu.find_attack("Up Smash"), 3, "Up Smash", "Up Smash (Late)")
    pikachu.find_attack("Up Smash").strength = 8
    pikachu.find_attack("Up Smash (Late)").strength = 6
    split_attack(pikachu, pikachu.find_attack("Down Smash"), 3, "Down Smash (Loop)", "Down Smash")
    pikachu.find_attack("Down Smash (Loop)").strength = 3
    pikachu.find_attack("Down Smash").strength = 6
    split_attack(pikachu, pikachu.find_attack("Neutral Aerial"), 3, "Neutral Aerial", "Neutral Aerial (Late)")
    pikachu.find_attack("Neutral Aerial").strength = 5
    pikachu.find_attack("Neutral Aerial (Late)").strength = 4
    pikachu.find_attack("Forward Aerial").strength = 2
    pikachu.find_attack("Back Aerial").strength = 5
    split_attack(pikachu, pikachu.find_attack("Up Aerial"), 2, "Up Aerial (Early)", "Up Aerial (Late)")
    pikachu.find_attack("Up Aerial (Early)").strength = 5
    pikachu.find_attack("Up Aerial (Late)").strength = 4
    pikachu.find_attack("Down Aerial").strength = 6
    pikachu.find_attack("Skull Bash").strength = 3
    pikachu.find_attack("Quick Attack").strength = 2
    pikachu.find_attack("Thunder").strength = 8

    roy.find_attack("Jab 1").strength = 3
    split_attack(roy, roy.find_attack("Dash Attack"), 3, "Dash Attack", "Dash Attack (Sour Spot)")
    roy.find_attack("Dash Attack").strength = 6
    roy.find_attack("Dash Attack (Sour Spot)").strength = 4
    split_attack(roy, roy.find_attack("Forward Tilt"), 3, "Forward Tilt", "Forward Tilt (Sour Spot)")
    roy.find_attack("Forward Tilt").strength = 6
    roy.find_attack("Forward Tilt (Sour Spot)").strength = 4
    split_attack_by_ids(roy, roy.find_attack("Up Tilt"), [3,7], "Up Tilt (Sour Spot)", "Up Tilt")
    roy.find_attack("Up Tilt").strength = 5
    roy.find_attack("Up Tilt (Sour Spot)").strength = 4
    split_attack(roy, roy.find_attack("Down Tilt"), 3, "Down Tilt", "Down Tilt (Sour Spot)")
    roy.find_attack("Down Tilt").strength = 5
    roy.find_attack("Down Tilt (Sour Spot)").strength = 3
    split_attack(roy, roy.find_attack("Forward Smash"), 3, "Forward Smash", "Forward Smash (Sour Spot)")
    roy.find_attack("Forward Smash").strength = 8
    roy.find_attack("Forward Smash (Sour Spot)").strength = 6
    split_attack(roy, roy.find_attack("Up Smash"), 3, "Up Smash (Loop)", "Up Smash")
    roy.find_attack("Up Smash (Loop)").strength = 3
    roy.find_attack("Up Smash").strength = 7
    split_attack_by_ids(roy, roy.find_attack("Down Smash"), [3,7], "Down Smash (Sour Spot)", "Down Smash")
    roy.find_attack("Down Smash").strength = 7
    roy.find_attack("Down Smash (Sour Spot)").strength = 4
    split_attack(roy, roy.find_attack("Neutral Aerial"), 4, "Neutral Aerial (First Hit)", "Neutral Aerial (Strong)")
    roy.find_attack("Neutral Aerial (First Hit)").strength = 2
    roy.find_attack("Neutral Aerial (Strong)").strength = 5
    split_attack(roy, roy.find_attack("Forward Aerial"), 3, "Forward Aerial", "Forward Aerial (Sour Spot)")
    roy.find_attack("Forward Aerial").strength = 4
    roy.find_attack("Forward Aerial (Sour Spot)").strength = 3
    split_attack(roy, roy.find_attack("Back Aerial"), 3, "Back Aerial", "Back Aerial (Sour Spot)")
    roy.find_attack("Back Aerial").strength = 4
    roy.find_attack("Back Aerial (Sour Spot)").strength = 3
    split_attack(roy, roy.find_attack("Up Aerial"), 3, "Up Aerial", "Up Aerial (Sour Spot)")
    roy.find_attack("Up Aerial").strength = 5
    roy.find_attack("Up Aerial (Sour Spot)").strength = 3
    split_attack(roy, roy.find_attack("Down Aerial"), 3, "Down Aerial", "Down Aerial (Sour Spot)")
    roy.find_attack("Down Aerial").strength = 5
    roy.find_attack("Down Aerial (Sour Spot)").strength = 3
    roy.find_attack("Flare Blade (Uncharged)").strength = 4
    roy.find_attack("Flare Blade (Charged)").strength = 10
    roy.find_attack("Double-Edge Dance (1st)").strength = 2
    roy.find_attack("Double-Edge Dance (2nd, Up)").strength = 3
    roy.find_attack("Double-Edge Dance (2nd, Down)").strength = 3
    split_attack(roy, roy.find_attack("Double-Edge Dance (3rd, Up)"), 3, "Double-Edge Dance (3rd, Up)", "Double-Edge Dance (3rd, Up, Meteor)")
    roy.find_attack("Double-Edge Dance (3rd, Up)").strength = 5
    roy.find_attack("Double-Edge Dance (3rd, Up, Meteor)").strength = 6
    roy.find_attack("Double-Edge Dance (3rd, Side)").strength = 6
    roy.find_attack("Double-Edge Dance (3rd, Down)").strength = 3
    roy.find_attack("Double-Edge Dance (4th, Up)").strength = 7
    roy.find_attack("Double-Edge Dance (4th, Side)").strength = 7
    split_attack(roy, roy.find_attack("Double-Edge Dance (4th, Down)"), 4, "Double-Edge Dance (4th, Down, Loop)", "Double-Edge Dance (4th, Down)")
    roy.find_attack("Double-Edge Dance (4th, Down, Loop)").strength = 2
    roy.find_attack("Double-Edge Dance (4th, Down)").strength = 5
    # Convert Set Knockback into some Base and normalize attack, it's too problematic to Shuffle
    blazer = roy.find_attack("Blazer")
    blazer.strength = 4
    blazer.damage = 5
    blazer.angle = 84
    blazer.growth = 100
    blazer.base = 20
    blazer.set = 200
    roy.find_attack("Counter").strength = 2

    samus.find_attack("Jab 1").strength = 2
    samus.find_attack("Jab 2").strength = 4
    split_attack(samus, samus.find_attack("Dash Attack"), 1, "Dash Attack", "Dash Attack (Late)")
    samus.find_attack("Dash Attack").strength = 6
    samus.find_attack("Dash Attack (Late)").strength = 4
    samus.find_attack("Forward Tilt").strength = 5
    samus.find_attack("Up Tilt").strength = 6
    samus.find_attack("Down Tilt").strength = 6
    samus.find_attack("Forward Smash").strength = 7
    split_attack(samus, samus.find_attack("Up Smash"), 8, "Up Smash (Loop)", "Up Smash")
    samus.find_attack("Up Smash (Loop)").strength = 4
    samus.find_attack("Up Smash").strength = 6
    samus.find_attack("Down Smash").strength = 7
    samus.find_attack("Neutral Aerial").strength = 6
    samus.find_attack("Forward Aerial").strength = 4
    split_attack(samus, samus.find_attack("Back Aerial"), 2, "Back Aerial", "Back Aerial (Sweet Spot)")
    samus.find_attack("Back Aerial").strength = 5
    samus.find_attack("Back Aerial (Sweet Spot)").strength = 6
    split_attack(samus, samus.find_attack("Up Aerial"), 2, "Up Aerial (Loop)", "Up Aerial")
    samus.find_attack("Up Aerial (Loop)").strength = 4
    samus.find_attack("Up Aerial").strength = 6
    samus.find_attack("Down Aerial").strength = 6
    samus.find_attack("Screw Attack").strength = 3
    samus.find_attack("Grapple Beam (Air)").strength = 3

    sheik.find_attack("Jab 1").strength = 3
    sheik.find_attack("Jab 2").strength = 2
    split_attack(sheik, sheik.find_attack("Dash Attack"), 2, "Dash Attack", "Dash Attack (Late)")
    sheik.find_attack("Dash Attack").strength = 5
    sheik.find_attack("Dash Attack (Late)").strength = 4
    sheik.find_attack("Forward Tilt").strength = 5
    split_attack(sheik, sheik.find_attack("Up Tilt"), 2, "Up Tilt", "Up Tilt (Late)")
    sheik.find_attack("Up Tilt").strength = 5
    sheik.find_attack("Up Tilt (Late)").strength = 3
    sheik.find_attack("Down Tilt").strength = 5
    split_attack(sheik, sheik.find_attack("Forward Smash"), 3, "Forward Smash (Early)", "Forward Smash")
    sheik.find_attack("Forward Smash (Early)").strength = 3
    sheik.find_attack("Forward Smash").strength = 6
    split_attack(sheik, sheik.find_attack("Up Smash"), 2, "Up Smash", "Up Smash (Late)")
    sheik.find_attack("Up Smash").strength = 8
    sheik.find_attack("Up Smash (Late)").strength = 6
    split_attack(sheik, sheik.find_attack("Down Smash"), 3, "Down Smash", "Down Smash (Late)")
    sheik.find_attack("Down Smash").strength = 7
    sheik.find_attack("Down Smash (Late)").strength = 5
    split_attack(sheik, sheik.find_attack("Neutral Aerial"), 3, "Neutral Aerial", "Neutral Aerial (Late)")
    sheik.find_attack("Neutral Aerial").strength = 6
    sheik.find_attack("Neutral Aerial (Late)").strength = 4
    sheik.find_attack("Forward Aerial").strength = 6
    split_attack(sheik, sheik.find_attack("Back Aerial"), 4, "Back Aerial", "Back Aerial (Late)")
    sheik.find_attack("Back Aerial").strength = 5
    sheik.find_attack("Back Aerial (Late)").strength = 3
    split_attack(sheik, sheik.find_attack("Back Aerial"), 3, "Back Aerial", "Back Aerial (Sweetspot)")
    sheik.find_attack("Back Aerial").strength = 5
    sheik.find_attack("Back Aerial (Sweetspot)").strength = 6
    split_attack(sheik, sheik.find_attack("Up Aerial"), 4, "Up Aerial", "Up Aerial (Late)")
    sheik.find_attack("Up Aerial").strength = 5
    sheik.find_attack("Up Aerial (Late)").strength = 3
    split_attack(sheik, sheik.find_attack("Up Aerial"), 3, "Up Aerial", "Up Aerial (Sweetspot)")
    sheik.find_attack("Up Aerial").strength = 5
    sheik.find_attack("Up Aerial (Sweetspot)").strength = 6
    sheik.find_attack("Down Aerial").strength = 5
    sheik.find_attack("Chain Dance (Initial hit only?)").strength = 4

    yoshi.find_attack("Jab 1").strength = 2
    yoshi.find_attack("Jab 2").strength = 3
    yoshi.find_attack("Dash Attack").strength = 5
    yoshi.find_attack("Forward Tilt").strength = 6
    yoshi.find_attack("Up Tilt").strength = 5
    yoshi.find_attack("Down Tilt").strength = 5
    yoshi.find_attack("Forward Smash").strength = 7
    yoshi.find_attack("Up Smash").strength = 7
    yoshi.find_attack("Down Smash").strength = 7
    split_attack(yoshi, yoshi.find_attack("Neutral Aerial"), 3, "Neutral Aerial", "Neutral Aerial (Late)")
    yoshi.find_attack("Neutral Aerial").strength = 6
    yoshi.find_attack("Neutral Aerial (Late)").strength = 4
    yoshi.find_attack("Forward Aerial").strength = 7
    yoshi.find_attack("Back Aerial").strength = 4
    yoshi.find_attack("Up Aerial").strength = 5
    yoshi.find_attack("Down Aerial").strength = 3
    yoshi.find_attack("Egg Roll").strength = 4
    yoshi.find_attack("Ground Pound").strength = 7

    young_link.find_attack("Jab 1").strength = 3
    young_link.find_attack("Jab 2").strength = 2
    young_link.find_attack("Jab 3").strength = 4
    young_link.find_attack("Dash Attack").strength = 5
    young_link.find_attack("Forward Tilt").strength = 6
    young_link.find_attack("Up Tilt").strength = 5
    young_link.find_attack("Down Tilt").strength = 6
    young_link.find_attack("Forward Smash").strength = 7
    split_attack(young_link, young_link.find_attack("Up Smash"), 8, "Up Smash (Loop)", "Up Smash (Strong)")
    young_link.find_attack("Up Smash (Loop)").strength = 3
    young_link.find_attack("Up Smash (Strong)").strength = 6
    young_link_downsmash = young_link.find_attack("Down Smash")
    young_link_downsmash.damage = 13
    young_link_downsmash.strength = 7
    young_link.find_attack("Neutral Aerial").strength = 5
    young_link.find_attack("Forward Aerial").strength = 6
    young_link.find_attack("Back Aerial").base = 15
    young_link.find_attack("Back Aerial").strength = 5
    young_link.find_attack("Up Aerial").base = 15
    young_link.find_attack("Up Aerial").strength = 6
    split_attack(young_link, young_link.find_attack("Down Aerial"), 2, "Down Aerial", "Down Aerial (Spike)")
    young_link.find_attack("Down Aerial").strength = 6
    young_link.find_attack("Down Aerial (Spike)").strength = 7
    young_link.find_attack("Forward Smash (Second Hit)").strength = 8
    split_attack(young_link, young_link.find_attack("Spin Attack (Ground)"), 4, "Spin Attack (Ground, Loop)", "Spin Attack (Ground, End)")
    young_link.find_attack("Spin Attack (Ground, Loop)").strength = 2
    young_link.find_attack("Spin Attack (Ground, End)").strength = 5
    young_link.find_attack("Spin Attack (Air)").strength = 3
    young_link.find_attack("Hookshot (Air)").strength = 4

    zelda.find_attack("Jab 1").strength = 3
    split_attack(zelda, zelda.find_attack("Dash Attack"), 2, "Dash Attack", "Dash Attack (Late)")
    zelda.find_attack("Dash Attack").strength = 6
    zelda.find_attack("Dash Attack (Late)").strength = 4
    zelda.find_attack("Forward Tilt").strength = 6
    zelda.find_attack("Forward Tilt").damage = 13
    zelda.find_attack("Up Tilt").strength = 5
    zelda.find_attack("Down Tilt").strength = 4
    split_attack(zelda, zelda.find_attack("Forward Smash"), 4, "Forward Smash (Loop)", "Forward Smash")
    zelda.find_attack("Forward Smash (Loop)").strength = 1
    zelda.find_attack("Forward Smash").strength = 7
    split_attack(zelda, zelda.find_attack("Up Smash"), 8, "Up Smash (Loop)", "Up Smash")
    zelda.find_attack("Up Smash (Loop)").strength = 1
    zelda.find_attack("Up Smash").strength = 7
    zelda.find_attack("Down Smash").strength = 5
    split_attack(zelda, zelda.find_attack("Neutral Aerial"), 4, "Neutral Aerial (Loop)", "Neutral Aerial")
    zelda.find_attack("Neutral Aerial (Loop)").strength = 2
    zelda.find_attack("Neutral Aerial").strength = 5
    split_attack(zelda, zelda.find_attack("Forward Aerial"), 2, "Forward Aerial", "Forward Aerial (Sweet Spot)")
    zelda.find_attack("Forward Aerial").strength = 4
    zelda.find_attack("Forward Aerial (Sweet Spot)").strength = 7
    split_attack(zelda, zelda.find_attack("Back Aerial"), 2, "Back Aerial", "Back Aerial (Sweet Spot)")
    zelda.find_attack("Back Aerial").strength = 4
    zelda.find_attack("Back Aerial (Sweet Spot)").strength = 7
    split_attack(zelda, zelda.find_attack("Up Aerial"), 2, "Up Aerial", "Up Aerial (Sweet Spot)")
    zelda.find_attack("Up Aerial").strength = 4
    zelda.find_attack("Up Aerial (Sweet Spot)").strength = 7
    zelda.find_attack("Down Aerial").strength = 5
    split_attack(zelda, zelda.find_attack("Nayru's Love"), 4, "Nayru's Love (Loop)", "Nayru's Love")
    zelda.find_attack("Nayru's Love (Loop)").strength = 2
    zelda.find_attack("Nayru's Love").strength = 4
    zelda.find_attack("Din's Fire (?)").strength = 3
    zelda.find_attack("Farore's Wind (?)").strength = 3

    def name_to_tag(string):
        nametag = ""
        nametag = string.lower()
        nametag = nametag.replace(" ", "")
        nametag = nametag.replace("(", "")
        nametag = nametag.replace(")", "")
        nametag = nametag.replace(",", "")
        nametag = nametag.replace("!", "")
        nametag = nametag.replace("-", "")
        nametag = nametag.replace("'", "")
        nametag = nametag.replace("&", "")
        nametag = nametag.replace(":", "")
        nametag = nametag.replace(".", "")
        return nametag
    
    for fighter in characters.fighters:
        for attack in fighter.attacks:
            tag = name_to_tag(attack.name)
            attack.tags.append(tag)
            characters.attack_tags.append(tag)
            attack.tags.append("attack")
        for throw in fighter.throws:
            tag = name_to_tag(throw.name)
            throw.tags.append(tag)
            characters.throw_tags.append(tag)
            throw.tags.append("throw")
        for attribute in fighter.attributes:
            tag = name_to_tag(attribute.name)
            attribute.tags.append(tag)
            attribute.tags.append("attribute")
            attribute.tags.append("common")
            characters.attribute_tags.append(tag)
        for attribute in fighter.special_attributes:
            tag = name_to_tag(attribute.name)
            attribute.tags.append(tag)
            attribute.tags.append("attribute")
            attribute.tags.append("special")
            characters.attribute_tags.append(tag)
        for attribute in fighter.article_attributes:
            tag = name_to_tag(attribute.name)
            attribute.tags.append(tag)
            attribute.tags.append("attribute")
            attribute.tags.append("special")
            attribute.tags.append("article")
            characters.attribute_tags.append(tag)

    
        
        
    

    
