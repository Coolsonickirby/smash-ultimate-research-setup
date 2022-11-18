import zlib, os

def make_hash40(source_str):
    return (len(source_str) << 32) + zlib.crc32(source_str.encode())

def load_hashes():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),  "Hashes", "Hashes_all.txt"), "r") as f:
        for line in f.readlines():
            line = line.strip()
            arc_hashes[make_hash40(line)] = line
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),  "Hashes", "ParamLabels.csv"), "r") as f:
        for line in f.readlines():
            line = line.strip()
            (hash40, value) = line.split(',')
            hash40 = int(hash40, base=16)
            param_hashes[hash40] = value
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),  "Hashes", "tone_names.txt"), "r") as f:
        for line in f.readlines():
            line = line.strip()
            nus3audio_hashes[make_hash40(line)] = line

def find_hash(hash_target):
    found = False
    if hash_target in arc_hashes:
        found = True
        print(f"ARC Hash: {arc_hashes[hash_target]}")
    if hash_target in param_hashes:
        found = True
        print(f"Param Hash: {param_hashes[hash_target]}")
    if hash_target in nus3audio_hashes:
        found = True
        print(f"N3A Tone Name Hash: {nus3audio_hashes[hash_target]}")
    if found == False:
        print("Hash could not be found!")

arc_hashes = {}
param_hashes = {}
nus3audio_hashes = {}

load_hashes()
while True:
    search_str = input("Lookup/Convert: ").strip()
    if search_str.startswith("0x") or search_str.isnumeric():
        hash_target = int(search_str, base=16) if search_str.startswith("0x") else int(search_str)
        find_hash(hash_target)
    else:
        print(f"Hash40 of {search_str}: {hex(make_hash40(search_str))}")
    print()
