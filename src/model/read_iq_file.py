import numpy as np
import os

def read_iq_file(filename, dtype=np.int8, root_dir=None):
    """
    Reads raw IQ data from binary file and returns normalized complex samples.

    Parameters
    ----------
    filename : str
        Path to the raw IQ file
    dtype : numpy dtype, optional
        Data type of samples in file (default = np.int8 for RTL-SDR)

    Returns
    -------
    iq : np.ndarray (complex64)
        Normalized complex IQ samples in range [-1, 1]
    """
    if dtype not in [np.int8, np.uint8]:  # restrict allowed types
        raise ValueError("Only int8 or uint8 raw files are supported")
    
    # Step 0: Build absolute path if root_dir is provided
    if root_dir:
        filename = os.path.join(root_dir, filename)

    # Step 1. Check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    
    # 1. Load raw data
    raw = np.fromfile(filename, dtype=dtype)
    # Split into I and Q
    I = raw[0::2].astype(np.float32) - 127.5
    Q = raw[1::2].astype(np.float32) - 127.5

    # Normalize
    I /= 127.5
    Q /= 127.5

    # Form complex signal
    iq = I + 1j*Q
    return iq

