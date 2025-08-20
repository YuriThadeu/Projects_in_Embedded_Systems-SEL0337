# Sistemas Operacionais e Ambiente Linux

## Prática 1 - Introdução à linha de comandos, terminal(shell/bash) e sistemas de arquivos Linux

### Autor(es):
- NOME: Yuri Thadeu Oliveira Costa
- N° USP: 14754821
***
***
### Guia da Prática

#### Resumo
Introdução aos sistemas de arquivos em terminais Linux (bash), criação de arquivos,
criação de diretórios, navegação entre diretórios, edição de textos e códigos a partir do
terminal.

#### Comandos importantes:
cd, ls, pwd, cat, find, grep, history, echo, touch, nano, man, help.

#### Comandos de manipulação de arquivos:
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

