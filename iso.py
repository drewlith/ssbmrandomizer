from util import to_word
#print("Start copying")
MAX_CAPACITY = 1459978240
CHUNK_SIZE = 5703040 # 256 Chunks
source = open('melee.iso', 'rb')
melee = open('output.iso', 'wb+')
melee.write(source.read())
source.close()

#print("Done copying")
def seek_and_read(offset, size):
    melee.seek(offset)
    return bytearray(melee.read(size))

def seek_and_write(offset, data):
    melee.seek(offset)
    melee.write(data)

def seek_and_read_word(offset):
    return seek_and_read(offset, 4)

def get_fst():
    return seek_and_read(fst_offset(), fst_size())

def get_dol():
    return seek_and_read(dol_offset(), dol_size())
    
def dol_offset():
    return to_word(seek_and_read_word(0x420))

def dol_size():
    return fst_offset() - dol_offset()

def fst_offset():
    return to_word(seek_and_read_word(0x0424))

def fst_size():
    return to_word(seek_and_read_word(0x0428))

def get_game_id():
    return seek_and_read(0, 6)

def set_game_id(new):
    seek_and_write(0, new)

def get_game_name():
    name_data = seek_and_read(0x0020, 0x3DF)
    name = bytearray()
    for byte in name_data:
        if byte == 0:
            break
        name.append(byte)
    return name

def set_game_name(new):
    if type(new) == str:
        new = new.encode('utf-8')
    new = bytearray(new)
    for i in range(0x3FF - len(new)):
        new.append(0)
    seek_and_write(0x0020, new)

def magic_word():
    return seek_and_read_word(0x001C).hex()

def write_dol(new_dol):
    seek_and_write(dol_offset(), new_dol)
