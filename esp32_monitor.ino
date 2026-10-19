/*
  Smart Home Environmental Monitor — ESP32 firmware starter
  Example hardware: DHT22, analog air-quality module, SSD1306 OLED, LED, active buzzer.
  Validate pinout and voltage limits for your exact modules before wiring.
  MQ-135 output is treated as a relative ADC indicator, not a calibrated ppm or safety reading.
*/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>

#define DHT_PIN 4
#define DHT_TYPE DHT22
#define AIR_PIN 34       // ADC input-only pin on many ESP32 DevKit boards; verify board
#define LED_PIN 2        // Board LED varies by model; use external LED + resistor if needed
#define BUZZER_PIN 25    // Use transistor driver if buzzer current requires it

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define OLED_ADDR 0x3C

const float TEMP_LIMIT_C = 32.0;
const float HUMIDITY_LIMIT = 70.0;
const int AIR_RAW_LIMIT = 2200; // Placeholder only; calibrate for your module/board.

DHT dht(DHT_PIN, DHT_TYPE);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

unsigned long lastSampleMs = 0;
const unsigned long SAMPLE_INTERVAL_MS = 2500;

void setAlert(bool active) {
  digitalWrite(LED_PIN, active ? HIGH : LOW);
  digitalWrite(BUZZER_PIN, active ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  setAlert(false);

  dht.begin();
  Wire.begin(21, 22); // Common ESP32 I2C defaults; verify board wiring.

  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR)) {
    Serial.println("ERROR: OLED initialization failed. Check wiring/address.");
  } else {
    display.clearDisplay();
    display.setTextColor(SSD1306_WHITE);
    display.setTextSize(1);
    display.setCursor(0, 0);
    display.println("Environmental Monitor");
    display.println("Starting sensors...");
    display.display();
  }

  // ESP32 ADC range/attenuation varies by Arduino core and board.
  // Ensure AIR_PIN voltage is safe before sampling.
  analogReadResolution(12);
  analogSetPinAttenuation(AIR_PIN, ADC_11db);
  Serial.println("Boot complete. Readings will be reported over Serial.");
}

void loop() {
  unsigned long now = millis();
  if (now - lastSampleMs < SAMPLE_INTERVAL_MS) return;
  lastSampleMs = now;

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int airRaw = analogRead(AIR_PIN);

  bool dhtValid = !isnan(humidity) && !isnan(temperature);
  bool alert = false;
  if (dhtValid) {
    alert = (temperature >= TEMP_LIMIT_C) ||
            (humidity >= HUMIDITY_LIMIT);
  }
  alert = alert || (airRaw >= AIR_RAW_LIMIT); // Calibrate threshold before use.
  setAlert(alert);

  Serial.println("---- Measurement ----");
  if (dhtValid) {
    Serial.printf("Temperature: %.1f C\n", temperature);
    Serial.printf("Humidity: %.1f %%RH\n", humidity);
  } else {
    Serial.println("ERROR: DHT22 read failed");
  }
  Serial.printf("Air sensor raw ADC (relative): %d\n", airRaw);
  Serial.printf("Alert: %s\n", alert ? "ACTIVE" : "OFF");

  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(1);
  display.println("Env Monitor (ESP32)");
  if (dhtValid) {
    display.printf("Temp: %.1f C\n", temperature);
    display.printf("Humidity: %.1f %%\n", humidity);
  } else {
    display.println("DHT22 read ERROR");
  }
  display.printf("Air raw: %d\n", airRaw);
  display.printf("Status: %s\n", alert ? "ALERT" : "NORMAL");
  display.display();
}
