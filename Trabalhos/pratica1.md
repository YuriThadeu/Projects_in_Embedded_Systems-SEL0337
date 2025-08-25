# Sistemas Operacionais e Ambiente Linux

## Prática 1 - Introdução à linha de comandos, terminal(shell/bash) e sistemas de arquivos Linux

### Autor(es)

- Yuri Thadeu Oliveira Costa
  - N° USP: 14754821
- Fabio Roberto Alcazar Frias Junior
  - N° USP: 14569060

***
***

### Guia da Prática

#### Resumo

Introdução aos sistemas de arquivos em terminais Linux (bash), criação de arquivos,
criação de diretórios, navegação entre diretórios, edição de textos e códigos a partir do
terminal.

#### Comandos importantes

cd, ls, pwd, cat, find, grep, history, echo, touch, nano, man, help.

#### Comandos de manipulação de arquivos

mv, rm, cp, mkdir, rmdir.

#### Objetivo

O objetivo desta prática é a familiarização com comandos utilizados em terminais Linux, a fim de realizar operações básicas em sistemas de arquivos, utilizando a linguagem de programação bash, padrão em sistemas operacionais Linux. O bash é um shell de comandos executados pelo computador para realizar tarefas passadas a ele, por meio da interpretação destes comandos.

#### Aplicação

Portanto, a partir dos comandos listados acima, e os conceitos passados em aula, a prática consiste em criar um diretório, e em uma pasta interna criar um arquivo de texto simples com o nome dos/das autores(as) da prática, e após isso, realizar manipulações com arquivos. Os passos para a execução da prática podem ser conferidos abaixo por meio da sequência de atividades a serem executadas no terminal.

#### Motivação

A motivação para conhecer os conceitos básicos da linguagem bash é que terminais em sistemas operacionais embarcados são de extrema importância, visto que em muitas aplicações, não é possível utilizar interfaces gráficas para configuração do sistema, devido a limitações de hardware, ou quando são necessárias manutenções em campo, e não há a disponibilidade de conexão de novos equipamentos para o uso da interface gráfica. Além disso, como visto pela teoria, o uso de recursos de uma SBC, como a Raspberry Pi, deve ser otimizado, visto que seu poder de processamento é reduzido comparado a um computador de uso geral. Desta forma, reduzir o poder de processamento na renderização de uma interface gráfica libera recursos do processador para as aplicações do produto.

#### Roteiro

Roteiro a ser seguido para execução da prática:

- Antes de iniciar a prática, escreva no terminal a partir do comando echo, “INÍCIO DA PRÁTICA 1”.
- Verifique em qual diretório o terminal está a partir do terminal, e sua posição relativa.
- Crie um diretório na pasta /home/sel com o código da disciplina.
- Acesse o diretório criado.
- Verifique se foi acessado o diretório desejado.
- Crie uma pasta interna, com o nome pratica_1
- Acesse a pasta interna
- Volte ao diretório “pai”
- Liste as pastas criadas
- Acesse novamente a pasta criada
- Crie um arquivo helloworld.txt
- Escreva o nome e número usp da dupla neste arquivo utilizando o nano.
- Dentro do nano, ao terminar de editar, pressione ctrl+x para salvar e sair.
- Visualize o que foi escrito utilizando o comando cat.
- Verifique se há somente um arquivo .txt dentro do seu diretório, a partir do comando de terminal (find / -name ‘*.txt’)
- Utilize o comando grep para encontrar ambos os números USP da dupla dentro do arquivo de texto.
- Copie o seu arquivo hello world para o próprio diretório com outro nome
- Mova a cópia para o diretório “pai” (utilizando relacionais ou o caminho do arquivo)
- Remova o arquivo original
- Saia da pasta interna (volte ao diretório pai utilizando os relacionais)
- Remova a pasta pratica_1
- Gere um arquivo backup_historico.txt com o histórico dos seus comandos (comandos de input/output)
- Utilize o comando tail -N para determinar quantas linhas serão salvas (inclua até encontrar a linha com o comando echo que demarca o início da prática). Este arquivo .txt gerado deverá ser entregue na tarefa correspondente a presente atividade prática.
- Extra:
  - Em todos os computadores do laboratório foi instalado o aplicativo neofetch, este mostra detalhes do hardware, mas também do sistema operacional e do ambientegráfico instalado, sendo um padrão quando se pretende compartilhar com outros usuários linux um status geral do seu sistema, seja para correção de problemas, avaliando o hardware instalado, ou para passar padrões de gráficos utilizados, para acompanhar o mesmo estilo de outra pessoa. Para isso, coloque o comando neofetch no terminal e será impressa as informações com uma logo da distribuição que está sendo utilizada no momento. Liste as principais informações retornadas por esse comando, a qual poderá ser acrescentada manualmente ao final do arquivo .txt com histórico de comandos salvo anteriormente.

  - No diretório do usuário (/home/sel), digite “ls -l” e escolha um dos arquivos apresentados no terminal para explicar as informações que aparecem acompanhada do arquivo, após digitar esse comando (normalmente, aparecerá algo como drw-rw-rw-r ou -rwxr …. deverá ser explicado o significado destas letras e a implicação que se tem para aquele arquivo). A explicação poderá ser acrescentada manualmente ao final do arquivo .txt salvo anteriormente.

