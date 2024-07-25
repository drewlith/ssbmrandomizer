import iso, characters, dat, os.path, random, os, subprocess
from util import to_word

# Modifies ISO file, retrieves and replaces files, and creates new ISO.

STRING_TABLE_OFFSET = 0x38D0 # Is there a way to calculate this offset?
# Would be useful for implementing Akaneia support.
ENTRY_SIZE = 0x0C

class ISOFile: # Contains FST data, and File data
    def __init__(self, data):
        self.entry_data = data
        self.file_data = None
        self.changed = False

    @property
    def type(self):
        if self.entry_data[0] == 0:
            return "File"
        return "Directory"

    @property
    def name(self):
        fst = iso.get_fst()
        offset = int.from_bytes(self.entry_data[0x01:0x04], "big") + STRING_TABLE_OFFSET
        name = bytearray()
        i = 0
        while True:
            byte = fst[offset+i]
            if byte == 0:
                return name
            name.append(byte)
            i += 1

    @property
    def offset(self):
        return to_word(self.entry_data[0x04:0x08])

    @offset.setter
    def offset(self, new):
        self.entry_data[0x04:0x08] = new.to_bytes(4, 'big')

    @property
    def size(self):
        return to_word(self.entry_data[0x08:0x0C])

    @size.setter
    def size(self, new):
        self.entry_data[0x08:0x0C] = new.to_bytes(4, 'big')

    def load_file_data(self):
        self.changed = True
        self.file_data = iso.seek_and_read(self.offset, self.size)

def get_file_entries():
    #print("Getting entries from fst...")
    fst = iso.get_fst()
    entries = []
    offset = 0
    while True: # Create Entries
        if offset >= STRING_TABLE_OFFSET:
            break
        entries.append(ISOFile(fst[offset:offset + ENTRY_SIZE]))
        offset += ENTRY_SIZE

    for entry in entries: # Add file data
        if entry.type == "File":
            end_of_file = entry.size + entry.offset

    return entries

def write_files(files):
    #print("Writing files to iso...")
    for file in files:
        if file.changed:
            iso.seek_and_write(file.offset, file.file_data)

def find_file(files, name):
    if len(files) <= 0:
        print("Error: No file entries!")
    for file in files:
        if name in file.name:
            return file
    print("No file found with name:", name)

def write_character_data(data_file, character):
    #print("Writing " + character.name + " file data...")
    for attack in character.attacks:
        for hitbox in attack.hitboxes:
            offset = hitbox.offset + 0x20 # Ignore Header
            data_file.file_data[offset:offset+len(hitbox.data)] = hitbox.data
    for throw in character.throws:
        offset = throw.offset + 0x20
        data_file.file_data[offset:offset+len(throw.data)] = throw.data
    dat.load_data(data_file.file_data)
    attributes_offset = dat.ft_attributes_offset() + 0x20
    for attribute in character.attributes:
        offset = attributes_offset + attribute.offset
        data_file.file_data[offset:offset+len(attribute.data)] = attribute.data
    special_offset = dat.ft_attributes_end() + 0x20
    for attribute in character.special_attributes:
        offset = special_offset + attribute.offset
        data_file.file_data[offset:offset+len(attribute.data)] = attribute.data
    for attribute in character.article_attributes:
        offset = character.articles_offsets[attribute.article_number] + attribute.offset + 0x20
        data_file.file_data[offset:offset+len(attribute.data)] = attribute.data

def write_all_character_data(files):
    for fighter in characters.fighters:
        write_character_data(find_file(files, fighter.data_file_name), fighter)

def create_xdelta(code):
    subprocess.run(['xdelta3', '-S', '-e', '-B 1430679552', '-s', "melee.iso", "output.iso", "seeds/" + code + ".xdelta"])

def write_iso(files):
    write_all_character_data(files)
    write_files(files)
    iso.melee.close()
