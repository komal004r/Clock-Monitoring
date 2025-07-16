# Clock-Monitoring

# ⏱ Mission-Critical Clock Monitor

A Verilog-based clock integrity checker designed to simulate, monitor, and validate clock behavior in **SoC-level digital verification environments**. It detects **glitches**, **halts**, and **unexpected transitions**, enhancing simulation observability using **graphical plots** and **audio alerts**.



## 📂 Repository Structure

```

.
├── clock\_monitor.v         # Main Verilog module (checker)
├── tb.v                    # Testbench injecting glitch/halt behavior
├── output.txt              # Simulation output file (time, clk, ref\_clk, logs)
├── graph\_plot.py           # Python script for plotting waveform
├── sound\_alert.py          # Python script for generating beeps on events
├── graph\_screenshot.png    # Captured waveform (optional for GitHub preview)
├── README.md               # You are here!

````

---

## 💡 Features

- 🧠 **Clock Glitch Detection**: Identifies unstable or rapid transitions beyond acceptable edge patterns.
- ❌ **Halt Identification**: Flags when the monitored clock stops toggling for extended cycles.
- 📊 **Python Visualization**: Plots `clk` and `ref_clk` waveform with color-coded event markers (INFO/ERROR).
- 🔉 **Audio Alerts**:
  - ✅ Short beep for stable transitions (`[INFO]`)
  - ⚠️ Long beep for glitches or halts (`[ERROR]` / HALTED)

---

## ⚙️ How It Works

1. The **Verilog testbench (`tb.v`)** simulates a clock with regular, glitchy, and halted phases.
2. Output (time, reference clock, clock, and log messages) is stored in `output.txt`.
3. The **Python scripts**:
   - `python.py`: Parses `output.txt` and draws a **step plot** of signal activity, showing when and where faults occur.
   - `sound_alert.py`: Reads the same file and triggers **beep sounds** based on event type.

---

## 🖼 Preview

![Waveform Screenshot](graph_screenshot.png)

> The graph above displays correct and faulty clock behavior:
> - 🟦 Blue = `clk`
> - 🟩 Green = `ref_clk`

## 🚀 To Run

1. **Simulate Verilog Code**  
   Use any Verilog simulator like `iverilog` or ModelSim to compile and run:

   ```bash
   iverilog -o monitor tb.v clock_monitor.v
   vvp monitor > output.txt
````

2. **Generate Graph**

   ```bash
   python python.py
   ```

3. **Play Sound Alerts**

   ```bash
   python sound_alert.py
   ```

   > ⚠️ Sound script uses `winsound` (Windows-only). Modify for cross-platform use if needed.



## 🛠 Tools & Tech

* Verilog HDL
* Python 3 (`matplotlib`, `winsound`)
* Digital Simulation (tested on Icarus Verilog)
* SoC DV context


## 📌 Applications

* SoC Verification (DV)
* Clock integrity testing
* Simulation automation tools
* Debugging digital timing errors

## 🧑‍💻 Author

Developed by [Komal Sharma](https://github.com/your-profile)
B.Tech in Electronics and IoT (EIOT), NSUT, Delhi

