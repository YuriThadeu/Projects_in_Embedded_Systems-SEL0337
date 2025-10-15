# Sistemas Operacionais e Ambiente Linux

## Prática 2 - Instalação e preparação do S.O. na Raspberry Pi

### Autor(es)

- Yuri Thadeu Oliveira Costa
  - N° USP: 14754821
- Fabio Roberto Alcazar Frias Junior
  - N° USP: 14569060

***

### Guia da Prática

#### Resumo

Introdução ao uso de instaladores de distribuições Linux, como o Debian Installer (uma versão derivada dele é utilizada no instalador do Raspberry Pi OS), configurações iniciais após instalação do sistema operacional, configuração do usuário root, conexão à internet, ativação do SSH, ativação dos drivers da câmera.

#### Conceitos importantes

Debian-installer, SSH, Embedded OS, Embedded Linux, Init system, VNC, Terminal Linux, Shell, Sudo, Segurança de root

#### Objetivo

O objetivo desta prática é a familiarização com ambientes de instalação de distribuições Linux mais utilizadas, como é o caso do Debian-installer, responsável pela instalação do Debian e de alguns projetos derivados dele, como o Raspberry Pi OS (antigo “Raspbian”). Além disso, a familiarização com esses sistemas para uso de outros ambientes como o Calamares, responsável pela instalação de diversas distribuições Linux conhecidas, desenvolvida por um brasileiro da Universidade Federal de Minas Gerais, e o Ubiquity, responsável pela instalação do Ubuntu e alguns derivados.

#### Aplicação

A prática consiste em realizar a instalação do sistema operacional Raspberry Pi OS, a partir do instalador fornecido pela Raspberry Pi Foundation, denominado “Raspberry Pi Imager”, e a partir dele, realizar as configurações do instalador Debian. Uma vez instalado o sistema operacional, deve-se realizar a alteração do acesso root padrão antes de conectá-lo à internet, impedindo que a placa possa ser acessada remotamente por usuários não autorizados na rede. Após isso, a conexão à internet pode ser feita de forma segura, habilitando a internet wireless da placa, e seus subsistemas importantes como o SSH, VNC, e o driver de câmera legacy.

#### Motivação

A motivação para conhecer os conceitos básicos da instalação de sistemas operacionais embarcados advém do fato de que os processos utilizados para a instalação de um sistema operacional embarcado são os mesmos para a instalação de uma distribuição comum, e em geral, todos os instaladores seguem processos semelhantes. Desta forma, conhecendo-se o processo para uma plataforma, pode-se generalizar os conceitos com maior facilidade para o uso de outras distribuições em projetos que necessitem de sistemas operacionais baseados em distribuições Linux (Kernel). Além disso, as configurações de segurança e inicialização são protocolos padrão que devem ser seguidos em qualquer sistema a ser utilizado conectado à internet.

***

### Roteiro

Roteiro a ser seguido para execução da prática:

- Cada grupo deverá anotar o número do kit recebido e utilizá-lo para as demais práticas, permanecendo com ele até o final da disciplina. É fundamental zelar pela integridade do equipamento, utilizando-o com cuidado e reportando imediatamente qualquer eventualidade.

- Antes de iniciar o processo, deve-se observar se o instalador “Raspberry Pi Imager” já está instalado no PC do laboratório (Ubuntu Linux). Caso contrário, deve-se realizar a instalação conforme instruções disponibilizadas aqui.

- Uma vez inicializado o Raspberry Pi Imager, deve ser feito o download da distribuição 64-bit com interface gráfica e instalação no cartão SD (“Raspberry Pi OS (64-bit)” - cuidado para não instalar a versão “Lite” que é sem interface gráfica e somente terminal Linux ou versões 32 bits). Para tanto, deve-se remover com cuidado o cartão SD da placa Raspberry Pi e conectá-lo ao PC por meio dos adaptadores micro SD-USB.

