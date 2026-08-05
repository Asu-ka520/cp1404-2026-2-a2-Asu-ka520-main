"""..."""


# TODO: Create your Album class in this file


"""
Album class to represent a single music album.
"""

class Album:
    """Represent an Album object."""

    def __init__(self, title="", artist="", year=0, is_complete=False):
        """Initialise an Album instance."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_complete = is_complete

    def __str__(self):
        """Return a string representation of an Album."""
        status = " (completed)" if self.is_complete else ""
        return f"{self.title} by {self.artist} ({self.year}){status}"

    def mark_completed(self):
        """Mark the album as completed."""
        self.is_complete = True

    def mark_required(self):
        """Mark the album as required."""
        self.is_complete = False

    def is_vintage(self):
        """Determine if the album is considered vintage (released <= 1977)."""
        return self.year <= 1977