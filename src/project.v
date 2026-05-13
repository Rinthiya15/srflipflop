/*
 * SR Flip-Flop Example for Tiny Tapeout
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_flipflop (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // always 1
    input  wire       clk,      // clock
    input  wire       rst_n     // active low reset
);

  // SR Flip-Flop inputs
  wire S = ui_in[0];   // Set input
  wire R = ui_in[1];   // Reset input

  reg Q;

  // SR Flip-Flop logic
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      Q <= 1'b0;
    else begin
      case ({S, R})
        2'b10: Q <= 1'b1; // Set
        2'b01: Q <= 1'b0; // Reset
        2'b00: Q <= Q;    // Hold
        2'b11: Q <= 1'bx; // Invalid condition
      endcase
    end
  end

  // Output assignments
  assign uo_out[0] = Q;     // Q output
  assign uo_out[1] = ~Q;    // Q̅ output
  assign uo_out[7:2] = 6'b0;

  // Unused IOs
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  // Prevent warnings
  wire _unused = &{ena, uio_in, ui_in[7:2], 1'b0};

endmodule
