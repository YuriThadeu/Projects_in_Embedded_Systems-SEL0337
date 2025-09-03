# Sistemas Operacionais e Ambiente Linux

## Prática 2 - Instalação e preparação do S.O. na Raspberry Pi

### Autor(es)

- Yuri Thadeu Oliveira Costa  
  - N° USP: 14754821

***

### Guia da Prática

#### Resumo

Introdução ao uso de instaladores de distribuições Linux, como o Debian Installer (uma versão derivada dele é utilizada no instalador do Raspberry Pi OS), configurações iniciais após instalação do sistema operacional, configuração do usuário root, conexão à internet, ativação do SSH, ativação dos drivers da câmera.

#### Conceitos importantes

- Debian-installer, SSH, Embedded OS, Embedded Linux, Init system, VNC, Terminal Linux, Shell, Sudo e segurança de root.

#### Objetivo

O objetivo desta prática é a familiarização com ambientes de instalação de distribuições Linux mais utilizadas, como é o caso do Debian-installer, responsável pela instalação do Debian e de alguns projetos derivados dele, como o Raspberry Pi OS (antigo “Raspbian”). Além disso, a familiarização com esses sistemas para uso de outros ambientes como o Calamares, responsável pela instalação de diversas distribuições Linux conhecidas, desenvolvida por um brasileiro da Universidade Federal de Minas Gerais, e o Ubiquity, responsável pela instalação do Ubuntu e alguns derivados.

#### Aplicação

A prática consiste em realizar a instalação do sistema operacional Raspberry Pi OS, a partir do instalador fornecido pela Raspberry Pi Foundation, denominado “Raspberry Pi Imager”, e a partir dele, realizar as configurações do instalador Debian. Uma vez instalado o sistema operacional, deve-se realizar a alteração do acesso root padrão antes de conectá-lo à internet, impedindo que a placa possa ser acessada remotamente por usuários não autorizados na rede. Após isso, a conexão à internet pode ser feita de forma segura, habilitando a internet wireless da placa, e seus subsistemas importantes como o SSH, VNC, e o driver de câmera legacy.

#### Motivação

A motivação para conhecer os conceitos básicos da instalação de sistemas operacionais embarcados advém do fato de que os processos utilizados para a instalação de um sistema operacional embarcado são os mesmos para a instalação de uma distribuição comum, e em geral, todos os instaladores seguem processos semelhantes. Desta forma, conhecendo-se o processo para uma plataforma, pode-se generalizar os conceitos com maior facilidade para o uso de outras distribuições em projetos que necessitem de sistemas operacionais baseados em distribuições Linux (Kernel). Além disso, as configurações de segurança e inicialização são protocolos padrão que devem ser seguidos em qualquer sistema a ser utilizado conectado à internet.

***

### Roteiro

Roteiro a ser seguido para execução da prática:

- Cada grupo deverá anotar o número do kit recebido e utilizá-lo para as demais práticas.
- Verifique se o Raspberry Pi Imager já está instalado no PC do laboratório.
- Faça o download da distribuição 64-bit com interface gráfica e instale no cartão SD.
- Conecte o cartão SD à Raspberry Pi, após a instalação, para acessar a interface gráfica.
- Conecte a fonte de alimentação, monitor, mouse e teclado à Raspberry Pi.
- Altere o usuário root usando o comando `sudo passwd root`.
- Conecte a Raspberry Pi à rede Wi-Fi do laboratório.
- Após a instalação e configurações básicas, reinicie o sistema usando `reboot`.
- Ative funções necessárias como SSH e VNC através do utilitário `raspi-config`.
- Instale o utilitário `neofetch` com o comando `sudo apt install neofetch` e tire um print do terminal.
- Atualize os pacotes do sistema com `sudo apt update && sudo apt upgrade`.
- Verifique o endereço IP da Raspberry Pi com `ifconfig` ou `ip addr`.
- Acesse a Raspberry Pi remotamente via VNC e SSH, realizando operações como copiar arquivos entre as máquinas.
- Gere um histórico de comandos no terminal e salve as configurações de hardware.

***

### Formato de entrega

- Enviar um arquivo `.txt` contendo o histórico de comandos usados no terminal Linux da Raspberry Pi, acrescido das configurações de hardware e software retornadas com os comandos `pinout` e `neofetch`.
- Respostas para as questões sobre a comparação entre as placas Raspberry Pi e SoCs.

***

### Resolução da Prática

#### Resposta salva no TXT e histórico do terminal

```txt
# Exemplo do histórico de comandos no terminal
$ sudo apt update
$ sudo apt upgrade
$ sudo raspi-config
$ sudo passwd root
$ neofetch
...
