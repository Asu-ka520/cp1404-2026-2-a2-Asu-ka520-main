"""Incomplete tests for Album class."""

"""Incomplete tests for Album class."""

from album import Album

def run_tests():
    """Test Album class."""

    # Test empty album (defaults)
    print("Test empty album:")
    empty_album = Album()
    print(empty_album)
    assert empty_album.title == ""
    assert empty_album.artist == ""
    assert empty_album.year == 0
    assert empty_album.is_complete is False

    # Test initial-value album
    print("Test initial value album:")
    new_album = Album("Fetch the Bolt Cutters", "Fiona Apple", 2020, True)
    print(new_album)
    assert new_album.title == "Fetch the Bolt Cutters"
    assert new_album.artist == "Fiona Apple"
    assert new_album.year == 2020
    assert new_album.is_complete is True

    # Test mark_required() and mark_completed()
    print("Test mark_required and mark_completed:")
    new_album.mark_required()
    assert new_album.is_complete is False
    new_album.mark_completed()
    assert new_album.is_complete is True

    # Test is_vintage()
    print("Test is_vintage:")
    vintage_album = Album("Rumours", "Fleetwood Mac", 1977, True)
    modern_album = Album("1989", "Taylor Swift", 2014, False)
    assert vintage_album.is_vintage() is True
    assert modern_album.is_vintage() is False

run_tests()
