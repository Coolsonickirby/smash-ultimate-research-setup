define my_bt
  set $frame = $fp
  set $prev_frame = 0
  while $frame != 0 && $prev_frame != $frame
      set $prev_frame = $frame
      p/x ((unsigned long long *)$frame)[1]
      set $frame = ((unsigned long long *)$frame)[0]
  end
end
define my_bt2
  set $frame = $fp
  set $prev_frame = 0
  while $frame != 0 && $prev_frame != $frame
    set $prev_frame = $frame
    set $addr = ((unsigned long long *)$frame)[1]
    printf "offset: %x\n", $addr-$main
    set $frame = ((unsigned long long *)$frame)[0]
  end
end
define no_op
  set {unsigned int}($main+$arg0) = 0xD503201F
end
define stub
  set {unsigned int}($main+$arg0) = 0xD65F03C0
end
define replace
  set {unsigned int}($main+$arg0) = $arg1
end
define get_pc
  printf "pc: %x\n", $pc - $main
end
define break_at
  b *$main+$arg0
end
define localize
  printf "offset: %x\n", $arg0 - $main
end
define prepare_rehook
  printf "replace %x %x\n", $arg0, ((unsigned int*)($main+$arg0))[0]
  printf "replace %x %x\n", $arg0+4, ((unsigned int*)($main+$arg0))[1]
  printf "replace %x %x\n", $arg0+8, ((unsigned int*)($main+$arg0))[2]
  printf "replace %x %x\n", $arg0+0xC, ((unsigned int*)($main+$arg0))[3]
end

define setup
   source ~/attach.py
end

define print_trace
   get_pc
   localize $lr
   my_bt2
end

define xxd
   dump binary memory dump.bin $arg0 $arg0+$arg1
   shell xxd dump.bin
end

set pagination off
target extended-remote 10.0.0.143:22225
setup
