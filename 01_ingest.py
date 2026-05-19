
# %%
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from transformers import AutoTokenizer

# %%
doc_convert = DocumentConverter()

chuncker = HybridChunker(
    tokenizer=AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2'),
    max_chunk_size=350,
)

doc = doc_convert.convert('data/document.txt')

chunks = list(chuncker.chunk(doc.document))
chunks

