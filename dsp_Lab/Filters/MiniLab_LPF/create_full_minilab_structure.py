import os

# Base path for MiniLab_LPF
base_path = r"C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\dsp_Lab\Filters\MiniLab_LPF"

# Phase definitions: folder name, subfolder, file name, template content
phases = {
    "Phase1_SignalGeneration": {
        "subfolder": "plots",
        "file": "signal_gen.py",
        "content": """# Phase 1: Signal Generation - generate and visualize IQ signals
import numpy as np
import matplotlib.pyplot as plt

def generate_iq():
    pass

if __name__ == '__main__':
    generate_iq()
"""
    },
    "Phase2_FilterDesign": {
        "subfolder": "plots",
        "file": "fir_design.py",
        "content": """# Phase 2: FIR Filter Design - design and visualize LPF coefficients
import numpy as np
from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt

def design_lpf():
    pass

if __name__ == '__main__':
    design_lpf()
"""
    },
    "Phase3_FilteringAnalysis": {
        "subfolder": "plots",
        "file": "filtering.py",
        "content": """# Phase 3: Filtering and Analysis - apply LPF and analyze results
import numpy as np
from scipy.signal import lfilter, filtfilt
import matplotlib.pyplot as plt

def apply_filter():
    pass

if __name__ == '__main__':
    apply_filter()
"""
    },
    "Phase4_AdvancedExperiments": {
        "subfolder": "results",
        "file": "ber_simulation.py",
        "content": """# Phase 4: Advanced Experiments - QPSK/OFDM simulation and BER analysis
import numpy as np
import matplotlib.pyplot as plt

def ber_simulation():
    pass

if __name__ == '__main__':
    ber_simulation()
"""
    },
}

# Create folders, subfolders, and files
for phase, info in phases.items():
    folder_path = os.path.join(base_path, phase)
    subfolder_path = os.path.join(folder_path, info["subfolder"])
    os.makedirs(subfolder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, info["file"])
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(info["content"])
        print(f"Created {file_path}")
    else:
        print(f"Skipped (already exists): {file_path}")

print("\nMini-Lab folder structure is now fully ready!")
