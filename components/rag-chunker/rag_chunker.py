"""Document chunker utility for local RAG pipelines."""

from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:
    """Split textual documents into overlapping chunks."""

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initialize the chunker.

        Args:
            chunk_size: Maximum number of characters per chunk.
            chunk_overlap: Number of characters to overlap between chunks.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
        )

    def split(self, text: str) -> List[str]:
        """
        Split a document into chunks.

        Args:
            text: The raw document text.

        Returns:
            A list of chunk strings.
        """
        return self._splitter.split_text(text)