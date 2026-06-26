# rag-chunker

## Purpose  
Provide a small, reusable utility to split documents into fixed-size chunks with overlap, enabling plug‑and‑play Retrieval‑Augmented Generation (RAG) pipelines.

## Technologies  
Python, LangChain

## Installation 
Create a virtual environment in the project folder

```bash
python -m venv .venv

# Activate the environment
# macOS / Linux
source .venv/bin/activate
# Windows (cmd)
.venv\Scripts\activate.bat
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```
Install required libraries
```bash
# (Optional) Upgrade pip inside the venv
python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Usage  

The component can be used programmatically as shown below **or** through its command‑line helper `test.py`.

### Programmatic usage

```python
from rag_chunker import DocumentChunker

text = """
LangChain is a powerful framework for building applications augmented with
retrieval. It offers various text splitters that can be used to chunk
documents before embedding.
"""

chunker = DocumentChunker(chunk_size=500, chunk_overlap=50)
chunks = chunker.split(text)
print(f"Generated {len(chunks)} chunks")
for i, c in enumerate(chunks, 1):
    print(f"--- Chunk {i} ---\n{c[:100]}...")
```

### Command‑line usage

```bash
python test.py sample.txt
```

The script reads the specified text file, splits it using `DocumentChunker`, and prints the resulting chunks. It prints the number of generated chunks followed by a preview of each chunk.