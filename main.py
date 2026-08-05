"""
Name: Hu Zedong
Date Started: 2026/08/03
Brief Project Description: A Kivy GUI application to manage an album archive,
allowing users to add, sort, and track completed/required albums.
GitHub URL: https://github.com/Asu-ka520/cp1404-2026-2-a2-Asu-ka520-main

"""
# TODO: Create your main program in this file using the AlbumArchiveApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from albumcollection import AlbumCollection
from album import Album

ALBUMS_FILENAME = "albums.json"
COLOR_REQUIRED = (0.0, 0.306, 0.306, 1)  # 深青色，匹配截图
COLOR_COMPLETED = (0.153, 0.153, 0.153, 1)  # 深灰色，匹配截图


class AlbumArchiveApp(App):
    """Kivy App for Album Archive."""

    def __init__(self, **kwargs):
        """Initialise the app."""
        super().__init__(**kwargs)
        self.collection = AlbumCollection()

    def build(self):
        """Build the Kivy GUI."""
        Window.size = (800, 600)
        self.title = "AlbumArchive"
        self.root = Builder.load_file('app.kv')
        return self.root

    def on_start(self):
        """Load data when app starts and create widgets."""
        self.collection.load_albums(ALBUMS_FILENAME)
        self.sort_albums('Completed')
        self.root.ids.bottom_status_label.text = "Welcome to Albums Archive 2.0"

    def on_stop(self):
        """Save data when app stops."""
        self.collection.save_albums(ALBUMS_FILENAME)

    def create_album_buttons(self):
        """Create dynamic buttons for each album in the collection."""
        self.root.ids.albums_box.clear_widgets()
        for album in self.collection.albums:
            btn = Button(text=str(album), size_hint_y=None, height=60)
            btn.background_color = COLOR_COMPLETED if album.is_complete else COLOR_REQUIRED
            btn.bind(on_release=lambda b, a=album: self.handle_album_click(a))
            self.root.ids.albums_box.add_widget(btn)

        required_count = self.collection.get_num_required()
        self.root.ids.top_status_label.text = f"Albums to listen to: {required_count}"

    def handle_album_click(self, album):
        """Handle when an album button is clicked to toggle its status."""
        if album.is_complete:
            album.mark_required()
            status_text = f"You need to listen to {album.title}"
        else:
            album.mark_completed()
            status_text = f"You have listened to {album.title}"

        if album.is_vintage():
            status_text += " (Vintage!)"

        self.root.ids.bottom_status_label.text = status_text

        current_sort = self.root.ids.sort_spinner.text
        self.sort_albums(current_sort)

    def sort_albums(self, sort_key):
        """Sort the album collection and redraw the GUI."""
        key_mapping = {
            'Completed': 'is_complete',
            'Title': 'title',
            'Artist': 'artist',
            'Year': 'year'
        }
        mapped_key = key_mapping.get(sort_key, 'is_complete')
        self.collection.sort(mapped_key)
        self.create_album_buttons()

    def add_new_album(self):
        """Handle adding a new album from the input fields with error checking."""
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_str = self.root.ids.year_input.text.strip()

        if not title or not artist or not year_str:
            self.root.ids.bottom_status_label.text = "Please complete all fields."
            return

        try:
            year = int(year_str)
        except ValueError:
            self.root.ids.bottom_status_label.text = "Please enter a valid number"
            return

        new_album = Album(title, artist, year, False)
        self.collection.add_album(new_album)

        self.clear_fields()
        current_sort = self.root.ids.sort_spinner.text
        self.sort_albums(current_sort)
        self.root.ids.bottom_status_label.text = f"Successfully added {title} by {artist} ({year})"

    def clear_fields(self):
        """Clear all text input fields and bottom status."""
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.bottom_status_label.text = ""


if __name__ == '__main__':
    AlbumArchiveApp().run()