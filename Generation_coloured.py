from colorama import Fore, Style, init
import random

def main():
    init(autoreset=True)
    print("\n🎬 Welcome to the Movie Personality Analyzer! 🎬")
    print("---------------------------------------------")
    year = int(input("\nWhich year are you born? "))
    height = float(input("What is your height (in cm)? "))
    weight = float(input("What is your weight (in kg)? "))
    country = input("Which country are you from? ")
    education = input("What is your level of education? ")
    hobbies = input("What are your hobbies? ")

    if 1883 <= year <= 1900:
        generation = "Lost Generation"
        color = Fore.RED
    elif 1901 <= year <= 1927:
        generation = "The Greatest Generation"
        color = Fore.MAGENTA
    elif 1928 <= year <= 1945:
        generation = "The Silent Generation"
        color = Fore.CYAN
    elif 1946 <= year <= 1964:
        generation = "Baby Boomers"
        color = Fore.GREEN
    elif 1965 <= year <= 1980:
        generation = "Generation X"
        color = Fore.WHITE
    elif 1981 <= year <= 1996:
        generation = "Millennials"
        color = Fore.YELLOW
    elif 1997 <= year <= 2012:
        generation = "Generation Z"
        color = Fore.BLUE
    elif year >= 2013:
        generation = "Generation Alpha"
        color = Fore.LIGHTRED_EX
    else:
        generation = "You are out!"
        color = Style.RESET_ALL

    print(f"\n{color}You are from: {generation}{Style.RESET_ALL}")

    with open("results.txt", "a") as file:
        file.write(f"User born in {year} -> {generation}\n")

    mood = input("\nWhat's your current mood? (e.g. relaxed, adventurous, romantic, curious): ").lower()

    movies = {
        "USA": [
            ("The Shawshank Redemption", "You value perseverance and have a deep belief in hope and redemption."),
            ("The Godfather", "You are authoritative, loyal, and strategic in life decisions."),
            ("Inception", "You are a critical thinker, often exploring dreams vs. reality."),
            ("Forrest Gump", "You see beauty in simplicity and value life's unpredictability."),
            ("The Dark Knight", "You wrestle with morality, and justice is your core principle."),
            ("Fight Club", "You challenge societal norms and seek personal identity."),
            ("Pulp Fiction", "You appreciate chaos and originality in storytelling."),
            ("The Matrix", "You question reality and seek a deeper truth in life."),
            ("Titanic", "You are romantic, nostalgic, and deeply emotional."),
            ("Interstellar", "You are visionary, with a deep sense of purpose beyond Earth.")
        ],
        "Egypt": [
            ("The Yacoubian Building", "You are observant and driven by social justice."),
            ("El Asliyyin", "You enjoy mystery and questioning the hidden systems around you."),
            ("Terrorism and Kebab", "You use humor to tackle serious issues."),
            ("Cairo 678", "You care deeply about gender rights and modern activism."),
            ("Ibrahim Labyad", "You're tough, loyal, and believe in raw emotions.")
        ],
        "India": [
            ("3 Idiots", "You value education that empowers and inspires change."),
            ("Dangal", "You're determined, resilient, and love overcoming odds."),
            ("Lagaan", "You thrive under pressure and believe in the power of unity."),
            ("Taare Zameen Par", "You deeply empathize with the misunderstood."),
            ("Swades", "You're connected to your roots and want to make a difference.")
        ],
        "Italy": [
            ("Life is Beautiful", "You are optimistic, finding joy even in adversity."),
            ("Cinema Paradiso", "You cherish memories and the emotional power of film.")
        ],
        "UK": [
            ("The King's Speech", "You overcome fear with dignity and quiet strength."),
            ("Sherlock Holmes", "You are inquisitive, intelligent, and love solving puzzles.")
        ],
        "France": [
            ("Amélie", "You're whimsical, romantic, and deeply thoughtful."),
            ("Blue is the Warmest Colour", "You embrace emotional depth and human complexity.")
        ],
        "Spain": [
            ("Pan's Labyrinth", "You're a dreamer with a sense of justice and wonder."),
            ("The Sea Inside", "You are reflective and wrestle with freedom and ethics.")
        ]
    }

    print("\n🎞️ Here are some film suggestions:")
    print("------------------------------------")

    movie_options = []
    index = 1
    for ctry, movie_list in movies.items():
        for title, _ in movie_list:
            print(f"{index}. {title} ({ctry})")
            movie_options.append((title, ctry))
            index += 1

    choice = int(input("\nEnter the number of the movie you like: "))
    selected_movie, selected_country = movie_options[choice - 1]

    for title, message in movies[selected_country]:
        if title == selected_movie:
            movie_message = message
            break

    print(f"\nBased on your profile and your choice of '{selected_movie}',")
    print(f"{Fore.CYAN}{movie_message}{Style.RESET_ALL}")

    with open("results.txt", "a") as file:
        file.write(f"Favorite movie: {selected_movie} ({selected_country}) -> {movie_message}\n")
        file.write(f"User mood: {mood}\n\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("\nPress Enter to exit...")
