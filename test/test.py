`default_nettype none
`timescale 1ns / 1ps

/*
 * Testbench for SR Flip-Flop (Tiny Tapeout)
 */

module tb;

  // Dump waveform
  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
  end

  // Inputs
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  // Outputs
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

`ifdef GL_TEST
  wire VPWR = 1'b1;
  wire VGND = 1'b0;
`endif

  // DUT Instantiation
  tt_um_srflipflop dut (

`ifdef GL_TEST
      .VPWR(VPWR),
      .VGND(VGND),
`endif

      .ui_in(ui_in),
      .uo_out(uo_out),
      .uio_in(uio_in),
      .uio_out(uio_out),
      .uio_oe(uio_oe),
      .ena(ena),
      .clk(clk),
      .rst_n(rst_n)
  );

  // Clock generation
  initial begin
    clk = 0;
    forever #5 clk = ~clk;
  end

  // Stimulus
  initial begin

    // Initialize signals
    ena    = 1'b1;
    rst_n  = 1'b0;
    ui_in  = 8'b0;
    uio_in = 8'b0;

    // Reset
    #10;
    rst_n = 1'b1;

    // -------------------
    // SR Flip-Flop Tests
    // -------------------

    // HOLD : S=0 R=0
    ui_in[0] = 0;   // S
    ui_in[1] = 0;   // R
    #10;
    $display("HOLD  : Q = %b", uo_out[0]);

    // SET : S=1 R=0
    ui_in[0] = 1;
    ui_in[1] = 0;
    #10;
    $display("SET   : Q = %b", uo_out[0]);

    // HOLD after SET
    ui_in[0] = 0;
    ui_in[1] = 0;
    #10;
    $display("HOLD  : Q = %b", uo_out[0]);

    // RESET : S=0 R=1
    ui_in[0] = 0;
    ui_in[1] = 1;
    #10;
    $display("RESET : Q = %b", uo_out[0]);

    // INVALID : S=1 R=1
    ui_in[0] = 1;
    ui_in[1] = 1;
    #10;
    $display("INVALID : Q = %b", uo_out[0]);

    // End simulation
    #10;
    $finish;
  end

endmodule
