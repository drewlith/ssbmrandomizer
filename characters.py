import dat, fst, struct
from util import to_word
fighters = []
bosses = []
items = None

ALL_CHARACTERS = ["bowser", "falcon", "dk", "dr", "falco", "fox",
            "gnw", "ganon", "popo", "nana", "jigglypuff", "kirby",
            "link", "luigi", "mario", "marth", "mewtwo", "ness", "peach", "pichu",
            "pikachu", "roy", "samus", "sheik", "yoshi", "younglink", "zelda",
            "boy", "girl", "gigabowser", "masterhand", "crazyhand"]

ALL_TAGS = ["shine", "recovery", "upb", "downb", "sideb", "neutralb", "nair", "fair", "bair", "dair", "upair", "zair",
            "pummel", "jab", "ftilt", "uptilt", "dtilt", "dashattack", "upsmash",
            "downsmash", "forwardsmash", "projectile", "multihit", "spike", "meteor",
            "sweetspot", "sourspot", "weakhit", "stronghit", "killthrow", "fthrow",
            "dthrow", "upthrow", "bthrow", "combothrow", "commandthrow",
            "normal", "special", "attack", "throw"]

attribute_tags = ["article", "special", "attribute", "common", "movement", "animation", "frames", "scale",
                  "projectile", "etc", "property"]
attack_tags = []
throw_tags = []

