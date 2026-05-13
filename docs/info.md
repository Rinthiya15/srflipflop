## How it works

SR Flip-Flop implemented in Verilog.

- `ui_in[0]` = Set (S)
- `ui_in[1]` = Reset (R)
- `uo_out[0]` = Q
- `uo_out[1]` = Q̅

## How to test
iverilog -o sim tb.v tt_um_srflipflop.v
vvp sim
gtkwave sr_flipflop.vcd

## External hardware

No external hardware required.
