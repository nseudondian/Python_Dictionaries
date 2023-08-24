# Pop() - removes a key-value pair based on a specified key.

# Syntax - dictionary.pop(key, default)

movie = {
    "title": "Inception",
    "casts": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
    "genre": "Science Fiction",
    "rating": 8.8 
    }
# popped_value = movie.pop('rating')
# popped_value = movie.pop('genre')

popped_value = movie.pop('director', 'Not specified')
print(popped_value)
    