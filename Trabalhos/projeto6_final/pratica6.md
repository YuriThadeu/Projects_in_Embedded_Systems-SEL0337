# Sistemas de tempo real - RTOS

## Prática 6 - trabalhando com FreeRTOS com ESP32/STM32

### Autor(es)

- Yuri Thadeu Oliveira Costa
  - N° USP: 14754821
- Fabio Roberto Alcazar Frias Junior
  - N° USP: 14569060

***
***

### Resolução da Pratica
Nesta prática, foi desenvolvido um programa que implementa um simples RTOS. A ideia é fazer a aquisição de um sensor capacitivo embutido na ESP32 e, por meio de uma comunicação Bluetooth, enviar para um dispositivo móvel o estado do sensor capacitivo: pressionado ou não pressionado.

Foram criadas duas tasks com prioridades diferentes: a "taskTouch" e "taskBluetooth".

A "taskTouch" é responsável por fazer a aquisição dos valores do sensor capacitivo a cada 100 ms. Já a "taskBluetooth" habilita a comunicação Bluetooth do ESP32  e envia os dados de leitura da "taskTouch". No ranking de prioridades, a "taskTouch" tem prioridade 2 e a "taskBluetooth" tem prioridade 1.

O aplicativo de celular utilizado foi o Serial Bluetooth Terminal. Ao executar o código pelo Platform.io, o ESP32 já aparece como opção de conexão via Bluetooth no aplicativo. O app possui uma espécie de terminal, onde os valores lidos pelo sensor capacitivo são exibidos. 

Além do conceito de tasks, também foi utilizado o conceito de queue, que cria uma fila para a troca de mensagens ou dados entre tasks ou entre uma task e uma interrupção, permitindo sincronizar processos em um ambiente multitarefa. Nesse caso, os dados da task "taskTouch" são enviados para a task "taskBluetooth".
