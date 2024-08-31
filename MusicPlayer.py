class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)

    def play(self):
        if self.playlist:
            print("Playing:", self.playlist[0])
        else:
            print("No songs in the playlist.")

    def fast_forward(self):
        if len(self.playlist) > 1:
            self.playlist = self.playlist[1:] + [self.playlist[0]]
            print("Fast forwarding to the next song.")
        else:
            print("Only one song in the playlist.")

    def pause(self):
        print("Paused.")

    def stop(self):
        print("Stopped.")

    def edit_playlist(self):
        while True:
            print("1. Add song")
            print("2. Remove song")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                song = input("Enter the song name: ")
                self.add_song(song)
            elif choice == 2:
                song = input("Enter the song name: ")
                self.remove_song(song)
            elif choice == 3:
                break
            else:
                print("Invalid choice.")
