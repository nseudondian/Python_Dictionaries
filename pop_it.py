# popitem() - returns the most recently added item showing the key and value. No argument


movie = {
    "title": "Inception",
    "casts": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
    "genre": "Science Fiction",
    "rating": 8.8,
    "director": "Paul"
    }
    
# print(movie.popitem()) 

key,value = movie.popitem()

print(f"Removed key: {key} and removed value: {value}")