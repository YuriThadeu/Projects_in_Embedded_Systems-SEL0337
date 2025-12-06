# Desenvolvimento de Linux embarcado

## Prática 5 - Init System, SystemD e Unit Files para serviços personalizados em Linux embarcado

### Autor(es)

- Yuri Thadeu Oliveira Costa
  - N° USP: 14754821
- Fabio Roberto Alcazar Frias Junior
  - N° USP: 14569060

***
***

### Guia da Prática

####

***
***

### Resolução da Pratica


para instalar a camera usei 

```sh
sudo apt update
sudo apt install libcamera-apps
```


como não deu certo a camera, adaptei uma webcam usb. usei o ls /dev/video* para ver se ela apareceu e usei o "sudo apt install fswebcam" e depois "ffplay /dev/video0" para testar a camera e ver o video em tempo real, e funcionou.  