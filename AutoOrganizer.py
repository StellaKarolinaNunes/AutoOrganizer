import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# ----------------------------- CONFIGURAÇÕES -----------------------------

EXTENSOES = {
    'DOCUMENTOS': ['.doc', '.docx', '.odt', '.txt', '.rtf', '.pdf', '.tex', '.md'],
    'PLANILHAS': ['.xls', '.xlsx', '.ods', '.csv', '.tsv'],
    'APRESENTAÇÕES': ['.ppt', '.pptx', '.odp', '.key'],
    'IMAGENS': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.tif', '.heic'],
    'AUDIO': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma'],
    'VIDEO': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    'ARQUIVOS_COMPACTADOS': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.dmg'],
    'CODIGO': ['.html', '.htm', '.css', '.js', '.ts', '.json', '.xml', '.py', '.java',
               '.c', '.cpp', '.h', '.cs', '.php', '.rb', '.sh', '.bat', '.sql'],
    'FONTES': ['.ttf', '.otf', '.woff', '.woff2'],
    'EXECUTAVEIS': ['.exe', '.msi', '.apk', '.app', '.deb', '.rpm', '.jar'],
    'OUTROS': ['.log', '.ini', '.bak', '.tmp', '.dat', '.db']
}

# ----------------------------- LÓGICA DE NEGÓCIO -----------------------------

def criar_pastas(pasta_origem):
    """Cria pastas de destino para cada categoria se não existirem."""
    for categoria in EXTENSOES:
        destino = os.path.join(pasta_origem, categoria)
        os.makedirs(destino, exist_ok=True)

def mover_arquivo_para_categoria(pasta_origem, arquivo):
    """Move um arquivo para a pasta correspondente à sua extensão."""
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
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
    criar_pastas(pasta_origem)
    for arquivo in os.listdir(pasta_origem):
        mover_arquivo_para_categoria(pasta_origem, arquivo)
    messagebox.showinfo("Concluído", "Arquivos organizados com sucesso!")

# ----------------------------- INTERFACE GRÁFICA -----------------------------

def selecionar_pasta():
    """Abre o seletor de pastas e chama a função de organização."""
    pasta = filedialog.askdirectory()
    if pasta:
        organizar_arquivos(pasta)

def configurar_janela(janela):
    """Centraliza e configura a aparência da janela."""
    janela.title("Organizador de Arquivos")
    largura, altura = 400, 200
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
    janela.resizable(False, False)

    estilo = ttk.Style()
    estilo.theme_use('clam')  # Pode testar: 'alt', 'vista', 'default', etc.

def criar_interface():
    """Cria a interface principal do aplicativo."""
    janela = tk.Tk()
    configurar_janela(janela)

    frame = ttk.Frame(janela, padding=20)
    frame.pack(expand=True)

    titulo = ttk.Label(frame, text="Organizador de Arquivos", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=(0, 10))

    instrucoes = ttk.Label(frame, text="Clique abaixo para escolher uma pasta", font=("Helvetica", 10))
    instrucoes.pack(pady=5)

    botao = ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta)
    botao.pack(pady=15)

    janela.mainloop()

# ----------------------------- MAIN -----------------------------

if __name__ == "__main__":
    criar_interface()
