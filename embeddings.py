from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def get(self, sentences):
       return self.model.encode(sentences)