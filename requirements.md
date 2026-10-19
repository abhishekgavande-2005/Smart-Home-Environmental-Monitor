# System Requirements — Smart Home Environmental Monitoring System

## 1. Purpose
Monitor indoor temperature and relative humidity, observe a broad analog air-quality sensor response, provide local status/alerts, and support later wireless reporting.

## 2. Functional requirements
- FR-01: Read temperature and humidity from a DHT22 at approximately 2-second intervals.
- FR-02: Sample the analog air-quality module and display a relative raw/normalized indicator after warm-up and calibration.
- FR-03: Display values and status on an I2C OLED.
- FR-04: Compare valid measurements with configurable thresholds and drive an LED/buzzer alert.
- FR-05: Report invalid sensor reads as faults rather than silently showing them as valid.
- FR-06: Keep local sensing and alerts independent from Wi-Fi availability.
- FR-07: A future extension may publish readings to a dashboard over Wi-Fi.

## 3. Non-functional requirements
- Local values refresh within approximately 2–3 seconds during normal operation.
- Alert logic reacts within 3 seconds after the firmware has a valid threshold-violating reading; sensor physical response time is separate.
- Firmware avoids long blocking delays for routine tasks.
- Components and software modules are separated for maintainability.
- Power comes from a stable USB supply during prototyping.
- Credentials must not be committed to a public repository.

## 4. Interfaces
- DHT22: digital single-wire interface, example DATA pin GPIO 4.
- MQ-135 module: analog output to an ESP32 ADC-capable input, example GPIO 34; verify voltage compatibility and condition the signal if needed.
- SSD1306 OLED: I2C, example SDA GPIO 21 and SCL GPIO 22.
- LED: GPIO output with current-limiting resistor, example GPIO 2 where suitable.
- Active buzzer: GPIO control via a transistor driver when required, example GPIO 25.
- Power: USB 5 V input to ESP32 board regulator; check module-specific supply requirements.

## 5. Constraints and safety
The MQ-135 is a broad-response sensor affected by warm-up, humidity, temperature, and calibration. It is not a certified CO, smoke, or combustible-gas alarm. Never use this prototype for life-safety decisions. Never expose an ESP32 ADC pin to a voltage above its permitted range.
