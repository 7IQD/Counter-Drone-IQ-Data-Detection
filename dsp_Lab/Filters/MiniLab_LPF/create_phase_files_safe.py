import os

# Base path for your MiniLab_LPF folder
base_path = r"C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\dsp_Lab\Filters\MiniLab_LPF"

# Phase folders, file names, and content
phase_files = {
    "Phase1_SignalGeneration": ("signal_gen.py",
        "# Phase 1: Signal Generation - generate and visualize IQ signals\n"
        "import numpy as np\nimport matplotlib.pyplot as plt\n\n"
        "def generate_iq():\n    pass\n\n"
        "if __name__ == '__main__':\n    generate_iq()"
    ),
    "Phase2_FilterDesign": ("fir_design.py",
        "# Phase 2: FIR Filter Design - design and visualize LPF coefficients\n"
        "import numpy as np\nfrom scipy.signal import firwin, freqz\nimport matplotlib.pyplot as plt\n\n"
        "def design_lpf():\n    pass\n\n"
        "if __name__ == '__main__':\n    design_lpf()"
    ),
    "Phase3_FilteringAnalysis": ("filtering.py",
        "# Phase 3: Filtering and Analysis - apply LPF and analyze results\n"
        "import numpy as np\nfrom scipy.signal import lfilter, filtfilt\nimport matplotlib.pyplot as plt\n\n"
        "def apply_filter():\n    pass\n\n"
        "if __name__ == '__main__':\n    apply_filter()"
    ),
    "Phase4_AdvancedExperiments": ("ber_simulation.py",
        "# Phase 4: Advanced Experiments - QPSK/OFDM simulation and BER analysis\n"
        "import numpy as np\nimport matplotlib.pyplot as plt\n\n"
        "def ber_simulation():\n    pass\n\n"
        "if __name__ == '__main__':\n    ber_simulation()"
    ),
}

# Create folders and files
for phase, (filename, content) in phase_files.items():
    folder_path = os.path.join(base_path, phase)
    os.makedirs(folder_path, exist_ok=True)  # create folder if missing
    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created {file_path}")
    else:
        print(f"Skipped (already exists): {file_path}")
