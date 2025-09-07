@echo off
REM Base path - adjust if needed
SET BASE_PATH=C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\dsp_Lab\Filters\MiniLab_LPF

REM Phase 1: Signal Generation
IF NOT EXIST "%BASE_PATH%\Phase1_SignalGeneration\signal_gen.py" (
    echo # Phase 1: Signal Generation - generate and visualize IQ signals > "%BASE_PATH%\Phase1_SignalGeneration\signal_gen.py"
)

REM Phase 2: FIR Filter Design
IF NOT EXIST "%BASE_PATH%\Phase2_FilterDesign\fir_design.py" (
    echo # Phase 2: FIR Filter Design - design and visualize LPF coefficients > "%BASE_PATH%\Phase2_FilterDesign\fir_design.py"
)

REM Phase 3: Filtering and Analysis
IF NOT EXIST "%BASE_PATH%\Phase3_FilteringAnalysis\filtering.py" (
    echo # Phase 3: Filtering and Analysis - apply LPF and analyze results > "%BASE_PATH%\Phase3_FilteringAnalysis\filtering.py"
)

REM Phase 4: Advanced Experiments
IF NOT EXIST "%BASE_PATH%\Phase4_AdvancedExperiments\ber_simulation.py" (
    echo # Phase 4: Advanced Experiments - QPSK/OFDM simulation and BER analysis > "%BASE_PATH%\Phase4_AdvancedExperiments\ber_simulation.py"
)

echo Empty Python files with headers created successfully.
pause
