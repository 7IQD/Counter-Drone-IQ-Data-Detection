import json
import os

# Metadata values
fs = 20000           # Sample rate
fc = 1e6             # Center frequency
description = "Hello World IQ snippet for filtering demo"

meta = {
    "global": {
        "core:datatype": "cf32_le",       # complex float32, little-endian
        "core:sample_rate": fs,
        "core:description": description,
        "core:center_freq": fc
    },
    "captures": [
        {
            "core:sample_start": 0,
            "core:frequency": fc
        }
    ]
}
# Save in same folder as hello.iq
folder = os.getcwd()  # C:\Users\Ani
meta_file = os.path.join(folder, 'hello.sigmf-meta')

with open(meta_file, 'w') as f:
    json.dump(meta, f, indent=4)

print("Metadata file created at:", meta_file)