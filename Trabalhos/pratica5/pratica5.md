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



## 🛠️ Guia de Comandos SystemD (Raspberry Pi)

Abaixo estão os comandos utilizados para gerenciar o serviço `projeto_final.service` criado nesta prática.

### 🔄 Controle do Serviço (Imediato)

* **Iniciar o serviço manualmente:**

    ```bash
    sudo systemctl start projeto_final.service
    ```

    *Uso: Roda o projeto agora, independente do boot.*

* **Parar o serviço:**

    ```bash
    sudo systemctl stop projeto_final.service
    ```

    *Uso: Encerra imediatamente o script e a câmera.*

* **Reiniciar o serviço (Atualizar Código):**

    ```bash
    sudo systemctl restart projeto_final.service
    ```

    *Uso: Aplica alterações feitas nos códigos Python/Bash sem precisar reiniciar a placa.*

### 🚀 Configuração de Boot (Inicialização)

* **Habilitar no Boot:**

    ```bash
    sudo systemctl enable projeto_final.service
    ```

    *Uso: Faz o programa iniciar sozinho toda vez que a Raspberry Pi for ligada.*

* **Desabilitar no Boot:**

    ```bash
    sudo systemctl disable projeto_final.service
    ```

    *Uso: Impede que o programa inicie sozinho (volta ao manual).*

### 🔍 Diagnóstico e Logs

* **Verificar Status:**

    ```bash
    sudo systemctl status projeto_final.service
    ```

    *Uso: Mostra se está rodando (Active: running), parado ou se deu erro, além das últimas linhas de log.*

* **Ver Log Completo (Debug):**

    ```bash
    journalctl -u projeto_final.service -b -e
    ```

    *Uso: Mostra todo o histórico de mensagens (prints) do programa desde o último boot. Útil para ver erros de Python.*

### ⚙️ Configuração do Sistema

* **Recarregar Daemon:**

    ```bash
    sudo systemctl daemon-reload
    ```

    *Uso: Obrigatório sempre que o arquivo `.service` for modificado.*


Dar Permissão de Execução

chmod +x /home/embarcados/embarcados/pratica5/git/Projects_in_Embedded_Systems-SEL0337/Trabalhos/pratica5/parte1/launcher.sh