class Fighter():
    def __init__(self, name, special_attribute_block_size, article_sizes = [], article_offsets = []):
        self.name = name
        self.subactions = dat.get_subactions()
        self.attributes = []
        self.special_attributes = []
        self.article_attributes = []
        self.articles = []
        self.attacks = []
        self.item_attacks = []
        self.throws = []
        self.add_attributes(dat.get_attribute_data())
        self.special_attribute_data = dat.get_special_attribute_data(special_attribute_block_size)
        self.articles_sizes = article_sizes
        self.articles_offsets = article_offsets
        self.articles_datas = []
        self.data_file_name = ""

    def add_attack(self, hitboxes, name, strength=0, tags=[], append_after=-1):
        new_tag_array = [] # Fixes an insane bug?
        for tag in tags:
            new_tag_array.append(tag)
        if len(hitboxes) < 1:
            return
        if append_after >= 0:
            self.attacks.insert(append_after, Attack(hitboxes, name, strength, new_tag_array))
        else:
            self.attacks.append(Attack(hitboxes, name, strength, new_tag_array))

    def add_item(self, hitboxes, name, strength, tags):
        self.item_attacks.append(Attack(hitboxes, name, strength, tags))

    def add_throw(self, throw, name, tags=[]):
        throw.name = name
        throw.tags = tags
        self.throws.append(throw)

    def add_attribute(self, attribute_data, offset, name, integer=False):
        self.attributes.append(Attribute(attribute_data[offset:offset+4], name, offset, integer))

    def add_attribute_special(self, attribute_data, offset, name, integer=False):
        self.special_attributes.append(Attribute(attribute_data[offset:offset+4], name, offset, integer))

    def add_attribute_article(self, attribute_data, offset, name, article_number=0, integer=False):
        attribute = Attribute(attribute_data[offset:offset+4], name, offset, integer)
        attribute.article_number = article_number
        self.article_attributes.append(attribute)

    def add_attributes(self, attribute_data):
        self.add_attribute(attribute_data, 0, "Initial Walk Velocity")
        self.add_attribute(attribute_data, 4, "Walk Acceleration")
        self.add_attribute(attribute_data, 8, "Walk Maximum Velocity")
        self.add_attribute(attribute_data, 12, "Slow Walk Max Velocity")
        self.add_attribute(attribute_data, 16, "Mid Walk Threshold")
        self.add_attribute(attribute_data, 20, "Fast Walk Threshold")
        self.add_attribute(attribute_data, 24, "Grounded Friction")
        self.add_attribute(attribute_data, 28, "Dash Initial Velocity")
        self.add_attribute(attribute_data, 32, "Dash & Run Acceleration A")
        self.add_attribute(attribute_data, 36, "Dash & Run Acceleration B")
        self.add_attribute(attribute_data, 40, "Dash & Run Terminal Velocity")
        self.add_attribute(attribute_data, 44, "Run Animation Scaling")
        self.add_attribute(attribute_data, 48, "Run Acceleration")
        self.add_attribute(attribute_data, 56, "Jumpsquat Frames")
        self.add_attribute(attribute_data, 60, "Jump Horizontal Velocity")
        self.add_attribute(attribute_data, 64, "Jump Vertical Velocity")
        self.add_attribute(attribute_data, 68, "Jump Momentum Multiplier")
        self.add_attribute(attribute_data, 72, "Jump Horizontal Max Velocity")
        self.add_attribute(attribute_data, 76, "Shorthop Vertical Velocity")
        self.add_attribute(attribute_data, 80, "Air Jump Multiplier")
        self.add_attribute(attribute_data, 84, "Double Jump Momentum")
        self.add_attribute(attribute_data, 88, "Number of Jumps", True)
        self.add_attribute(attribute_data, 92, "Gravity Scale")
        self.add_attribute(attribute_data, 96, "Terminal Velocity")
        self.add_attribute(attribute_data, 100, "Air Mobility A")
        self.add_attribute(attribute_data, 104, "Air Mobility B")
        self.add_attribute(attribute_data, 108, "Aerial Horizontal Max Velocity")
        self.add_attribute(attribute_data, 112, "Air Friction")
        self.add_attribute(attribute_data, 116, "Fast Fall Terminal Velocity")
        self.add_attribute(attribute_data, 124, "Jab 2 Frame Window")
        self.add_attribute(attribute_data, 128, "Jab 3 Frame Window")
        self.add_attribute(attribute_data, 132, "Turnaround Frames")
        self.add_attribute(attribute_data, 136, "Weight")
        self.add_attribute(attribute_data, 140, "Model Scale")
        self.add_attribute(attribute_data, 144, "Shield Size")
        self.add_attribute(attribute_data, 148, "Shield Break Velocity")
        self.add_attribute(attribute_data, 152, "Rapid Jab Window (Frames)")
        self.add_attribute(attribute_data, 168, "Ledgejump Horizontal Velocity")
        self.add_attribute(attribute_data, 172, "Ledgejump Vertical Velocity")
        self.add_attribute(attribute_data, 176, "Item Throw Velocity")
        self.add_attribute(attribute_data, 224, "Kirby Star Damage")
        self.add_attribute(attribute_data, 228, "Landing Lag Frames: Empty")
        self.add_attribute(attribute_data, 232, "Landing Lag Frames: Neutral Air")
        self.add_attribute(attribute_data, 236, "Landing Lag Frames: Forward Air")
        self.add_attribute(attribute_data, 240, "Landing Lag Frames: Back Air")
        self.add_attribute(attribute_data, 244, "Landing Lag Frames: Up Air")
        self.add_attribute(attribute_data, 248, "Landing Lag Frames: Down Air")
        self.add_attribute(attribute_data, 252, "Victory Screen Window Model Scale")
        self.add_attribute(attribute_data, 260, "Wall Jump Horizontal Velocity")
        self.add_attribute(attribute_data, 264, "Wall Jump Vertical Velocity")

    def find_attribute(self, name):
        for attribute in self.attributes:
            if name in attribute.name:
                return attribute
        for attribute in self.special_attributes:
            if name in attribute.name:
                return attribute
        for attribute in self.article_attributes:
            if name in attribute.name:
                return attribute
        print("No attribute found with name: ", name)

    def find_attack(self, name):
        for attack in self.attacks:
            if name in attack.name:
                return attack
        print("No attack found with name: ", name)            

class Attribute():
    def __init__(self, data, name, offset, integer=False):
        self.data = data
        self.name = name
        self.tags = []
        self.offset = offset
        self.integer = integer
        self.article_number = 0
        self.original_value = 0
        self.log_notes = ""

    @property
    def value(self):
        if self.integer:
            return to_word(self.data)
        return struct.unpack('>f',self.data)[0]

    @value.setter
    def value(self, value):
        if self.integer:
            data = value.to_bytes(4, 'big')
            return
        data = struct.pack('>f', value)
        self.data = data

    def add_tag(self, tag):
        for entry in ALL_TAGS:
            if tag in entry:
                self.tags.append(tag)
                return
        print("Invalid tag: ", tag)

    def has_tag(self, name):
        for tag in self.tags:
            if tag == name:
                return True
            else:
                return False
        
