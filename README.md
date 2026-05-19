# RAGIA

Projeto de ingestão de texto que usa `docling` e `transformers` para converter documentos e gerar chunks.

## Visão geral

Este repositório contém um script de ingestão que:

- converte um arquivo de texto em um documento `docling` usando `DocumentConverter`
- usa `HybridChunker` para partir o texto em chunks
- utiliza o tokenizer do modelo `sentence-transformers/all-MiniLM-L6-v2` via `transformers`

## Estrutura do projeto

- `01_ingest.py` - script principal de ingestão e chunking.
- `pyproject.toml` - gerencia as dependências do projeto.
- `data/document.txt` - arquivo de exemplo usado para ingestão.

## Requisitos

- Python 3.13 ou superior
- Dependências instaladas a partir de `pyproject.toml`

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

O script carrega `data/document.txt`, converte o documento e gera uma lista de chunks em memória usando `HybridChunker`.

## Dependências principais

- `docling>=2.94.0`
- `transformers>=5.8.1`

## Observações

- O pipeline atual não grava os chunks em disco; ele cria `chunks = list(chuncker.chunk(doc.document))` e mantém o resultado em memória.
- Você pode estender `01_ingest.py` para salvar os chunks em arquivo, imprimir estatísticas ou integrar com um serviço de busca.
- O arquivo `README.md` é referenciado pelo `pyproject.toml` como `readme`.
