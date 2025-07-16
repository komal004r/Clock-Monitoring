import matplotlib.pyplot as plt

times = []
ref_clk = []
clk = []
info_times = []
error_times = []

with open("op1.txt", "r", encoding="utf-8-sig") as f:
    for line in f:
        line = line.strip()

        # Skip headers, logs, or messages
        if not line or line.startswith("Time") or "Simulation" in line or "CLK HALTED" in line or "tb.v" in line:
            continue

        # Parse INFO and ERROR logs
        if "[INFO]" in line:
            if "time" in line:
                try:
                    info_times.append(int(line.split("at time")[-1].strip()))
                except ValueError:
                    pass
            continue

        if "[ERROR]" in line:
            if "time" in line:
                try:
                    error_times.append(int(line.split("at time")[-1].strip()))
                except ValueError:
                    pass
            continue

        # Parse clock values only if all are integers
        tokens = line.split()
        if len(tokens) == 3:
            try:
                t, r, c = int(tokens[0]), int(tokens[1]), int(tokens[2])
                times.append(t)
                ref_clk.append(r)
                clk.append(c)
            except ValueError:
                continue

'''with open("output.txt", "r") as f:
    for line in f:
        if line.startswith("Time") or line.startswith("Simulation"):
            continue

        if "[INFO]" in line:
            parts = line.split("at time")
            if len(parts) == 2:
                info_times.append(int(parts[1].strip()))
        elif "[ERROR]" in line:
            parts = line.split("at time")
            if len(parts) == 2:
                error_times.append(int(parts[1].strip()))
        else:
            tokens = line.strip().split()
            if len(tokens) == 3:
                try:
                    t, r, c = int(tokens[0]), int(tokens[1]), int(tokens[2])
                    times.append(t)
                    ref_clk.append(r)
                    clk.append(c)
                except ValueError:
                    continue  # skip corrupted or non-numeric lines'''

# Plot
'''plt.figure(figsize=(12, 5))
plt.step(times, clk, label="clk", where="post", color="blue")
plt.step(times, ref_clk, label="ref_clk", where="post", color="green")

# Add event markers
for t in info_times:
    plt.axvline(t, color='cyan', linestyle='--', label='INFO OK' if t == info_times[0] else "")
for t in error_times:
    plt.axvline(t, color='red', linestyle='--', label='HALT ERROR' if t == error_times[0] else "")

plt.title("Mission-Critical Clock Monitor Visualization")
plt.xlabel("Time")
plt.ylabel("Signal Level")
plt.yticks([0, 1])
plt.grid(True)
plt.legend()
plt.xlim(min(times), max(times))       # Show full time range
plt.xticks(range(min(times), max(times)+1, 10))  # Show ticks every 10 units

plt.tight_layout()
plt.show()
'''

print(f"Times parsed: {len(times)}")
print(f"Max time: {max(times) if times else 'N/A'}")

# Plot only if there is timing data
if times:
    plt.figure(figsize=(12, 5))
    plt.step(times, clk, label="clk", where="post", color="blue")
    plt.step(times, ref_clk, label="ref_clk", where="post", color="green")

    for t in info_times:
        plt.axvline(t, color='cyan', linestyle='--', label='INFO OK' if t == info_times[0] else "")
    for t in error_times:
        plt.axvline(t, color='red', linestyle='--', label='HALT ERROR' if t == error_times[0] else "")

    plt.title("Mission-Critical Clock Monitor Visualization")
    plt.xlabel("Time")
    plt.ylabel("Signal Level")
    plt.yticks([0, 1])
    plt.grid(True)
    plt.legend()

    # ✅ Safely add time limits
    plt.xlim(min(times), max(times))
    plt.xticks(range(min(times), max(times)+1, 10))

    plt.tight_layout()
    plt.show()
else:
    print("❌ No valid timing data found. Check your output.txt formatting.")