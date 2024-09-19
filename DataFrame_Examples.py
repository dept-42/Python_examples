
import pandas as pd 

# DataFrame examples
entry_number = 0

# 1. "Create a Series from scratch from a list"
entry_number += 1
print(f"{entry_number}. Create a Series from scratch from a list")
print()
movies = ["Easy Rider", "Chinatown", "Five Easy Pieces", "Carnal Knowledge"]
print(f"the list is: {movies}")
print(f"moviesL: {movies}")
print()
print("Create a series with 'movie_series = pd.Series(movies)")
movie_series = pd.Series(movies)
print(f"movie_series: \n {movie_series}")
print()
print("-" * 50)
print()

# 2. "Create a Series from scratch from a list, define custom index"
entry_number += 1
print(f"{entry_number}. Create a Series from scratch from a list")
print()
movies = ["Easy Rider", "Chinatown", "Five Easy Pieces", "Carnal Knowledge"]
print(f"the list is: {movies}")
print(f"moviesL: {movies}")
print()
print("Create a series with 'movie_series = pd.Series(movies, index = [\"a\",\"b\",\"c\"]')")
movie_series = pd.Series(movies,index=["a","b","c","d"])
print(f"movie_series: \n {movie_series}")
print()
print("-" * 50)
print()

# 3. Create a DataFrame from scratch from a dictionary
entry_number += 1
print(f"{entry_number}. Create a DataFrame from scratch from a dictionary")
print()
movies_dict = {"Title":["Easy Rider", "Chinatown", "Five Easy Pieces","Carnal Knowledge"]}
print(f"the dictionary is: \n{movies_dict}")
print()
print("Create a dataframe with dictionary 'movies = pd.Series(movies)'")
movie_df = pd.DataFrame(movies_dict)
print(f"movies_df: \n {movie_df}")
print()
print("-" * 50)
print()

# 4. Create a DataFrame from scratch from a dictionary of lists
entry_number += 1
print(f"{entry_number}. Create a DataFrame from scratch from a dictionary")
print()
movies_db = {
    "Title":["Easy Rider", "Chinatown", "Five Easy Pieces","Carnal Knowledge"],
    "Year":["1969", "1974", "1970","1971"],
    "Director":["Dennis Hopper", "Roman Polanski", "Bob Rafelson","Mike Nichols"]
}
print(f"the list of dictionaries is: \n{movies_db}")
print()
print("Create a dataframe witha list of  dictionaries 'movies_db = pd.Series(movies)'")
movieDB_df = pd.DataFrame(movies_db)
print(f"movieDB_df: \n {movieDB_df}")
print()
print("-" * 50)
print()

# 4. Create a DataFrame from scratch from a list of dictionaries
entry_number += 1
print(f"{entry_number}. Create a DataFrame from scratch from a dictionary")
print()
movies_db2 = [
    {"Title" : "Chinatown", "Year" :  "1974", "Director" : "Roman Polanski"},
    {"Title" : "Five Easy Pieces", "Year" : "1970", "Director" : "Bob Rafelson"},
    {"Title" : "Carnal Knowledge", "Year" : "1971", "Director" : "Mike Nichols"}
]
print(f"the list of dictionaries is: \n{movies_db2}")
print()
print("Create a dataframe witha list of  dictionaries 'movies_db = pd.Series(movies)'")
movieDB2_df = pd.DataFrame(movies_db2)
print(f"movieDB_df: \n {movieDB2_df}")
print()
print("-" * 50)
print()