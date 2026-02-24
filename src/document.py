class Document:
    """
    Represents a document in the full-text engine.
    
    Attributes:
        id (str): Unique identifier for the document.
        title (str): Title of the document.
        content (str): Content of the document.
    """
    def __init__(self, id: str, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

# Global variables for storing documents and indexes
# documents: A dictionary mapping document IDs to Document instances
# indexes: A dictionary mapping index names to their respective data structures

documents = {}
indexes = {}