- Nas configurações do imager, já é possível ser feita a alteração do usuário (configurar usuário como “sel”, computador: raspberrypi e senha “usp”), porém, não é possível ainda alterar senha de root, por este motivo, não deve-se conectá-lo à internet antes de ser feita esta configuração, a fim de garantir a segurança do dispositivo.

- Desta forma, ao final da instalação, pode-se conectar o cartão SD à Raspberry Pi, já tendo acesso à interface gráfica.

- Ligar a placa Raspberry Pi conectando a fonte de alimentação na entrada (micro USB), e conectar os periféricos do computador: cabo HDMI do monitor, mouse e teclado via USB (remover cabo HDMI, mouse e teclado do PC e conectar na Raspberry Pi). Como a placa não possui power button, o boot acontece logo após conectar a fonte de alimentação (desde que o cartão SD com a imagem já tenha sido devidamente inserido no slot).

- Conforme discorrido, deve-se como primeira atividade alterar o usuário root por meio do comando `sudo passwd root`, para o nome de usuário e senha iguais aos dos computadores da bancada, garantindo que usuários da rede não possam acessá-la remotamente.

- Com o usuário root configurado, pode-se conectá-la à rede Wi-Fi do laboratório (LabMicros - senha: seluspeesc@). Procure pelo Wi-Fi no caso superior direito da interface gráfica do sistema operacional. Caso não apareça, definir o país Brasil nas configurações que aparecer.

- Uma vez instalados e configurados os parâmetros básicos do sistema, reiniciar o sistema por meio do comando `reboot`.

- Em seguida, pode-se acessar o utilitário de configuração do sistema (`sudo raspi-config`) a fim de ativar algumas funções que serão úteis em práticas seguintes, como o acesso a SSH, e VNC, além de visualizar outras configurações possíveis de se ativar, como I2C, por exemplo, etc (acessar a opção “3 - Interface Options”).

- Com todas as opções necessárias habilitadas, pode-se instalar o utilitário de terminal `neofetch` (`sudo apt install neofetch`), com ele pode-se observar alguns parâmetros do hardware e do sistema operacional instalados.

- Salve um print da imagem dele (output do terminal após a execução do comando neofetch) para permitir a consulta posterior (no documento de entrega, os parâmetros mostrados pelo neofetch deverão ser explicados a partir da teoria vista). Faça o mesmo procedimento para os parâmetros mostrados no terminal quando executado o comando “pinout”.

- Com todos os procedimentos realizados, pode-se atualizar os pacotes a partir do gerenciador de pacotes no terminal (`sudo apt update && sudo apt upgrade`).

- Verifique o endereço “IP” da Raspberry Pi digitando `ifconfig` ou `ip addr`. (verificar o IP em “Wlan0” se a placa estiver conectada à rede Wi-Fi; ou o IP em “eth0:” se estiver usando a rede cabeada/Ethernet).

- Após conectar a Raspberry e configurar todos os pacotes e configurações já executadas, faça o acesso remoto à Raspberry Pi via VNC a partir de um computador que esteja conectado à mesma rede Wi-Fi ou a partir de um smartphone (instalar o app VNC Viewer e digitar o IP da Rasp). Certifique-se de que o VNC esteja habilitado na Raspberry Pi, conforme passo anterior realizado pelo utilitário “sudo raspi-config”. Para a conexão remota acontecer e os passos anteriores funcionarem, o computador host (PC ou smartphone) e o computador remoto (Rasp) devem estar conectados à mesma rede. O acesso também poderá ser feito por Wi-Fi, conectando a Rasp à rede Lab. Micros e acessando ela remotamente por meio daqueles PCs do laboratório que possuem conexão cabeada conectadas diretamente ao roteador da rede Lab.Micros.

- Da mesma forma, tente realizar o acesso remoto à Raspberry Pi de um outro grupo via SSH (secure shell) (`ssh rasp_user_name@<rasp IP>` - ex.: `ssh sel@192.168.0.16`) a partir da sua placa e vice-versa. Realize alguma operação para validar o acesso remoto via SSH. Por exemplo, copiar um arquivo da sua placa e colocar na placa remota ou vice-versa (`cp /home/user/localfile.txt sel@192.168.1.100:/home/pi/` ou `cp pi@192.168.1.100:/home/pi/remotefile.txt /home/user/`). Confirme a operação com comando `ls`. Lembrando que, para a conexão remota acontecer e os passos anteriores funcionarem, o computador host e o computador remoto devem estar conectados à mesma rede e com SSH habilitado.

