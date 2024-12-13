# PDF to Sheet - Extrator de Dados de Relatórios

Este projeto foi criado para facilitar a análise de relatórios de vendas de combustíveis do sistema Xpert, permitindo que informações como data, valor, veículo e quilometragem sejam extraídas automaticamente do arquivo PDF.

Além disso, foi desenvolvida uma API simples para receber arquivos PDF e retornar os dados em formato JSON, bem como uma interface web para interação rápida e intuitiva. O projeto também suporta a exportação dos dados extraídos para arquivos CSV e Excel.

## Funcionalidades

- Extrai informações de data, valor, veículo e quilometragem de relatórios em PDF.
- API com um endpoint para envio de PDFs e recebimento dos dados em JSON.
- Interface web simples para upload e análise dos arquivos.
- Exportação dos dados extraídos para **CSV** e **Excel**.
- Fácil configuração e execução utilizando **Docker**.

## Tecnologias Utilizadas

- **Python:** Lógica de extração e construção da API.
- **FastAPI:** Framework para construção rapida de APIs robustas.
- **PyPDF2:** Biblioteca para manipulação e extração de dados de PDFs.
- **Pandas:** Para manipulação e exportação dos dados.
- **HTML/CSS + JavaScript:** Interface web simples.
- **Docker:** Para criar um ambiente isolado e garantir execução rápida e consistente.

## Instalação

Certifique-se de ter o Docker instalado em sua máquina.

1. Clone este repositório:

    ```bash
    git clone https://github.com/DevDeividMoura/pdf-to-sheet.git
    cd pdf-to-sheet
    ```

2. Construa e inicie o contêiner:

    ```bash
    docker-compose up --build
    ```

3. Acesse a interface no navegador:

- http://localhost:8080

    A API estará disponível em:

- http://localhost:8080/api/v1/upload-pdf/

## Como Usar

### Via Interface Web
- Acesse a [Interface Web](http://localhost:8080) no navegador.
- Faça o upload do arquivo PDF desejado.
- Visualize os dados extraídos diretamente na interface.
- Exporte os dados para CSV ou Excel com um clique.

### Via API
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

## Roadmap

- [ ] Suporte para múltiplos formatos de relatórios.
- [ ] Validação e tratamento de erros avançados.
- [ ] Melhorias na interface web.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Autor:
[Deivid Carvalho Moura](https://github.com/DevDeividMoura) - 
Desenvolvedor Back-End Python | Automação e APIs

---
Se precisar de ajustes, é só me avisar! 🚀

