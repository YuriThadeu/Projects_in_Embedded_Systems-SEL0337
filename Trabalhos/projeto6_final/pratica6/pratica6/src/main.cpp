#include <Arduino.h>
#include "BluetoothSerial.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"

#define TOUCH_THRESHOLD  20       // Ajuste conforme o hardware

BluetoothSerial SerialBT;
QueueHandle_t touchQueue;

typedef struct {
    uint16_t valor;
    uint8_t tocado;   // 0 = LIVRE | 1 = TOCADO
} TouchData;

void taskTouch(void *pvParameters) {
    TouchData data;

    while (true) {
        data.valor  = touchRead(13);
        data.tocado = (data.valor < TOUCH_THRESHOLD) ? 1 : 0;

        xQueueSend(touchQueue, &data, portMAX_DELAY);

        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

void taskBluetooth(void *pvParameters) {
    TouchData recebido;

    SerialBT.begin("ESP32_Touch_RTOS");
    Serial.println("Bluetooth iniciado");

    while (true) {
        if (xQueueReceive(touchQueue, &recebido, portMAX_DELAY) == pdTRUE) {
            SerialBT.print("Valor Touch: ");
            SerialBT.print(recebido.valor);
            SerialBT.print(" | Estado: ");
            SerialBT.println(recebido.tocado ? "TOCADO" : "LIVRE");
        }
    }
}

void setup() {
    Serial.begin(115200);
    delay(1000);

    Serial.println("Sistema iniciado");

    touchQueue = xQueueCreate(5, sizeof(TouchData));
    if (touchQueue == NULL) {
        Serial.println("Erro ao criar a fila");
        while (true);
    }

    xTaskCreate(taskTouch, "TaskTouch", 2048, nullptr, 2, nullptr);

    xTaskCreate(taskBluetooth, "TaskBluetooth", 4096, nullptr, 1, nullptr);
}

void loop() {
}
