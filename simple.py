import characters
from random import randint as rng
from random import uniform as rng_f
from util import percent_chance
# Automatically chooses randomization settings for more streamlined seed creation.
# Most users will probably use this feature.

def get_flag_parameter(flag):
    #print(flag)
    for char in flag:
        if char == " ":
            parameter = int(flag[flag.index(char)+1:])
            return parameter
    print("No parameter!")

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

def activate_flag(flag): # 1 = Lite, 2 = Normal, 3 = Crazy!, 4 = Chaos (No balance)
    mod = get_flag_parameter(flag)
    
    if "&attack_damage" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if attack.damage > 7:
                        attack.damage = rng(attack.damage - mod * 2, attack.damage + mod * 3)
                    else:
                        attack.damage = rng(1 + mod, 8 + mod)
                for tag in attack.tags:
                    if tag == "projectile" or tag == "multihit":
                        if attack.damage > 3:
                            if percent_chance(99):
                                attack.damage = rng(2,3)
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    attack.damage = rng(1,22)
                    if percent_chance(1):
                        attack.damage = rng(23,34)
        # Shield Damage
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(5 * mod):
                        attack.shield_damage = rng(1, 4 + (mod*2)) * 5
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(5 * mod):
                        attack.shield_damage = rng(1, 40)
                    elif percent_chance(1):
                        attack.shield_damage = rng(40, 75)
                        
    if "&attack_angle" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(50):
                        if attack.angle == 361:
                            if percent_chance(50):
                                attack.angle = rng(35 - (mod * 5), 70 + (mod * 15))
                            else:
                                attack.angle = 361
                        else:
                            attack.angle = rng(attack.angle - (mod * 5), attack.angle + (mod * 15))
                    elif percent_chance(50):
                        attack.angle = rng(8-mod,28+mod) * 5
                    elif percent_chance(20):
                        attack.angle = 361
                    elif percent_chance(5):
                        attack.angle = 270
                    else:
                        attack.angle = rng(0,72) * 5
                    if attack.angle < 0:
                        attack.angle = attack.angle + 360
                    if attack.angle > 360 and attack.angle != 361:
                        attack.angle = attack.angle - 360
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(15):
                        attack.angle = 361
                    else:
                        attack.angle = rng(0,361)
                        
    if "&attack_growth" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(50):
                        if attack.growth > 40:
                            attack.growth = rng(attack.growth - (mod * 10), attack.growth + (mod * 10))
                    else:
                        attack.growth = rng(14 - mod,21 + mod) * 5
                    if attack.growth < 20:
                        attack.growth = 20
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(80):
                        attack.growth = rng(70,130)
                    else:
                        attack.growth = rng(0,200)

    if "&attack_setkb" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if attack.set_kb > 20:
                        if percent_chance(75):
                            attack.set_kb = rng(attack.set_kb - (mod * 5), attack.set_kb + (mod * 10))
                    elif percent_chance(1 * mod):
                        attack.set_kb = rng(9 - mod,23 + mod) * 5
                if attack.set_kb > attack.damage * 6:
                    attack.set_kb = attack.damage * 5
                if attack.set_kb < 0:
                    attack.set_kb = 0
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(5):
                        if percent_chance(75):
                            attack.set_kb = rng(30,150)
                        else:
                            attack.set_kb = rng(0,240)

    if "&attack_base" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if attack.base > 20:
                        attack.base = rng(attack.base - (mod * 5), attack.base + (mod * 5))
                    elif percent_chance(10 * mod):
                        attack.base = rng(4 - mod,12 + mod) * 5
                    if attack.base < 0:
                        attack.base = 0
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(40):
                        attack.base = rng(10,80)
                    elif percent_chance(1):
                        if percent_chance(20):
                            attack.base = rng(80,200)

    if "&attack_element" in flag:
        normal_elements = [0,1,2,3,4,13,15]
        contain_elements = [5,9,12]
        screw_attack = 14
        sleep = [6,7]
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(10 * mod):
                        attack.element = normal_elements[rng(0,len(normal_elements) - 1)]
                    elif percent_chance(mod):
                        attack.element = contain_elements[rng(0,len(contain_elements) - 1)]
                if attack.element == 6 or attack.element == 7:
                    if "Sing" not in attack.name:
                        attack.element = 0
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(75):
                        attack.element = normal_elements[rng(0,len(normal_elements) - 1)]
                    elif percent_chance(25):
                        attack.element = contain_elements[rng(0,len(contain_elements) - 1)]
                    elif percent_chance(10):
                        attack.element = screw_attack
                    elif percent_chance(5):
                        attack.element = sleep[0]
                    elif percent_chance(2):
                        attack.element = sleep[1]

    if "&attack_sfx" in flag:
        good_sfx = []
        for fighter in characters.fighters:
            for attack in fighter.attacks:
                for sfx in good_sfx:
                    if attack.sfx == sfx:
                        break
                good_sfx.append(attack.sfx)
        if percent_chance(25 * mod):
            attack.sfx = good_sfx[rng(0,len(good_sfx) - 1)]

    if "&attack_size" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(10 * (mod * mod)):
                        attack.size = rng(attack.size - (200 * mod), attack.size + (200 * mod))
                    if attack.size < 200:
                        attack.size = 200
        else:
            for fighter in characters.fighters:
                for attack in fighter.attacks:
                    if percent_chance(40):
                        attack.size = rng(4,64) * 50

    if "&throw_damage" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if throw.damage > 5:
                        throw.damage = rng(throw.damage - mod, throw.damage + mod * 2)
                    else:
                        throw.damage = rng(1 + mod, 5 + mod)
        else:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                  throw.damage = rng(1,16)
                if percent_chance(1):
                    throw.damage = rng(1,28)

    if "&throw_angle" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(100 - mod * 10):
                        throw.angle = rng(throw.angle - mod * 10, throw.angle + mod * 10)
                    elif percent_chance(110 - mod * 10):
                        throw.angle = rng(40 - mod * 10, 80 + mod * 10)
                    else:  
                        throw.angle = rng(0, 360)
        else:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(85):
                        throw.angle = rng(0, 180)
                    else:
                        throw.angle = rng(0, 360)

    if "&throw_growth" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(80 - mod * 10):
                        if throw.growth > 30:
                            throw.growth = rng(throw.growth - mod * 10, throw.growth + mod * 10)
                    elif percent_chance(50):
                        throw.growth = 100
                    else:
                        throw.growth = rng(40 - mod * 10, 90 + mod * 10)
        else:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    throw.growth = rng(25, 130)

    if "&throw_setkb" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if throw.set_kb > 30:
                        throw.set_kb = rng(throw.set_kb - mod * 10, throw.set_kb + mod * 10)
                    elif percent_chance(mod - 1):
                        throw.set_kb = rng(20, 50 + mod * 10)
        else:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(10):
                        throw.set_kb = rng(25, 120)

    if "&throw_base" in flag:
        if mod < 4:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(75):
                        if throw.base > 15:
                            throw.base = rng(throw.base - mod * 5, throw.base + mod * 5)
                    else:
                        throw.base = rng(mod * 5, 30 + mod * 5)
        else:
            for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(60):
                        throw.base = rng(0, 80)
                    if percent_chance(1):
                        if percent_chance(20):
                            throw.base = rng(80, 200)

    if "&throw_element" in flag:
        for fighter in characters.fighters:
                for throw in fighter.throws:
                    if percent_chance(mod * 25):
                        throw.element = rng(0,3)

    if "&attributes" in flag:
        for fighter in characters.fighters:
            for attribute in fighter.attributes:
                attribute.value = percent_range(attribute.value, 100 - 12 * mod, 100 + 12 * mod)
                
    if "&special_attributes" in flag:
        if mod > 3:
            for fighter in characters.fighters:
                for attribute in fighter.special_attributes:
                    attribute.value = percent_range(attribute.value, 10, 500)
                for attribute in fighter.article_attributes:
                    attribute.value = percent_range(attribute.value, 10, 500)
        else:
            bowser = characters.find_fighter("Bowser")
            if percent_chance(5*mod) or mod > 3:
                bowser.find_attribute("Passive Super Armor").value = rng_f(0,100)
            bowser.find_attribute("Flame Breath Recharge Rate: Fuel").value = rng_f(0.7 - 0.2 * mod, 0.7 + 0.3 * mod)
            bowser.find_attribute("Flame Breath Recharge Rate: Flame Size").value = rng_f(0.7 - 0.2 * mod, 0.7 + 0.3 * mod)
            bowser.find_attribute("Flame Breath Max Fuel").value = rng_f(360 - 100 * mod, 360 + 100 * mod)
            bowser.find_attribute("Koopa Klaw Bite Damage").value = rng(2, 3 * mod)
            bowser.find_attribute("Koopa Klaw Grab Duration").value = rng_f(250 - 50 * mod, 250 + 50 * mod)
            bowser.find_attribute("Whirling Fortress Aerial Vertical Momentum").value = rng_f(1.77 - 0.4 * mod, 1.77 + 1 * mod)
            bowser.find_attribute("Whirling Fortress Gravity").value = rng_f(0.05 - 0.01 * mod, 0.05 + 0.02 * mod)
            bowser.find_attribute("Whirling Fortress Aerial Vertical Momentum 2nd Half").value = rng_f(1 - 0.2 * mod, 1 + 0.4 * mod)
            bowser.find_attribute("Whirling Fortress Ground Speed").value = rng_f(1.5 - 0.4 * mod, 1.5 + 0.7 * mod)
            bowser.find_attribute("Whirling Fortress Momentum Preservation").value = rng_f(1.6 - 0.3 * mod, 1.6 + 0.7 * mod)
            bowser.find_attribute("Whirling Fortress Grounded Turning Speed").value = rng_f(0.15 - 0.04 * mod, 0.15 + 0.10 * mod)
            bowser.find_attribute("Whirling Fortress Aerial Mobility").value = rng_f(0.02 - 0.005 * mod, 0.2 + 0.1 * mod)
            bowser.find_attribute("Whirling Fortress Landing Lag").value = rng_f(50 - 15 * mod, 50 + 5 * mod)
            if percent_chance(10 * mod):
                bowser.find_attribute("Whirling Fortress Landing Lag").value = 1
            bowser.find_attribute("Bowser Bomb Aerial Horizontal Momentum Multiplier").value = rng_f(1.1 - 0.2 * mod, 1.1 + 0.3 * mod)
            bowser.find_attribute("Bowser Bomb Initial Aerial Vertical Momentum").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.15 * mod)
            bowser.find_attribute("Bowser Bomb Horizontal Momentum Preservation").value = rng_f(0.015 - 0.003 * mod, 0.015 + 0.01 * mod)
            bowser.find_attribute("Bowser Bomb Vertical Momentum Deceleration Rate").value = rng_f(0.03 - 0.005 * mod, 0.03 + 0.005 * mod)
            bowser.find_attribute("Bowser Bomb Gravity Scale").value = rng_f(0.4 - 0.06 * mod, 0.4 + 0.06 * mod)
            bowser.find_attribute("Bowser Bomb Descent Speed").value = rng_f(-7.5 - 2 * mod, -7.5 + 2 * mod)
            bowser.find_attribute("Flame Velocity").value = rng_f(1.9 - 0.4 * mod, 1.9 + 0.6 * mod)
            bowser.find_attribute("Flame Acceleration").value = rng_f(2.2 - 0.4 * mod, 2.2 + 0.6 * mod)
            bowser.find_attribute("Flame Min. Angle").value = rng_f(2.18 - 0.6 * mod, 2.18 + 0.4 * mod)
            bowser.find_attribute("Flame Max Angle").value = rng_f(2.53 - 0.3 * mod, 2.53 + 0.3 * mod)

            falcon = characters.find_fighter("Captain Falcon")
            falcon.find_attribute("Falcon Punch Momentum").value = rng_f(30.0 - 5.0 * mod, 30.0 + 10.0 * mod)
            falcon.find_attribute("Aerial Falcon Punch Angle Difference").value = rng_f(1.95 - 0.195 * mod, 1.95 + 0.195 * mod)
            falcon.find_attribute("Aerial Falcon Punch Vertical Momentum").value = rng_f(0.92 - 0.1 * mod, 0.92 + 0.05 * mod)
            falcon.find_attribute("Raptor Boost Gravity After Hit").value = rng_f(0.18 - 0.05 * mod, 0.18 + 0.5 * mod)
            falcon.find_attribute("Raptor Boost Gravity After Whiff A").value = rng_f(0.05 - 0.01 * mod, 0.05 + 0.02 * mod)
            falcon.find_attribute("Raptor Boost Gravity After Whiff B").value = rng_f(3.18 - 1.0 * mod, 3.18 + 1.0 * mod)
            falcon.find_attribute("Raptor Boost Whiff Landing Lag").value = rng_f(20.0 - 4.0 * mod, 20.0 + 2 * mod)
            falcon.find_attribute("Raptor Boost Success Landing Lag").value = rng_f(40.0 - 8.0 * mod, 40.0 + 4.0 * mod)
            falcon.find_attribute("Falcon Dive Air Friction Multiplier").value = rng_f(1.1 - 0.3 * mod, 1.1 + 0.5 * mod)
            falcon.find_attribute("Falcon Dive Horizontal Momentum").value = rng_f(0.85 - 0.2 * mod, 0.85 + 0.2 * mod)
            falcon.find_attribute("Falcon Dive Freefall Speed Multiplier").value = rng_f(0.72 - 0.2 * mod, 0.72 + 0.2 * mod)
            falcon.find_attribute("Falcon Dive Landing Lag").value = rng_f(30.0 - 6 * mod, 30.0 + 3.0 * mod)
            falcon.find_attribute("Falcon Dive Gravity During Throw").value = rng_f(0.3 - 0.08 * mod, 0.3 + 0.1 * mod)
            falcon.find_attribute("Falcon Kick Speed Modifier After Hit").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.2 * mod)
            falcon.find_attribute("Falcon Kick Ground Lag Multiplier").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.4 * mod)
            falcon.find_attribute("Falcon Kick Landing Lag Multiplier").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.4 * mod)
            falcon.find_attribute("Falcon Kick Ground Traction").value = rng_f(1.6 - 0.4 * mod, 1.6 + 0.6 * mod)
            falcon.find_attribute("Falcon Kick Landing Traction").value = rng_f(3.0 - 0.6 * mod, 3.0 + 0.8 * mod)

            dk = characters.find_fighter("Donkey Kong")
            dk.find_attribute("Cargo Hold Turn Speed").value = rng_f(6.0 - 1 * mod, 6.0 + 1.5 * mod)
            dk.find_attribute("Cargo Hold Jump Startup").value = rng_f(3.0 - 0.7 * mod, 3.0 + 1 * mod)
            dk.find_attribute("Cargo Hold Jump Landing Lag").value = rng_f(15.0 - 4 * mod, 15.0 + 1.5 * mod)
            dk.find_attribute("Giant Punch Arm Swings Needed To Full Charge").value = rng(10 - 3 * mod, 10 + 2 * mod)
            dk.find_attribute("Giant Punch Damage Increase Per Swing").value = rng(mod, mod + mod)
            dk.find_attribute("Giant Punch Grounded Forward Velocity (Charged)").value = rng_f(0.12 - 0.02 * mod, 0.12 + 0.2 * mod)
            dk.find_attribute("Giant Punch Landing Lag").value = rng_f(20.0 - 5.0 * mod, 20.0 + 3.0 * mod)
            dk.find_attribute("Headbutt Momentum Transfer Modifier").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.02 * mod)
            dk.find_attribute("Headbutt Gravity").value = rng_f(0.05 - 0.01 * mod, 0.05 + 0.05 * mod)
            if percent_chance(mod * 5):
                dk.find_attribute("Headbutt Gravity").value = dk.find_attribute("Headbutt Gravity").value * -1
            dk.find_attribute("Spinning Kong Aerial Vertical Velocity").value = rng_f(0.675 - 0.2 * mod, 0.675 + 0.3 * mod)
            dk.find_attribute("Spinning Kong Aerial Gravity").value = rng_f(0.07 - 0.02 * mod, 0.07 + 0.02 * mod)
            dk.find_attribute("Spinning Kong Grounded Horizontal Velocity").value = rng_f(0.85 - 0.2 * mod, 0.85 + 0.2 * mod)
            dk.find_attribute("Spinning Kong Aerial Horizontal Velocity").value = rng_f(1.4 - 0.4 * mod, 1.4 + 0.4 * mod)
            dk.find_attribute("Spinning Kong Grounded Mobility").value = rng_f(0.025 - 0.005 * mod, 0.025 + 0.01 * mod)
            dk.find_attribute("Spinning Kong Aerial Mobility").value = rng_f(0.05 - 0.01 * mod, 0.05 + 0.02 * mod)
            dk.find_attribute("Spinning Kong Landing Lag").value = rng_f(40.0 - 8.0 * mod, 40.0 + 4.0 * mod)
            dk.find_attribute("Hand Slap Hitbox X Offset 1").value = rng_f(12.0 - 2 * mod, 12.0 + 2 * mod)
            dk.find_attribute("Hand Slap Hitbox X Offset 2").value = rng_f(6.2 - 1 * mod, 6.2 + 1 * mod)

            dr = characters.find_fighter("Dr. Mario")
            dr.find_attribute("Super Sheet Horizontal Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1 * mod)
            dr.find_attribute("Super Sheet Horizontal Velocity").value = rng_f(0.0025 - 0.0005 * mod, 0.0025 + 0.001 * mod)
            dr.find_attribute("Super Sheet Vertical Momentum").value = rng_f(0.7 - 0.07 * mod, 0.7 + 0.07 * mod)
            dr.find_attribute("Super Sheet Gravity").value = rng_f(0.025 - 0.005 * mod, 0.025 + 0.01 * mod)
            dr.find_attribute("Super Sheet Max Falling Speed").value = rng_f(0.7 - 0.2 * mod, 0.7 + 0.2 * mod)
            dr.find_attribute("Super Sheet Reflection Bubble Size").value = rng_f(6.5 - 1 * mod, 6.5 + 2 * mod)
            dr.find_attribute("Super Sheet Reflection Damage Multiplier").value = rng_f(1.5 - 0.15 * mod, 1.5 + 0.25 * mod)
            dr.find_attribute("Super Sheet Projectile Reflection Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            dr.find_attribute("Super Jump Punch Freefall Mobility").value = rng_f(0.6 - 0.1 * mod, 0.6 + 0.2 * mod)
            dr.find_attribute("Super Jump Punch Landing Lag").value = rng_f(30.0 - 8.0 * mod, 30.0 + 3.0 * mod)
            dr.find_attribute("Super Jump Punch Max Angle Change").value = rng_f(18.0 - 4 * mod, 18.0 + 4 * mod)
            dr.find_attribute("Super Jump Punch Initial Horizontal Momentum").value = rng_f(0.6666 - 0.15 * mod, 0.6666 + 0.3 * mod)
            dr.find_attribute("Super Jump Punch Initial Gravity").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.1 * mod)
            dr.find_attribute("Super Jump Punch Initial Vertical Momentum").value = rng_f(0.95 - 0.2 * mod, 0.95 + 0.8 * mod)
            dr.find_attribute("Dr. Tornado Grounded Rise Resistance").value = rng_f(0.5 - 0.15 * mod, 0.5 + 0.1 * mod)
            dr.find_attribute("Dr. Tornado Base Air Speed").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.5 * mod)
            dr.find_attribute("Dr. Tornado Horizontal Velocity Limit").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.2 * mod)
            dr.find_attribute("Dr. Tornado Horizontal Acceleration").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            dr.find_attribute("Dr. Tornado Horizontal Drift").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.04 * mod)
            dr.find_attribute("Dr. Tornado Deceleration Rate").value = rng_f(0.66 - 0.15 * mod, 0.66 + 0.25 * mod)
            dr.find_attribute("Dr. Tornado Velocity Gain From B Press").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.5 * mod)
            dr.find_attribute("Dr. Tornado Terminal Velocity").value = rng_f(1.4 - 0.3 * mod, 1.4 + 0.4 * mod)
            #dr.find_attribute("Dr. Tornado Landing Lag").value = rng(0 - 0.0 * mod, 0 + 0.0 * mod)
            dr.find_attribute("Megavitamin Initial Velocity").value = rng_f(1.4 - 0.4 * mod, 1.4 + 0.5 * mod)
            dr.find_attribute("Megavitamin Angle").value = rng_f(-0.6981 - 0.2 * mod, -0.6981 + 0.2 * mod)
            dr.find_attribute("Megavitamin Duration").value = rng_f(75.0 - 10 * mod, 75.0 + 12 * mod)
            dr.find_attribute("Megavitamin Bounce Height").value = rng_f(0.9 - 0.2 * mod, 0.9 + 0.3 * mod)

            falco = characters.find_fighter("Falco")
            if percent_chance(mod * 10):
                falco.find_attribute("Blaster Launch Angle").value = rng_f(-0.5 - 0.2 * mod, 0.5 + 0.2 * mod)
            falco.find_attribute("Blaster Launch Speed").value = rng_f(5.0 - 1 * mod, 5.0 + 1 * mod)
            #falco.find_attribute("Blaster Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            falco.find_attribute("Phantasm Gravity Frame Delay").value = rng_f(15.0 - 3 * mod, 15.0 + 3 * mod)
            falco.find_attribute("Phantasm Initial Horizontal Momentum").value = rng_f(1.5 - 0.4 * mod, 1.5 + 0.5 * mod)
            falco.find_attribute("Phantasm Ground Friction").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.025 * mod)
            falco.find_attribute("Phantasm Air Dash Speed").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1 * mod)
            falco.find_attribute("Phantasm Air Dash Momentum").value = rng_f(0.07 - 0.02 * mod, 0.07 + 0.03 * mod)
            falco.find_attribute("Phantasm Air Dash Vertical Deceleration").value = rng_f(5.0 - 1 * mod, 5.0 + 1 * mod)
            falco.find_attribute("Phantasm Ending Gravity").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.02 * mod)
            falco.find_attribute("Phantasm Landing Lag").value = rng_f(20.0 - 4.0 * mod, 20.0 + 2.0 * mod)
            falco.find_attribute("Fire Bird Gravity Frame Delay").value = rng_f(15.0 - 4 * mod, 15.0 + 3 * mod)
            falco.find_attribute("Fire Bird Startup Horizontal Momentum").value = rng_f(1.25 - 0.3 * mod, 1.25 + 0.3 * mod)
            falco.find_attribute("Fire Bird Startup Aerial Momentum Preservation").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            falco.find_attribute("Fire Bird Fall Acceleration").value = rng_f(0.016 - 0.004 * mod, 0.016 + 0.005 * mod)
            falco.find_attribute("Fire Bird Frames of Travel").value = rng_f(22.0 - 4 * mod, 22.0 + 3 * mod)
            falco.find_attribute("Fire Bird Aerial Ending Momentum").value = rng_f(4.0 - 1 * mod, 4.0 + 1 * mod)
            falco.find_attribute("Fire Bird Travel Speed").value = rng_f(4.2 - 1 * mod, 4.2 + 1 * mod)
            falco.find_attribute("Fire Bird Reverse Acceleration").value = rng_f(0.17 - 0.04 * mod, 0.17 + 0.04 * mod)
            falco.find_attribute("Fire Bird Grounded Ending Momentum").value = rng_f(1.5 - 0.3 * mod, 1.5 + 0.3 * mod)
            falco.find_attribute("Fire Bird Bounce Horizontal Velocity").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.3 * mod)
            falco.find_attribute("Fire Bird Landing Lag").value = rng_f(18.0 - 3 * mod, 18.0 + 2 * mod)
            falco.find_attribute("Fire Bird Landing Lag After Bounce").value = rng_f(40.0 - 4.0 * mod, 40.0 + 4.0 * mod)
            falco.find_attribute("Reflector Release Frames").value = rng_f(18.0 - 4 * mod, 18.0 + 3 * mod)
            falco.find_attribute("Reflector Turn Animation Frames").value = rng_f(4.0 - 1 * mod, 4.0 + 1 * mod)
            if percent_chance(5 * mod):
                falco.find_attribute("Reflector Gravity Frame Delay").value = rng_f(3.0, 10.0)
            falco.find_attribute("Reflector Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 0.5 * mod)
            falco.find_attribute("Reflector Fall Acceleration").value = rng_f(0.0267 - 0.007 * mod, 0.0267 + 0.007 * mod)
            falco.find_attribute("Reflector Max Damage Reflectable").value = rng(25 - 5 * mod, 25 + 5  * mod)
            falco.find_attribute("Reflector Reflection Damage Multiplier").value = rng_f(1.5 - 0.25 * mod, 1.5 + 0.25 * mod)
            falco.find_attribute("Reflector Reflection Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.50 * mod)
            falco.find_attribute("Laser Duration").value = rng_f(100.0 - 25 * mod, 100.0 + 40 * mod)
            falco.find_attribute("Laser Max Horizontal Stretch").value = rng_f(3.0 - 0.8 * mod, 3.0 + 1 * mod)
            falco.find_attribute("Phantasm Duration of After Image").value = rng_f(100.0 - 20 * mod, 100.0 + 20 * mod)

            fox = characters.find_fighter("Fox")
            if percent_chance(mod * 10):
                fox.find_attribute("Blaster Launch Angle").value = rng_f(-0.5 - 0.2 * mod, 0.5 + 0.2 * mod)
            fox.find_attribute("Blaster Launch Speed").value = rng_f(7.0 - 2 * mod, 7.0 + 2 * mod)
            #fox.find_attribute("Blaster Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            fox.find_attribute("Illusion Gravity Frame Delay").value = rng_f(15.0 - 3 * mod, 15.0 + 3 * mod)
            fox.find_attribute("Illusion Initial Horizontal Momentum").value = rng_f(1.5 - 0.25 * mod, 1.5 + 0.4 * mod)
            fox.find_attribute("Illusion Ground Friction").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.025 * mod)
            fox.find_attribute("Illusion Air Dash Speed").value = rng_f(2.0 - 0.3 * mod, 2.0 + 0.3 * mod)
            fox.find_attribute("Illusion Air Dash Momentum").value = rng_f(0.07 - 0.015 * mod, 0.07 + 0.015 * mod)
            fox.find_attribute("Illusion Air Dash Vertical Deceleration").value = rng_f(5.0 - 1 * mod, 5.0 + 1 * mod)
            fox.find_attribute("Illusion Ending Gravity").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.02 * mod)
            fox.find_attribute("Illusion Landing Lag").value = rng_f(20.0 - 5.0 * mod, 20.0 + 3.0 * mod)
            fox.find_attribute("Fire Fox Gravity Frame Delay").value = rng_f(15.0 - 3 * mod, 15.0 + 3 * mod)
            fox.find_attribute("Fire Fox Startup Horizontal Momentum").value = rng_f(1.25 - 0.3 * mod, 1.25 + 0.3 * mod)
            fox.find_attribute("Fire Fox Startup Aerial Momentum Preservation").value = rng_f(0.02 - 0.006 * mod, 0.02 + 0.01 * mod)
            fox.find_attribute("Fire Fox Fall Acceleration").value = rng_f(0.015 - 0.003 * mod, 0.015 + 0.004 * mod)
            fox.find_attribute("Fire Fox Frames of Travel").value = rng_f(30.0 - 6 * mod, 30.0 + 6 * mod)
            fox.find_attribute("Fire Fox Aerial Ending Momentum").value = rng_f(6.0 - 1 * mod, 6.0 + 1 * mod)
            fox.find_attribute("Fire Fox Travel Speed").value = rng_f(3.8 - 1 * mod, 3.8 + 1 * mod)
            fox.find_attribute("Fire Fox Reverse Acceleration").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.025 * mod)
            fox.find_attribute("Fire Fox Grounded Ending Momentum").value = rng_f(1.5 - 0.4 * mod, 1.5 + 0.4 * mod)
            fox.find_attribute("Fire Fox Bounce Horizontal Velocity").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.2 * mod)
            fox.find_attribute("Fire Fox Landing Lag").value = rng_f(18.0 - 4 * mod, 18.0 + 2* mod)
            fox.find_attribute("Fire Fox Landing Lag After Bounce").value = rng_f(20.0 - 5 * mod, 20.0 + 2.0 * mod)
            fox.find_attribute("Reflector Release Frames").value = rng_f(18.0 - 3 * mod, 18.0 + 3 * mod)
            fox.find_attribute("Reflector Turn Animation Frames").value = rng_f(4.0 - 1 * mod, 4.0 + 1 * mod)
            if percent_chance(mod * 5):
                fox.find_attribute("Reflector Gravity Frame Delay").value = rng_f(3.0, 10.0)
            fox.find_attribute("Reflector Momentum Preservation").value = rng_f(2.0 - 0.4 * mod, 2.0 + 0.4 * mod)
            fox.find_attribute("Reflector Fall Acceleration").value = rng_f(0.0267 - 0.0027 * mod, 0.0267 + 0.0027 * mod)
            fox.find_attribute("Reflector Max Damage Reflectable").value = rng(25 - 5 * mod, 25 + 5  * mod)
            fox.find_attribute("Reflector Reflection Damage Multiplier").value = rng_f(1.5 - 0.25 * mod, 1.5 + 0.50 * mod)
            fox.find_attribute("Reflector Reflection Speed Multiplier").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.4 * mod)
            fox.find_attribute("Laser Duration").value = rng_f(35.0 - 8 * mod, 35.0 + 8 * mod)
            fox.find_attribute("Laser Max Horizontal Stretch").value = rng_f(3.0 - 0.8 * mod, 3.0 + 2 * mod)
            fox.find_attribute("Illusion Duration of After Image").value = rng_f(100.0 - 20.0 * mod, 100.0 + 20.0 * mod)

            gnw = characters.find_fighter("Mr. Game & Watch")
            gnw.find_attribute("Model Width").value = rng_f(0.01 - 0.002 * mod, 0.01 + 0.005 * mod)
            gnw.find_attribute("Chef Multi Hit Begin Frame").value = rng_f(3.0 - 0.5 * mod, 3.0 + 0.5 * mod)
            gnw.find_attribute("Chef Max Sausages").value = rng_f(5.0 - 1 * mod, 5.0 + 2 * mod)
            gnw.find_attribute("Judgment Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1 * mod)
            gnw.find_attribute("Judgment Momentum Preservation Modifier").value = rng_f(0.0025 - 0.0005 * mod, 0.0025 + 0.0005 * mod)
            gnw.find_attribute("Fire! Launch Angle Modifier").value = rng_f(0.25 - 0.025 * mod, 0.25 + 0.025 * mod)
            gnw.find_attribute("Fire! Launch Angle Max Difference").value = rng_f(0.5236 - 0.1 * mod, 0.5236 + 0.1 * mod)
            gnw.find_attribute("Fire! Landing Lag").value = rng_f(40.0 - 7 * mod, 40.0 + 2 * mod)
            gnw.find_attribute("Oil Panic Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 0.5 * mod)
            gnw.find_attribute("Oil Panic Momentum Preservation Modifier").value = rng_f(0.0025 - 0.0005 * mod, 0.0025 + 0.0008 * mod)
            gnw.find_attribute("Oil Panic Fall acceleration").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.01 * mod)
            gnw.find_attribute("Oil Panic Base Damage").value = rng_f(5.0 - 1 * mod, 5.0 + 2 * mod)
            gnw.find_attribute("Oil Panic Damage Multiplier").value = rng_f(1.5 - 0.25 * mod, 1.5 + 0.5 * mod)
            gnw.find_attribute("Oil Panic Absorption Bubble Size").value = rng_f(5.5 - 1 * mod, 5.5 + 2 * mod)
            gnw.find_attribute("Sausage Wall Bounce Multiplier").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.2 * mod)
            gnw.find_attribute("Sausage Duration").value = rng_f(80.0 - 10 * mod, 80.0 + 15 * mod)
            gnw.find_attribute("Sausage 1 Horizontal Velocity").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.2 * mod)
            gnw.find_attribute("Sausage 1 Vertical Velocity").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.2 * mod)
            gnw.find_attribute("Sausage 1 Gravity Velocity").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.01 * mod)
            gnw.find_attribute("Sausage 1 Spin Intensity").value = rng_f(2.5 - 0.5 * mod, 2.5 + 0.5 * mod)
            gnw.find_attribute("Sausage 1 Spin Intensity Multiplier").value = rng_f(0.1745 - 0.03 * mod, 0.1745 + 0.03 * mod)
            gnw.find_attribute("Sausage 2 Horizontal Velocity").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.2 * mod)
            gnw.find_attribute("Sausage 2 Vertical Velocity").value = rng_f(1.1 - 0.11 * mod, 1.1 + 0.11 * mod)
            gnw.find_attribute("Sausage 2 Gravity Velocity").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.01 * mod)
            gnw.find_attribute("Sausage 2 Spin Intensity").value = rng_f(2.5 - 0.5 * mod, 2.5 + 0.5 * mod)
            gnw.find_attribute("Sausage 2 Spin Intensity Multiplier").value = rng_f(0.5411 - 0.1 * mod, 0.5411 + 0.1 * mod)
            gnw.find_attribute("Sausage 3 Horizontal Velocity").value = rng_f(0.6 - 0.1 * mod, 0.6 + 0.1 * mod)
            gnw.find_attribute("Sausage 3 Vertical Velocity").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.3 * mod)
            gnw.find_attribute("Sausage 3 Gravity Velocity").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.01 * mod)
            gnw.find_attribute("Sausage 3 Spin Intensity").value = rng_f(2.5 - 0.5 * mod, 2.5 + 0.5 * mod)
            gnw.find_attribute("Sausage 3 Spin Intensity Multiplier").value = rng_f(0.1396 - 0.04 * mod, 0.1396 + 0.04 * mod)
            gnw.find_attribute("Sausage 4 Horizontal Velocity").value = rng_f(0.4 - 0.1 * mod, 0.4 + 0.1 * mod)
            gnw.find_attribute("Sausage 4 Vertical Velocity").value = rng_f(1.3 - 0.3 * mod, 1.3 + 0.3 * mod)
            gnw.find_attribute("Sausage 4 Gravity Velocity").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.01 * mod)
            gnw.find_attribute("Sausage 4 Spin Intensity").value = rng_f(2.5 - 0.5 * mod, 2.5 + 0.5 * mod)
            gnw.find_attribute("Sausage 4 Spin Intensity Multiplier").value = rng_f(0.733 - 0.2 * mod, 0.733 + 0.2 * mod)
            gnw.find_attribute("Sausage 5 Horizontal Velocity").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.05 * mod)
            gnw.find_attribute("Sausage 5 Vertical Velocity").value = rng_f(1.4 - 0.3 * mod, 1.4 + 0.4 * mod)
            gnw.find_attribute("Sausage 5 Gravity Velocity").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.04 * mod)
            gnw.find_attribute("Sausage 5 Spin Intensity").value = rng_f(2.5 - 0.5 * mod, 2.5 + 1 * mod)
            gnw.find_attribute("Sausage 5 Spin Intensity Multiplier").value = rng_f(0.2094 - 0.0509 * mod, 0.2094 + 0.15 * mod)

            ganon = characters.find_fighter("Ganondorf")
            ganon.find_attribute("Warlock Punch Momentum").value = rng_f(45.0 - 5 * mod, 45.0 + 15 * mod)
            ganon.find_attribute("Aerial Warlock Punch Angle Difference").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.2 * mod)
            ganon.find_attribute("Aerial Warlock Punch Vertical Momentum").value = rng_f(0.92 - 0.2 * mod, 0.92 + 0.2 * mod)
            ganon.find_attribute("Gerudo Dragon Gravity After Hit").value = rng_f(1.0 - 0.2 * mod, 1.0 + 0.2 * mod)
            ganon.find_attribute("Gerudo Dragon Gravity After Whiff A").value = rng_f(0.05 - 0.001 * mod, 0.05 + 0.02 * mod)
            ganon.find_attribute("Gerudo Dragon Gravity After Whiff B").value = rng_f(3.18 - 0.5 * mod, 3.18 + 0.8 * mod)
            ganon.find_attribute("Gerudo Dragon Whiff Landing Lag").value = rng_f(20.0 - 5 * mod, 20.0 + 2.0 * mod)
            ganon.find_attribute("Gerudo Dragon Success Landing Lag").value = rng_f(40.0 - 10 * mod, 40.0 + 4.0 * mod)
            ganon.find_attribute("Dark Dive Air Friction Multiplier").value = rng_f(1.1 - 0.3 * mod, 1.1 + 0.5 * mod)
            ganon.find_attribute("Dark Dive Horizontal Momentum").value = rng_f(0.85 - 0.2 * mod, 0.85 + 0.3 * mod)
            ganon.find_attribute("Dark Dive Freefall Speed Multiplier").value = rng_f(0.72 - 0.2 * mod, 0.72 + 0.3 * mod)
            ganon.find_attribute("Dark Dive Landing Lag").value = rng_f(30.0 - 7 * mod, 30.0 + 7 * mod)
            ganon.find_attribute("Dark Dive Gravity During Throw").value = rng_f(0.33 - 0.1 * mod, 0.33 + 0.13 * mod)
            ganon.find_attribute("Wizard's Foot Speed Modifier After Hit").value = rng_f(0.7 - 0.2 * mod, 0.7 + 0.2 * mod)
            ganon.find_attribute("Wizard's Foot Ground Lag Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.3 * mod)
            ganon.find_attribute("Wizard's Foot Landing Lag Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.3 * mod)
            ganon.find_attribute("Wizard's Foot Ground Traction").value = rng_f(1.6 - 0.4 * mod, 1.6 + 0.5 * mod)
            ganon.find_attribute("Wizard's Foot Landing Traction").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1* mod)

            popo = characters.find_fighter("Popo")
            popo.find_attribute("Spawn Offset").value = rng_f(5.0 - 1 * mod, 5.0 + 1.5 * mod)
            popo.find_attribute("Ice Shot Aerial Vertical Momentum").value = rng_f(1.5 - 0.3 * mod, 1.5 + 0.3 * mod)
            popo.find_attribute("Ice Shot Landing Lag").value = rng_f(16.0 - 4 * mod, 16.0 + 2 * mod)
            popo.find_attribute("Ice Shot Spawn X-Offset").value = rng_f(12.0 - 2 * mod, 12.0 + 2 * mod)
            popo.find_attribute("Ice Shot Spawn Y-Offset").value = rng_f(18.0 - 2 * mod, 18.0 + 3 * mod)
            popo.find_attribute("Squall Hammer Height Gain From B").value = rng_f(0.6 - 0.1 * mod, 0.6 + 0.2 * mod)
            popo.find_attribute("Squall Hammer Base Vertical Velocity").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.3 * mod)
            popo.find_attribute("Squall Hammer Initial Horizontal Velocity").value = rng_f(1.8 - 0.3 * mod, 1.8 + 0.3 * mod)
            popo.find_attribute("Squall Hammer Slope Angle Modifier").value = rng_f(0.09 - 0.02 * mod, 0.09 + 0.02 * mod)
            popo.find_attribute("Squall Hammer Aerial Horizontal Mobility").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.03 * mod)
            popo.find_attribute("Squall Hammer Ground Horizontal Mobility").value = rng_f(0.9 - 0.2 * mod, 0.9 + 0.3 * mod)
            popo.find_attribute("Squall Hammer Momentum Gain From B").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.4 * mod)
            popo.find_attribute("Squall Hammer Horizontal Wall Bounce").value = rng_f(0.75 - 0.2 * mod, 0.75 + 0.3 * mod)
            popo.find_attribute("Squall Hammer Vertical Wall Bounce").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.2 * mod)
            popo.find_attribute("Squall Hammer Solo Gravity").value = rng_f(0.1 - 0.02 * mod, 0.1 + 0.03 * mod)
            popo.find_attribute("Squall Hammer Duo Gravity").value = rng_f(0.1 - 0.02 * mod, 0.1 + 0.03 * mod)
            popo.find_attribute("Squall Hammer Solo Terminal Velocity").value = rng_f(2.8 - 0.5 * mod, 2.8 + 0.7 * mod)
            popo.find_attribute("Squall Hammer Duo Terminal Velocity").value = rng_f(2.8 - 0.5 * mod, 2.8 + 0.7 * mod)
            popo.find_attribute("Squall Hammer Duration of Modified Gravity").value = rng_f(50.0 - 10 * mod, 50.0 + 10 * mod)
            popo.find_attribute("Squall Hammer Uphill Friction").value = rng_f(0.6 - 0.1 * mod, 0.6 + 0.15 * mod)
            popo.find_attribute("Squall Hammer Aerial Initial Horizontal Velocity").value = rng_f(0.67 - 0.2 * mod, 0.67 + 0.2 * mod)
            popo.find_attribute("Squall Hammer Ground Friction").value = rng_f(0.25 - 0.07 * mod, 0.25 + 0.10 * mod)
            popo.find_attribute("Squall Hammer Landing Lag").value = rng_f(30.0 - 7 * mod, 30.0 + 3.0 * mod)
            popo.find_attribute("Belay Freefall Air Speed Multiplier").value = rng_f(1.3 - 0.4 * mod, 1.3 + 0.4 * mod)
            popo.find_attribute("Belay Landing Lag").value = rng_f(25.0 - 5 * mod, 25.0 + 3 * mod)
            popo.find_attribute("Belay Horizontal Velocity Deceleration").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1 * mod)
            popo.find_attribute("Belay Fall Acceleration").value = rng_f(0.03 - 0.007 * mod, 0.03 + 0.01 * mod)
            popo.find_attribute("Belay Duo Positive Vertical Momentum").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.5 * mod)
            popo.find_attribute("Belay Duo Negative Vertical Momentum").value = rng_f(12.0 - 4 * mod, 12.0 + 6 * mod)
            popo.find_attribute("Belay Gravity").value = rng_f(0.1 - 0.02 * mod, 0.1 + 0.05 * mod)
            popo.find_attribute("Belay Terminal Velocity").value = rng_f(1.5 - 0.35 * mod, 1.5 + 0.5 * mod)
            popo.find_attribute("Belay Solo Climber Vertical Momentum").value = rng_f(1.8 - 0.3 * mod, 1.8 + 0.4 * mod)
            popo.find_attribute("Belay Solo Climber Gravity").value = rng_f(0.1 - 0.03 * mod, 0.1 + 0.05 * mod)
            popo.find_attribute("Belay Solo Climber Terminal Velocity").value = rng_f(1.5 - 0.25 * mod, 1.5 + 0.25 * mod)
            popo.find_attribute("Belay Air Mobility Multiplier").value = rng_f(1.7 - 0.4 * mod, 1.7 + 0.5 * mod)
            popo.find_attribute("Belay Air Speed Multiplier").value = rng_f(1.7 - 0.4 * mod, 1.7 + 0.5 * mod)
            popo.find_attribute("Blizzard Delay Between Shots").value = rng_f(5.0 - 1 * mod, 5.0 + 1.5 * mod)
            popo.find_attribute("Blizzard Hitboxes X Offset").value = rng_f(2.0 - 0.4 * mod, 2.0 + 0.5 * mod)
            popo.find_attribute("Blizzard Hitboxes Y Offset").value = rng_f(2.0 - 0.4 * mod, 2.0 + 0.5 * mod)
            popo.find_attribute("CPU Squall Hammer Height Gain From B").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.3 * mod)
            popo.find_attribute("CPU Squall Hammer Base Vertical Velocity").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.4 * mod)
            popo.find_attribute("CPU Squall Hammer Initial Horizontal Velocity").value = rng_f(1.8 - 0.4 * mod, 1.8 + 0.5 * mod)
            popo.find_attribute("CPU Squall Hammer Slope Angle Modifier").value = rng_f(0.1 - 0.03 * mod, 0.1 + 0.05 * mod)
            popo.find_attribute("CPU Squall Hammer Aerial Horizontal Mobility").value = rng_f(0.14 - 0.04 * mod, 0.14 + 0.05 * mod)
            popo.find_attribute("CPU Squall Hammer Ground Horizontal Mobility").value = rng_f(1.5 - 0.4 * mod, 1.5 + 0.5 * mod)
            popo.find_attribute("CPU Squall Hammer Momentum Gain From B").value = rng_f(1.8 - 0.5 * mod, 1.8 + 0.6 * mod)
            popo.find_attribute("CPU Squall Hammer Horizontal Wall Bounce").value = rng_f(0.75 - 0.2 * mod, 0.75 + 0.2 * mod)
            popo.find_attribute("CPU Squall Hammer Vertical Wall Bounce").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            popo.find_attribute("CPU Squall Hammer Solo Gravity").value = rng_f(0.1 - 0.02 * mod, 0.1 + 0.05 * mod)
            popo.find_attribute("CPU Squall Hammer Duo Gravity").value = rng_f(0.1 - 0.02 * mod, 0.1 + 0.05 * mod)
            popo.find_attribute("CPU Squall Hammer Solo Terminal Velocity").value = rng_f(2.8 - 0.7 * mod, 2.8 + 1 * mod)
            popo.find_attribute("CPU Squall Hammer Duo Terminal Velocity").value = rng_f(2.8 - 0.7 * mod, 2.8 + 1 * mod)
            popo.find_attribute("CPU Squall Hammer Duration of Modified Gravity").value = rng_f(50.0 - 10 * mod, 50.0 + 12 * mod)
            popo.find_attribute("CPU Squall Hammer Uphill Friction").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            popo.find_attribute("CPU Squall Hammer Aerial Initial Horizontal Velocity").value = rng_f(0.65 - 0.15 * mod, 0.65 + 0.25 * mod)
            popo.find_attribute("CPU Squall Hammer Traction").value = rng_f(0.25 - 0.05 * mod, 0.25 + 0.07 * mod)
            popo.find_attribute("CPU Squall Hammer Landing Lag").value = rng_f(30.0 - 7 * mod, 30.0 + 3.0 * mod)
            popo.find_attribute("CPU Belay Freefall Air Speed Multiplier").value = rng_f(0.6 - 0.1 * mod, 0.6 + 0.2 * mod)
            popo.find_attribute("CPU Belay Landing Lag").value = rng_f(30.0 - 7 * mod, 30.0 + 3.0 * mod)
            popo.find_attribute("CPU Belay Horizontal Velocity Deceleration").value = rng_f(3.1 - 0.7 * mod, 3.1 + 1 * mod)
            popo.find_attribute("CPU Belay Gravity").value = rng_f(0.1 - 0.02 * mod, 0.1 + 0.05 * mod)
            popo.find_attribute("CPU Belay Terminal Velocity").value = rng_f(1.5 - 0.25 * mod, 1.5 + 0.5 * mod)
            popo.find_attribute("CPU Belay Solo Climber Vertical Momentum").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            popo.find_attribute("Ice Shot Duration").value = rng_f(60.0 - 10 * mod, 60.0 + 17 * mod)
            popo.find_attribute("Ice Shot Speed").value = rng_f(1.5 - 0.4 * mod, 1.5 + 0.7 * mod)
            popo.find_attribute("Ice Shot Gravity").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            popo.find_attribute("Blizzard Hitbox Duration").value = rng_f(10.0 - 2 * mod, 10.0 + 5 * mod)
            popo.find_attribute("Blizzard Hitbox Velocity").value = rng_f(2.0 - 0.6 * mod, 2.0 + 1 * mod)
            popo.find_attribute("Blizzard Hitbox Rise Acceleration").value = rng_f(0.125 - 0.03 * mod, 0.125 + 0.05 * mod)
            popo.find_attribute("Blizzard Minimum Angle of Hitbox Spread").value = rng_f(0.7854 - 0.2 * mod, 0.7854 + 0.2 * mod)
            popo.find_attribute("Blizzard Maximum Angle of Hitbox Spread").value = rng_f(1.7453 - 0.2 * mod, 1.7453 + 0.2 * mod)
            popo.find_attribute("Belay String Length").value = rng(40 - 7 * mod, 40 + 13 * mod)
            popo.find_attribute("Belay String Retraction Speed").value = rng(25 - 6 * mod, 25 + 6 * mod)
            popo.find_attribute("Belay String Gravity").value = rng_f(0.05 - 0.01 * mod, 0.05 + 0.02 * mod)
            popo.find_attribute("Belay String Length 2").value = rng(44 - 7 * mod, 44 + 13 * mod)
            popo.find_attribute("Belay String Elasticity").value = rng(60 - 6 * mod, 60 + 6 * mod)

            nana = characters.find_fighter("Nana")

            jigglypuff = characters.find_fighter("Jigglypuff")
            jigglypuff.find_attribute("Jumps Turn Duration").value = rng(12 - 3 * mod, 12 + 3 * mod)
            jigglypuff.find_attribute("Jumps Horizontal Momentum Backward").value = rng_f(0.3 - 0.06 * mod, 0.3 + 0.1 * mod)
            jigglypuff.find_attribute("Jumps Horizontal Momentum Forward").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.2 * mod)
            jigglypuff.find_attribute("Jumps Turn Momentum").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.3 * mod)
            jigglypuff.find_attribute("Jumps Horizontal Momentum Neutral").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.3 * mod)
            jigglypuff.find_attribute("Jump 1 Vertical Momentum").value = rng_f(1.65 - 0.3 * mod, 1.65 + 0.3 * mod)
            jigglypuff.find_attribute("Jump 2 Vertical Momentum").value = rng_f(1.59 - 0.3 * mod, 1.59 + 0.3 * mod)
            jigglypuff.find_attribute("Jump 3 Vertical Momentum").value = rng_f(1.47 - 0.3 * mod, 1.47 + 0.2 * mod)
            jigglypuff.find_attribute("Jump 4 Vertical Momentum").value = rng_f(1.36 - 0.4 * mod, 1.36 + 0.2 * mod)
            jigglypuff.find_attribute("Jump 5 Vertical Momentum").value = rng_f(1.25 - 0.4 * mod, 1.25 + 0.2 * mod)
            jigglypuff.find_attribute("Number of Jumps").value = rng(5 - 1 * mod, 5 + 1 * mod)
            jigglypuff.find_attribute("Rollout Duration").value = rng(90 - 20 * mod, 90 + 25 * mod)
            jigglypuff.find_attribute("Rollout Start Air Height Offset").value = rng_f(0.07 - 0.01 * mod, 0.07 + 0.02 * mod)
            jigglypuff.find_attribute("Rollout Bounciness").value = rng_f(1.3 - 0.3 * mod, 1.3 + 0.6 * mod)
            jigglypuff.find_attribute("Rollout Gravity During Roll").value = rng_f(0.05 - 0.01 * mod, 0.05 + 0.01 * mod)
            jigglypuff.find_attribute("Rollout Base Rolling Speed").value = rng_f(6.0 - 1 * mod, 6.0 + 1 * mod)
            jigglypuff.find_attribute("Rollout Max Rolling Speed").value = rng_f(16.0 - 3 * mod, 16.0 + 5 * mod)
            jigglypuff.find_attribute("Rollout Aerial X-Axis Momentum Forward").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.1 * mod)
            jigglypuff.find_attribute("Rollout Aerial Initial Momentum").value = rng_f(1.0 - 0.3 * mod, 1.0 + 0.4 * mod)
            jigglypuff.find_attribute("Rollout Max Momentum").value = rng_f(2.0 - 0.2 * mod, 2.0 + 0.2 * mod)
            jigglypuff.find_attribute("Rollout Spinning Speed").value = rng_f(0.5 - 0.1 * mod, 0.5 + 0.25 * mod)
            jigglypuff.find_attribute("Rollout Spinning Turn Speed").value = rng_f(4.0 - 1 * mod, 4.0 + 1 * mod)
            jigglypuff.find_attribute("Rollout Bounciness A").value = rng_f(0.4 - 0.1 * mod, 0.4 + 0.2 * mod)
            jigglypuff.find_attribute("Rollout Bounciness B").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            jigglypuff.find_attribute("Rollout Base Damage").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1 * mod)
            jigglypuff.find_attribute("Rollout Damage Multiplier").value = rng_f(3.0 - 0.7 * mod, 3.0 + 1 * mod)
            jigglypuff.find_attribute("Rollout Horizontal Bounce On Hit").value = rng_f(-0.13 - -0.03 * mod, -0.13 + -0.05 * mod)
            jigglypuff.find_attribute("Rollout Vertical Bounce on Hit").value = rng_f(1.6 - 0.3 * mod, 1.6 + 0.8 * mod)
            jigglypuff.find_attribute("Rollout Input Modifier").value = rng_f(0.6 - 0.1 * mod, 0.6 + 0.2 * mod)
            jigglypuff.find_attribute("Rollout Charge Rate").value = rng_f(50.0 - 10 * mod, 50.0 + 15 * mod)
            jigglypuff.find_attribute("Rollout Charge Time").value = rng_f(180.0 - 30 * mod, 180.0 + 35 * mod)
            jigglypuff.find_attribute("Rollout Spin Charge Animation").value = rng_f(0.21 - 0.05 * mod, 0.21 + 0.07 * mod)
            jigglypuff.find_attribute("Rollout Speed Variable").value = rng_f(40.0 - 10 * mod, 40.0 + 15 * mod)
            jigglypuff.find_attribute("Rollout Spin Animation Post Hit").value = rng_f(1.3 - 0.4 * mod, 1.3 + 0.58 * mod)
            jigglypuff.find_attribute("Rollout Air Speed").value = rng_f(0.03 - 0.008 * mod, 0.03 + 0.01 * mod)
            jigglypuff.find_attribute("Rollout Turn Rate Variable").value = rng_f(0.9 - 0.2 * mod, 0.9 + 0.3 * mod)
            jigglypuff.find_attribute("Rollout Landing Lag").value = rng_f(30.0 - 8 * mod, 30.0 + 3.0 * mod)

            kirby = characters.find_fighter("Kirby")
            kirby.find_attribute("Jumps Turn Duration").value = rng(12 - 2 * mod, 12 + 2 * mod)
            kirby.find_attribute("Jumps Horizontal Momentum Backward").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            kirby.find_attribute("Jumps Horizontal Momentum Forward").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            kirby.find_attribute("Jumps Turn Momentum").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            kirby.find_attribute("Jumps Horizontal Momentum Neutral").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            kirby.find_attribute("Jump 1 Vertical Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Jump 2 Vertical Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Jump 3 Vertical Momentum").value = rng_f(1.73 - 0.4325 * mod, 1.73 + 0.865 * mod)
            kirby.find_attribute("Jump 4 Vertical Momentum").value = rng_f(1.56 - 0.39 * mod, 1.56 + 0.78 * mod)
            kirby.find_attribute("Jump 5 Vertical Momentum").value = rng_f(1.33 - 0.3325 * mod, 1.33 + 0.665 * mod)
            kirby.find_attribute("Number of Jumps").value = rng(5 - 1 * mod, 5 + 1 * mod)
            kirby.find_attribute("Inhale Gravity of Inhaled Player").value = rng_f(0.45 - 0.1125 * mod, 0.45 + 0.225 * mod)
            kirby.find_attribute("Inhale Velocity of Outer Grab Box").value = rng_f(0.9 - 0.225 * mod, 0.9 + 0.45 * mod)
            kirby.find_attribute("Inhale Velocity of Inner Grab Box").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            kirby.find_attribute("Inhale Speed").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            kirby.find_attribute("Inhale Breakout Resistance").value = rng_f(12.0 - 3.0 * mod, 12.0 + 6.0 * mod)
            kirby.find_attribute("Inhale Duration Divisor").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            kirby.find_attribute("Inhale Base Duration").value = rng_f(250.0 - 62.5 * mod, 250.0 + 125.0 * mod)
            kirby.find_attribute("Inhale Star Deceleration Rate").value = rng_f(12.0 - 3.0 * mod, 12.0 + 6.0 * mod)
            kirby.find_attribute("Inhale Star Duration Divisor").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            kirby.find_attribute("Inhale Star Base Duration").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            kirby.find_attribute("Inhale Star Swallow Duration").value = rng_f(10.0 - 2.5 * mod, 10.0 + 5.0 * mod)
            kirby.find_attribute("Inhale Star Spin Animation Duration").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            kirby.find_attribute("Inhale Walk Speed").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            kirby.find_attribute("Inhale Jump Height").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            kirby.find_attribute("Inhale Stop Momentum").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            kirby.find_attribute("Inhale Spit Horizontal Velocity").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            kirby.find_attribute("Inhale Spit Velocity Deceleration Rate").value = rng_f(0.13 - 0.0325 * mod, 0.13 + 0.065 * mod)
            kirby.find_attribute("Inhale Spit Release Angle").value = rng_f(1.309 - 0.3272 * mod, 1.309 + 0.6545 * mod)
            kirby.find_attribute("Inhale Swallow Star Vertical Velocity").value = rng_f(2.8 - 0.7 * mod, 2.8 + 1.4 * mod)
            kirby.find_attribute("Inhale Swallow Star Gravity").value = rng_f(0.17 - 0.0425 * mod, 0.17 + 0.085 * mod)
            kirby.find_attribute("Inhale Spit Star Release Opponent Horizontal Velocity").value = rng_f(0.73 - 0.1825 * mod, 0.73 + 0.365 * mod)
            kirby.find_attribute("Inhale Spit Star Release Opponent Vertical Velocity").value = rng_f(2.3 - 0.575 * mod, 2.3 + 1.15 * mod)
            kirby.find_attribute("Inhale Copy Ability Lose Odds").value = rng_f(32.0 - 8.0 * mod, 32.0 + 8.0 * mod)
            kirby.find_attribute("Hammer Aerial Vertical Momentum").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            kirby.find_attribute("Hammer Landing Lag").value = rng_f(16.0 - 8.0 * mod, 16.0 + 4.0 * mod)
            kirby.find_attribute("Final Cutter Vertical Momentum").value = rng_f(0.9 - 0.225 * mod, 0.9 + 0.45 * mod)
            kirby.find_attribute("Final Cutter Horizontal Momentum").value = rng_f(8.0 - 2.0 * mod, 8.0 + 4.0 * mod)
            kirby.find_attribute("Final Cutter X-Offset of Projectile").value = rng_f(3.5 - 0.875 * mod, 3.5 + 1.75 * mod)
            kirby.find_attribute("Final Cutter Y-Offset of Projectile").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Stone Max Duration").value = rng(150 - 38 * mod, 150 + 38 * mod)
            kirby.find_attribute("Stone Minimum Duration").value = rng(18 - 4 * mod, 18 + 4 * mod)
            kirby.find_attribute("Stone Slide Acceleration").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            kirby.find_attribute("Stone Slide Max Speed").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Stone Gravity").value = rng_f(4.5 - 1.125 * mod, 4.5 + 2.25 * mod)
            #kirby.find_attribute("Stone HP").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            #kirby.find_attribute("Stone Resistance").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            #kirby.find_attribute("Stone Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Flame Breath Recharge Rate: Fuel").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            kirby.find_attribute("Flame Breath Recharge Rate: Flame Size").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            kirby.find_attribute("Flame Breath Max Fuel").value = rng_f(360.0 - 90.0 * mod, 360.0 + 180.0 * mod)
            kirby.find_attribute("Charge Shot Charge Time").value = rng_f(7.0 - 1.75 * mod, 7.0 + 3.5 * mod)
            kirby.find_attribute("Charge Shot Recoil").value = rng_f(-0.1 - -0.025 * mod, -0.1 + -0.05 * mod)
            kirby.find_attribute("Charge Shot Frames Per Charge Level").value = rng(16 - 4 * mod, 16 + 4 * mod)
            kirby.find_attribute("Charge Shot Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Toad Aerial Vertical Momentum").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            kirby.find_attribute("Toad Fall Acceleration").value = rng_f(0.025 - 0.0063 * mod, 0.025 + 0.0125 * mod)
            kirby.find_attribute("Toad Detection Bubble Size").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            kirby.find_attribute("Giant Punch Swings to Fully Charge").value = rng(10 - 2 * mod, 10 + 2 * mod)
            kirby.find_attribute("Giant Punch Damage Increase Per Swing").value = rng(2 - 0 * mod, 2 + 0 * mod)
            kirby.find_attribute("Giant Punch Grounded Horizontal Velocity").value = rng_f(0.12 - 0.03 * mod, 0.12 + 0.06 * mod)
            kirby.find_attribute("Giant Punch Landing Lag").value = rng_f(20.0 - 5.0 * mod, 20.0 + 3.0 * mod)
            kirby.find_attribute("PK Flash Grounded Animation Loop Frames").value = rng(30 - 8 * mod, 30 + 8 * mod)
            kirby.find_attribute("PK Flash Air Animation Loop Frames").value = rng(25 - 6 * mod, 25 + 6 * mod)
            kirby.find_attribute("PK Flash Falling Acceleration Delay").value = rng(10 - 2 * mod, 10 + 2 * mod)
            kirby.find_attribute("PK Flash Charge Release Delay").value = rng(30 - 8 * mod, 30 + 8 * mod)
            kirby.find_attribute("PK Flash Gravity").value = rng_f(0.017 - 0.0043 * mod, 0.017 + 0.0085 * mod)
            kirby.find_attribute("PK Flash Landing Lag").value = rng_f(30.0 - 8 * mod, 30.0 + 4.0 * mod)
            kirby.find_attribute("Pikachu Thunder Jolt Ground Spawn X-Offset").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            kirby.find_attribute("Pikachu Thunder Jolt Ground Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Pikachu Thunder Jolt Air Spawn X-Offset").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            kirby.find_attribute("Pikachu Thunder Jolt Air Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Pikachu Thunder Jolt Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Pichu Thunder Jolt Ground Spawn X-Offset").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            kirby.find_attribute("Pichu Jolt Ground Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Pichu Jolt Air Spawn X-Offset").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            kirby.find_attribute("Pichu Jolt Air Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Pichu Jolt Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Falcon Punch Momentum").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            kirby.find_attribute("Aerial Falcon Punch Angle Difference").value = rng_f(1.95 - 0.4875 * mod, 1.95 + 0.975 * mod)
            kirby.find_attribute("Aerial Falcon Punch Vertical Momentum").value = rng_f(0.92 - 0.01 * mod, 0.92 + 0.01 * mod)
            kirby.find_attribute("Warlock Punch Momentum").value = rng_f(45.0 - 11.25 * mod, 45.0 + 22.5 * mod)
            kirby.find_attribute("Aerial Warlock Punch Angle Difference").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            kirby.find_attribute("Aerial Warlock Punch Vertical Momentum").value = rng_f(0.92 - 0.01 * mod, 0.92 + 0.01 * mod)
            if percent_chance(5 * mod):
                kirby.find_attribute("Fox Blaster Launch Angle").value = rng_f(-1 - 0.5 * mod, 1 + 0.5 * mod)
            kirby.find_attribute("Fox Blaster Launch Speed").value = rng_f(7.0 - 1.75 * mod, 7.0 + 3.5 * mod)
            #kirby.find_attribute("Fox Blaster Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            if percent_chance(5 * mod):
                kirby.find_attribute("Falco Blaster Launch Angle").value = rng_f(-1 - 0.5 * mod, 1 + 0.5 * mod)
            kirby.find_attribute("Falco Blaster Launch Speed").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            #kirby.find_attribute("Falco Blaster Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Bow Frames For Max Charge").value = rng_f(60.0 - 15.0 * mod, 60.0 + 10.0 * mod)
            kirby.find_attribute("Bow Charge Speed").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.25 * mod)
            #kirby.find_attribute("Bow Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Nayru's Love Gravity Delay").value = rng(4 - 1 * mod, 4 + 1 * mod)
            kirby.find_attribute("Nayru's Love Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Nayru's Love Fall Acceleration").value = rng_f(0.0267 - 0.0067 * mod, 0.0267 + 0.0133 * mod)
            kirby.find_attribute("Nayru's Love Max Damage Reflectable").value = rng(50 - 12 * mod, 50 + 12 * mod)
            #kirby.find_attribute("Nayru's Love Reflection Bubble Size").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            #kirby.find_attribute("Nayru's Love Reflection Damage Multiplier").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            #kirby.find_attribute("Nayru's Love Reflection Speed Multiplier").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Rollout Duration").value = rng(90 - 22 * mod, 90 + 22 * mod)
            kirby.find_attribute("Rollout Start Air Height Offset").value = rng_f(0.07 - 0.0175 * mod, 0.07 + 0.035 * mod)
            kirby.find_attribute("Rollout Bounciness").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            kirby.find_attribute("Rollout Gravity During Roll").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            kirby.find_attribute("Rollout Base Rolling Speed").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            kirby.find_attribute("Rollout Max Rolling Speed").value = rng_f(16.0 - 4.0 * mod, 16.0 + 8.0 * mod)
            kirby.find_attribute("Rollout Aerial X-Axis Momentum Forward").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            kirby.find_attribute("Rollout Aerial Initial Momentum").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            kirby.find_attribute("Rollout Max Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Rollout Spinning Speed").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            kirby.find_attribute("Rollout Spinning Turn Speed").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            kirby.find_attribute("Rollout Bounciness A").value = rng_f(0.4 - 0.1 * mod, 0.4 + 0.2 * mod)
            kirby.find_attribute("Rollout Bounciness B").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            kirby.find_attribute("Rollout Base Damage").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            kirby.find_attribute("Rollout Damage Multiplier").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1 * mod)
            kirby.find_attribute("Rollout Horizontal Bounce On Hit").value = rng_f(-0.13 - 0.0325 * mod, -0.13 + 0.065 * mod)
            kirby.find_attribute("Rollout Vertical Bounce on Hit").value = rng_f(1.6 - 0.4 * mod, 1.6 + 0.8 * mod)
            kirby.find_attribute("Rollout Input Modifier").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            kirby.find_attribute("Rollout Charge Rate").value = rng_f(50.0 - 12.5 * mod, 50.0 + 25.0 * mod)
            kirby.find_attribute("Rollout Charge Time").value = rng_f(180.0 - 45.0 * mod, 180.0 + 90.0 * mod)
            kirby.find_attribute("Rollout Spin Charge Animation").value = rng_f(0.21 - 0.0525 * mod, 0.21 + 0.105 * mod)
            kirby.find_attribute("Rollout Speed Variable").value = rng_f(40.0 - 10.0 * mod, 40.0 + 20.0 * mod)
            kirby.find_attribute("Rollout Spin Animation Post Hit").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            kirby.find_attribute("Rollout Air Speed").value = rng_f(0.03 - 0.0075 * mod, 0.03 + 0.015 * mod)
            kirby.find_attribute("Rollout Turn Rate Variable").value = rng_f(0.9 - 0.225 * mod, 0.9 + 0.45 * mod)
            kirby.find_attribute("Rollout Landing Lag").value = rng_f(30.0 - 8 * mod, 30.0 + 3 * mod)
            kirby.find_attribute("Shield Breaker Loops For Full Charge").value = rng(4 - 1 * mod, 4 + 1 * mod)
            kirby.find_attribute("Shield Breaker Base Damage").value = rng(7 - 1 * mod, 7 + 1 * mod)
            kirby.find_attribute("Shield Breaker Damage Per Loop").value = rng(5 - 1 * mod, 5 + 1 * mod)
            kirby.find_attribute("Shield Breaker Momentum Preservation").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            kirby.find_attribute("Shield Breaker Deceleration Rate").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            kirby.find_attribute("Flare Blade Loops For Full Charge").value = rng(7 - 1 * mod, 7 + 1 * mod)
            kirby.find_attribute("Flare Blade Base Damage").value = rng(6 - 2 * mod, 6 + 2 * mod)
            kirby.find_attribute("Flare Blade Damage Per Loop").value = rng(5 - 1 * mod, 5 + 1 * mod)
            kirby.find_attribute("Flare Blade Momentum Preservation").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            kirby.find_attribute("Flare Blade Deceleration Rate").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            kirby.find_attribute("Shadow Ball Charge Increment").value = rng_f(7.0 - 1.75 * mod, 7.0 + 2 * mod)
            kirby.find_attribute("Shadow Ball Release Momentum Grounded").value = rng_f(-0.2 - -0.05 * mod, -0.2 + -0.1 * mod)
            kirby.find_attribute("Shadow Ball Release Momentum Air").value = rng_f(-0.4 - -0.1 * mod, -0.4 + -0.2 * mod)
            kirby.find_attribute("Shadow Ball Loops For Full Charge").value = rng(16 - 4 * mod, 16 + 4 * mod)
            #kirby.find_attribute("Shadow Ball Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Ice Shot Aerial Vertical Momentum").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            kirby.find_attribute("Ice Shot Landing Lag").value = rng_f(16.0 - 4.0 * mod, 16.0 + 2.0 * mod)
            kirby.find_attribute("Ice Shot Spawn X-Offset").value = rng_f(12.0 - 3.0 * mod, 12.0 + 3.0 * mod)
            kirby.find_attribute("Ice Shot Spawn Y-Offset").value = rng_f(18.0 - 4 * mod, 18.0 + 4 * mod)
            kirby.find_attribute("Egg Lay Horizontal Momentum").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            kirby.find_attribute("Egg Lay Vertical Momentum").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            kirby.find_attribute("Egg Lay Damage Multiplier").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            kirby.find_attribute("Egg Lay Growth Time").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            kirby.find_attribute("Egg Lay Base Duration").value = rng_f(200.0 - 50.0 * mod, 200.0 + 100.0 * mod)
            kirby.find_attribute("Egg Lay Breakout Resistance").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            kirby.find_attribute("Egg Lay Wiggle Out").value = rng_f(14.0 - 3.5 * mod, 14.0 + 7.0 * mod)
            kirby.find_attribute("Egg Lay Release Intangibility").value = rng(14 - 4 * mod, 14 + 4 * mod)
            kirby.find_attribute("Egg Lay Break Out Horizontal Velocity").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            kirby.find_attribute("Egg Lay Break Out Vertical Velocity").value = rng_f(2.4 - 0.6 * mod, 2.4 + 1.2 * mod)
            kirby.find_attribute("Chef Multi Hit Begin Frame").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            kirby.find_attribute("Chef Max Sausages").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            kirby.find_attribute("Final Cutter Velocity").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            kirby.find_attribute("Final Cutter Duration").value = rng_f(25.0 - 6.25 * mod, 25.0 + 10 * mod)
            kirby.find_attribute("Final Cutter Deceleration Rate").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)

            link = characters.find_fighter("Link")
            link.find_attribute("Bow Frames For Max Charge").value = rng_f(60.0 - 15.0 * mod, 60.0 + 30.0 * mod)
            link.find_attribute("Bow Charge Speed").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            #link.find_attribute("Bow Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            link.find_attribute("Boomerang Launch Angle").value = rng_f(0.4538 - 0.1134 * mod, 0.4538 + 0.2269 * mod)
            link.find_attribute("Boomerang Smash Launch Velocity").value = rng_f(3.1 - 0.775 * mod, 3.1 + 1.55 * mod)
            link.find_attribute("Boomerang Tilt Launch Velocity").value = rng_f(2.4 - 0.6 * mod, 2.4 + 1.2 * mod)
            link.find_attribute("Spin Attack Landing Lag").value = rng_f(24.0 - 6.0 * mod, 24.0 + 12.0 * mod)
            link.find_attribute("Spin Attack Horizontal Momentum").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            link.find_attribute("Spin Attack Aerial Mobility").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            link.find_attribute("Spin Attack Momentum Preservation").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            link.find_attribute("Spin Attack Vertical Momentum").value = rng_f(2.3 - 0.575 * mod, 2.3 + 1.15 * mod)
            link.find_attribute("Spin Attack Landing Gravity").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            link.find_attribute("Down Aerial Bounce Momentum").value = rng_f(1.33 - 0.3325 * mod, 1.33 + 0.665 * mod)
            link.find_attribute("Down Aerial Hitbox Reapply Rate").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            link.find_attribute("Down Aerial Hitbox 0 Damage On Rehit").value = rng(6 - 1 * mod, 6 + 1 * mod)
            link.find_attribute("Down Aerial Hitbox 1 Damage On Rehit").value = rng(8 - 1 * mod, 8 + 1 * mod)
            link.find_attribute("Down Aerial Hitbox 2 Damage On Rehit").value = rng(8 - 1 * mod, 8 + 1 * mod)
            link.find_attribute("Sword Trail Width").value = rng_f(1.59 - 0.3975 * mod, 1.59 + 0.795 * mod)
            link.find_attribute("Sword Trail Height").value = rng_f(1.59 - 0.3975 * mod, 1.59 + 0.795 * mod)
            link.find_attribute("Hookshot Grab Delay").value = rng(7 - 2 * mod, 7 + 1 * mod)
            link.find_attribute("Hookshot Grab Chain Release Begin").value = rng(10 - 2 * mod, 10 + 2 * mod)
            link.find_attribute("Hookshot Grab Chain Retract Begin").value = rng(55 - 14 * mod, 55 + 14 * mod)
            link.find_attribute("Hookshot Grab Chain Retract Finish").value = rng(79 - 20 * mod, 79 + 20 * mod)
            link.find_attribute("Hookshot Dash Grab Delay").value = rng(7 - 2 * mod, 7 + 2 * mod)
            link.find_attribute("Hookshot Dash Grab Chain Release Begin").value = rng(11 - 3 * mod, 11 + 3 * mod)
            link.find_attribute("Hookshot Dash Grab Chain Retract Begin").value = rng(63 - 16 * mod, 63 + 16 * mod)
            link.find_attribute("Hookshot Dash Grab Chain Retract Finish").value = rng(88 - 22 * mod, 88 + 22 * mod)
            link.find_attribute("Hookshot Air Delay").value = rng(5 - 1 * mod, 5 + 1 * mod)
            link.find_attribute("Hookshot Air Chain Release Begin").value = rng(10 - 2 * mod, 10 + 2 * mod)
            link.find_attribute("Hookshot Air Chain Retract Begin").value = rng(47 - 12 * mod, 47 + 12 * mod)
            link.find_attribute("Hookshot Air Chain Retract Finish").value = rng(58 - 14 * mod, 58 + 14 * mod)
            link.find_attribute("Hookshot Wall Release Jump Height").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            link.find_attribute("Hookshot Hang Duration").value = rng(180 - 45 * mod, 180 + 45 * mod)
            link.find_attribute("Hylian Shield Collision Bubble Size").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            link.find_attribute("Hylian Shield Impact Momentum Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            link.find_attribute("Bomb Duration").value = rng(300 - 75 * mod, 300 + 75 * mod)
            link.find_attribute("Bomb Max Bounces").value = rng(6 - 1 * mod, 6 + 1 * mod)
            link.find_attribute("Bomb Bounce Rehit Rate").value = rng(10 - 2 * mod, 10 + 2 * mod)
            link.find_attribute("Bomb Explosion Flash Frames").value = rng(96 - 24 * mod, 96 + 24 * mod)
            link.find_attribute("Bomb HP").value = rng(6 - 1 * mod, 6 + 1 * mod)
            link.find_attribute("Bomb Horizontal Velocity to Detonate").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            link.find_attribute("Bomb Base Launch Speed on Hit").value = rng_f(-0.03 - -0.0075 * mod, -0.03 + -0.015 * mod)
            link.find_attribute("Bomb Launch Speed Multiplier on Hit").value = rng_f(0.03 - 0.0075 * mod, 0.03 + 0.015 * mod)
            link.find_attribute("Boomerang Tilt Duration").value = rng(140 - 35 * mod, 140 + 35 * mod)
            link.find_attribute("Boomerang Smash Duration").value = rng(170 - 42 * mod, 170 + 42 * mod)
            link.find_attribute("Boomerang Launch Velocity").value = rng_f(0.047 - 0.0117 * mod, 0.047 + 0.0235 * mod)
            link.find_attribute("Boomerang Release Angle Multiplier").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            link.find_attribute("Boomerang Return Transition Smoothness").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            link.find_attribute("Boomerang Return Angle Modifier").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            link.find_attribute("Boomerang Return Homing Accuracy 1").value = rng_f(0.75 - 0.1875 * mod, 0.75 + 0.375 * mod)
            link.find_attribute("Boomerang Return Homing Accuracy 2").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            link.find_attribute("Boomerang Rebound Angle Modifier").value = rng_f(140.0 - 35.0 * mod, 140.0 + 70.0 * mod)
            link.find_attribute("Boomerang Return Acceleration").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            link.find_attribute("Boomerang Spin Speed").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            link.find_attribute("Boomerang Frame Delay Between SFX").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            link.find_attribute("Boomerang Trail Effect 1 Delay").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            link.find_attribute("Boomerang Trail Effect 2 Delay").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            link.find_attribute("Hookshot Number of Chains").value = rng(15 - 4 * mod, 15 + 4 * mod)
            link.find_attribute("Hookshot Distance Between Chains").value = rng_f(1.8 - 0.45 * mod, 1.8 + 0.9 * mod)
            link.find_attribute("Hookshot Chain Launch Speed").value = rng_f(2.7 - 0.675 * mod, 2.7 + 1.35 * mod)
            link.find_attribute("Hookshot Chain Gravity").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            link.find_attribute("Hookshot Chain Retraction Speed").value = rng_f(3.6 - 0.9 * mod, 3.6 + 1.8 * mod)
            link.find_attribute("Hookshot Ground Length Modifier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            link.find_attribute("Hookshot Air Length Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            link.find_attribute("Arrow Duration (Air)").value = rng_f(60.0 - 15.0 * mod, 60.0 + 30.0 * mod)
            link.find_attribute("Arrow Uncharged Velocity").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            link.find_attribute("Arrow Charged Velocity Multiplier").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            link.find_attribute("Arrow Uncharged Damage").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            link.find_attribute("Arrow Full Charge Damage").value = rng_f(18.0 - 4.5 * mod, 18.0 + 9.0 * mod)
            link.find_attribute("Arrow Duration (Ground)").value = rng_f(50.0 - 12.5 * mod, 50.0 + 25.0 * mod)
            link.find_attribute("Arrow Gravity").value = rng_f(0.053 - 0.0132 * mod, 0.053 + 0.0265 * mod)
            link.find_attribute("Arrow Arc Modifier (Cosmetic only)").value = rng_f(0.6981 - 0.1745 * mod, 0.6981 + 0.3491 * mod)

            luigi = characters.find_fighter("Luigi")
            luigi.find_attribute("Green Missile Charge Rate").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            luigi.find_attribute("Green Missile Frames to Fully Charge").value = rng_f(90.0 - 22.5 * mod, 90.0 + 45.0 * mod)
            luigi.find_attribute("Green Missile Tilt Damage").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            luigi.find_attribute("Green Missile Traction Multiplier").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            luigi.find_attribute("Green Missile Horizontal Momentum").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            luigi.find_attribute("Green Missile Horizontal Momentum Multiplier").value = rng_f(0.0167 - 0.0042 * mod, 0.0167 + 0.0083 * mod)
            luigi.find_attribute("Green Missile Vertical Momentum").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            luigi.find_attribute("Green Missile Vertical Momentum Multiplier").value = rng_f(0.01 - 0.0025 * mod, 0.01 + 0.005 * mod)
            luigi.find_attribute("Green Missile Gravity on Launch").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            luigi.find_attribute("Green Missile Ending Friction Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            luigi.find_attribute("Green Missile Launch End Horizontal Deceleration").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            luigi.find_attribute("Green Missile Launch End Gravity Multiplier").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            luigi.find_attribute("Green Missile Misfire Chance").value = rng_f(8.0 - 2.0 * mod, 8.0 + 4.0 * mod)
            luigi.find_attribute("Green Missile Misfire Horizontal Momentum").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            luigi.find_attribute("Green Missile Misfire Vertical Momentum").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            luigi.find_attribute("Super Jump Punch Freefall Mobility").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            luigi.find_attribute("Super Jump Punch Landing Lag").value = rng_f(40.0 - 10.0 * mod, 40.0 + 5.0 * mod)
            luigi.find_attribute("Super Jump Punch Air Control During Up B").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            luigi.find_attribute("Super Jump Punch Air Control Input Modifier").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            luigi.find_attribute("Super Jump Punch Gravity").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            luigi.find_attribute("Super Jump Punch Air Vertical Momentum").value = rng_f(0.95 - 0.2375 * mod, 0.95 + 0.475 * mod)
            luigi.find_attribute("Cyclone Momentum From Initial B Tap").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            luigi.find_attribute("Cyclone Grounded Horizontal Momentum").value = rng_f(2.35 - 0.5875 * mod, 2.35 + 1.175 * mod)
            luigi.find_attribute("Cyclone Aerial Horizontal Momentum").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            luigi.find_attribute("Cyclone Grounded Momentum Modifier").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            luigi.find_attribute("Cyclone Aerial Momentum Modifier").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.04 * mod)
            luigi.find_attribute("Cyclone Ending Friction").value = rng_f(0.66 - 0.165 * mod, 0.66 + 0.33 * mod)
            luigi.find_attribute("Cyclone Max Vertical Momentum From B Tap").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            luigi.find_attribute("Cyclone Gravity Modifier During B Tap").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            luigi.find_attribute("Fireball Spin Animation Speed").value = rng_f(0.85 - 0.2125 * mod, 0.85 + 0.425 * mod)
            luigi.find_attribute("Fireball Gravity").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            luigi.find_attribute("Fireball Terminal Velocity").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            luigi.find_attribute("Fireball Initial Velocity").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            luigi.find_attribute("Fireball Duration").value = rng_f(50.0 - 12.5 * mod, 50.0 + 25.0 * mod)
            luigi.find_attribute("Fireball Bounce Multiplier").value = rng_f(0.9 - 0.225 * mod, 0.9 + 0.45 * mod)

            mario = characters.find_fighter("Mario")
            mario.find_attribute("Cape Horizontal Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            mario.find_attribute("Cape Horizontal Velocity").value = rng_f(0.0025 - 0.0006 * mod, 0.0025 + 0.0012 * mod)
            mario.find_attribute("Cape Vertical Momentum").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            mario.find_attribute("Cape Gravity").value = rng_f(0.025 - 0.0063 * mod, 0.025 + 0.0125 * mod)
            mario.find_attribute("Cape Max Falling Speed").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            mario.find_attribute("Cape Reflection Bubble Size").value = rng_f(6.5 - 1.625 * mod, 6.5 + 3.25 * mod)
            mario.find_attribute("Cape Reflection Damage Multiplier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            mario.find_attribute("Cape Projectile Reflection Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            mario.find_attribute("Super Jump Punch Freefall Mobility").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            mario.find_attribute("Super Jump Punch Landing Lag").value = rng_f(30.0 - 8 * mod, 30.0 + 3 * mod)
            mario.find_attribute("Super Jump Punch Max Angle Change").value = rng_f(18.0 - 4.5 * mod, 18.0 + 9.0 * mod)
            mario.find_attribute("Super Jump Punch Initial Horizontal Momentum").value = rng_f(0.6666 - 0.1666 * mod, 0.6666 + 0.3333 * mod)
            mario.find_attribute("Super Jump Punch Initial Gravity").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            mario.find_attribute("Super Jump Punch Initial Vertical Momentum").value = rng_f(0.95 - 0.2375 * mod, 0.95 + 0.475 * mod)
            mario.find_attribute("Tornado Grounded Rise Resistance").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            mario.find_attribute("Tornado Base Air Speed").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            mario.find_attribute("Tornado Horizontal Velocity Limit").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            mario.find_attribute("Tornado Horizontal Acceleration").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            mario.find_attribute("Tornado Horizontal marioift").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.04 * mod)
            mario.find_attribute("Tornado Deceleration Rate").value = rng_f(0.66 - 0.165 * mod, 0.66 + 0.33 * mod)
            mario.find_attribute("Tornado Velocity Gain From B Press").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            mario.find_attribute("Tornado Terminal Velocity").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            #mario.find_attribute("Tornado Landing Lag").value = rng(0 - 0 * mod, 0 + 0 * mod)
            mario.find_attribute("Fireball Initial Velocity").value = rng_f(1.5 - 0.35 * mod, 1.5 + 0.5 * mod)
            mario.find_attribute("Fireball Initial Angle").value = rng_f(-0.17 - 0.1 * mod, -0.17 + 0.1 * mod)
            mario.find_attribute("Fireball Duration").value = rng_f(75 - 20 * mod, 75 + 25 * mod)
            mario.find_attribute("Fireball Bounce Muliplier").value = rng_f(0.9 - 0.2 * mod, 0.9 + 0.2 * mod)

            marth = characters.find_fighter("Marth")
            marth.find_attribute("Shield Breaker Loops For Full Charge").value = rng(4 - 1 * mod, 4 + 1 * mod)
            marth.find_attribute("Shield Breaker Base Damage").value = rng(7 - 2 * mod, 7 + 2 * mod)
            marth.find_attribute("Shield Breaker Damage Per Loop").value = rng(5 - 1 * mod, 5 + 1 * mod)
            marth.find_attribute("Shield Breaker Momentum Preservation").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            marth.find_attribute("Shield Breaker Deceleration Rate").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            marth.find_attribute("Dancing Blade Aerial Horizontal Momentum Preservation").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            marth.find_attribute("Dancing Blade Aerial Horizontal Deceleration").value = rng_f(0.0025 - 0.0006 * mod, 0.0025 + 0.0012 * mod)
            marth.find_attribute("Dancing Blade Aerial Vertical Boost").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            marth.find_attribute("Dancing Blade Aerial Vertical Deceleration").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            marth.find_attribute("Dancing Blade Gravity").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            marth.find_attribute("Dolphin Slash Freefall Mobility").value = rng_f(0.4 - 0.1 * mod, 0.4 + 0.2 * mod)
            marth.find_attribute("Dolphin Slash Landing Lag").value = rng_f(34.0 - 8.5 * mod, 34.0 + 17.0 * mod)
            marth.find_attribute("Dolphin Slash Displacement From Input").value = rng_f(0.6666 - 0.1666 * mod, 0.6666 + 0.3333 * mod)
            marth.find_attribute("Dolphin Slash Aerial Height Ratio").value = rng_f(1.1 - 0.275 * mod, 1.1 + 0.55 * mod)
            marth.find_attribute("Dolphin Slash Gravity After Use").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            marth.find_attribute("Dolphin Slash Max Fall Speed After Use").value = rng_f(1.8 - 0.45 * mod, 1.8 + 0.9 * mod)
            marth.find_attribute("Counter Horizontal Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            marth.find_attribute("Counter Horizontal Deceleration").value = rng_f(0.0025 - 0.0006 * mod, 0.0025 + 0.0012 * mod)
            marth.find_attribute("Counter Gravity").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.02 * mod)
            marth.find_attribute("Counter Maximum Falling Speed").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            marth.find_attribute("Counter Damage Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            marth.find_attribute("Counter Hitlag").value = rng_f(11.0 - 2.75 * mod, 11.0 + 5.5 * mod)
            marth.find_attribute("Counter Detection Bubble Size").value = rng_f(8.5 - 2.125 * mod, 8.5 + 4.25 * mod)
            marth.find_attribute("Sword Trail Fade").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            marth.find_attribute("Sword Trail Length").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            marth.find_attribute("Sword Trail Width").value = rng_f(1.75 - 0.4375 * mod, 1.75 + 0.875 * mod)
            marth.find_attribute("Sword Trail Height").value = rng_f(9.63 - 2.4075 * mod, 9.63 + 4.815 * mod)

            mewtwo = characters.find_fighter("Mewtwo")
            #mewtwo.find_attribute("Shadow Ball Charge Increment").value = rng_f(7.0 - 1.75 * mod, 7.0 + 3.5 * mod)
            mewtwo.find_attribute("Shadow Ball Release Momentum Grounded").value = rng_f(-0.2 - -0.05 * mod, -0.2 + -0.1 * mod)
            mewtwo.find_attribute("Shadow Ball Release Momentum Air").value = rng_f(-0.4 - -0.1 * mod, -0.4 + -0.2 * mod)
            mewtwo.find_attribute("Shadow Ball Loops For Full Charge").value = rng(16 - 4 * mod, 16 + 4 * mod)
            mewtwo.find_attribute("Shadow Ball Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Confusion Aerial Vertical Lift").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            mewtwo.find_attribute("Confusion Max Damage Reflectable").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Confusion Reflection Bubble Size").value = rng_f(10.0 - 2.5 * mod, 10.0 + 5.0 * mod)
            mewtwo.find_attribute("Confusion Reflection Damage Multiplier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            mewtwo.find_attribute("Confusion Reflection Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            mewtwo.find_attribute("Teleport Travel Time").value = rng(10 - 2 * mod, 10 + 2 * mod)
            mewtwo.find_attribute("Teleport Initial Momentum 1").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            mewtwo.find_attribute("Teleport Initial Momentum 2").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            mewtwo.find_attribute("Teleport Ending Momentum").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            mewtwo.find_attribute("Teleport Ending Momentum Multiplier").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            mewtwo.find_attribute("Teleport Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            mewtwo.find_attribute("Disable Base Falling Acceleration").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.04 * mod)
            mewtwo.find_attribute("Disable Falling Acceleration Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            mewtwo.find_attribute("Disable X-Offset").value = rng_f(4.5 - 1.125 * mod, 4.5 + 2.25 * mod)
            mewtwo.find_attribute("Disable Y-Offset").value = rng_f(4.5 - 1.125 * mod, 4.5 + 2.25 * mod)
            mewtwo.find_attribute("Disable Duration").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Disable Travel Speed").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Duration").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            mewtwo.find_attribute("Shadow Ball Launch Angle").value = rng_f(2.7 - 0.675 * mod, 2.7 + 1.35 * mod)
            mewtwo.find_attribute("Shadow Ball Uncharged Speed").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Charged Speed").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Uncharged Damage").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Full Charge Damage").value = rng_f(-0.0 - -0.0 * mod, -0.0 + -0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Uncharged Size").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Full Charge Size").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            mewtwo.find_attribute("Shadow Ball Wiggle Intensity").value = rng(0 - 0 * mod, 0 + 0 * mod)
            mewtwo.find_attribute("Shadow Ball Wiggle Modifier").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            mewtwo.find_attribute("Shadow Ball Wiggle Smoothness").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)

            ness = characters.find_fighter("Ness")
            ness.find_attribute("PK Flash Grounded Animation Loop Frames").value = rng(30 - 8 * mod, 30 + 8 * mod)
            ness.find_attribute("PK Flash Air Animation Loop Frames").value = rng(25 - 6 * mod, 25 + 6 * mod)
            ness.find_attribute("PK Flash Falling Acceleration Delay").value = rng(10 - 2 * mod, 10 + 2 * mod)
            ness.find_attribute("PK Flash Charge Release Delay").value = rng(30 - 8 * mod, 30 + 8 * mod)
            ness.find_attribute("PK Flash Gravity").value = rng_f(0.017 - 0.0043 * mod, 0.017 + 0.0085 * mod)
            ness.find_attribute("PK Flash Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            ness.find_attribute("PK Fire Air Launch Trajectory").value = rng_f(-0.6632 - -0.1658 * mod, -0.6632 + -0.3316 * mod)
            ness.find_attribute("PK Fire Aerial Velocity").value = rng_f(2.5 - 0.625 * mod, 2.5 + 1.25 * mod)
            ness.find_attribute("PK Fire Ground Launch Trajectory").value = rng_f(-0.0628 - -0.0157 * mod, -0.0628 + -0.0314 * mod)
            ness.find_attribute("PK Fire Ground Velocity").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            ness.find_attribute("PK Fire Spawn X-Offset").value = rng_f(3.2 - 0.8 * mod, 3.2 + 1.6 * mod)
            ness.find_attribute("PK Fire Spawn Y-Offset").value = rng_f(1.1 - 0.275 * mod, 1.1 + 0.55 * mod)
            ness.find_attribute("PK Fire Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            ness.find_attribute("PK Thunder Animation Timer On Hit").value = rng(24 - 6 * mod, 24 + 6 * mod)
            ness.find_attribute("PK Thunder Fall Delay").value = rng(30 - 8 * mod, 30 + 8 * mod)
            ness.find_attribute("PK Thunder Fall Acceleration").value = rng_f(0.017 - 0.0043 * mod, 0.017 + 0.0085 * mod)
            ness.find_attribute("PK Thunder 2 Momentum").value = rng_f(3.6 - 0.9 * mod, 3.6 + 1.8 * mod)
            ness.find_attribute("PK Thunder 2 Deceleration Rate").value = rng_f(0.072 - 0.018 * mod, 0.072 + 0.036 * mod)
            ness.find_attribute("PK Thunder 2 Landing Lag").value = rng_f(24.0 - 6.0 * mod, 24.0 + 12.0 * mod)
            ness.find_attribute("PK Magnet Initial Cooldown").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            ness.find_attribute("PK Magnet Fall Delay").value = rng(4 - 1 * mod, 4 + 1 * mod)
            ness.find_attribute("PK Magnet Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            ness.find_attribute("PK Magnet Fall Acceleration").value = rng_f(0.0267 - 0.0067 * mod, 0.0267 + 0.0133 * mod)
            ness.find_attribute("PK Magnet Healing Multiplier").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            ness.find_attribute("PK Magnet Absorption Bubble Size").value = rng_f(8.5 - 2.125 * mod, 8.5 + 4.25 * mod)
            ness.find_attribute("Yo-Yo Smash Charge Duration").value = rng_f(60.0 - 15.0 * mod, 60.0 + 30.0 * mod)
            ness.find_attribute("Yo-Yo Smash Charge Damage Multiplier").value = rng_f(350.0 - 87.5 * mod, 350.0 + 175.0 * mod)
            ness.find_attribute("Yo-Yo Smash Charge Hitbox Rehit Rate").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            ness.find_attribute("Baseball Bat Max Damage Reflectable").value = rng(4 - 1 * mod, 4 + 1 * mod)
            ness.find_attribute("Baseball Bat Reflection Damage Multiplier").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            ness.find_attribute("Baseball Bat Reflection Speed Multiplier").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            ness.find_attribute("PK Fire Spark Duration").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            ness.find_attribute("PK Fire Spark Y Offset").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            ness.find_attribute("PK Fire Pillar Duration").value = rng_f(100.0 - 25.0 * mod, 100.0 + 50.0 * mod)
            ness.find_attribute("PK Fire Pillar Hurtbox Resistance").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            ness.find_attribute("PK Fire Pillar Size Decay Multiplier").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            ness.find_attribute("PK Flash Charge Duration").value = rng_f(120.0 - 30.0 * mod, 120.0 + 60.0 * mod)
            ness.find_attribute("PK Flash Charge Hitbox Size Modifier").value = rng_f(100.0 - 25.0 * mod, 100.0 + 50.0 * mod)
            ness.find_attribute("PK Flash Charge Initial Graphic Size Multiplier").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            ness.find_attribute("PK Flash Charge Graphic Growth Multiplier").value = rng_f(1.7 - 0.425 * mod, 1.7 + 0.85 * mod)
            ness.find_attribute("PK Flash Charge Horizontal Momentum").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            ness.find_attribute("PK Flash Charge Peak Rising Height").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            ness.find_attribute("PK Flash Charge Control Sensitivity").value = rng_f(0.01 - 0.0025 * mod, 0.01 + 0.005 * mod)
            ness.find_attribute("PK Flash Charge Projectile Gravity").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            ness.find_attribute("PK Flash Charge Detonation Delay").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            ness.find_attribute("PK Thunder Duration").value = rng_f(120.0 - 30.0 * mod, 120.0 + 60.0 * mod)
            ness.find_attribute("PK Thunder Speed").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            ness.find_attribute("PK Thunder Initial Angle").value = rng_f(90.0 - 22.5 * mod, 90.0 + 45.0 * mod)
            ness.find_attribute("PK Thunder Turning Sensitivity").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            ness.find_attribute("PK Thunder Turning Radius").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            ness.find_attribute("PK Flash 2 Hitbox Size Modifier").value = rng_f(100.0 - 25.0 * mod, 100.0 + 50.0 * mod)
            ness.find_attribute("PK Flash 2 Graphic Size Multiplier").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            ness.find_attribute("PK Flash 2 Graphic Growth Multiplier").value = rng_f(1.7 - 0.425 * mod, 1.7 + 0.85 * mod)
            ness.find_attribute("PK Flash 2 Base Damage").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            ness.find_attribute("PK Flash 2 Damage Multiplier").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            ness.find_attribute("Yo-Yo Number of String Segments").value = rng(20 - 5 * mod, 20 + 5 * mod)
            ness.find_attribute("Yo-Yo Number of Up-Smash String Segments").value = rng(9 - 2 * mod, 9 + 2 * mod)
            ness.find_attribute("Yo-Yo Number of Down-Smash String Segments").value = rng(11 - 3 * mod, 11 + 3 * mod)
            ness.find_attribute("Yo-Yo String Size").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            ness.find_attribute("Yo-Yo Spin Animation Speed").value = rng_f(0.4363 - 0.1091 * mod, 0.4363 + 0.2182 * mod)
            ness.find_attribute("Yo-Yo Charge Spin Animation Speed").value = rng_f(0.3491 - 0.0873 * mod, 0.3491 + 0.1745 * mod)
            ness.find_attribute("Yo-Yo Charge Spin Animation Speed Modifier").value = rng_f(0.8727 - 0.2182 * mod, 0.8727 + 0.4363 * mod)
            ness.find_attribute("Yo-Yo Charge Horizontal Release Velocity").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            ness.find_attribute("Yo-Yo Charge Pull Acceleration").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            ness.find_attribute("Yo-Yo Max Charge Horizontal Velocity").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            ness.find_attribute("Yo-Yo Charge Vertical Release Velocity").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            ness.find_attribute("Yo-Yo Charge Base Gravity").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            ness.find_attribute("Yo-Yo Charge Terminal Velocity").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            ness.find_attribute("Yo-Yo Charge Horizontal Pull Strength").value = rng_f(0.001 - 0.0003 * mod, 0.001 + 0.0005 * mod)
            ness.find_attribute("Yo-Yo Frame for Up Smash Model Rotation Change").value = rng(4 - 1 * mod, 4 + 1 * mod)
            ness.find_attribute("Yo-Yo Frame for Up Smash Snap to Palm").value = rng(49 - 12 * mod, 49 + 12 * mod)
            ness.find_attribute("Yo-Yo Frame for Down Smash Model Rotation Change").value = rng(5 - 1 * mod, 5 + 1 * mod)
            ness.find_attribute("Yo-Yo Frame for Down Smash Snap to Palm").value = rng(60 - 15 * mod, 60 + 15 * mod)

            peach = characters.find_fighter("Peach")
            peach.find_attribute("Float Duration").value = rng_f(150.0 - 37.5 * mod, 150.0 + 75.0 * mod)
            peach.find_attribute("Vegetable Base Odds (1/X)").value = rng(128 - 32 * mod, 128 + 32 * mod)
            peach.find_attribute("Vegetable Item 1 Odds (Y/X)").value = rng(2 - 0 * mod, 2 + 0 * mod)
            peach.find_attribute("Vegetable Item 1 ID").value = rng(6 - 2 * mod, 6 + 2 * mod)
            peach.find_attribute("Vegetable Item 2 Odds (Y/X)").value = rng(3 - 1 * mod, 3 + 1 * mod)
            peach.find_attribute("Vegetable Item 2 ID").value = rng(7 - 2 * mod, 7 + 2 * mod)
            peach.find_attribute("Vegetable Item 3 Odds (Y/X)").value = rng(1 - 0 * mod, 1 + 0 * mod)
            peach.find_attribute("Vegetable Item 3 ID").value = rng(12 - 3 * mod, 12 + 3 * mod)
            peach.find_attribute("Peach Bomber Tilt Horizontal Momentum").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            peach.find_attribute("Peach Bomber Smash Horizontal Momentum").value = rng_f(3.5 - 0.875 * mod, 3.5 + 1.75 * mod)
            peach.find_attribute("Peach Bomber Vertical Momentum").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            peach.find_attribute("Peach Bomber Vertical Recoil").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            peach.find_attribute("Peach Parasol Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            peach.find_attribute("Peach Parasol Launch Control Modifier").value = rng_f(18.0 - 4.5 * mod, 18.0 + 9.0 * mod)
            peach.find_attribute("Toad Aerial Vertical Momentum").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            peach.find_attribute("Toad Fall Acceleration").value = rng_f(0.025 - 0.0063 * mod, 0.025 + 0.0125 * mod)
            peach.find_attribute("Toad Detection Bubble Size").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            peach.find_attribute("Turnip Duration").value = rng_f(140.0 - 35.0 * mod, 140.0 + 70.0 * mod)
            peach.find_attribute("Turnip #1 Odds").value = rng(35 - 9 * mod, 35 + 9 * mod)
            peach.find_attribute("Turnip #1 Damage").value = rng(2 - 0 * mod, 2 + 0 * mod)
            peach.find_attribute("Turnip #2 Odds").value = rng(6 - 2 * mod, 6 + 2 * mod)
            peach.find_attribute("Turnip #2 Damage").value = rng(2 - 0 * mod, 2 + 0 * mod)
            peach.find_attribute("Turnip #3 Odds").value = rng(5 - 1 * mod, 5 + 1 * mod)
            peach.find_attribute("Turnip #3 Damage").value = rng(2 - 0 * mod, 2 + 0 * mod)
            peach.find_attribute("Turnip #4 Odds").value = rng(3 - 1 * mod, 3 + 1 * mod)
            peach.find_attribute("Turnip #4 Damage").value = rng(2 - 0 * mod, 2 + 0 * mod)
            peach.find_attribute("Turnip #5 Odds").value = rng(3 - 1 * mod, 3 + 1 * mod)
            peach.find_attribute("Turnip #5 Damage").value = rng(2 - 0 * mod, 2 + 0 * mod)
            peach.find_attribute("Turnip #6 Odds").value = rng(4 - 1 * mod, 4 + 1 * mod)
            peach.find_attribute("Turnip #6 Damage").value = rng(6 - 2 * mod, 6 + 2 * mod)
            peach.find_attribute("Turnip #7 Odds").value = rng(1 - 0 * mod, 1 + 0 * mod)
            peach.find_attribute("Turnip #7 Damage").value = rng(12 - 3 * mod, 12 + 3 * mod)
            peach.find_attribute("Turnip #8 Odds").value = rng(1 - 0 * mod, 1 + 0 * mod)
            peach.find_attribute("Turnip #8 Damage").value = rng(30 - 8 * mod, 30 + 8 * mod)
            peach.find_attribute("Toad Counter Velocity").value = rng_f(10.0 - 2.5 * mod, 10.0 + 5.0 * mod)
            peach.find_attribute("Toad Counter Distance Modifier").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            peach.find_attribute("Toad Counter Scatter Modifier").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            peach.find_attribute("Toad Counter Angle").value = rng_f(1.7453 - 0.4363 * mod, 1.7453 + 0.8727 * mod)

            pichu = characters.find_fighter("Pichu")
            pichu.find_attribute("Thunder Jolt Ground Spawn X-Offset").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            pichu.find_attribute("Thunder Jolt Ground Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            pichu.find_attribute("Thunder Jolt Air Spawn X-Offset").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            pichu.find_attribute("Thunder Jolt Air Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            pichu.find_attribute("Thunder Jolt Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            pichu.find_attribute("Skull Bash Smash Window").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            pichu.find_attribute("Skull Bash Charge Rate").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            pichu.find_attribute("Skull Bash Max Charge Duration").value = rng_f(180.0 - 45.0 * mod, 180.0 + 90.0 * mod)
            pichu.find_attribute("Skull Bash Tilt Damage").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            pichu.find_attribute("Skull Bash Traction Multiplier").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            pichu.find_attribute("Skull Bash Falling Speed").value = rng_f(0.04 - 0.01 * mod, 0.04 + 0.02 * mod)
            pichu.find_attribute("Skull Bash Horizontal Launch Momentum").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            pichu.find_attribute("Skull Bash Horizontal Momentum Multiplier").value = rng_f(0.0167 - 0.0042 * mod, 0.0167 + 0.0083 * mod)
            pichu.find_attribute("Skull Bash Vertical Launch Momentum").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            pichu.find_attribute("Skull Bash Vertical Momentum Multiplier").value = rng_f(0.007 - 0.0018 * mod, 0.007 + 0.0035 * mod)
            pichu.find_attribute("Skull Bash Gravity During Launch Animation").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pichu.find_attribute("Skull Bash Ending Friction Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            pichu.find_attribute("Skull Bash Horizontal Deceleration").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            pichu.find_attribute("Skull Bash Gravity During End of Launch").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            pichu.find_attribute("Agility Travel Distance").value = rng(8 - 2 * mod, 8 + 2 * mod)
            pichu.find_attribute("Agility Momentum Variable").value = rng_f(0.0267 - 0.0067 * mod, 0.0267 + 0.0133 * mod)
            pichu.find_attribute("Agility Grounded Model Rotation").value = rng_f(0.2618 - 0.0654 * mod, 0.2618 + 0.1309 * mod)
            pichu.find_attribute("Agility Grounded Model Width Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pichu.find_attribute("Agility Grounded Model Height Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pichu.find_attribute("Agility Air Model Length Multiplier").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            pichu.find_attribute("Agility Air Model Rotation").value = rng_f(0.2618 - 0.0654 * mod, 0.2618 + 0.1309 * mod)
            pichu.find_attribute("Agility Air Model Width Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pichu.find_attribute("Agility Air Model Height Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pichu.find_attribute("Agility Air Model Length Multiplier").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            pichu.find_attribute("Agility Base Dash Momentum").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            pichu.find_attribute("Agility Start Momentum Boost").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            pichu.find_attribute("Agility Second Dash Length Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            pichu.find_attribute("Agility Momentum Preservation").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            pichu.find_attribute("Agility Momentum Variable 2").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            pichu.find_attribute("Agility Landing Lag").value = rng_f(12.0 - 3.0 * mod, 12.0 + 6.0 * mod)
            pichu.find_attribute("Thunder Vertical Momentum Gain on Strike").value = rng_f(0.66 - 0.165 * mod, 0.66 + 0.33 * mod)
            pichu.find_attribute("Thunder Fall Acceleration on Strike").value = rng_f(0.016 - 0.004 * mod, 0.016 + 0.008 * mod)
            pichu.find_attribute("Thunder Travel Speed").value = rng_f(-5.0 - -1.25 * mod, -5.0 + -2.5 * mod)
            pichu.find_attribute("Thunder Displacement of Thunder Cloud").value = rng_f(-18.0 - -4.5 * mod, -18.0 + -9.0 * mod)
            pichu.find_attribute("Thunder Spawn Y-Offset").value = rng_f(150.0 - 37.5 * mod, 150.0 + 75.0 * mod)
            pichu.find_attribute("Thunder Number of Bursts").value = rng(4 - 1 * mod, 4 + 1 * mod)
            pichu.find_attribute("Thunder Delay Between Bursts").value = rng(8 - 2 * mod, 8 + 2 * mod)
            pichu.find_attribute("Thunder Maximum Travel Distance").value = rng_f(40.0 - 10.0 * mod, 40.0 + 20.0 * mod)
            pichu.find_attribute("Thunder Vertical Collision Detection").value = rng_f(40.0 - 10.0 * mod, 40.0 + 20.0 * mod)
            pichu.find_attribute("Thunder Size of Self-hit Collision Detection").value = rng_f(38.0 - 9.5 * mod, 38.0 + 19.0 * mod)
            pichu.find_attribute("Thunder Jolt Duration").value = rng_f(100.0 - 25.0 * mod, 100.0 + 50.0 * mod)
            pichu.find_attribute("Thunder Jolt Launch Angle").value = rng_f(-0.6981 - -0.1745 * mod, -0.6981 + -0.3491 * mod)
            pichu.find_attribute("Thunder Jolt Aerial Launch Velocity").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)

            pikachu = characters.find_fighter("Pikachu")
            pikachu.find_attribute("Thunder Jolt Ground Spawn X-Offset").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            pikachu.find_attribute("Thunder Jolt Ground Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            pikachu.find_attribute("Thunder Jolt Air Spawn X-Offset").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            pikachu.find_attribute("Thunder Jolt Air Spawn Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            pikachu.find_attribute("Thunder Jolt Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            pikachu.find_attribute("Skull Bash Smash Window").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            pikachu.find_attribute("Skull Bash Charge Rate").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            pikachu.find_attribute("Skull Bash Max Charge Duration").value = rng_f(90.0 - 22.5 * mod, 90.0 + 45.0 * mod)
            pikachu.find_attribute("Skull Bash Tilt Damage").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            pikachu.find_attribute("Skull Bash Traction Multiplier").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            pikachu.find_attribute("Skull Bash Falling Speed").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            pikachu.find_attribute("Skull Bash Horizontal Launch Momentum").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            pikachu.find_attribute("Skull Bash Horizontal Momentum Multiplier").value = rng_f(0.0167 - 0.0042 * mod, 0.0167 + 0.0083 * mod)
            pikachu.find_attribute("Skull Bash Vertical Launch Momentum").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pikachu.find_attribute("Skull Bash Vertical Momentum Multiplier").value = rng_f(0.01 - 0.0025 * mod, 0.01 + 0.005 * mod)
            pikachu.find_attribute("Skull Bash Gravity During Launch Animation").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            pikachu.find_attribute("Skull Bash Ending Friction Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            pikachu.find_attribute("Skull Bash Horizontal Deceleration").value = rng_f(0.05 - 0.0125 * mod, 0.05 + 0.025 * mod)
            pikachu.find_attribute("Skull Bash Gravity During End of Launch").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            pikachu.find_attribute("Quick Attack Travel Distance").value = rng(5 - 1 * mod, 5 + 1 * mod)
            pikachu.find_attribute("Quick Attack Momentum Variable").value = rng_f(0.0267 - 0.0067 * mod, 0.0267 + 0.0133 * mod)
            pikachu.find_attribute("Quick Attack Grounded Model Rotation").value = rng_f(0.2618 - 0.0654 * mod, 0.2618 + 0.1309 * mod)
            pikachu.find_attribute("Quick Attack Grounded Model Width Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pikachu.find_attribute("Quick Attack Grounded Model Height Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pikachu.find_attribute("Quick Attack Air Model Length Multiplier").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            pikachu.find_attribute("Quick Attack Air Model Rotation").value = rng_f(0.2618 - 0.0654 * mod, 0.2618 + 0.1309 * mod)
            pikachu.find_attribute("Quick Attack Air Model Width Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pikachu.find_attribute("Quick Attack Air Model Height Multiplier").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            pikachu.find_attribute("Quick Attack Air Model Length Multiplier").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            pikachu.find_attribute("Quick Attack Base Dash Momentum").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            pikachu.find_attribute("Quick Attack Start Momentum Boost").value = rng_f(5.9 - 1.475 * mod, 5.9 + 2.95 * mod)
            pikachu.find_attribute("Quick Attack Second Dash Length Multiplier").value = rng_f(0.9 - 0.225 * mod, 0.9 + 0.45 * mod)
            pikachu.find_attribute("Quick Attack Momentum Preservation").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            pikachu.find_attribute("Quick Attack Momentum Variable 2").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            pikachu.find_attribute("Quick Attack Landing Lag").value = rng_f(24.0 - 6.0 * mod, 24.0 + 12.0 * mod)
            pikachu.find_attribute("Thunder Vertical Momentum Gain on Strike").value = rng_f(0.66 - 0.165 * mod, 0.66 + 0.33 * mod)
            pikachu.find_attribute("Thunder Fall Acceleration on Strike").value = rng_f(0.016 - 0.004 * mod, 0.016 + 0.008 * mod)
            pikachu.find_attribute("Thunder Travel Speed").value = rng_f(-5.0 - -1.25 * mod, -5.0 + -2.5 * mod)
            pikachu.find_attribute("Thunder Displacement of Thunder Cloud").value = rng_f(-18.0 - -4.5 * mod, -18.0 + -9.0 * mod)
            pikachu.find_attribute("Thunder Spawn Y-Offset").value = rng_f(150.0 - 37.5 * mod, 150.0 + 75.0 * mod)
            pikachu.find_attribute("Thunder Number of Bursts").value = rng(4 - 1 * mod, 4 + 1 * mod)
            pikachu.find_attribute("Thunder Delay Between Bursts").value = rng(8 - 2 * mod, 8 + 2 * mod)
            pikachu.find_attribute("Thunder Maximum Travel Distance").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            pikachu.find_attribute("Thunder Vertical Collision Detection").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            pikachu.find_attribute("Thunder Size of Self-hit Collision Detection").value = rng_f(-0.0 - -0.0 * mod, -0.0 + -0.0 * mod)
            pikachu.find_attribute("Thunder Jolt Duration").value = rng_f(100.0 - 25.0 * mod, 100.0 + 50.0 * mod)
            pikachu.find_attribute("Thunder Jolt Launch Angle").value = rng_f(-0.6981 - -0.1745 * mod, -0.6981 + -0.3491 * mod)
            pikachu.find_attribute("Thunder Jolt Aerial Launch Velocity").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)

            roy = characters.find_fighter("Roy")
            roy.find_attribute("Flare Blade Loops For Full Charge").value = rng(7 - 1 * mod, 7 + 1 * mod)
            roy.find_attribute("Flare Blade Base Damage").value = rng(6 - 1 * mod, 6 + 1 * mod)
            roy.find_attribute("Flare Blade Damage Per Loop").value = rng(5 - 1 * mod, 5 + 1 * mod)
            roy.find_attribute("Flare Blade Momentum Preservation").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            roy.find_attribute("Flare Blade Deceleration Rate").value = rng_f(0.02 - 0.005 * mod, 0.02 + 0.01 * mod)
            roy.find_attribute("Double-Edge Dance Aerial Horizontal Momentum Preservation").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            roy.find_attribute("Double-Edge Dance Aerial Horizontal Deceleration").value = rng_f(0.0025 - 0.0006 * mod, 0.0025 + 0.0012 * mod)
            roy.find_attribute("Double-Edge Dance Aerial Vertical Boost").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            roy.find_attribute("Double-Edge Dance Aerial Vertical Deceleration").value = rng_f(0.08 - 0.02 * mod, 0.08 + 0.04 * mod)
            roy.find_attribute("Double-Edge Dance Gravity").value = rng_f(1.8 - 0.45 * mod, 1.8 + 0.9 * mod)
            roy.find_attribute("Blazer Freefall Mobility").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            roy.find_attribute("Blazer Landing Lag").value = rng_f(30.0 - 8 * mod, 30.0 + 3 * mod)
            roy.find_attribute("Blazer Displacement From Input").value = rng_f(0.6666 - 0.1666 * mod, 0.6666 + 0.3333 * mod)
            roy.find_attribute("Blazer Aerial Height Ratio").value = rng_f(1.1 - 0.275 * mod, 1.1 + 0.55 * mod)
            roy.find_attribute("Blazer Gravity After Use").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            roy.find_attribute("Blazer Max Fall Speed After Use").value = rng_f(1.8 - 0.45 * mod, 1.8 + 0.9 * mod)
            roy.find_attribute("Counter Horizontal Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            roy.find_attribute("Counter Horizontal Deceleration").value = rng_f(0.0025 - 0.0006 * mod, 0.0025 + 0.0012 * mod)
            roy.find_attribute("Counter Gravity").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            roy.find_attribute("Counter Maximum Falling Speed").value = rng_f(1.4 - 0.35 * mod, 1.4 + 0.7 * mod)
            roy.find_attribute("Counter Damage Multiplier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            roy.find_attribute("Counter Hitlag").value = rng_f(13.0 - 3.25 * mod, 13.0 + 6.5 * mod)
            roy.find_attribute("Counter Detection Bubble Size").value = rng_f(8.5 - 2.125 * mod, 8.5 + 4.25 * mod)
            roy.find_attribute("Sword Trail Fade").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            roy.find_attribute("Sword Trail Length").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            roy.find_attribute("Sword Trail Width").value = rng_f(2.6 - 0.65 * mod, 2.6 + 1.3 * mod)
            roy.find_attribute("Sword Trail Height").value = rng_f(11.2 - 2.8 * mod, 11.2 + 5.6 * mod)

            samus = characters.find_fighter("Samus")
            samus.find_attribute("Bomb Self-Hit Animation Delay").value = rng_f(10.0 - 2.5 * mod, 10.0 + 5.0 * mod)
            samus.find_attribute("Bomb Self-Hit Grounded Launch Angle").value = rng_f(0.7854 - 0.1963 * mod, 0.7854 + 0.3927 * mod)
            samus.find_attribute("Bomb Self-Hit Momentum").value = rng_f(1.7 - 0.425 * mod, 1.7 + 0.85 * mod)
            samus.find_attribute("Bomb Self-Hit Horizontal Velocity Multiplier").value = rng_f(0.7 - 0.175 * mod, 0.7 + 0.35 * mod)
            samus.find_attribute("Charge Shot Charge Time").value = rng_f(7.0 - 1.75 * mod, 7.0 + 3.5 * mod)
            samus.find_attribute("Charge Shot Recoil").value = rng_f(-0.1 - -0.025 * mod, -0.1 + -0.05 * mod)
            samus.find_attribute("Charge Shot Frames Per Charge Level").value = rng(16 - 4 * mod, 16 + 4 * mod)
            samus.find_attribute("Charge Shot Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            samus.find_attribute("Missile Smash Window").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            samus.find_attribute("Missile Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            samus.find_attribute("Missile Momentum Preservation Multiplier").value = rng_f(0.0025 - 0.0006 * mod, 0.0025 + 0.0012 * mod)
            samus.find_attribute("Missile Spawn X-Offset").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Screw Attack Grounded Start Horizontal Momentum").value = rng_f(0.35 - 0.0875 * mod, 0.35 + 0.175 * mod)
            samus.find_attribute("Screw Attack Control Variable").value = rng_f(0.017 - 0.0043 * mod, 0.017 + 0.0085 * mod)
            samus.find_attribute("Screw Attack Air Friction").value = rng_f(0.57 - 0.1425 * mod, 0.57 + 0.285 * mod)
            samus.find_attribute("Screw Attack Aerial Vertical Momentum").value = rng_f(2.5 - 0.625 * mod, 2.5 + 1.25 * mod)
            samus.find_attribute("Screw Attack Landing Lag").value = rng_f(24.0 - 6.0 * mod, 24.0 + 12.0 * mod)
            samus.find_attribute("Morph Ball Bomb Ground Vertical Momentum").value = rng_f(1.1 - 0.275 * mod, 1.1 + 0.55 * mod)
            samus.find_attribute("Morph Ball Bomb Air Vertical Momentum").value = rng_f(0.9 - 0.225 * mod, 0.9 + 0.45 * mod)
            samus.find_attribute("Morph Ball Bomb Ground Mobility").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            samus.find_attribute("Morph Ball Bomb Air Mobility").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            samus.find_attribute("Morph Ball Bomb Ground Acceleration Multiplier").value = rng_f(22.0 - 5.5 * mod, 22.0 + 11.0 * mod)
            samus.find_attribute("Morph Ball Bomb Air Acceleration Multiplier").value = rng_f(22.0 - 5.5 * mod, 22.0 + 11.0 * mod)
            samus.find_attribute("Morph Ball Bomb Ground Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Morph Ball Bomb Air Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Morph Ball Bomb X-Offset").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            samus.find_attribute("Morph Ball Bomb Y-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            samus.find_attribute("Grapple Beam Grab Delay").value = rng(7 - 2 * mod, 7 + 2 * mod)
            #samus.find_attribute("Grapple Beam Grab Chain Release Begin").value = rng(17 - 4 * mod, 17 + 4 * mod)
            #samus.find_attribute("Grapple Beam Grab Chain Retract Begin").value = rng(75 - 19 * mod, 75 + 19 * mod)
            #samus.find_attribute("Grapple Beam Grab Chain Retract Finish").value = rng(93 - 23 * mod, 93 + 23 * mod)
            samus.find_attribute("Grapple Beam Dash Grab Delay").value = rng(7 - 2 * mod, 7 + 2 * mod)
            #samus.find_attribute("Grapple Beam Dash Grab Chain Release Begin").value = rng(17 - 4 * mod, 17 + 4 * mod)
            #samus.find_attribute("Grapple Beam Dash Grab Chain Retract Begin").value = rng(40 - 10 * mod, 40 + 10 * mod)
            #samus.find_attribute("Grapple Beam Dash Grab Chain Retract Finish").value = rng(64 - 16 * mod, 64 + 16 * mod)
            samus.find_attribute("Grapple Beam Air Delay").value = rng(1 - 0 * mod, 1 + 0 * mod)
            #samus.find_attribute("Grapple Beam Air Chain Release Begin").value = rng(7 - 2 * mod, 7 + 2 * mod)
            #samus.find_attribute("Grapple Beam Air Chain Retract Begin").value = rng(40 - 10 * mod, 40 + 10 * mod)
            #samus.find_attribute("Grapple Beam Air Chain Retract Finish").value = rng(58 - 14 * mod, 58 + 14 * mod)
            samus.find_attribute("Grapple Beam Wall Release Jump Height").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Grapple Beam Hang Duration").value = rng(0 - 0 * mod, 0 + 0 * mod)
            samus.find_attribute("Bomb Duration").value = rng_f(72.0 - 18.0 * mod, 72.0 + 36.0 * mod)
            samus.find_attribute("Charge Shot Duration").value = rng_f(70.0 - 17.5 * mod, 70.0 + 35.0 * mod)
            samus.find_attribute("Charge Shot Angle").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            samus.find_attribute("Charge Shot Base Velocity").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            samus.find_attribute("Charge Shot Charged Velocity").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            samus.find_attribute("Charge Shot Initial Size").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            samus.find_attribute("Charge Shot Full Charge Graphic Size").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            samus.find_attribute("Missile Duration").value = rng_f(110.0 - 27.5 * mod, 110.0 + 55.0 * mod)
            samus.find_attribute("Missile Deceleration Frame").value = rng_f(60.0 - 15.0 * mod, 60.0 + 30.0 * mod)
            samus.find_attribute("Missile Initial Velocity").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            samus.find_attribute("Missile Velocity After Deceleration").value = rng_f(0.95 - 0.2375 * mod, 0.95 + 0.475 * mod)
            samus.find_attribute("Missile Deceleration Rate").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            samus.find_attribute("Missile Homing Accuracy").value = rng_f(0.0192 - 0.0048 * mod, 0.0192 + 0.0096 * mod)
            samus.find_attribute("Missile Max Homing Angle").value = rng_f(0.8727 - 0.2182 * mod, 0.8727 + 0.4363 * mod)
            samus.find_attribute("Missile Homing Modifier").value = rng_f(0.0175 - 0.0044 * mod, 0.0175 + 0.0087 * mod)
            samus.find_attribute("Super Missile Duration").value = rng_f(75.0 - 18.75 * mod, 75.0 + 37.5 * mod)
            samus.find_attribute("Super Missile Acceleration Frame").value = rng_f(10.0 - 2.5 * mod, 10.0 + 5.0 * mod)
            samus.find_attribute("Super Missile Initial Velocity").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            samus.find_attribute("Super Missile Acceleration Rate").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            samus.find_attribute("Super Missile Terminal Velocity").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            samus.find_attribute("Grapple Beam Recoil On Angled Surface").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            samus.find_attribute("Grapple Beam Number of Segments").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            samus.find_attribute("Grapple Beam Distance Between Segments").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Grapple Beam Elasticity").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Grapple Beam Launch Speed").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            samus.find_attribute("Grapple Beam Gravity").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            samus.find_attribute("Grapple Beam Retraction Speed").value = rng_f(2.6 - 0.65 * mod, 2.6 + 1.3 * mod)
            samus.find_attribute("Grapple Beam End Retraction Speed").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            samus.find_attribute("Grapple Beam Ground Length Modifier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            samus.find_attribute("Grapple Beam Air Length Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)

            sheik = characters.find_fighter("Sheik")
            sheik.find_attribute("Chain Dance Base Duration").value = rng_f(10.0 - 2.5 * mod, 10.0 + 5.0 * mod)
            sheik.find_attribute("Chain Dance Rehit Rate").value = rng_f(16.0 - 4.0 * mod, 16.0 + 8.0 * mod)
            #sheik.find_attribute("Chain Dance Control Frame").value = rng_f(32.0 - 8.0 * mod, 32.0 + 16.0 * mod)
            #sheik.find_attribute("Chain Dance Retraction Delay Frame").value = rng_f(18.0 - 4.5 * mod, 18.0 + 9.0 * mod)
            #sheik.find_attribute("Chain Dance Retraction Begin Frame").value = rng_f(28.0 - 7.0 * mod, 28.0 + 14.0 * mod)
            sheik.find_attribute("Vanish Vertical Momentum").value = rng_f(3.5 - 0.875 * mod, 3.5 + 1.75 * mod)
            sheik.find_attribute("Vanish Physics Variable").value = rng_f(0.19 - 0.0475 * mod, 0.19 + 0.095 * mod)
            sheik.find_attribute("Vanish Fall Acceleration").value = rng_f(0.25 - 0.0625 * mod, 0.25 + 0.125 * mod)
            sheik.find_attribute("Vanish Travel Distance").value = rng(20 - 5 * mod, 20 + 5 * mod)
            sheik.find_attribute("Vanish Base Momentum").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            sheik.find_attribute("Vanish Momentum Variable").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            sheik.find_attribute("Vanish Momentum After Poof").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            sheik.find_attribute("Vanish Momentum After Poof 2").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            sheik.find_attribute("Vanish Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            sheik.find_attribute("Transform Horizontal Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            sheik.find_attribute("Transform Vertical Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            sheik.find_attribute("Needles Air Duration").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            sheik.find_attribute("Needles Ground Duration").value = rng_f(120.0 - 30.0 * mod, 120.0 + 60.0 * mod)
            sheik.find_attribute("Needles Travel Speed").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            sheik.find_attribute("Chain Number of Segments").value = rng(20 - 5 * mod, 20 + 5 * mod)
            sheik.find_attribute("Chain Size").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            sheik.find_attribute("Chain Gravity/Elasticity").value = rng_f(0.09 - 0.0225 * mod, 0.09 + 0.045 * mod)
            sheik.find_attribute("Chain Collision Sensitivity").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            sheik.find_attribute("Chain Gravity Modifier").value = rng_f(0.16 - 0.04 * mod, 0.16 + 0.08 * mod)
            sheik.find_attribute("Chain Rebound Sensitivity").value = rng_f(7.5 - 1.875 * mod, 7.5 + 3.75 * mod)
            sheik.find_attribute("Chain Movement Modifier 2").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            sheik.find_attribute("Chain Mystery Value 1").value = rng_f(7.5 - 1.875 * mod, 7.5 + 3.75 * mod)
            sheik.find_attribute("Chain Mystery Value 2").value = rng_f(2.13 - 0.5325 * mod, 2.13 + 1.065 * mod)
            sheik.find_attribute("Chain Mystery Value 3").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            sheik.find_attribute("Chain Mystery Value 4").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            sheik.find_attribute("Chain Falling Speed").value = rng_f(0.98 - 0.245 * mod, 0.98 + 0.49 * mod)
            sheik.find_attribute("Chain Rebound Modifier 1").value = rng_f(0.88 - 0.22 * mod, 0.88 + 0.44 * mod)
            sheik.find_attribute("Chain Rebound Modifier 2").value = rng_f(0.68 - 0.17 * mod, 0.68 + 0.34 * mod)
            sheik.find_attribute("Chain Delay Before Fall Acceleration").value = rng_f(0.78 - 0.195 * mod, 0.78 + 0.39 * mod)
            sheik.find_attribute("Chain Falling Mod").value = rng_f(0.78 - 0.195 * mod, 0.78 + 0.39 * mod)
            sheik.find_attribute("Chain Movement Modifier 2").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            sheik.find_attribute("Chain Spawn Position").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            sheik.find_attribute("Chain Movement Modifier 3").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            sheik.find_attribute("Chain Movement Modifier 4").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            sheik.find_attribute("Chain Rebound from Collision").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            sheik.find_attribute("Chain Movement Modifier 5").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)

            yoshi = characters.find_fighter("Yoshi")
            yoshi.find_attribute("Flutter Jump Turn Duration").value = rng(12 - 3 * mod, 12 + 3 * mod)
            yoshi.find_attribute("Flutter Jump Super Armor").value = rng_f(120.0 - 30.0 * mod, 120.0 + 60.0 * mod)
            yoshi.find_attribute("Egg Lay Horizontal Momentum").value = rng_f(0.68 - 0.17 * mod, 0.68 + 0.34 * mod)
            yoshi.find_attribute("Egg Lay Vertical Momentum").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            yoshi.find_attribute("Egg Lay Damage Multiplier").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            yoshi.find_attribute("Egg Lay Growth Time").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            yoshi.find_attribute("Egg Lay Base Duration").value = rng_f(200.0 - 50.0 * mod, 200.0 + 100.0 * mod)
            yoshi.find_attribute("Egg Lay Breakout Resistance").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            yoshi.find_attribute("Egg Lay Wiggle Out").value = rng_f(14.0 - 3.5 * mod, 14.0 + 7.0 * mod)
            yoshi.find_attribute("Egg Lay Release Intangibility").value = rng(14 - 4 * mod, 14 + 4 * mod)
            yoshi.find_attribute("Egg Lay Break Out Horizontal Velocity").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            yoshi.find_attribute("Egg Lay Break Out Vertical Velocity").value = rng_f(2.4 - 0.6 * mod, 2.4 + 1.2 * mod)
            yoshi.find_attribute("Egg Roll Max Duration").value = rng(360 - 90 * mod, 360 + 90 * mod)
            yoshi.find_attribute("Egg Roll Minimum Duration").value = rng(50 - 12 * mod, 50 + 12 * mod)
            yoshi.find_attribute("Egg Roll Duration Subtraction on Hit").value = rng(40 - 10 * mod, 40 + 10 * mod)
            yoshi.find_attribute("Egg Roll Horizontal Momentum").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            yoshi.find_attribute("Egg Roll Vertical Momentum").value = rng_f(2.1 - 0.525 * mod, 2.1 + 1.05 * mod)
            yoshi.find_attribute("Egg Roll Spin Intensity").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            yoshi.find_attribute("Egg Roll First Land Momentum").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            yoshi.find_attribute("Egg Roll Smash Momentum Multiplier").value = rng_f(1.2 - 0.3 * mod, 1.2 + 0.6 * mod)
            yoshi.find_attribute("Egg Roll Gravity").value = rng_f(0.13 - 0.0325 * mod, 0.13 + 0.065 * mod)
            yoshi.find_attribute("Egg Roll Ending Gravity").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            yoshi.find_attribute("Egg Roll Accleration").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            yoshi.find_attribute("Egg Roll Speed Modifier").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            yoshi.find_attribute("Egg Roll Damage From Speed Modifier").value = rng_f(1.25 - 0.3125 * mod, 1.25 + 0.625 * mod)
            yoshi.find_attribute("Egg Roll Air Acceleration").value = rng_f(1.6 - 0.4 * mod, 1.6 + 0.8 * mod)
            yoshi.find_attribute("Egg Roll Smash Window Ground").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            yoshi.find_attribute("Egg Roll Smash Window Air").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            yoshi.find_attribute("Egg Roll Spin On Turn Modifier").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            yoshi.find_attribute("Egg Roll Horizontal Recoil").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            yoshi.find_attribute("Egg Roll Vertical Recoil").value = rng_f(1.7 - 0.425 * mod, 1.7 + 0.85 * mod)
            yoshi.find_attribute("Egg Roll Velocity Mod On Recoil").value = rng_f(0.4 - 0.1 * mod, 0.4 + 0.2 * mod)
            yoshi.find_attribute("Egg Roll Friction").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            yoshi.find_attribute("Egg Roll Boost on Landing").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            yoshi.find_attribute("Egg Roll Damage Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            yoshi.find_attribute("Egg Roll Damage Ratio").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            yoshi.find_attribute("Egg Roll Aerial Damage Reduction").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            yoshi.find_attribute("Egg Roll Aerial Ending Acceleration").value = rng_f(0.4 - 0.1 * mod, 0.4 + 0.2 * mod)
            yoshi.find_attribute("Egg Roll Acceleration Variable 1").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            yoshi.find_attribute("Egg Roll Acceleration Variable 2").value = rng_f(1.1 - 0.275 * mod, 1.1 + 0.55 * mod)
            yoshi.find_attribute("Egg Roll Ending Horizontal Velocity").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            yoshi.find_attribute("Egg Roll Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            yoshi.find_attribute("Egg Throw Angle Variable 1").value = rng_f(0.65 - 0.1625 * mod, 0.65 + 0.325 * mod)
            yoshi.find_attribute("Egg Throw Angle Variable 2").value = rng_f(0.5236 - 0.1309 * mod, 0.5236 + 0.2618 * mod)
            yoshi.find_attribute("Egg Throw Angle Variable 3").value = rng_f(0.0698 - 0.0175 * mod, 0.0698 + 0.0349 * mod)
            yoshi.find_attribute("Egg Throw Angle Variable 4").value = rng_f(1.2741 - 0.3185 * mod, 1.2741 + 0.637 * mod)
            yoshi.find_attribute("Egg Throw Base Launch Speed").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            yoshi.find_attribute("Egg Throw Launch Speed B Press Modifier").value = rng_f(0.23 - 0.0575 * mod, 0.23 + 0.115 * mod)
            yoshi.find_attribute("Egg Throw X-Offset").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            yoshi.find_attribute("Egg Throw Y-Offset").value = rng_f(5.0 - 1.25 * mod, 5.0 + 2.5 * mod)
            yoshi.find_attribute("Egg Throw Spin Intensity").value = rng_f(-2.1 - -0.525 * mod, -2.1 + -1.05 * mod)
            yoshi.find_attribute("Ground Pound Descent Speed").value = rng_f(-5.0 - -1.25 * mod, -5.0 + -2.5 * mod)
            yoshi.find_attribute("Ground Pound Star X-Offset").value = rng_f(8.0 - 2.0 * mod, 8.0 + 4.0 * mod)
            yoshi.find_attribute("Ground Pound Star Y-Offset").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            yoshi.find_attribute("Tongue Minimum Pull Speed").value = rng_f(16.0 - 4.0 * mod, 16.0 + 8.0 * mod)
            yoshi.find_attribute("Tongue Max Pull Speed").value = rng_f(28.0 - 7.0 * mod, 28.0 + 14.0 * mod)
            yoshi.find_attribute("Egg Duration").value = rng_f(54.0 - 13.5 * mod, 54.0 + 27.0 * mod)
            yoshi.find_attribute("Star Velocity").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            yoshi.find_attribute("Star Acceleration").value = rng_f(-0.02 - -0.005 * mod, -0.02 + -0.01 * mod)

            younglink = characters.find_fighter("Young Link")
            younglink.find_attribute("Bow Frames For Max Charge").value = rng_f(45.0 - 11.25 * mod, 45.0 + 22.5 * mod)
            younglink.find_attribute("Bow Charge Speed").value = rng_f(1.33 - 0.3325 * mod, 1.33 + 0.665 * mod)
            younglink.find_attribute("Bow Landing Lag").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            younglink.find_attribute("Boomerang Launch Angle").value = rng_f(0.8727 - 0.2182 * mod, 0.8727 + 0.4363 * mod)
            younglink.find_attribute("Boomerang Smash Launch Velocity").value = rng_f(2.9 - 0.725 * mod, 2.9 + 1.45 * mod)
            younglink.find_attribute("Boomerang Tilt Launch Velocity").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            younglink.find_attribute("Spin Attack Landing Lag").value = rng_f(24.0 - 6.0 * mod, 24.0 + 12.0 * mod)
            younglink.find_attribute("Spin Attack Horizontal Momentum").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            younglink.find_attribute("Spin Attack Aerial Mobility").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            younglink.find_attribute("Spin Attack Momentum Preservation").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            younglink.find_attribute("Spin Attack Vetical Momentum").value = rng_f(2.31 - 0.5775 * mod, 2.31 + 1.155 * mod)
            younglink.find_attribute("Spin Attack Landing Gravity").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            younglink.find_attribute("Down Aerial Bounce Momentum").value = rng_f(1.33 - 0.3325 * mod, 1.33 + 0.665 * mod)
            younglink.find_attribute("Down Aerial Hitbox Reapply Rate").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            younglink.find_attribute("Down Aerial Hitbox 0 Damage On Rehit").value = rng(8 - 2 * mod, 8 + 2 * mod)
            younglink.find_attribute("Down Aerial Hitbox 1 Damage On Rehit").value = rng(9 - 2 * mod, 9 + 2 * mod)
            younglink.find_attribute("Down Aerial Hitbox 2 Damage On Rehit").value = rng(9 - 2 * mod, 9 + 2 * mod)
            younglink.find_attribute("Sword Trail Width").value = rng_f(1.59 - 0.3975 * mod, 1.59 + 0.795 * mod)
            younglink.find_attribute("Sword Trail Height").value = rng_f(1.59 - 0.3975 * mod, 1.59 + 0.795 * mod)
            younglink.find_attribute("Hookshot Grab Delay").value = rng(7 - 2 * mod, 7 + 2 * mod)
            younglink.find_attribute("Hookshot Grab Chain Release Begin").value = rng(10 - 2 * mod, 10 + 2 * mod)
            younglink.find_attribute("Hookshot Grab Chain Retract Begin").value = rng(55 - 14 * mod, 55 + 14 * mod)
            younglink.find_attribute("Hookshot Grab Chain Retract Finish").value = rng(79 - 20 * mod, 79 + 20 * mod)
            younglink.find_attribute("Hookshot Dash Grab Delay").value = rng(7 - 2 * mod, 7 + 2 * mod)
            younglink.find_attribute("Hookshot Dash Grab Chain Release Begin").value = rng(13 - 3 * mod, 13 + 3 * mod)
            younglink.find_attribute("Hookshot Dash Grab Chain Retract Begin").value = rng(55 - 14 * mod, 55 + 14 * mod)
            younglink.find_attribute("Hookshot Dash Grab Chain Retract Finish").value = rng(88 - 22 * mod, 88 + 22 * mod)
            younglink.find_attribute("Hookshot Air Delay").value = rng(5 - 1 * mod, 5 + 1 * mod)
            younglink.find_attribute("Hookshot Air Chain Release Begin").value = rng(10 - 2 * mod, 10 + 2 * mod)
            younglink.find_attribute("Hookshot Air Chain Retract Begin").value = rng(47 - 12 * mod, 47 + 12 * mod)
            younglink.find_attribute("Hookshot Air Chain Retract Finish").value = rng(58 - 14 * mod, 58 + 14 * mod)
            younglink.find_attribute("Hookshot Wall Release Jump Height").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            younglink.find_attribute("Hookshot Hang Duration").value = rng(180 - 45 * mod, 180 + 45 * mod)
            younglink.find_attribute("Deku Shield Collision Bubble Size").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            younglink.find_attribute("Deku Shield Impact Momentum Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            younglink.find_attribute("Bomb Duration").value = rng(300 - 75 * mod, 300 + 75 * mod)
            younglink.find_attribute("Bomb Max Bounces").value = rng(6 - 2 * mod, 6 + 2 * mod)
            younglink.find_attribute("Bomb Bounce Rehit Rate").value = rng(10 - 2 * mod, 10 + 2 * mod)
            younglink.find_attribute("Bomb Explosion Flash Frames").value = rng(96 - 24 * mod, 96 + 24 * mod)
            younglink.find_attribute("Bomb HP").value = rng(6 - 2 * mod, 6 + 2 * mod)
            younglink.find_attribute("Bomb Horizontal Velocity to Detonate").value = rng_f(0.8 - 0.2 * mod, 0.8 + 0.4 * mod)
            younglink.find_attribute("Bomb Base Launch Speed on Hit").value = rng_f(-0.03 - -0.0075 * mod, -0.03 + -0.015 * mod)
            younglink.find_attribute("Bomb Launch Speed Multiplier on Hit").value = rng_f(0.03 - 0.0075 * mod, 0.03 + 0.015 * mod)
            younglink.find_attribute("Boomerang Tilt Duration").value = rng(140 - 35 * mod, 140 + 35 * mod)
            younglink.find_attribute("Boomerang Smash Duration").value = rng(180 - 45 * mod, 180 + 45 * mod)
            younglink.find_attribute("Boomerang Launch Velocity").value = rng_f(0.047 - 0.0117 * mod, 0.047 + 0.0235 * mod)
            younglink.find_attribute("Boomerang Release Angle Multiplier").value = rng_f(2.4 - 0.6 * mod, 2.4 + 1.2 * mod)
            younglink.find_attribute("Boomerang Return Transition Smoothness").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            younglink.find_attribute("Boomerang Return Angle Modifier").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            younglink.find_attribute("Boomerang Return Homing Accuracy 1").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            younglink.find_attribute("Boomerang Return Homing Accuracy 2").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            younglink.find_attribute("Boomerang Rebound Angle Modifier").value = rng_f(140.0 - 35.0 * mod, 140.0 + 70.0 * mod)
            younglink.find_attribute("Boomerang Return Acceleration").value = rng_f(6.0 - 1.5 * mod, 6.0 + 3.0 * mod)
            younglink.find_attribute("Boomerang Spin Speed").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            younglink.find_attribute("Boomerang Frame Delay Between SFX").value = rng_f(20.0 - 5.0 * mod, 20.0 + 10.0 * mod)
            younglink.find_attribute("Boomerang Trail Effect 1 Delay").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            younglink.find_attribute("Boomerang Trail Effect 2 Delay").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            younglink.find_attribute("Hookshot Number of Chains").value = rng(10 - 2 * mod, 10 + 2 * mod)
            younglink.find_attribute("Hookshot Distance Between Chains").value = rng_f(1.8 - 0.45 * mod, 1.8 + 0.9 * mod)
            younglink.find_attribute("Hookshot Chain Launch Speed").value = rng_f(2.7 - 0.675 * mod, 2.7 + 1.35 * mod)
            younglink.find_attribute("Hookshot Chain Gravity").value = rng_f(0.1 - 0.025 * mod, 0.1 + 0.05 * mod)
            younglink.find_attribute("Hookshot Chain Retraction Speed").value = rng_f(3.6 - 0.9 * mod, 3.6 + 1.8 * mod)
            younglink.find_attribute("Hookshot Ground Length Modifier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            younglink.find_attribute("Hookshot Air Length Modifier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            younglink.find_attribute("Arrow Duration (Air)").value = rng_f(55.0 - 13.75 * mod, 55.0 + 27.5 * mod)
            younglink.find_attribute("Arrow Uncharged Velocity").value = rng_f(1.3 - 0.325 * mod, 1.3 + 0.65 * mod)
            younglink.find_attribute("Arrow Charged Velocity Multiplier").value = rng_f(4.0 - 1.0 * mod, 4.0 + 2.0 * mod)
            younglink.find_attribute("Arrow Uncharged Damage").value = rng_f(8.0 - 2.0 * mod, 8.0 + 4.0 * mod)
            younglink.find_attribute("Arrow Full Charge Damage").value = rng_f(15.0 - 3.75 * mod, 15.0 + 7.5 * mod)
            younglink.find_attribute("Arrow Duration (Ground)").value = rng_f(50.0 - 12.5 * mod, 50.0 + 25.0 * mod)
            younglink.find_attribute("Arrow Gravity").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            younglink.find_attribute("Arrow Arc Modifier (Cosmetic only)").value = rng_f(1.2217 - 0.3054 * mod, 1.2217 + 0.6109 * mod)

            zelda = characters.find_fighter("Zelda")
            zelda.find_attribute("Nayru's Love Gravity Delay").value = rng(4 - 1 * mod, 4 + 1 * mod)
            zelda.find_attribute("Nayru's Love Momentum Preservation").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            zelda.find_attribute("Nayru's Love Fall Acceleration").value = rng_f(0.0267 - 0.0067 * mod, 0.0267 + 0.0133 * mod)
            zelda.find_attribute("Nayru's Love Max Damage Reflectable").value = rng(50 - 12 * mod, 50 + 12 * mod)
            zelda.find_attribute("Nayru's Love Reflection Bubble Size").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            zelda.find_attribute("Nayru's Love Reflection Damage Multiplier").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            zelda.find_attribute("Nayru's Love Reflection Speed Multiplier").value = rng_f(1.0 - 0.25 * mod, 1.0 + 0.5 * mod)
            zelda.find_attribute("Din's Fire Max Hold Time").value = rng(25 - 6 * mod, 25 + 6 * mod)
            zelda.find_attribute("Din's Fire Gravity Delay").value = rng(10 - 2 * mod, 10 + 2 * mod)
            zelda.find_attribute("Din's Fire Frames for Auto Charge").value = rng(14 - 4 * mod, 14 + 4 * mod)
            zelda.find_attribute("Din's Fire X-Offset").value = rng_f(4.5 - 1.125 * mod, 4.5 + 2.25 * mod)
            zelda.find_attribute("Din's Fire Y-Offset").value = rng_f(-0.8 - -0.2 * mod, -0.8 + -0.4 * mod)
            zelda.find_attribute("Din's Fire Fall Acceleration").value = rng_f(0.019 - 0.0047 * mod, 0.019 + 0.0095 * mod)
            zelda.find_attribute("Din's Fire Landing Lag").value = rng_f(24.0 - 6.0 * mod, 24.0 + 12.0 * mod)
            zelda.find_attribute("Farore's Wind Horizontal Momentum Preservation").value = rng_f(1.5 - 0.375 * mod, 1.5 + 0.75 * mod)
            zelda.find_attribute("Farore's Wind Vertical Momentum Preservation").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            zelda.find_attribute("Farore's Wind Fall Acceleration").value = rng_f(0.03 - 0.0075 * mod, 0.03 + 0.015 * mod)
            zelda.find_attribute("Farore's Wind Travel Distance").value = rng(20 - 5 * mod, 20 + 5 * mod)
            zelda.find_attribute("Farore's Wind Base Momentum").value = rng_f(2.2 - 0.55 * mod, 2.2 + 1.1 * mod)
            zelda.find_attribute("Farore's Wind Momentum Variable").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            zelda.find_attribute("Farore's Wind Momentum After Warp").value = rng_f(0.6 - 0.15 * mod, 0.6 + 0.3 * mod)
            zelda.find_attribute("Farore's Wind Momentum After Warp 2").value = rng_f(0.2 - 0.05 * mod, 0.2 + 0.1 * mod)
            zelda.find_attribute("Farore's Wind Momentum Landing Lag").value = rng_f(30.0 - 7.5 * mod, 30.0 + 15.0 * mod)
            zelda.find_attribute("Farore's Wind Horizontal Momentum Modifier").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            zelda.find_attribute("Farore's Wind Vertical Momentum Modifier").value = rng_f(2.0 - 0.5 * mod, 2.0 + 1.0 * mod)
            zelda.find_attribute("Din's Fire Charge Maximum Duration").value = rng_f(65.0 - 16.25 * mod, 65.0 + 32.5 * mod)
            zelda.find_attribute("Din's Fire Charge Damage Growth Window").value = rng_f(60.0 - 15.0 * mod, 60.0 + 30.0 * mod)
            zelda.find_attribute("Din's Fire Charge Launch Angle").value = rng_f(0.0 - 0.0 * mod, 0.0 + 0.0 * mod)
            zelda.find_attribute("Din's Fire Charge Initial Velocity").value = rng_f(0.5 - 0.125 * mod, 0.5 + 0.25 * mod)
            zelda.find_attribute("Din's Fire Charge Acceleration").value = rng_f(0.06 - 0.015 * mod, 0.06 + 0.03 * mod)
            zelda.find_attribute("Din's Fire Charge Max Velocity").value = rng_f(7.0 - 1.75 * mod, 7.0 + 3.5 * mod)
            zelda.find_attribute("Din's Fire Charge Vertical Meneuverability").value = rng_f(0.0244 - 0.0061 * mod, 0.0244 + 0.0122 * mod)
            zelda.find_attribute("Din's Fire Charge Maximum Curve Angle").value = rng_f(1.3963 - 0.3491 * mod, 1.3963 + 0.6981 * mod)
            zelda.find_attribute("Din's Fire Charge Detonation Delay").value = rng_f(22.0 - 5.5 * mod, 22.0 + 11.0 * mod)
            zelda.find_attribute("Din's Fire Explosion Hitbox Size").value = rng_f(60.0 - 15.0 * mod, 60.0 + 30.0 * mod)
            zelda.find_attribute("Din's Fire Explosion Initial Graphic Size").value = rng_f(0.3 - 0.075 * mod, 0.3 + 0.15 * mod)
            zelda.find_attribute("Din's Fire Explosion Graphic Growth Multiplier").value = rng_f(1.7 - 0.425 * mod, 1.7 + 0.85 * mod)
            zelda.find_attribute("Din's Fire Explosion Base Damage").value = rng_f(3.0 - 0.75 * mod, 3.0 + 1.5 * mod)
            zelda.find_attribute("Din's Fire Explosion Damage Multiplier").value = rng_f(0.17 - 0.0425 * mod, 0.17 + 0.085 * mod)

    
def start(flags):
    flags += " -"
    flag_array = []
    parameter = 0
    current_flag = ""
    recording = False
    for char in flags:
        if char == "&" and not recording:
            current_flag += char
            recording = True
        elif char == "-" and recording:
            recording = False
            flag_array.append(current_flag)
            current_flag = ""
        elif char == "&" and recording:
            flag_array.append(current_flag)
            current_flag = char
        elif recording:
            current_flag += char
            
    for flag in flag_array:
        activate_flag(flag)
            
        
    