class Attack():
    def __init__(self, hitboxes, name, strength, tags):
        self.hitboxes = hitboxes
        self.name = name
        self.strength = strength
        self.tags = tags
        self.original_values = []
        self.log_notes = []

    @property
    def damage(self):
        return self.hitboxes[0].damage
    
    @damage.setter
    def damage(self, value):
        for hitbox in self.hitboxes:
            hitbox.damage = value
            
    @property
    def angle(self):
        return self.hitboxes[0].angle
    
    @angle.setter
    def angle(self, value):
        for hitbox in self.hitboxes:
            hitbox.angle = value
            
    @property
    def growth(self):
        return self.hitboxes[0].growth
    
    @growth.setter
    def growth(self, value):
        for hitbox in self.hitboxes:
            hitbox.growth = value
            
    @property
    def set_kb(self):
        return self.hitboxes[0].set_kb

    @set_kb.setter
    def set_kb(self, value):
        for hitbox in self.hitboxes:
            hitbox.set_kb = value

    @property
    def base(self):
        return self.hitboxes[0].base

    @base.setter
    def base(self, value):
        for hitbox in self.hitboxes:
            hitbox.base = value

    @property
    def element(self):
        return self.hitboxes[0].element

    @element.setter
    def element(self, value):
        for hitbox in self.hitboxes:
            hitbox.element = value

    @property
    def shield_damage(self):
        return self.hitboxes[0].shield_damage

    @shield_damage.setter
    def shield_damage(self, value):
        for hitbox in self.hitboxes:
            hitbox.shield_damage = value

    @property
    def sfx(self):
        return self.hitboxes[0].sfx

    @sfx.setter
    def sfx(self, value):
        for hitbox in self.hitboxes:
            hitbox.sfx = value

    @property
    def size(self):
        return self.hitboxes[0].size

    @size.setter
    def size(self, value):
        for hitbox in self.hitboxes:
            hitbox.size = value

    def add_tag(self, tag):
        for _tag in self.tags:
            if tag in _tag:
                print("Tag already exists! Skipping")
                return
        for entry in ALL_TAGS:
            if tag in entry:
                self.tags.append(tag)
                return
        print("Invalid tag: ", tag)

    def add_tags(self, tags):
        for tag in tags:
            self.add_tag(tag)

    def has_tag(self, name):
        for tag in self.tags:
            if tag == name:
                return True
            else:
                return False

def find_fighter(name):
    for fighter in fighters:
        if name == fighter.name:
            return fighter
    print("No fighter found with name:", name)

def add_fighter(player_data, name, special_attribute_block_size, articles_sizes=[], articles_offsets=[], boss=False):
    #print("Getting data from", name)
    player_data.load_file_data()
    dat.load_data(player_data.file_data)
    fighter = Fighter(name, special_attribute_block_size)
    fighter.data_file_name = player_data.name
    if boss:
        bosses.append(fighter)
    else:
        fighters.append(fighter)
    fighter.articles_sizes = articles_sizes
    fighter.articles_offsets = articles_offsets
    fighter.articles_datas = dat.get_article_data(fighter)

