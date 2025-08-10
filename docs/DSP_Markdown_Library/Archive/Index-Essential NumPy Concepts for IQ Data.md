### Essential NumPy Concepts for IQ Data and SDR

1. **Array creation & data types**

   * Creating arrays (`np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`)
   * Understanding data types (`dtype`), especially complex types (`np.complex64`, `np.complex128`)

2. **Indexing & slicing**

   * Basic and advanced indexing (integer, boolean, fancy)
   * Negative indexing and step slicing
   * Multi-dimensional slicing

3. **Broadcasting**

   * Rules and examples (including `np.newaxis`)
   * Practical use cases in signal scaling, mixing, filtering

4. **Memory views and copies**

   * Difference between views and copies
   * How slicing returns views
   * Impact on memory and performance

5. **Array reshaping and dimension manipulation**

   * `reshape()`, `ravel()`, `flatten()`
   * `transpose()`, `swapaxes()`
   * `expand_dims()`, `squeeze()`

6. **Vectorized operations**

   * Arithmetic on arrays without loops
   * Applying mathematical functions element-wise (`np.sin`, `np.abs`, etc.)

7. **Complex number operations**

   * Handling IQ data as complex arrays
   * Extracting real, imaginary, magnitude, phase (`np.real`, `np.imag`, `np.abs`, `np.angle`)

8. **Statistical and aggregation functions**

   * `mean()`, `std()`, `sum()`, `max()`, `min()`
   * Along axes for multi-dimensional data

9. **File I/O with NumPy**

   * Saving and loading arrays (`np.save`, `np.load`, `np.fromfile`)
   * Working with raw IQ data files

10. **Linear algebra basics**

    * Dot products, matrix multiplication (`np.dot`, `@` operator)
    * Useful for MIMO SDR processing or beamforming

11. **Fast Fourier Transform (FFT) basics**

    * `np.fft.fft`, `np.fft.ifft`, frequency bins understanding
    * Windowing and zero-padding (prepare for spectral analysis)

12. **Masking and filtering**

    * Boolean masks to select data
    * Applying filters or thresholding

---

