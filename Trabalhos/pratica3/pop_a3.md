# Passo a passo para resolver critérios da parte 1

## Apaga o histórico da sessão atual e o salva em disco (limpando o arquivo)

history -c && history -w

## Cria um ambiente virtual chamado "venv"

### (Use python3 para garantir que está usando uma versão recente do Python)

python3 -m venv venv

## Ativa o ambiente virtual

source venv/bin/activate

## Instala a biblioteca necessária para o seu código

pip install gpiozero

## Verifica as bibliotecas instaladas neste ambiente

pip freeze

## Executa o seu script Python

### (Certifique-se de que o arquivo "pratica3_11.py" está neste mesmo diretório)

python pratica3_11.py

## Opcional: exibe o novo histórico de comandos

history
