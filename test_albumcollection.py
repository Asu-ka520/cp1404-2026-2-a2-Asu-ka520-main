"""Incomplete tests for AlbumCollection class."""

from album import Album
from albumcollection import AlbumCollection

ALBUMS_FILENAME = "albums.json"


def run_tests():
    """Test empty AlbumCollection."""
    print("Test empty album collection")
    album_collection = AlbumCollection()
    assert album_collection.albums == []
    print(album_collection)

    # Test loading albums
    print("Test loading albums")
    album_collection.load_albums(ALBUMS_FILENAME)
    assert album_collection.albums
    print(album_collection)

    # Test sorting albums
    print("Test sorting - title")
    album_collection.sort("title")
    try:
        assert album_collection.albums[0].title <= album_collection.albums[1].title
    except IndexError:
        print("Not enough albums to test")
    print(album_collection)

    print("Test sorting - year")
    album_collection.sort("year")
    try:
        assert album_collection.albums[0].year <= album_collection.albums[1].year
    except IndexError:
        print("Not enough albums to test")
    print(album_collection)

    # Test adding a new Album
    print("Test adding a new Album")
    album_collection.add_album(Album("Mas Amable", "DJ Python", 2020, False))
    print(album_collection)

    # Test required and completed counts
    print("Test counts:")
    assert album_collection.get_num_required() >= 1
    assert album_collection.get_num_completed() >= 0

    # Test saving (check data file manually)
    album_collection.save_albums("test_albums_output.json")


run_tests()
