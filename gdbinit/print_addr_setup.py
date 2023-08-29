# Get addresses from gdb
address = gdb.execute("p/x $curr_addr", to_string=True)
address = address[address.index("=") + 2:]
address = int(address,0)

offset_kind = gdb.execute("p $offset_kind", to_string=True)
offset_kind = offset_kind[offset_kind.index('"') + 1:-2]

main_title = gdb.execute("p $main_title", to_string=True)
try:
  main_title = main_title[main_title.index('"') + 1:-2]
except:
  main_title = "" 

# Set up list of relevant executables
executable_list = []
is_module = False
found = False
info = gdb.execute("mon get info", to_string=True)

for line in info.split('\n'):
    if line.startswith("Modules:"):
        is_module = True
        continue
    if is_module:
        application_info = line.strip()
        if application_info == "":
            break
        start_addr = application_info.split(" ")[0]
        end_addr = application_info.split(" ")[2]
        title = application_info.split(" ")[3]
        variable_title = title.split('.')[0]
        executable_tuple = (variable_title,int(start_addr,0),int(end_addr,0))
        executable_list.append(executable_tuple)

for executable in executable_list:
    if executable[1] <= address <= executable[2]:
        if executable[0] in main_title:
            print("%s: %s -> %s" % (offset_kind, "main", hex(address - executable[1])))
            found = True
        else:
            print("%s: %s -> %s" % (offset_kind, executable[0], hex(address - executable[1])))
            found = True

if found == False:
    print("%s: unknown -> %s" % (offset_kind, hex(address)))
