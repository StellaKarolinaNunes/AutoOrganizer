 <h1 align="center">
       AutorOrganize
    <br />
    <br />
    <a href="https://github.com/StellaKarolinaNunes/AutoOrganizer">
     <img src="./assets/images/Banner.png " alt="AutoOrganizer Banner " width="100%">
    </a>
  </h1>

</div>

<p align="center">
  <img src="https://img.shields.io/badge/python-02569B?style=for-the-badge&logo=python&logoColor=white" alt="python">
  <img src="https://img.shields.io/badge/Status-Gratuito-green?style=for-the-badge" alt="Status">
  <a href="https://github.com/StellaKarolinaNunes/AutoOrganizer/blob/main/LICENSE"><img src="https://img.shields.io/github/license/StellaKarolinaNunes/AutoOrganizer?style=flat&logo=open-source-initiative&logoColor=white" alt="Licença"></a>
</p>

<br>

---

##  Introdução
O **AutoOrganize** é uma aplicação desenvolvida em **Python** que automatiza a organização de arquivos em pastas categorizadas por extensão. Com uma interface gráfica intuitiva construída em **Tkinter**, o programa facilita a gestão de diretórios desordenados, movendo arquivos de forma inteligente para subpastas como **IMAGENS**, **DOCUMENTOS**, **VÍDEOS** e **CÓDIGO**. A lógica é simples: ao selecionar uma pasta, o sistema varre seu conteúdo e redireciona cada item para sua categoria correspondente. Arquivos com extensões não identificadas são agrupados na pasta **OUTROS**, garantindo uma organização completa. Além de funcional, o projeto preza pela experiência do usuário, oferecendo uma interface moderna, limpa e de fácil interação.

<br>

## Por que AutoOrganize?
Manter arquivos organizados manualmente pode ser uma tarefa exaustiva e demorada. O **AutoOrganize** resolve esse problema ao oferecer:

* **Economia de Tempo:** 
* **Aumento de Produtividade:** 
* **Redução de Desordem:** 

<br>

## A Solução
O **AutoOrganize** automatiza a organização de arquivos através de um script inteligente que identifica o tipo de cada arquivo e o move para o local correto de forma instantânea.

<br>

 ## Funcionalidades Principais
*  Interface gráfica moderna e intuitiva com `Tkinter` + `ttk`
*  Criação automática de pastas por tipo de arquivo
*  Organização de arquivos por categoria

<br>

## Gravação do projeto

