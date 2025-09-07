# MiniLab_LPF — Exercises Index

This index tracks all exercises across **Phase 1–4**.  
Each task links back to the relevant script (in `exercises/`) or notes.  
Mark checkboxes ✅ as you complete them.

---

## Phase 1 — Signal Generation & Noise

- [ ] **SNR Sweep** → `exercises/exercises_phase1.py`
  - IQ with SNR = [0, 10, 20, 30, 40] dB
  - PSD comparison (noise floor rises)
- [ ] **Duration Sweep**
  - Durations = [0.005, 0.01, 0.05] s
  - Longer = better FFT resolution
- [ ] **Frequency Sweep**
  - f = [500, 1000, 2000] Hz
  - PSD peak shifts correctly
- [ ] **Selective Noise (I-only vs Q-only)**
  - Add Gaussian noise to only I, then only Q
  - Compare PSD & time waveforms

---

## Phase 2 — FIR Low-Pass Filter Design

- [ ] **Filter Order Variation** → `exercises/exercises_phase2.py`
  - Orders = [31, 63, 127]
  - Compare transition width & stopband
- [ ] **Cutoff Frequency Experiment**
  - Cutoff = [0.1, 0.2, 0.3] × Nyquist
  - Bandwidth tradeoffs

---

## Phase 3 — Filtering & Analysis

- [ ] **lfilter vs filtfilt** → `exercises/exercises_phase3.py`
  - Compare delay & artifacts
- [ ] **SNR Before vs After Filtering**
  - Measure improvement in-band
- [ ] **Group Delay Measurement**
  - Expect ≈ N/2 for FIR
- [ ] **Attenuation Measurement**
  - Stopband attenuation via `20*log10(|H(f)|)`

---

## Phase 4 — Advanced / Optional

- [ ] **QPSK Symbol Filtering** → `exercises/exercises_phase4.py`
  - Constellation before/after
- [ ] **BER vs SNR Curve**
  - Sweep SNR, plot BER vs theory
- [ ] **Real SDR Data Test** (optional)
  - RTL-SDR/HackRF capture
- [ ] **Reproducibility Checklist**
  - Save params, seeds, coeffs, results

---

👉 These **14 exercises** form the complete **MiniLab_LPF training pipeline**.  
Keep results (plots, notes) in the `exercises/plots/` folder.

```

---

### Folder Structure Recap

```
MiniLab_LPF/
├── Phase1_SignalGeneration/
├── Phase2_FilterDesign/
├── Phase3_FilteringAnalysis/
├── Phase4_Advanced/
├── exercises/                     # all exercise scripts
│   ├── exercises_phase1.py
│   ├── exercises_phase2.py
│   ├── exercises_phase3.py
│   ├── exercises_phase4.py
│   └── plots/
├── docs/
│   ├── Phase1_notes.md
│   ├── Phase2_notes.md
│   ├── Phase3_notes.md
│   ├── Phase4_notes.md
│   └── Exercises_index.md   ✅
└── README.md
```

---

