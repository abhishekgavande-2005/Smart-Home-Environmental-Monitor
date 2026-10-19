# Smart Home Environmental Monitoring System

Week 1 internship project: system requirements analysis, block diagram, software simulation, and ESP32 firmware starter.

## Features
- Temperature and relative-humidity monitoring interface
- Simulated air-quality index for desktop demonstration
- Configurable thresholds and visual alerts
- ESP32 firmware starter for DHT22 + analog air-quality module + I2C OLED + buzzer/LED
- Requirements, architecture, and test plan

> **Important:** The desktop simulation generates synthetic values. It is not reading physical sensors. The firmware is a starter and must be compiled, wired, and tested on the actual board before reporting hardware results. The MQ-135 is not a certified safety detector.

## Project layout
- `simulation/dashboard.py` — desktop dashboard simulation (Python standard library / Tkinter)
- `firmware/esp32_monitor/esp32_monitor.ino` — ESP32 Arduino firmware starter
- `docs/block_diagram.png` — system architecture
- `docs/requirements.md` — requirements and interfaces
- `tests/test_plan.md` — verification plan

## Run the desktop simulation (Windows 11)
1. Install Python 3 if needed. During installation, enable **Add Python to PATH**.
2. Extract this repository folder.
3. Open Command Prompt in the project folder.
4. Run:
   ```bat
   python simulation\dashboard.py
   ```
5. Use **Simulate threshold event** to demonstrate an alert and **Pause/Resume** to stop/start updates.

Tkinter is usually included with the standard Windows Python installer. No `pip install` is required.

## Hardware plan
Parts: ESP32 development board, DHT22, MQ-135 module (optional and only for relative trend indication), I2C SSD1306 OLED, LED + resistor, optional active buzzer, stable USB supply.

Example ESP32 pin plan (verify your exact board/module):
- DHT22 DATA -> GPIO 4 (use pull-up if required by sensor module)
- MQ-135 AO -> GPIO 34 through safe signal conditioning; ensure ADC voltage never exceeds the ESP32's allowed input range
- OLED SDA -> GPIO 21, SCL -> GPIO 22 (common ESP32 DevKit defaults)
- LED -> GPIO 2 through suitable resistor (board LED polarity varies)
- Active buzzer driver input -> GPIO 25; use a transistor driver if current exceeds GPIO capability
- All signal grounds common where required

Do not power a high-current load from a GPIO. Confirm each module's voltage requirements and pinout.

## Arduino IDE setup
1. Install Arduino IDE and the Espressif ESP32 board package.
2. Install libraries: **DHT sensor library by Adafruit**, **Adafruit Unified Sensor**, and **Adafruit SSD1306**.
3. Select the correct ESP32 board and COM port.
4. Review pins and module voltage compatibility before wiring.
5. Compile and upload `firmware/esp32_monitor/esp32_monitor.ino`.
6. Open Serial Monitor at 115200 baud and compare serial readings with the OLED.
7. Record genuine test observations in `tests/test_plan.md`.

## GitHub submission
Create a public repository named `Smart-Home-Environmental-Monitor`, then upload these files. In the internship form, paste the actual repository URL, for example `https://github.com/YOUR-USERNAME/Smart-Home-Environmental-Monitor` after replacing the placeholder with your username. Do not submit the example URL unchanged.

## Honest reporting
This repository contains a proposed architecture, a desktop simulation, and firmware starter code. Describe only the work you have actually run and verified. Do not claim that physical sensors, Wi-Fi dashboard publishing, or hardware tests work until you have tested them.