![Gravação](https://github.com/user-attachments/assets/2a61656b-e2c3-4d83-9cf1-fe0e8c23369a)



 ##  Estrutura de Pastas
 ```bash
AutoOrganizer/
├── assets/                        # Arquivos estáticos
│   ├── images/                    # Imagens
│   │   └── Banner.png             # O banner que criamos
│   ├── styles/                    # Estilos
│   │   ├── colors.py              # Configurações de cores
│   │   ├── fonts.py               # Configurações de fontes
│   │   └── __init__.py            # Marca a pasta como pacote
│   └── __init__.py                # Marca a pasta como pacote
├── src/                           # Código fonte
│   ├── core/                      # Lógica principal
│   │   ├── file_organizer.py      # Lógica de movimentação de arquivos
│   │   ├── logger.py              # Sistema de registro de atividades  
│   │   └── __init__.py            # Marca a pasta como pacote
│   ├── gui/                       # Interface gráfica
│   │   ├── main_window.py         # Interface gráfica principal
│   │   ├── widgets/               # Componentes customizados
│   │   │   └── __init__.py        # Futuros componentes customizados  
│   │   └── __init__.py            # Marca a pasta como pacote
│   ├── utils/                     # Utilitários
│   │   ├── config.py              # Constantes
│   │   ├── file_types.py          # Tipos de arquivos e extensões
│   │   └── __init__.py            # Marca a pasta como pacote
│   └── __init__.py                # Marca a pasta como pacote
├── tests/                         # Pasta reservada para testes unitários
├── AutoOrganizer.py               # Arquivo principal (Ponto de Entrada)
├── README.md                      # Documentação do projeto
└── requirements.txt               # Lista de dependências  
 ```

<br>
 
##  Instalação

### Pré-requisitos para Rodar AutoOrganizer na sua maquina 

* **Python** 3.7 ou superior instalado
* **Tkinter shutil, os** – Bibliotecas padrão do Python
* **Ambiente de execução:**  
* Caso não tenha um ambiente local, utilize **plataformas online** (basta clicar no nome desejado) como: 
  * [Replit](https://replit.com/languages/python3) 
  * [Google Colab](https://colab.google/) 
  * [PythonAnywhere](https://www.pythonanywhere.com/) 
  * [Trinket](https://trinket.io/features/python3) 
  * [Programiz](https://www.programiz.com/python-programming/online-compiler/)
  * [onecompiler](https://onecompiler.com/python)
  * [onlinegdb](https://www.onlinegdb.com/online_python_compiler)  
 
 <br>

 ###  Instalação Rápida

#### 1. Clone o repositório
```bash
git clone https://github.com/StellaKarolinaNunes/AutoOrganizer.git
```

#### 2. Entre na pasta
```bash
cd AutoOrganizer
```

#### 3. Execute o App
```bash
python AutoOrganizer.py
```

#### 4. Empacotar como .exe (Opcional)
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed AutoOrganizer.py
```

#### 5. Empacotar como linux
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed AutoOrganizer.py
```

> **Saiba mais**: Acesse o site oficial da documentação Python para guias completos: [ documentação do python ](https://docs.python.org/3/)

<br>

##  Roadmap

### Fase 1: Interface & UX
- [x] **Interface Modular**: Separação de lógica e estilo em arquivos distintos.
- [ ] **Tema Dark/Light**: Alternância de temas para melhor conforto visual.
- [ ] **Suporte a Drag & Drop**: Permitir arrastar a pasta diretamente para a janela.

### Fase 2: Funcionalidades Core
- [ ] **Configuração de Categorias**: Permitir que o usuário crie suas próprias pastas e defina quais extensões vão para cada uma.
- [ ] **Função Desfazer (Undo)**: Reverter a última organização feita caso o usuário se arrependa.
- [ ] **Visualização Antecipada**: Mostrar uma lista do que será movido antes de confirmar a ação.

### Fase 3: Avançado
- [ ] **Organização Agendada**: Opção para rodar o script automaticamente todos os dias às 18:00, por exemplo.
- [ ] **LOG em Arquivo**: Salvar o histórico de movimentações em um arquivo [.txt](cci:7://file:///home/stella_karolina/StudioProjects/AutoOrganizer/requirements.txt:0:0-0:0) para controle.

<br>

##  Contribuição
Contribuições são muito bem-vindas! Siga estes passos:

### Como Contribuir
1. **Fork** este repositório
2. **Clone** seu fork localmente
3. **Crie** uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`
4. **Faça** suas alterações e commits
5. **Teste** suas modificações
6. **Abra** um Pull Request detalhado

<br>

###  Diretrizes

- Código limpo e bem comentado
- Mensagens de commit claras e objetivas
- Teste todas as funcionalidades
- Mantenha a documentação atualizada
- Siga os padrões de código existentes

<br>

##  Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

``` bash
MIT License - você pode usar, modificar e distribuir livremente,
mantendo a referência ao repositório original.
```

 <br>

 ## Contato

 Se você tiver dúvidas, sugestões ou quiser saber mais sobre o projeto, entre em contato:

 - **Principais Desenvolvedores:** [Stella Karolina](https://github.com/StellaKarolinaNunes)
 - **Repositório:** [HandHelp no GitHub](https://github.com/StellaKarolinaNunes/Tcc_HandHelp)
 - **LinkedIn:** [Stella Karolina Nunes](https://www.linkedin.com/in/stella-karolina/)

 <br>

## Créditos

O **AutoOrganizer** é construído com o apoio de tecnologias e comunidades incríveis:

- **Linguagem:** [Python](https://www.python.org/)
- **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html)  
- **Manipulação de Arquivos:** [Shutil](https://docs.python.org/3/library/shutil.html) & [OS](https://docs.python.org/3/library/os.html) 
- **Badges:** [Shields.io](https://shields.io/) 
- **Empacotamento:** [PyInstaller](https://pyinstaller.org/) 
- **Assistência de Design & Estrutura:** [Antigravity](https://google.com) 
- **Ícones:** [Simple Icons](https://simpleicons.org/)

 
### Desenvolvimento Principal

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/StellaKarolinaNunes">
        <img src="https://github.com/StellaKarolinaNunes.png" width="100px" alt="Stella Karolina"/>
        <br />
        <sub><b>Stella Karolina (Desenvolvedora)</b></sub>
        <br />
      </a>
    </td>
  </tr>
</table>
 