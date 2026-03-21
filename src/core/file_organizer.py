import os
import shutil
from tkinter import messagebox
from src.utils.file_types import EXTENSOES
from src.core.logger import logger
from src.utils.config import SUCCESS_MSG, ERROR_MSG

def criar_pastas(pasta_origem):
    """Cria pastas de destino para cada categoria se não existirem."""
    logger.info(f"Criando pastas de categoria em: {pasta_origem}")
    for categoria in EXTENSOES:
        destino = os.path.join(pasta_origem, categoria)
        os.makedirs(destino, exist_ok=True)
    # Garante que a pasta OUTROS exista explicitamente
    os.makedirs(os.path.join(pasta_origem, 'OUTROS'), exist_ok=True)

def mover_arquivo_para_categoria(pasta_origem, arquivo):
    """Move um arquivo para a pasta correspondente à sua extensão."""
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    
    # Se já estiver dentro de uma das pastas de categoria, ignore.
    if not os.path.isfile(caminho_arquivo):
        return
    
    _, ext = os.path.splitext(arquivo)
    ext = ext.lower()

    for categoria, lista_ext in EXTENSOES.items():
        if ext in lista_ext:
            shutil.move(caminho_arquivo, os.path.join(pasta_origem, categoria, arquivo))
            return

    # Caso não encontre a extensão, move para OUTROS
    shutil.move(caminho_arquivo, os.path.join(pasta_origem, 'OUTROS', arquivo))

def organizar_arquivos(pasta_origem):
    """Organiza todos os arquivos da pasta selecionada por categorias."""
    try:
        logger.info(f"Iniciando organização da pasta: {pasta_origem}")
        criar_pastas(pasta_origem)
        for arquivo in os.listdir(pasta_origem):
            mover_arquivo_para_categoria(pasta_origem, arquivo)
        
        logger.info("Organização concluída com sucesso!")
        messagebox.showinfo("Concluído", SUCCESS_MSG)
    except Exception as e:
        logger.error(f"Erro ao organizar arquivos: {e}")
        messagebox.showerror("Erro", f"{ERROR_MSG}{e}")
