import winsound
import time

# Define sounds
def short_beep():
    winsound.Beep(1000, 200)  # short OK beep

def long_beep():
    winsound.Beep(600, 700)   # long warning beep

# Read simulation log
with open("output.txt", "r", encoding="latin1") as f:
    for line in f:
        line = line.strip()

        if "[INFO]" in line:
            print("✅ OK:", line)
            short_beep()
            time.sleep(0.1)

        elif "[ERROR]" in line or "HALTED" in line:
            print("⚠️  Issue:", line)
            long_beep()
            time.sleep(0.5)

# ✅ Wait at end so user hears final sounds
input("\n🎧 Done. Press Enter to exit...")
