"""..."""
# TODO: Copy your first assignment to this file, commit, then refactor it to use Album and AlbumCollection classes


F"""
Console program using Album and AlbumCollection classes.
"""

import random
from album import Album
from albumcollection import AlbumCollection

FILENAME = "albums.json"

def main():
    """Main function to run the console program."""
    print("Albums Archive 2.0 by Your Name")
    collection = AlbumCollection()
    collection.load_albums(FILENAME)
    print(f"{len(collection.albums)} albums loaded from {FILENAME}")

    collection.sort('is_complete')

    while True:
        display_menu()
        choice = input(">>> ").upper().strip()

        if choice == 'D':
            display_albums(collection)
        elif choice == 'R':
            recommend_album(collection)
        elif choice == 'A':
            add_album(collection)
        elif choice == 'M':
            mark_album_completed(collection)
        elif choice == 'Q':
            collection.save_albums(FILENAME)
            print(f"{len(collection.albums)} albums saved to {FILENAME}\nHave a nice day :)")
            break
        else:
            print("Invalid menu choice")

def display_menu():
    """Display the main menu."""
    print("\nMenu:")
    print("D - Display all albums")
    print("R - Recommend a random album")
    print("A - Add a new album")
    print("M - Mark an album as completed")
    print("Q - Quit")

def display_albums(collection):
    """Display all albums in the collection."""
    if not collection.albums:
        print("No albums!")
        return

    max_title_len = max(len(album.title) for album in collection.albums)
    max_artist_len = max(len(album.artist) for album in collection.albums)

    for i, album in enumerate(collection.albums, 1):
        prefix = " " if album.is_complete else "*"
        print(f"{prefix}{i}. {album.title:<{max_title_len}} by {album.artist:<{max_artist_len}} {album.year}")

    required_count = collection.get_num_required()
    print(f"{len(collection.albums)} albums in archive. You still want to listen to {required_count} albums.")

def recommend_album(collection):
    """Recommend a random required album."""
    required_albums = [album for album in collection.albums if not album.is_complete]

    if not required_albums:
        print("No albums left to listen to!")
        return

    recommended = random.choice(required_albums)
    print("Not sure what to listen to next?")
    print(f"How about... {recommended.title} by {recommended.artist}?")

def add_album(collection):
    """Add a new album via user input."""
    title = get_valid_string("Title: ")
    artist = get_valid_string("Artist: ")
    year = get_valid_number("Year: ", low=0)

    new_album = Album(title, artist, year, False)
    collection.add_album(new_album)
    collection.sort('is_complete')
    print(f"{title} by {artist} ({year}) added to Albums Archive.")

def mark_album_completed(collection):
    """Mark a selected album as completed."""
    if collection.get_num_required() == 0:
        print("No required albums.")
        return

    display_albums(collection)
    print("Enter the number of an album to mark as completed")

    album_index = get_valid_number(">>> ", low=1, high=len(collection.albums)) - 1
    album = collection.albums[album_index]

    if album.is_complete:
        print(f"You have already completed {album.title}")
    else:
        album.mark_completed()
        collection.sort('is_complete')
        print(f"{album.title} by {album.artist} completed!")

def get_valid_string(prompt):
    """Get a non-empty string from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be blank")

def get_valid_number(prompt, low, high=None):
    """Get a valid integer from the user within a range."""
    while True:
        try:
            value = int(input(prompt))
            if value <= low - 1:
                print(f"Number must be > {low - 1}")
            elif high is not None and value > high:
                print("Invalid album number")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number")

if __name__ == '__main__':
    main()