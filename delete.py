# del - statement that deletes a key-value pair based on a specified key. Can delete an entire dictionary.

# Syntax: del dictionary[key]- deletes key, del dictionary - deletes the entire dict

movie = {
    "title": "Inception",
    "casts": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
    "genre": "Science Fiction",
    "rating": 8.8 
    }

del movie

print(movie)

