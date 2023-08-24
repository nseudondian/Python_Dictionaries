# get() - retrieves the value associated with a given key. 

# Syntax: dict.get(key, default)
# dict.get(key)

movie = {
    "title": "Inception",
    "casts": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
    "genre": "Science Fiction",
    "rating": 8.8 
    }
   
# title = movie.get('title') 
# print(title)

# director = movie.get('director', 'Key, director, not found in the movie dictionary' )

director = movie.get('director')
print(director)
