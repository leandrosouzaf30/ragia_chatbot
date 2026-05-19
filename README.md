# RAGIA

Projeto simples para ingestão de texto usando `docling` e o `HybridChunker`.

## Visão geral

Este repositório contém um script de ingestão que carrega dados de texto e prepara chunks usando a biblioteca `docling`.

## Estrutura do projeto

- `01_ingest.py` - script principal de ingestão e preparação de texto.
- `pyproject.toml` - gerencia as dependências do projeto.
- `data/document.txt` - arquivo de exemplo usado para ingestão.

## Requisitos

- Python 3.13 ou superior
- Dependências do projeto declaradas em `pyproject.toml`

## Instalação

No diretório `ragia`, crie e ative um ambiente virtual, depois instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

## Uso

Execute o script de ingestão:

```bash
cd ragia
python 01_ingest.py
```

O script inicializa o `HybridChunker` da biblioteca `docling` e imprime uma mensagem de carregamento.

## Observações

- O `README.md` também é referenciado pelo arquivo `pyproject.toml`.
- Ajuste `01_ingest.py` para adicionar processamento adicional de texto e saída de chunks, conforme necessário.
