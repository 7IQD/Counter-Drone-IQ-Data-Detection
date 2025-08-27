import numpy as np
import os

def read_iq_file(filename, dtype=np.uint8, root_dir=None):
    """
    Reads raw IQ data from binary file and returns normalized complex samples.
    """
    if dtype not in [np.int8, np.uint8]:
        raise ValueError("Only int8 or uint8 raw files are supported")
    
    # Step 0: Resolve path
    if root_dir is None:
        script_dir = os.path.dirname(__file__)
        root_dir = os.path.join(script_dir, "data")
    
    filepath = os.path.join(root_dir, filename)
    
    # Step 1: Load raw data
    raw = np.fromfile(filepath, dtype=dtype)
        
    #Step 3. Split into I and Q
    I = raw[0::2].astype(np.float32)
    Q = raw[1::2].astype(np.float32)

    # Step 4: Normalize
    if dtype == np.uint8:
        I = (I - 127.5) / 127.5
        Q = (Q - 127.5) / 127.5
    else:  # int8 case (-128..127)
        I /= 128.0
        Q /= 128.0

    # Step 5. Form complex signal
    iq = I + 1j * Q
    return iq
