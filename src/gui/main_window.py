import tkinter as tk
from tkinter import filedialog, ttk
from src.core.file_organizer import organizar_arquivos
from assets.styles.fonts import FONT_TITLE, FONT_DEFAULT
from assets.styles.colors import THEME_NAME
from src.utils.config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TITLE_TEXT, 
    SUBTITLE_TEXT, INSTRUCTIONS_TEXT, FOOTER_TEXT
)

def selecionar_pasta():
    """Abre o seletor de pastas e chama a função de organização."""
    pasta = filedialog.askdirectory()
    if pasta:
        organizar_arquivos(pasta)

def configurar_janela(janela):
    """Centraliza e configura a aparência da janela."""
    janela.title(TITLE_TEXT)
    largura, altura = WINDOW_WIDTH, WINDOW_HEIGHT
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
    janela.resizable(False, False)

    estilo = ttk.Style()
    estilo.theme_use(THEME_NAME)

def criar_interface():
    """Cria a interface principal do aplicativo."""
    janela = tk.Tk()
    configurar_janela(janela)

    # Frame Principal
    frame = ttk.Frame(janela, padding=20)
    frame.pack(expand=True, fill="both")

    # Conteúdo
    titulo = ttk.Label(frame, text=TITLE_TEXT, font=FONT_TITLE)
    titulo.pack(pady=(0, 10))

    subtitulo = ttk.Label(frame, text=SUBTITLE_TEXT, font=FONT_DEFAULT)
    subtitulo.pack(pady=(0, 20))

    instrucoes = ttk.Label(frame, text=INSTRUCTIONS_TEXT, font=FONT_DEFAULT)
    instrucoes.pack(pady=5)

    botao = ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta)
    botao.pack(pady=15, ipadx=10, ipady=5)

    # Nota de rodapé
    rodape = ttk.Label(frame, text=FOOTER_TEXT, font=("Helvetica", 8, "italic"))
    rodape.pack(side="bottom", pady=5)

    janela.mainloop()
