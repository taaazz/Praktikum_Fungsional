from functools import reduce

# Data movies
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def show_movie_info(movie):
    print(f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}, Genre: {movie['genre']}")

def count_movies_by_genre(movies):
    genres = set(movie["genre"] for movie in movies)
    genre_counts = {genre: len([movie for movie in movies if movie["genre"] == genre]) for genre in genres}
    for genre, count in genre_counts.items():
        print(f"Jumlah Film Berdasarkan Genre '{genre}': {count}")

def average_rating_by_year(movies):
    def calculate_average(year):
        year_movies = list(filter(lambda movie: movie["year"] == year, movies))
        total_rating = sum(map(lambda movie: movie["rating"], year_movies))
        return total_rating / len(year_movies) if year_movies else 0.0

    years = set(movie["year"] for movie in movies)
    return {year: calculate_average(year) for year in years}

def find_highest_rated_movie(movies):
    return reduce(lambda x, y: x if x["rating"] > y["rating"] else y, movies)

while True:
    print("\nMenu Tugas:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    task = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if task == "1":
         count_movies_by_genre(movies)
    elif task == "2":
        average_ratings = average_rating_by_year(movies)
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        for year, average in average_ratings.items():
            print(f"Tahun {year}: {average}")
    elif task == "3":
        highest_rated_movie = find_highest_rated_movie(movies)
        print("\nFilm dengan Rating Tertinggi:")
        show_movie_info(highest_rated_movie)
    elif task == "4":
        title = input("Masukkan judul film yang ingin dicari: ")
        found_movie = next((movie for movie in movies if movie["title"].lower() == title.lower()), None)
        if found_movie:
            print("\nInformasi Film:")
            show_movie_info(found_movie)
        else:
            print("\nFilm dengan judul tersebut tidak ditemukan.")
    elif task == "5":
        print("Program Selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
