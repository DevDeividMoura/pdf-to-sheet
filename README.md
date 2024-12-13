
<p align="center">
    <img src="https://raw.githubusercontent.com/DevDeividMoura/pdf-to-sheet/refs/heads/main/src/static/logo.png" align="center" width="10%">
</p>
<p align="center"><h1 align="center">PDF to Sheet</h1></p>
<p align="center"><em>Converta PDFs em planilhas de forma fácil e rápida!</em></p>

<p align="center">
    <img src="https://img.shields.io/github/license/DevDeividMoura/pdf-to-sheet?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/DevDeividMoura/pdf-to-sheet?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/count/DevDeividMoura/pdf-to-sheet?style=default&color=0080ff" alt="repo-language-count">
</p>

## Índice

- [Visão Geral](#🔮-visão-geral)
- [Demonstração](#🔮-visão-geral)
- [Funcionalidades](#☄️-funcionalidades)
- [Começando](#🛸-começando)
  - [Pré-requisitos](#📋-pré-requisitos)
  - [Instalação](#⚙️-instalação)
  - [Executando](#🚀-executando)
  - [Como Usar](#🤖-como-usar)
- [Roadmap](#🏎️💨-roadmap)
- [Contribuindo](#🔰-contribuindo)
- [Licença](#🎗-licença)

---

## 🔮 Visão Geral

O **PDF to Sheet** simplifica a conversão de relatorios PDF (Xpert) para formatos de planilha de forma fácil. Sua interface amigável permite o upload e processamento sem complicações, gerando saídas estruturadas para fácil manipulação dos dados. Ideal para profissionais que lidam com tarefas manuais de extração de dados, este projeto agiliza o processo de conversão, aumentando a produtividade e eficiência.

---

## ☄️ Funcionalidades

|  | Funcionalidade                | Resumo                                                                                       |
| :---- | :---------------------------- | :------------------------------------------------------------------------------------------- |
| ⚙️    | **Arquitetura**               | Utiliza **FastAPI** para APIs, **Pydantic** para validação e **Docker** para implantação.     |
| 🧩    | **Modularidade**              | Padrão **MVC** com módulos específicos para APIs, manipulação de arquivos e processamento.    |
| ⚡️    | **Desempenho**                | Conversão rápida com **PyPDF2** e **Pandas** para otimização de processamento de dados.       |
| 🛡️    | **Segurança**                 | Middleware **CORS**, validação de tipos de arquivo e boas práticas para proteger dados.       |
| 🌐    | **Interface Web Intuitiva**   | Interface simples para upload e análise de arquivos.                                         |
| 🔄    | **Extração e Conversão**      | Extração de dados específicos de PDFs e exportação para **CSV** e **Excel**.                 |
| 📦    | **Dependências**              | Uso de **pip** e **Docker** para ambientes consistentes e instalação de bibliotecas.          |
| 🚀    | **Escalabilidade**            | Planejado para crescimento com **FastAPI** assíncrono e escalonamento via **Docker**.         |

---
## 🛸 Começando

### 📋 Pré-requisitos

Antes de começar com pdf-to-sheet, certifique-se de que seu ambiente de execução atende aos seguintes requisitos:

- **Linguagem de Programação:** Python 3.10+
- **Gerenciador de Pacotes:** Pip
- **Tempo de Execução de Contêiner:** Docker *(Opicional)*


### ⚙️ Instalação

Instale pdf-to-sheet usando um dos seguintes métodos:

**Construir a partir do código-fonte:**

1. Clone o repositório pdf-to-sheet:
    ```sh
    ❯ git clone https://github.com/DevDeividMoura/pdf-to-sheet
    ```

2. Navegue até o diretório do projeto:
    ```sh
    ❯ cd pdf-to-sheet
    ```

3. Instale as dependências do projeto:


    **Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

    ```sh
    ❯ pip install -r requirements.txt
    ```


    **Usando `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

    ```sh
    ❯ docker compose --build
    ```

### 🚀 Executando 
Execute pdf-to-sheet usando o seguinte comando no `terminal`:


```sh
❯ chmod +x ./start.sh

❯ ./start.sh
```


**Usando `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker compose up -d
```
---
### 🤖 Como Usar

#### 💻 Via Interface Web
- Acesse a [Interface Web](http://localhost:8080) no navegador.
- Faça o upload do arquivo PDF desejado.
- Visualize os dados extraídos diretamente na interface.
- Exporte os dados para CSV ou Excel com um clique.

#### </> Via API
1. Envie um arquivo PDF para o endpoint /api/upload utilizando uma ferramenta como Postman ou curl:

    ```bash
    curl -X POST http://localhost:8080/api/v1/upload-pdf/ \
        -F "file=@seu-relatorio.pdf"
    ```

2. O retorno será um JSON com os dados extraídos:

    ```json
    {
        "success": true,
        "message": "Data extracted successfully",
        "data": [
            {
                "Data": "01/01/2024",
                "Posto": "Auto Posto",
                "Total": "230,28",
                "Placa": "STRADA (ABC-1234)",
                "Odômetro": "118466"
            },
            ...
        ]
    }
    ```
---
## 🏎️💨 Roadmap

- [ ] **`Tarefa 1`**: Suporte para múltiplos formatos de relatórios.
- [ ] **`Tarefa 2`**: Validação e tratamento de erros avançados.
- [ ] **`Tarefa 3`**: Melhorias na interface web.


---
## 🔰 Contribuindo

- **💬 [Participe das Discussões](https://github.com/DevDeividMoura/pdf-to-sheet/discussions)**: Compartilhe suas ideias, forneça feedback ou faça perguntas.
- **🐛 [Reportar Problemas](https://github.com/DevDeividMoura/pdf-to-sheet/issues)**: Submeta bugs encontrados ou registre solicitações de funcionalidades para o projeto `pdf-to-sheet`.
- **💡 [Enviar Pull Requests](https://github.com/DevDeividMoura/pdf-to-sheet/blob/main/CONTRIBUTING.md)**: Revise PRs abertas e envie seus próprios PRs.


<br>
<p align="left">
   <a href="https://github.com{/DevDeividMoura/pdf-to-sheet/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=DevDeividMoura/pdf-to-sheet">
   </a>
</p>

---
## 🎗 Licença

Lançado sob a [Licença MIT](LICENSE).

