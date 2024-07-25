import random, iso, fst, gecko, characters, flag_parser, fighter_data, simple, string, log, util, os.path, get_adv_data

def start(_flags="", code=""):
    if len(code) > 0: # Seed is being generated from website
        if os.path.exists("seeds/" + code + ".xdelta"): # Seed has already been generated
            print("Seed already exists.")
            return 1 # Don't generate again
        
    source = open('melee.iso', 'rb')
    iso.melee = open('output.iso', 'wb+')
    iso.melee.write(source.read())
    source.close()

    flags = _flags
    
    # Grab ISO Files
    melee_files = fst.get_file_entries()

    # Add Fighters from .dat files
    characters.add_fighters(melee_files)
    # Wrap player file data
    fighter_data.add_all(melee_files)

    # Gecko Codes
    gecko.expand_dol()
    gecko.default_codes()
    gecko.code_flags(flags)
    
    # Flags
    if "-seed" not in flags:
        seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
        flags = "-seed " + seed +  " " + flags
    else:
        seed = util.get_flag(flags, "seed", True)
        
    random.seed(seed)
    log.get_start_values()
    simple.start(flags)
    flag_parser.start(flags)
    #get_adv_data.start()
    # Finish
    log.create_log_dict(flags, True, code)
    fst.write_iso(melee_files)
    if len(code) > 0:
        fst.create_xdelta(code)