- Importante: após ter certeza de que concluiu todas as tarefas desta atividade prática e ter feito um backup do arquivo .txt salvo com o histórico dos comandos (ou seja, certifique-se de enviar o arquivo para seu e-mail, drive/nuvem, ou salvar em um pen-drive etc.), exclua todos os arquivos e pastas que você gerou durante a atividade prática dentro do diretório “/home/sel”. Da mesma forma, limpe o histórico do terminal. Essa ação será necessária uma vez que outras turmas desta disciplina também irão realizar essa atividade prática nos computadores do laboratório. Não é necessário documentar este último passo de exclusão dos arquivos, tampouco salvar em arquivo .txt. o histórico do comando usado para limpar o histórico do terminal. Atenção: excluir somente os arquivos e pastas que você criou dentro do diretório /home/sel. Ter cuidado para não excluir outros arquivos e pastas importantes que ficam dentro deste diretório (Documents, Desktop, Downloads, .config etc). Portanto, sempre verifique o conteúdo dentro de um diretório por meio do comando “ls”, para identificar os arquivos que serão excluídos.
- Caso esteja usando seu próprio computador para executar essa atividade durante a aula prática, desconsidere a solicitação acima de exclusão dos arquivos e limpeza do histórico, pois ela só é válida para trabalhos realizados nos PCs do LabMicros.

#### Critérios de avaliação

Uso correto dos comandos de manipulação de arquivos e sequência (seguindo a ordem do roteiro) que será verificada pelo histórico, atendimento aos “extras”, apresentação do arquivo com histórico salvo.

#### Formato de entrega

Realizar o upload do arquivo .txt na tarefa correspondente ou arquivo “readme.md” do Github (opcional, caso não queira apresentar no formato .txt).

#### Bibliografia

- Guia com mais de 500 comandos Linux (explicados).
- Material de aula: Cap. 1 Sistemas Operacionais e Kernel; Cap. 2 Ambiente Linux, Distros, Terminal.

***
***

### Resolução da Pratica

#### Resposta salva no TXT e histórico do terminal

```txt
yurit@YPC:/home/sel/SEL0337$ history    
    1  echo "inicio da pratica 1"
    2  pwd
    3  sudo mkdir /home/sel
    4  sudo mkdir /home/sel/SEL0337
    5  cd /home/sel/SEL0337
    6  pwd
    7  sudo mkdir pratica1
    8  cd pratica1
    9  cd ..
   10  ls
   11  cd pratica1
   12  sudo touch helloworld.txt
   13  sudo nano helloworld.txt
   14  cat helloworld.txt
   15  sudo find . -name "*.txt"
   16  grep "14754821" helloworld.txt
   17  sudo cp helloworld.txt helloworld_copia.txt
   18  sudo mv helloworld_copia.txt ..
   19  sudo rm helloworld.txt
   20  cd ..
   21  sudo rmdir pratica1
   22  neofetch
   23  sudo ls -l /home/sel
   24  history | tail -25 > backup_hist.txt
   25  history
```

#### Comentários sobre os códigos feitos + extra1 e extra2

