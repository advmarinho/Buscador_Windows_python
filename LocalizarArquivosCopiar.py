import os
import shutil


# pyinstaller --onefile --noconsole .\nome.py
# pyinstaller --onefile --console .\LocalizarArquivosCopiar.py


print('Siga as instruções  ')
print('Software by ADS - Anderson Marinho  \n\n')


caminho_original = input(r' Digite o caminho dos arquivos que deseja encontrar:-->|')
print('\n')
caminho_novo = input(r' Digite o caminho para onde dejesa copiar os arquivos:-->|')
print('\n')


again2 = 's'
while(again2 == 's'):
    termo1 = str(input(' Digite o termo a ser buscado no nome do arquivo, exemplos: FOL/AUT ou a extensão .pdf/.xls:-->|'))
    print('\n')
    again   = 1 #input(r' Digite a quantidade de vezes que irá repetir a busca, mínimo uma vez "1" :-->|')
    print('\n')
    
    # LOCALIZANDO OS ARQUIVOS
    for num in range(int(again)):
        print('\n')
        termo = termo1
        for raiz, diretorios, arquivos in os.walk(caminho_original):
            for arquivo in arquivos:
                if termo1 in arquivo:
                    caminho_completo = os.path.join(raiz, arquivo)
                    caminhoRaiz = os.path.join(raiz)
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                    print('Patas: ', caminhoRaiz)
                    print('__Arq: ','\t', nome_arquivo, ext_arquivo, sep='')
                    
        seguir = input('\nTecle "S" para COPIAR os arquivos encontrados na pasta indicada ou "N" para sair (S/N): ').lower()
        seguir = seguir.lower()
        if seguir == 's':
            # COPIANDO OS ARQUIVOS
            try:
                os.mkdir(caminho_novo)
            except FileExistsError as e:
                print(f'Pasta {caminho_novo} já existe: ')
                print(e)
            for root, dirs, files in os.walk(caminho_original):
                for file in files:
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(caminho_novo, file)
                    if  str(termo) in file:
                        print(file)
                        try:
                            shutil.copy(old_file_path, new_file_path)
                            print('Arquivo copiado com sucesso!')
                        except shutil.SameFileError:
                            pass
                        
                        print('\n')
                        print(f'Arquivo {dir} copiado com sucesso! \n')
                    pass
    again2 = input("Deseja Repetir a busca? (S/N): ").lower()
print('\nFim da execução!')
