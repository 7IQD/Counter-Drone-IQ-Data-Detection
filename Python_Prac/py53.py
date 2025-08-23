import numpy as np

filename = r"C:\IQ_Data\Prac_1.bin"
raw = np.fromfile(filename, dtype=np.uint8)
print("Captured Raw Data:", raw)
Replay_1 = np.copy(raw, order="K")

out_filename = r"C:\IQ_Data\Replay_1.bin"
Replay_1.tofile(out_filename)
print(f"Replay file written to: {out_filename}")

reloaded =  np.fromfile(out_filename, dtype=np.uint8)
if np.array_equal(raw, reloaded):
    print("✅ SUCCESS: Replay file matches the original")
else:
    print("❌ ERROR: Files differ")