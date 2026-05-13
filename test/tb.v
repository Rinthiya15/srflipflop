`default_nettype none
`timescale 1ns / 1ps

/* 
   Testbench for SR Flip-Flop
*/

module tb ();

  // Dump waveforms
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

  // Instantiate DUT
  tt_um_srflipfop user_project (

`ifdef GL_TEST
      .VPWR(VPWR),
      .VGND(VGND),
`endif

      .ui_in  (ui_in),
      .uo_out (uo_out),
      .uio_in (uio_in),
      .uio_out(uio_out),
      .uio_oe (uio_oe),
      .ena    (ena),
      .clk    (clk),
      .rst_n  (rst_n)
  );

  // Clock generation
  initial begin
    clk = 0;
    forever #5 clk = ~clk;   // 10ns clock period
  end

  // Test sequence
  initial begin

    // Initialize
    ena    = 1'b1;
    rst_n  = 1'b0;
    ui_in  = 8'b0;
    uio_in = 8'b0;

    // Apply reset
    #10;
    rst_n = 1'b1;

    // -------------------------
    // SR Flip-Flop Test Cases
    // -------------------------

    // Hold condition S=0 R=0
    ui_in[0] = 0; // S
    ui_in[1] = 0; // R
    #10;

    // Set condition S=1 R=0
    ui_in[0] = 1;
    ui_in[1] = 0;
    #10;

    // Hold condition
    ui_in[0] = 0;
    ui_in[1] = 0;
    #10;

    // Reset condition S=0 R=1
    ui_in[0] = 0;
    ui_in[1] = 1;
    #10;

    // Invalid condition S=1 R=1
    ui_in[0] = 1;
    ui_in[1] = 1;
    #10;

    // Finish simulation
    $finish;
  end

endmodule
