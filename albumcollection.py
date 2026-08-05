"""..."""


# TODO: Create your AlbumCollection class in this file


"""
AlbumCollection class to manage a collection of Album objects.
"""

import json
from album import Album

class AlbumCollection:
    """Represent a collection of Album objects."""

    def __init__(self):
        """Initialise an empty AlbumCollection."""
        self.albums = []

    def add_album(self, album):
        """Add a single Album object to the collection."""
        self.albums.append(album)

    def get_num_required(self):
        """Get the number of required (not complete) albums."""
        return sum(1 for album in self.albums if not album.is_complete)

    def get_num_completed(self):
        """Get the number of completed albums."""
        return sum(1 for album in self.albums if album.is_complete)

    def load_albums(self, filename):
        """Load albums from a JSON file into Album objects in the list."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for album_data in data:
                    album = Album(
                        title=album_data.get('title', ''),
                        artist=album_data.get('artist', ''),
                        year=album_data.get('year', 0),
                        is_complete=album_data.get('is_complete', False)
                    )
                    self.albums.append(album)
        except FileNotFoundError:
            pass # Keep the list empty if file doesn't exist

    def save_albums(self, filename):
        """Save albums from the album list into a JSON file."""
        data = []
        for album in self.albums:
            data.append({
                'title': album.title,
                'artist': album.artist,
                'year': album.year,
                'is_complete': album.is_complete
            })
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def sort(self, sort_key):
        """Sort the album list by the given key, then by title."""
        if sort_key == 'is_complete':
            self.albums.sort(key=lambda x: (x.is_complete, x.title))
        elif sort_key == 'title':
            self.albums.sort(key=lambda x: (x.title, x.title))
        elif sort_key == 'artist':
            self.albums.sort(key=lambda x: (x.artist, x.title))
        elif sort_key == 'year':
            self.albums.sort(key=lambda x: (x.year, x.title))