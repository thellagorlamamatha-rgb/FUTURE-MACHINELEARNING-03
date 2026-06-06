from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_description, resume):

    # Store texts
    documents = [job_description, resume]

    # Create TF-IDF object
    tfidf = TfidfVectorizer()

    # Convert text to vectors
    matrix = tfidf.fit_transform(documents)

    # Calculate similarity
    similarity_score = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    return similarity_score[0][0]