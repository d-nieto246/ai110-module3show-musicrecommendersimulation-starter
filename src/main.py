"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(label: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)
    print(f"\nProfile : {label}")
    print(f"Prefs   : {user_prefs}")
    print("=" * 40)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score : {score:.2f}")
        print(f"   Why   : {explanation}")
        print("-" * 40)


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        ("Pop Fan (baseline)",        {"genre": "pop",       "mood": "happy",      "energy": 0.8}),
        ("Chill Indie",               {"genre": "indie",     "mood": "chill",      "energy": 0.3}),
        ("Workout Hip-Hop",           {"genre": "hip-hop",   "mood": "energetic",  "energy": 0.95}),
        ("Conflicting (sad + 0.9)",   {"genre": "pop",       "mood": "sad",        "energy": 0.9}),
        ("Nonexistent genre/mood",    {"genre": "classical", "mood": "nostalgic",  "energy": 0.5}),
        ("Zero energy",               {"genre": "lofi",      "mood": "chill",      "energy": 0.0}),
        ("Max energy",                {"genre": "rock",      "mood": "intense",    "energy": 1.0}),
        ("All-miss",                  {"genre": "country",   "mood": "melancholy", "energy": 0.5}),
    ]

    for label, prefs in profiles:
        print_recommendations(label, prefs, songs)


if __name__ == "__main__":
    main()
