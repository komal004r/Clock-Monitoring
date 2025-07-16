module tb;

  reg clk = 0;
  reg ref_clk = 0;
  reg clk_enable = 1;
  reg [31:0] counter = 0;

  // Instantiate the DUT (Device Under Test)
  clock_monitor_counter uut (.clk(clk), .ref_clk(ref_clk));

  // Generate clocks
  always #10 if (clk_enable) clk = ~clk;    // Main clock (standard)
  always #1 ref_clk = ~ref_clk;             // Reference clock

  // Glitchy behavior — toggles clk irregularly based on counter
  always @(posedge ref_clk) begin
    if (clk_enable) begin
      counter <= counter + 1;
      if (counter % 2 == 0)  // Glitch-like toggle every 2 cycles
        clk <= ~clk;
    end
  end

  initial begin
  clk_enable = 1;
  #100;
  clk_enable = 0;
  $display("CLK HALTED at time %0t", $time);
  #40;
  clk_enable = 1;
  $display("CLK RESUMED at time %0t", $time);
end


  // Display waveforms and timing
  initial begin
    $display("Time\tref_clk\tclk");
    $monitor("%0t\t%b\t%b", $time, ref_clk, clk);
  end

  // Simulation flow control
  initial begin
    $display("Simulation started");
    #200;
    $finish;
  end

endmodule
