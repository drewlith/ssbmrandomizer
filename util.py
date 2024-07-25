import random

MASK = [1, 2, 4, 8, 16, 32, 64, 128]
CLEAR_MASK = [254, 253, 251, 247, 239, 223, 191, 127]

def get_bit(data, bit): # lowest index = least significant. Use on Bytearray
    index = (len(data)-1) - bit // 8
    if data[index] & MASK[bit%8] == MASK[bit%8]: return 1
    else: return 0

def set_bit(data, bit):
    index = (len(data)-1) - bit // 8
    data[index] = data[index] | MASK[bit%8]
    return data

def clear_bit(data, bit):
    index = (len(data)-1) - bit // 8
    data[index] = data[index] & CLEAR_MASK[bit%8]
    return data

def get_value(data, offset, size):
    value = 0
    for i in range(size):
        if get_bit(data, offset+i) == 1:
            value += 2**i
    return value

def set_value(data, offset, size, value):
    for i in range(size):
        if value & 2**i == 2**i: data = set_bit(data,offset+i)
        else: data = clear_bit(data, offset+i)
    return data

def to_word(data, offset=0):
    return get_value(data, offset*32, 32)

def percent_chance(chance): # Util, enter chance in %
    rng = random.randint(0,99)
    if rng < chance:
        return True
    else:
        return False

def get_flag(flags, name, is_string=False, is_float=False): # Gets values after flag name
    name = name.replace(" ", "")
    index = flags.find(name)
    index += len(name)
    string = ""
    if is_string == False:
        parameters = []
        param = ""
        while True:
            if index > len(flags)-1:
                parameters.append(int(param))
                break
            if flags[index] == "&" or flags[index] == "-": # Flag Delimiters
                parameters.append(int(param))
                break
            if flags[index] == ":": # Parameter Delimiter
                parameters.append(int(param))
                param = ""
            else:
                param += flags[index]
            index += 1
        return parameters
    else:
        while True:
            char = flags[index]
            if char == "&" or char == "-": # Flag Delimiters
                break
            string += char
            index += 1
        string = string.replace(" ", "")
        return string
