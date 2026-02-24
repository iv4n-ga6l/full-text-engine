from inverted_index import init as init_inverted_index
from tfidf_index import init as init_tfidf_index

if __name__ == "__main__":
    # Initialize the inverted index
    init_inverted_index()

    # Initialize the TF-IDF index
    init_tfidf_index()

    # Add other program startup logic here
    print("Indexes initialized successfully.")