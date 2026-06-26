"""
Command-line helper for rag-chunker component.

Usage:
    python test.py <path_to_text_file>
"""

import sys
import json
from rag_chunker import DocumentChunker


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python test.py <path_to_text_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    # Read the input text file
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Initialize the chunker with default settings
    chunker = DocumentChunker()
    chunks = chunker.split(text)

    # Prepare a concise output: number of chunks and a preview of each chunk
    output = {
        "num_chunks": len(chunks),
        "chunks": [c[:200] + ("..." if len(c) > 200 else "") for c in chunks],
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
