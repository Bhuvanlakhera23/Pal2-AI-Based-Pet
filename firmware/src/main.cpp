#include <Arduino.h>
#include <driver/i2s.h>

void setup() {
  Serial.begin(115200);
  while (!Serial);  // Wait for Serial Monitor
  Serial.println("Setup started");

  // I2S (PDM Mic) configuration
  i2s_config_t i2s_config = {
    .mode = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX | I2S_MODE_PDM),
    .sample_rate = 16000,
    .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT,
    .channel_format = I2S_CHANNEL_FMT_ONLY_LEFT,
    .communication_format = I2S_COMM_FORMAT_STAND_I2S,
    .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1,
    .dma_buf_count = 4,
    .dma_buf_len = 256,
    .use_apll = false,
    .tx_desc_auto_clear = false,
    .fixed_mclk = 0
  };

  i2s_pin_config_t pin_config = {
    .bck_io_num = I2S_PIN_NO_CHANGE,   // Not used in PDM
    .ws_io_num = 42,                   // CLK
    .data_out_num = I2S_PIN_NO_CHANGE,
    .data_in_num = 41                  // DATA
  };

  esp_err_t err;
  err = i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  if (err != ESP_OK) {
    Serial.println("I2S install failed!");
    return;
  }

  err = i2s_set_pin(I2S_NUM_0, &pin_config);
  if (err != ESP_OK) {
    Serial.println("I2S set pin failed!");
    return;
  }

  Serial.println("I2S Mic initialized.");
}

void loop() {
  static int16_t samples[256];
  size_t bytes_read;

  esp_err_t result = i2s_read(I2S_NUM_0, samples, sizeof(samples), &bytes_read, portMAX_DELAY);
  if (result == ESP_OK && bytes_read > 0) {
    for (int i = 0; i < bytes_read / 2; ++i) {
      Serial.println(samples[i]);
    }
  }
}
