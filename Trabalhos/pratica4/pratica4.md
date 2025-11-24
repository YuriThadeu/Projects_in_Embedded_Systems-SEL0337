# SBC, GPIO, Python, Protocolos, GitHub e APIs

## Prática 4 - Introdução ao uso de protocolos de comunicação na Raspberry Pi

### Autor(es)

- Yuri Thadeu Oliveira Costa
  - N° USP: 14754821
- Fabio Roberto Alcazar Frias Junior
  - N° USP: 14569060

***
***

### Guia da Prática

Essa prática teve como objetivo implementar uma comunicação serial entre um Arduino UNO e uma Raspberry Pi 3 B+. Será feita a leitura de um valor analógico de um potenciômetro conectado ao Arduino, que deverá enviar essa informação para a Raspberry Pi via comunicação serial I2C.

### Resolução da Pratica

Em um primeiro momento, foi realizada a montagem dos componentes eletrônicos. Vale ressaltar que o Arduino opera com uma tensão de 0 V a 5 V em seus GPIOs, enquanto a Raspberry Pi 3 opera com uma tensão de 0 V a 3.3 V, sendo necessário um módulo level shifter para realizar a conexão entre os pinos. A montagem pode ser vista na ![figura 1](https://github.com/fabiooju/Projects_in_Embedded_Systems-SEL0337/blob/develop/Trabalhos/pratica4/comunicacao_i2c_arduino/montagem_componentes.jpg)

Depois disso, foi desenvolvido um código para realizar a leitura analógica de um potenciômetro conectado ao Arduino. Este código foi validado separadamente ao de comunicação serial para evitar possíveis erros. Ademais, a comunicação serial foi validada usando um código de exemplo fornecido no roteiro da prática.

Por fim, foi desenvolvido um código em Python para que a Raspberry Pi pudesse ler o valor da leitura analógica do potenciômetro proveniente dpo Arduino.

Vale ressaltar que a resolução do conversor AD do Arduino é de 10 bits, porém o barramento do I2C possui largura de 8 bits, ou seja, é necessário fazer uma conversão dos valores.

Por fim, foi possível validar o funcionamento do projeto pelo print dos valores de leitura do potenciômetro via terminal da Raspberry Pi, que pode ser vista no ! [Video 1](https://github.com/fabiooju/Projects_in_Embedded_Systems-SEL0337/blob/develop/Trabalhos/pratica4/comunicacao_i2c_arduino/video_resposta_terminal.mp4).