def add_fighters(melee_files):
    fighters.clear()
    bosses.clear()
    add_fighter(fst.find_file(melee_files, b'PlKp.dat'), "Bowser", 0xA0, [0x18], [0x40D8])
    add_fighter(fst.find_file(melee_files, b'PlCa.dat'), "Captain Falcon", 0x8C)
    add_fighter(fst.find_file(melee_files, b'PlDk.dat'), "Donkey Kong", 0x74)
    add_fighter(fst.find_file(melee_files, b'PlDr.dat'), "Dr. Mario", 0x84, [0x14], [0x3BD4])
    add_fighter(fst.find_file(melee_files, b'PlFc.dat'), "Falco", 0xD4, [0x28, 0x8], [0x3F50, 0x4140])
    add_fighter(fst.find_file(melee_files, b'PlFx.dat'), "Fox", 0xD4, [0x28, 0x8], [0x3E94, 0x409C])
    add_fighter(fst.find_file(melee_files, b'PlGw.dat'), "Mr. Game & Watch", 0x94, [0x74], [0x4378])
    add_fighter(fst.find_file(melee_files, b'PlGn.dat'), "Ganondorf", 0x8C)
    add_fighter(fst.find_file(melee_files, b'PlPp.dat'), "Popo", 0x15C, [0x34, 0x18, 0x24], [0x3ADC, 0x3BB0, 0x3CA0])
    add_fighter(fst.find_file(melee_files, b'PlNn.dat'), "Nana", 0x15C)
    add_fighter(fst.find_file(melee_files, b'PlPr.dat'), "Jigglypuff", 0x100)
    add_fighter(fst.find_file(melee_files, b'PlKb.dat'), "Kirby", 0x424, [0x10], [0x7B2C])
    add_fighter(fst.find_file(melee_files, b'PlLk.dat'), "Link", 0xDC, [0x34, 0x64, 0x64, 0x2C], [0x4204, 0x40C0, 0x3E58, 0x3F48])
    add_fighter(fst.find_file(melee_files, b'PlLg.dat'), "Luigi", 0x98, [0x84, 0x10], [0x3A3C, 0x3A74])
    add_fighter(fst.find_file(melee_files, b'PlMr.dat'), "Mario", 0x84, [0x14], [0x3A98])
    add_fighter(fst.find_file(melee_files, b'PlMs.dat'), "Marth", 0x98)
    add_fighter(fst.find_file(melee_files, b'PlMt.dat'), "Mewtwo", 0x88, [0x8, 0x30], [0x3390, 0x3CD8])
    add_fighter(fst.find_file(melee_files, b'PlNs.dat'), "Ness", 0xDC, [0x8, 0xC, 0x2C, 0x14, 0x14, 0x5C],
                                                                [0x3E48, 0x3F10, 0x3C78, 0x4024, 0x3C7C, 0x4284])
    add_fighter(fst.find_file(melee_files, b'PlPe.dat'), "Peach", 0xC0, [0x48, 0x10], [0x40E8, 0x42E0])
    add_fighter(fst.find_file(melee_files, b'PlPc.dat'), "Pichu", 0xF8, [0xC, 0xC], [0x3CBC, 0x3B34])
    add_fighter(fst.find_file(melee_files, b'PlPk.dat'), "Pikachu", 0xF8, [0xC, 0xC], [0x3E1C, 0x3C74])
    add_fighter(fst.find_file(melee_files, b'PlFe.dat'), "Roy", 0x98)
    add_fighter(fst.find_file(melee_files, b'PlSs.dat'), "Samus", 0xD3, [0x10, 0x20, 0x38, 0x7C], [0x4124, 0x3E90, 0x4018, 0x4210])
    add_fighter(fst.find_file(melee_files, b'PlSk.dat'), "Sheik", 0x74, [0xC, 0x6C], [0x3994, 0x3C1C])
    add_fighter(fst.find_file(melee_files, b'PlYs.dat'), "Yoshi", 0x138, [0x8, 0x8], [0x3A68, 0x3B4C])
    add_fighter(fst.find_file(melee_files, b'PlCl.dat'), "Young Link", 0xDC, [0x34, 0x64, 0x64, 0x2C], [0x43E0, 0x429C, 0x4034, 0x4124])
    add_fighter(fst.find_file(melee_files, b'PlZd.dat'), "Zelda", 0xA8, [0x30, 0x14], [0x3EC8, 0x3FA0])
    add_fighter(fst.find_file(melee_files, b'PlBo.dat'), "Boy", 0x4, [], [], True)
    add_fighter(fst.find_file(melee_files, b'PlGl.dat'), "Girl", 0x4, [], [], True)
    add_fighter(fst.find_file(melee_files, b'PlGk.dat'), "Giga Bowser", 0x4, [], [], True)
    add_fighter(fst.find_file(melee_files, b'PlMh.dat'), "Master Hand", 0x4, [], [], True)
    add_fighter(fst.find_file(melee_files, b'PlCh.dat'), "Crazy Hand", 0x4, [], [], True)