- Finalizar o acesso remoto e gerar um histórico de texto dos comandos utilizados no terminal ao longo desta atividade prática. Salve essas informações para entrega na tarefa, fazendo o mesmo procedimento da prática anterior de, manualmente, anotar as configurações de hardware retornadas após digitar neofetch e pinout no terminal.

- **OBS.** Uma opção para salvar o arquivo `.txt` da Raspberry Pi para o PC é acessar seu e-mail/drive a partir da Raspberry Pi, usando navegador Web, e salvá-lo na sua conta. Outra opção é utilizar um pen-drive.

- Por fim, execute a seguinte atualização (será útil para práticas futuras - certifique-se de digitar corretamente a sequência ou copiar e colar no terminal): `sudo rpi-update cac01bed1224743104cb2a4103605f269f207b1a #6.1.54`.

- Execute um comando para limpar o histórico terminal.

- Após finalizar a prática, desligar a Raspberry Pi por meio do comando `sudo poweroff` ou `sudo shutdown -h now`.

- Desconectar os periféricos (mouse, teclado e cabo HDMI) e conectá-los novamente ao PC. Desconectar a fonte de alimentação da Raspberry Pi. Guardar a placa e a fonte nas respectivas embalagens, deixando-as da forma que as recebeu no início da prática.

- Anotar o número da embalagem que você usou para sempre usar a mesma placa nas próximas atividades práticas.

- Importa lembrar que os mesmos kits são usados por outras 3 turmas distintas ao longo do semestre. Portanto, além do cuidado e zelo que deve-se tomar pelas placas, as outras turmas irão repetir esses mesmos procedimentos, instalando novamente a imagem Linux no cartão SD que você usou. Portanto, faça sempre um backup dos seus arquivos fora do Raspberry Pi.

***

### Formato de entrega

- **Histórico de comandos**: Enviar um arquivo `.txt` contendo o histórico de comandos usados no terminal Linux da Raspberry Pi, acrescido das configurações de hardware e software retornadas com os comandos `pinout`, `neofetch` (basta editar manualmente o arquivo e listar apenas as características chaves mais importantes do hardware, como arquitetura, kernel, versão ARM, SoC, CPUs, capacidade etc., enfatizando também qual o requisito chave para um hardware rodar Linux embarcado e porque não é possível em microcontroladores).
  
  - **Identificação**: Em caso de duplas, somente uma pessoa poderá fazer a entrega. Entretanto, lembrar de identificar no arquivo de entrega o nome e Nº USP dos integrantes.

### Questões
  
  1. Em até 10 linhas, compare de forma geral as placas SBCs Raspberry Pi 3B+, Raspberry Pi 4B e Raspberry Pi 5 em termos de recursos, limitações e novidades presentes na última versão.
  
  2. Em até 10 linhas, compare os seguintes SoCs em termos de núcleos, arquitetura, GPU e conectividade:
     - BCM2837B0 (Raspberry Pi 3B+)
     - BCM2711 (Raspberry Pi 4)
     - BCM2712 (Raspberry Pi 5)

     Relacione esses SoCs com outros do mercado (escolher somente outros dois modelos a partir das alternativas abaixo):
     - Amlogic S905X3 (Set-Top-Box BTV11 - disponível no laboratório)
     - Texas Instruments AM3358 (SBC BeagleBone Black - disponível no laboratório)
     - Rockchip RK3288 (SBC ASUS Tinker Board) ou RK3588S (SBC Orange Pi 5), ou outra SBC comercial de sua escolha.
     - NXP i.MX6 - Computador em Módulo (CoM) Toradex Colibri iMX6 e placa base Aster (disponível no laboratório).

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

```

#### Resposta das Questões
