
import json                                     # Lidar com os arquivos JSON
from pathlib import Path                        # LIDAR COM OS CAMINHOS DO WINDOWS

class BancoFake :
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes":[]}            #CLIENTES INICIANDO COMO VAZIO 

        # CARREGAR VALORES ANTERIORES SALVOS 
        self._carregar()

    def _carregar(self):
        """ Carrega dados do arquivo Json, se existir.
        caso nao exista, inicia banco novo """

        caminho = Path(self.arquivo_db)
        # VERIFICA SE ARQUIVO EXISTE 
        if caminho.is_file():
            #abrindo arquivo no modo leitura em utf-8 (pt-br)
            with open(caminho, 'r', encoding="utf-8") as arquivo:
                #Carregar dados anteriores ja salvos
                self.dados = json.load(arquivo)
        else:
            #Chamar funçao para criar novo arquivo 
            self._salvar()

    def _salvar(self):
        """ SAlVAR CONTEUDO DO SELF.DADOS NO JSON """

        # abrir o arquivo no modo w (escrita)
        with open(self.arquivo_db, 'w', encoding="utf-8") as dados :
            # REALIZAR UM DUMP DE PYTHON PARA JSON
            # ensure_ascii = False
            #indent = identificaçao -> 4 recuo
            json.dump(self.dados, dados, ensure_ascii=False, indent=4)

    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()
    def listar_clientes(self):
        return self.dados["clientes"]

