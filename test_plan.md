# Verification Test Plan

Record the date, setup, expected result, observed result, and pass/fail for each test. Leave observations blank until the test is actually performed.

| ID | Test | Procedure | Expected result | Actual result |
|---|---|---|---|---|
| T-01 | Desktop simulation starts | Run `python simulation/dashboard.py` | Window opens and values update | Not tested yet |
| T-02 | Simulation threshold alert | Click “Simulate threshold event” | Alert status changes visibly | Not tested yet |
| T-03 | Simulation pause/resume | Click Pause, wait, then Resume | Values stop and restart | Not tested yet |
| T-04 | DHT22 reading | Connect sensor and observe serial output | Valid temperature/humidity appear | Not tested yet |
| T-05 | DHT22 fault | Disconnect sensor safely while powered down, then restart | Firmware reports sensor read error | Not tested yet |
| T-06 | OLED | Connect display and start firmware | Values/status appear | Not tested yet |
| T-07 | Air-quality ADC | Verify voltage range, then observe raw ADC trend after warm-up | Raw trend is shown without overvoltage | Not tested yet |
| T-08 | Local alert | Use a safe test threshold or temporary test value | LED/buzzer activates at threshold | Not tested yet |
| T-09 | Wi-Fi-independent behavior | If Wi-Fi is later added, disable router | Local monitoring continues | Not implemented/tested yet |

## Evidence to collect
- Screenshot of the desktop simulation.
- Arduino IDE compile result and Serial Monitor screenshot.
- Photo of wiring and OLED output after actual hardware test.
- Write down actual results; do not mark tests as passed without evidence.
