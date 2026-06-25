<div align="center">

# AutoOrganizer

### Aplicação desktop em Python para organização automática de arquivos

<a href="https://github.com/StellaKarolinaNunes/AutoOrganizer">
  <img src="./assets/images/Banner.png" alt="Banner do projeto AutoOrganizer" width="100%">
</a>

<br>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">

<img src="https://img.shields.io/badge/Tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter">

<img src="https://img.shields.io/badge/Desktop%20App-4B5563?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Desktop App">

<img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-F59E0B?style=for-the-badge" alt="Status do projeto">

<br><br>

<p align="center">
  <a href="https://github.com/StellaKarolinaNunes/AutoOrganizer">
    <img src="https://img.shields.io/badge/⌘%20Explorar%20Código--Fonte-181717?style=for-the-badge&logo=github&logoColor=white" alt="Explorar Código-Fonte">
  </a>
  <a href="https://github.com/user-attachments/assets/2a61656b-e2c3-4d83-9cf1-fe0e8c23369a">
    <img src="https://img.shields.io/badge/▶%20Ver%20Gravação%20do%20Projeto-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Ver Gravação do Projeto">
  </a>
</p>

</div>

---

## Sobre o projeto

O **AutoOrganizer** é uma aplicação desktop desenvolvida em **Python** para automatizar a organização de arquivos em diretórios.

A ferramenta permite selecionar uma pasta e organizar automaticamente seus arquivos em subpastas categorizadas, como **Imagens**, **Documentos**, **Vídeos**, **Áudios**, **Códigos** e **Outros**.

O projeto foi criado com foco em produtividade, organização digital e experiência do usuário. A interface gráfica foi construída com **Tkinter** e utiliza uma estrutura modular para separar a lógica de organização, configurações, estilos e interface visual.

> Este projeto foi desenvolvido para fins educacionais e de portfólio, com foco em automação de tarefas, organização de código em Python e criação de interfaces desktop.

---

## Objetivo

O AutoOrganizer busca reduzir o tempo gasto na organização manual de arquivos.

Em vez de mover documentos, imagens e vídeos um por um, o usuário pode selecionar uma pasta e permitir que o sistema identifique automaticamente as extensões dos arquivos, criando categorias apropriadas e movendo cada item para o local correspondente.

A proposta é oferecer uma solução simples, intuitiva e útil para manter pastas pessoais, acadêmicas ou profissionais mais organizadas.

---

## Funcionalidades

* **Seleção de Pasta:** permite escolher o diretório que será organizado.
* **Organização Automática:** identifica arquivos e move cada item para sua categoria correspondente.
* **Criação de Pastas:** gera automaticamente subpastas de acordo com os tipos de arquivo encontrados.
* **Categorias Inteligentes:** organiza arquivos em grupos como Imagens, Documentos, Vídeos, Áudios, Códigos e Outros.
* **Suporte a Extensões Diversas:** reconhece diferentes formatos de arquivos.
* **Interface Gráfica:** aplicação desktop com interface desenvolvida em Tkinter.
* **Feedback Visual:** apresenta informações para orientar o usuário durante a organização.
* **Sistema de Logs:** estrutura preparada para registrar movimentações e atividades realizadas.
* **Código Modular:** separação entre interface, lógica de negócio, configurações e utilitários.
* **Tratamento de Arquivos Desconhecidos:** extensões não identificadas são direcionadas para a pasta `OUTROS`.

---

## Tecnologias utilizadas

| Tecnologia  | Aplicação no projeto                       |
| ----------- | ------------------------------------------ |
| Python      | Linguagem principal da aplicação           |
| Tkinter     | Construção da interface gráfica            |
| ttk         | Componentes visuais aprimorados            |
| os          | Manipulação de caminhos e diretórios       |
| shutil      | Movimentação de arquivos                   |
| PyInstaller | Empacotamento da aplicação para executável |
| Git         | Controle de versão                         |

---

## Destaques técnicos

* Arquitetura organizada por camadas e responsabilidades;
* Separação entre lógica de arquivos, interface gráfica e configurações;
* Uso de módulos reutilizáveis para facilitar manutenção;
* Estrutura preparada para testes unitários;
* Categorias de arquivos centralizadas em arquivo específico;
* Sistema preparado para logs de movimentação;
* Estilos, cores e fontes organizados separadamente;
* Estrutura preparada para expansão futura com novos recursos.

---

## Demonstração

<div align="center">

