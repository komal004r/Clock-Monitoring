module clock_monitor_counter #(parameter MAX_WAIT = 50, parameter MIN_WAIT = 3)(
    input wire clk,
    input wire ref_clk
);

  reg last_clk_state = 0;
  integer counter = 0;

  always @(posedge ref_clk) begin
    counter = counter + 1;

    if (clk !== last_clk_state) begin
      if (counter < MIN_WAIT) begin
        $display("[ERROR] Clock glitch! Too fast at time %0t", $time);
      end
      else if (counter > MAX_WAIT) begin
        $display("[ERROR] Clock halted or too slow at time %0t", $time);
      end
      else begin
        $display("[INFO] Clock OK, Edge seen after %0d cycles at time %0t", counter, $time);
      end

      last_clk_state = clk;
      counter = 0;  // Reset the counter after detecting a change
    end
  end

endmodule
