class Movie:
    def __init__(self, Title,Year,Rating,Language,local):
        self.Title= Title
        self.Year= Year
        self.Rating = Rating
        self.Language =Language
        # Below attribute are local, we can use in only class
        local =local
        print(local)

fav_movie = Movie("ACE",2025,9.5,"Telugu","AP")
my_fav_movie = Movie("Titanic",1997,10,"Telugu","TG")
print("--------")
print(fav_movie.Title)
print(fav_movie.Year)
print(fav_movie.Language)
print(fav_movie.Rating)

print("--------")
print(my_fav_movie.Title)
print(my_fav_movie.Year)
print(my_fav_movie.Language)
print(my_fav_movie.Rating)