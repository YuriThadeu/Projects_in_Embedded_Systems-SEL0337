# Desenvolvimento de Linux Embarcado

## Prática 5 - Init System, SystemD e Integração de Visão Computacional

### Autores

- Yuri Thadeu Oliveira Costa
  - N° USP: 14754821
- Fabio Roberto Alcazar Frias Junior
  - N° USP: 14569060

***
***

### 📝 Sobre o Projeto

- **Documento Base:** [📄 Roteiro da Prática (PDF)](Roteiro_pratica-5_eletrica.pdf)

Este projeto consiste na implementação de um sistema de controle de acesso facial automatizado para Raspberry Pi. O desenvolvimento seguiu uma abordagem incremental: iniciamos com testes básicos de hardware, evoluímos para a lógica de visão computacional (desafio extra), integramos tudo em um serviço de inicialização automática (SystemD) e documentamos todo o processo utilizando controle de versão (Git).

O objetivo final é um dispositivo que, ao ser ligado, inicia automaticamente a câmera, valida a identidade do usuário e transita para um modo de espera sinalizado por LEDs.

***
***

### 🚀 Etapa 1: Testes Iniciais de Hardware

Antes de implementar a lógica complexa, realizamos testes básicos para compreender o controle das GPIOs via terminal (Shell Script), sem a necessidade de Python num primeiro momento. O objetivo foi validar o circuito de LEDs e entender como o sistema de arquivos Linux interage com o hardware (`sysfs`).

- **Script de Teste (Blink Simples):** [testes_iniciais/blink.sh](testes_iniciais/blink.sh)
- **Serviço de Teste (Unit File básico):** [testes_iniciais/blink.service](testes_iniciais/blink.service)

***

### 👁️ Etapa 2: Desenvolvimento da Visão Computacional (Parte 3)

Nesta etapa, focamos no desafio de implementar o reconhecimento facial. Durante o processo, enfrentamos problemas de compatibilidade com a câmera original (CSI) e a biblioteca `libcamera-apps`, o que exigiu uma adaptação de hardware e software.

#### 2.1 Adaptação da Câmera (Troubleshooting)

Inicialmente, tentamos utilizar os drivers nativos da Raspberry Pi, mas o sistema não detectou o módulo CSI corretamente. A solução adotada foi migrar para uma **Webcam USB**.

Para validar a nova câmera e garantir que o Linux a reconheceu, utilizamos os seguintes comandos de diagnóstico:

```bash
ls /dev/video* # Verifica se o dispositivo foi montado
sudo apt install fswebcam ffmpeg
ffplay /dev/video0       # Teste de streaming em tempo real
```

#### 2.2 Lógica de Reconhecimento

Com a câmera funcional, desenvolvemos dois scripts principais em Python utilizando a biblioteca **OpenCV**:

1. **Cadastro de Usuário Mestre:** Um script auxiliar que captura a face do usuário autorizado e salva uma imagem de referência (`usuario_mestre.jpg`).

      - *Código:* [parte3/cadastrar/_face.py](parte3/cadastrar_face.py)

2. **Sistema de Validação (`pvc_rasp.py`):** Este é o "cérebro" da visão computacional. Ele utiliza o classificador **Haar Cascade** para detectar rostos na imagem ao vivo e, em seguida, realiza uma comparação de **histograma de cores** entre o rosto detectado e a imagem mestre. Se a semelhança for superior a 50%, o acesso é concedido.

      - *Código:* [parte3/pvc/_rasp.py](parte3/pvc_rasp.py)
      - *Recursos:* [parte3/haarcascade/_frontalface/_default.xml](parte3/haarcascade_frontalface_default.xml)

-----

### ⚙️ Etapa 3: Integração e Automação (Parte 1)

Após validar a visão computacional, o objetivo foi integrar esse módulo ao controle de hardware e automatizar a execução no boot (inicialização) da Raspberry Pi.

#### 3.1 O Script Orquestrador (`launcher.sh`)

Para garantir que os programas rodassem na ordem correta, criamos um script em Shell (`launcher.sh`). Ele atua como um gerenciador:

1. Aguardar o carregamento da interface gráfica.
2. Executar o reconhecimento facial (Parte 3).
3. Após o término (sucesso ou erro), iniciar o modo Blink (Parte 1).

<!-- end list -->

- *Código:* [parte1/launcher.sh](parte1/launcher.sh)

#### 3.2 Modo de Espera (`blink_final.py`)

O código de blink foi aprimorado em relação aos testes iniciais. Agora em Python, ele possui uma função de **interrupção**, onde o sistema verifica constantemente o estado do botão físico, permitindo encerrar o serviço de forma limpa a qualquer momento.

- *Código:* [parte1/blink/_final.py](parte1/blink_final.py)

#### 3.3 Configuração do SystemD (`projeto_final.service`)

A automação foi feita criando um serviço no SystemD. Um desafio crucial nesta etapa foi permitir que o serviço (rodando em background) abrisse janelas na interface gráfica. Isso foi resolvido definindo o usuário correto (`User=embarcados`) e as variáveis de ambiente de display (`DISPLAY=:0`).

- *Arquivo de Serviço:* [parte1/projeto/_final.service](parte1/projeto_final.service)

#### 3.4 Correção de Permissões

Durante a integração, o serviço falhou com erro `203/EXEC Permission denied`. A solução foi conceder permissão explícita de execução ao orquestrador:

```bash
chmod +x /home/embarcados/embarcados/pratica5/git/Projects_in_Embedded_Systems-SEL0337/Trabalhos/pratica5/parte1/launcher.sh
```

-----

### 📂 Etapa 4: Documentação e Versionamento (Parte 2)

Durante todo o desenvolvimento, utilizamos o **Git** para controle de versão, garantindo um histórico seguro das alterações nos códigos. O repositório foi clonado na Raspberry Pi, os códigos foram desenvolvidos localmente e sincronizados com o GitHub.

- **Log de Histórico Git:** [parte2/historico/_git.txt](parte2/historico_git.txt)

-----

-----

### 🏁 Conclusão e Metodologia

A metodologia de etapas adotada neste projeto seguiu um fluxo lógico incremental, visando cobrir integralmente os requisitos propostos no roteiro da Prática 5 (Partes 1, 2 e 3).

Optou-se por isolar primeiramente o problema de hardware (testes iniciais), garantindo que os atuadores funcionassem antes de introduzir a complexidade do software. Em seguida, atacou-se o desafio de maior complexidade (Visão Computacional - Parte 3) de forma independente. Somente após garantir a estabilidade desses dois módulos, partiu-se para a automação e integração via SystemD (Parte 1).

Essa estratégia permitiu diagnosticar e corrigir falhas específicas (como a incompatibilidade da câmera CSI e problemas de permissão gráfica) de forma isolada, resultando em um sistema robusto onde a orquestração final apenas une componentes já validados. A documentação via Git (Parte 2) permeou todo o processo, registrando a evolução do projeto passo a passo.

-----

-----

### 🖼️ Anexos e Demonstração

#### 📸 Montagem do Hardware

Abaixo, a imagem do circuito montado, exibindo a conexão da Webcam USB, os LEDs de status (Verde/Vermelho) e o botão de interrupção.

- **Visualizar Foto:** [parte2/montagem.jpg](parte2/montagem.jpg)

#### 🎥 Vídeo de Funcionamento

Demonstração completa do sistema: Boot automático -/> Abertura da Câmera -/> Validação Facial -/> Transição para o Blink -/> Encerramento via Botão.

- **Visualizar Vídeo:** [parte2/funcionamento.mp4](parte2/funcionamento.mp4)

<!-- end list -->