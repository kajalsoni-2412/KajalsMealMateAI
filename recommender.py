import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_meals(meal_type, cuisine, diet, goal, mood):

    data = pd.read_csv("meals.csv")

    # Strict Filtering
    filtered_data = data[
        (data["meal_type"].str.lower() == meal_type.lower()) &
        (data["diet"].str.lower() == diet.lower()) &
        (data["cuisine"].str.lower() == cuisine.lower())
    ]

    # No matching meals
    if filtered_data.empty:
        return None

    filtered_data = filtered_data.copy()

    # User Preference
    user_input = f"{goal} {mood}".lower()

    # Features for similarity
    meal_features = (
        filtered_data["goal"].str.lower()
        + " "
        + filtered_data["mood"].str.lower()
    ).tolist()

    meal_features.append(user_input)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(meal_features)

    user_vector = tfidf_matrix[-1]
    meal_vectors = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(
        user_vector,
        meal_vectors
    )

    filtered_data["score"] = similarity_scores[0]

    recommendations = filtered_data.sort_values(
        by="score",
        ascending=False
    )

    return recommendations.head(
        min(5, len(recommendations))
    )