![Gravação do AutoOrganizer](https://github.com/user-attachments/assets/2a61656b-e2c3-4d83-9cf1-fe0e8c23369a)

</div>

---

## Estrutura do projeto

```bash
AutoOrganizer/
├── assets/
│   ├── images/
│   │   └── Banner.png
│   │
│   ├── styles/
│   │   ├── colors.py
│   │   ├── fonts.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── src/
│   ├── core/
│   │   ├── file_organizer.py
│   │   ├── logger.py
│   │   └── __init__.py
│   │
│   ├── gui/
│   │   ├── main_window.py
│   │   ├── widgets/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── file_types.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── tests/
│   └── testes-unitarios/
│
├── AutoOrganizer.py
├── requirements.txt
├── README.md
└── LICENSE
```

> Pastas geradas durante a execução ou empacotamento da aplicação, como `build/`, `dist/` e `__pycache__/`, não aparecem na estrutura principal porque não devem ser versionadas no Git.

---

## Como executar o projeto

### Pré-requisitos

Antes de iniciar, é necessário ter instalado:

* Python `3.7` ou superior;
* Git;
* Tkinter;
* Terminal ou editor compatível com Python;
* VS Code, PyCharm ou outra IDE de sua preferência.

### 1. Clone o repositório

```bash
git clone https://github.com/StellaKarolinaNunes/AutoOrganizer.git
```

### 2. Acesse a pasta do projeto

```bash
cd AutoOrganizer
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python AutoOrganizer.py
```

Em alguns sistemas Linux, pode ser necessário utilizar:

```bash
python3 AutoOrganizer.py
```

---

## Gerar executável

### Windows

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed AutoOrganizer.py
```

O executável será gerado na pasta:

```bash
dist/
```

### Linux

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed AutoOrganizer.py
```

Depois, execute o arquivo gerado dentro da pasta `dist/`.

---

## Roadmap

### Interface e experiência do usuário

* [x] Interface gráfica organizada com Tkinter;
* [x] Separação entre estilos, fontes e cores;
* [ ] Alternância entre tema claro e escuro;
* [ ] Suporte a arrastar e soltar pastas na interface;
* [ ] Barra de progresso durante a organização;
* [ ] Histórico visual de arquivos movidos;
* [ ] Melhorias de acessibilidade na interface.

### Funcionalidades principais

* [x] Organização automática por extensão;
* [x] Criação de pastas por categoria;
* [x] Tratamento de arquivos não identificados;
* [ ] Criação de categorias personalizadas;
* [ ] Configuração de extensões por categoria;
* [ ] Visualização dos arquivos antes da confirmação;
* [ ] Função de desfazer última organização;
* [ ] Proteção contra sobrescrita de arquivos com nomes iguais.

### Recursos avançados

* [ ] Organização agendada de diretórios;
* [ ] Histórico completo de movimentações;
* [ ] Exportação de logs em `.txt`, `.csv` ou `.json`;
* [ ] Filtros para ignorar arquivos e pastas específicas;
* [ ] Sistema de backup antes de movimentações;
* [ ] Suporte a múltiplos diretórios monitorados;
* [ ] Empacotamento oficial para Windows e Linux.

---

## Contribuição

Contribuições são bem-vindas.

```bash
# Faça um fork do projeto

# Crie uma branch para sua funcionalidade
git checkout -b feature/nova-funcionalidade

# Faça suas alterações
git add .

# Crie um commit descritivo
git commit -m "feat: adiciona nova funcionalidade"

# Envie sua branch
git push origin feature/nova-funcionalidade
```

Depois, abra um Pull Request explicando as alterações realizadas.

### Diretrizes

* Mantenha o código organizado e legível;
* Utilize nomes claros para arquivos, funções e classes;
* Preserve a separação entre interface e lógica de negócio;
* Teste as funcionalidades antes de enviar alterações;
* Atualize a documentação quando necessário;
* Evite adicionar arquivos temporários, builds ou executáveis ao repositório.

---

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

```text
MIT License

Você pode usar, modificar e distribuir este projeto,
desde que mantenha os créditos e a referência ao repositório original.
```

---

## Créditos

* **Desenvolvimento:** [Stella Karolina Nunes](https://github.com/StellaKarolinaNunes)
* **Linguagem:** [Python](https://www.python.org/)
* **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html)
* **Componentes Visuais:** [ttk](https://docs.python.org/3/library/tkinter.ttk.html)
* **Manipulação de Arquivos:** [os](https://docs.python.org/3/library/os.html) e [shutil](https://docs.python.org/3/library/shutil.html)
* **Empacotamento:** [PyInstaller](https://pyinstaller.org/)
* **Badges:** [Shields.io](https://shields.io/)
* **Ícones:** [Simple Icons](https://simpleicons.org/)
