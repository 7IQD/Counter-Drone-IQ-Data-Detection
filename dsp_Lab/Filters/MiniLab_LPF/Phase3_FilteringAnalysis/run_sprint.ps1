Write-Host "---------------------------------"
Write-Host "Starting IQ Signal Detection Sprint"
Write-Host "---------------------------------"

python iq_signal_detection.py | Tee-Object -FilePath logs\sprint_output.txt

Write-Host "---------------------------------"
Write-Host "Sprint Completed. Logs saved to logs\sprint_output.txt"
Write-Host "---------------------------------"
