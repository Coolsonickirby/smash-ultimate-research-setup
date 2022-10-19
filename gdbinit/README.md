# gdbinit

```
Usage:
1. Download both `.gdbinit` & `attach.py` and place either in your home directory or wherever you are running GDB from
2. Open `.gdbinit` and change the IP address at the end of the file to whatever your switch ip is

(Manual Attaching)
3. When you open GDB it will attempt to connect to your switch and wait on an application to open. It will say something like attach 0xXX where 0xXX is a process ID. Type that to attach to the process
4. Run mon get info and copy the address for the main executable (in our case cross2_Release.nsss and type set $main = <main address>, without the angled brackets and replacing main address with the address you copied.

Now you have access to the following functions
    1. `my_bt`: Prints the backtrace as absolute addresses. Often misses the first address on the backtrace but you can just p/x $lr for that.
    2. `my_bt2`: Prints the backtrace with offsets relative to the base of main.
    3. `no_op <offset>`: Takes an offset into main and NOPs the instruction at that address
    4. `stub <offset>`: Takes an offset into main and stubs the function at that address
    5. `replace <offset> <new_instruction>`: Replaces the instruction at an offset with the new instruction
    6. `get_pc`: Gets the PC as an offset relative to the base of main
    7. `break_at <offset>`: Sets a breakpoint at an offset relative to the base of main
    8. `localize <register/address>`: Converts the value in the register (or the passed address) to an offset relative to the base of main
    9. `xxd <address> <size>`: Print a xxd dump of the address (will most likely work on Unix Systems only!)
    10. `usual`: Runs `get_pc`, `localize $lr`, & `my_bt2` to get the current offset, the calling offset, and the backtrace in one command instead of three
```
This is all blujay's stuff. Check him out at [Twitter](https://twitter.com/jayblu_/) and support him on [Ko-Fi](https://ko-fi.com/bludev)!