```shell
# Início da prática
echo "INÍCIO DA PRÁTICA 1"

# Verificar diretório atual
pwd

# Criar diretório da disciplina em /home/sel (precisa de sudo)
sudo mkdir /home/sel
sudo mkdir /home/sel/SEL0337
cd /home/sel/SEL0337
pwd

# Criar pasta interna
sudo mkdir pratica_1
cd pratica_1
cd ..
ls
cd pratica_1

# Criar arquivo e editar
sudo touch helloworld.txt
sudo nano helloworld.txt   # editar com nome e NUSP, salvar com CTRL+X

#As entradas são: 
#Yuri Thadeu Oliveira Costa         - 14754821
#Fabio Roberto Alcazar Frias Junior - 14569060

# Visualizar conteúdo
cat helloworld.txt

# Verificar arquivos .txt
# sudo find / -name "*.txt" -> esse arquivo lista TODOS os arquivos .txt do seu computador
sudo find . -name "*.txt"  #troque para esse com ponto, já que mostra somente os da pasta atual

# Buscar números USP (não precisa sudo se já tem leitura)
grep "14754821" helloworld.txt

# Copiar arquivo
sudo cp helloworld.txt helloworld_copia.txt

# Mover cópia para diretório pai
sudo mv helloworld_copia.txt ..

# Remover arquivo original
sudo rm helloworld.txt

# Sair da pasta interna
cd ..

# Remover pasta pratica_1
sudo rmdir pratica_1

# Extra 1: Mostrar informações do sistema
# sudo apt install neofetch """se não estiver instalado"""
neofetch

# ENTRADA E SAIDA
"yurit@YPC:/home/sel$ neofetch
            .-/+oossssoo+/-.               yurit@YPC
        `:+ssssssssssssssssss+:`           ---------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 24.04.3 LTS on Windows 10 x86_64
    .ossssssssssssssssssdMMMNysssso.       Kernel: 6.6.87.2-microsoft-standard-WSL2
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Uptime: 2 hours, 12 mins
  +ssssssssshmydMMMMMMMNddddyssssssss+     Packages: 636 (dpkg)
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Shell: bash 5.2.21
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Theme: Adwaita [GTK3]
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Icons: Adwaita [GTK3]
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Terminal: Relay(2330)
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: Intel Ultra 7 155H (22) @ 2.995GHz
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   GPU: 7dd7:00:00.0 Microsoft Corporation Basic Render Driver
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Memory: 438MiB / 15742MiB
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

"


# EXPLICAÇÂO

"
Explicação do comando neofetch

Saída do comando:
----------------------------------------------------
OS: Ubuntu 24.04.3 LTS on Windows 10 x86_64
Kernel: 6.6.87.2-microsoft-standard-WSL2
Uptime: 2 hours, 12 mins
Packages: 636 (dpkg)
Shell: bash 5.2.21
Theme: Adwaita [GTK3]
Icons: Adwaita [GTK3]
Terminal: Relay(2330)
CPU: Intel Ultra 7 155H (22) @ 2.995GHz
GPU: Microsoft Basic Render Driver
Memory: 438MiB / 15742MiB
----------------------------------------------------

Detalhes das informações principais:
- OS: Sistema operacional em execução, no caso Ubuntu 24.04.3 rodando sobre Windows 10 via WSL2.
- Kernel: Versão do núcleo Linux utilizada pelo sistema (6.6.87.2).
- Uptime: Tempo em que o sistema está ativo desde a última inicialização (2h12min).
- Packages: Quantidade de pacotes instalados gerenciados pelo dpkg (636).
- Shell: Shell em uso pelo terminal, aqui bash versão 5.2.21.
- Theme/Icons: Tema visual e ícones ativos no ambiente gráfico (Adwaita, padrão do GNOME/GTK3).
- Terminal: Aplicativo de terminal em execução (Relay, no contexto do WSL2).
- CPU: Processador do sistema, no caso Intel Ultra 7 155H com 22 threads a ~2.99GHz.
- GPU: Controlador gráfico detectado (driver básico da Microsoft).
- Memory: Quantidade de memória RAM usada (438 MiB) em relação ao total disponível (15742 MiB).

Implicação prática:
O comando neofetch permite verificar rapidamente o estado do sistema,
incluindo versão do SO, kernel, hardware principal (CPU, GPU, RAM),
pacotes e shell utilizado. Essas informações são úteis para
diagnóstico, suporte e documentação do ambiente de trabalho.
"

# Extra 2: Listagem detalhada no diretório do usuário
sudo ls -l /home/sel

# ENTRADA E SAIDA

"yurit@YPC:/home/sel$ ls -l
total 4
drwxr-xr-x 2 root root 4096 Aug 24 18:31 SEL0337"

# EXPLICAÇÂO

"Explicação do comando ls -l sobre o diretório SEL0337

Saída analisada:
drwxr-xr-x 2 root root 4096 Aug 24 18:31 SEL0337

Detalhes:
- d : indica que é um diretório (se fosse "-", seria um arquivo comum).
- rwx : permissões do dono (root) -> pode ler (r), escrever (w) e acessar (x).
- r-x : permissões do grupo (root) -> pode ler e acessar, mas não escrever.
- r-x : permissões de outros usuários -> podem ler e acessar, mas não escrever.
- 2 : número de links do diretório.
- root root : primeiro root é o dono, segundo root é o grupo dono.
- 4096 : tamanho em bytes do diretório (valor padrão em sistemas ext4).
- Aug 24 18:31 : data e hora da última modificação.
- SEL0337 : nome do diretório.

Implicação prática:
Somente o usuário root pode criar, excluir ou modificar arquivos dentro desse diretório.
Usuários comuns podem apenas visualizar o conteúdo e acessar a pasta, mas não alterar
seu conteúdo sem utilizar privilégios de superusuário (sudo).
"


# Gerar arquivo de histórico e Ajustar número de linhas com tail
history | tail -25 > backup_historico.txt 


# No final de tudo, executar o comando para limpar a pasta
sudo rm -rf /home/sel #cuidado com isso, digite corretamente!!
history –c # limpesa do histórico
```