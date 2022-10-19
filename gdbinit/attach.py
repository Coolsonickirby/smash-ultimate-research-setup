main_start = [
    "cross2_Release.nss", # Super Smash Bros. Ultimate
    "Balloon15.nss" # Kirby and the Forgotten Land
]

print("Executing 'monitor wait application' (Launch your game)")
print()
res = gdb.execute("monitor wait application", to_string=True).strip()

print("Output of 'monitor wait application' (will attach automatically if nothing went wrong):")
print(res)
print()
attach = res.split('\n')[-1]
attach_command = attach[attach.index('`') + 1:attach.rindex('`')]

print("Executing '%s'" % attach_command)
gdb.execute(attach_command)

print()
print("Looking for main addresses...")
found = False
info = gdb.execute("mon get info", to_string=True)
for line in info.split('\n'):
    for start in main_start:
        if start in line:
            print("Found %s address start! Setting $main to it..." % start)
            res = line.strip()
            main = res.split(" ")[0]
            gdb.execute("set $main = %s" % main)
            print("Set $main to %s (%s address start)" % (main, start))
            found = True
            break
if not found:
    print("Could not find any of: %s!" % ' - '.join(main_start))
else:
    print()
    print("You can now do your stuff (make sure to `continue` so the game can start after setting up your break/watch points)")