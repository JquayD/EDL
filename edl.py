import os
import getpass
import yt_dlp
import time

class Proksesor:
    def __init__(self)-> None:
    # Initializing the Download dir, user input will be taken in consideration
        self.name = getpass.getuser()
        self.download_path = input("Folder path: ")
        self.ensure_download_path()

    def ensure_download_path(self):
    # Parsing to make sure the inputted dir exists.
        if "~" in self.download_path:
            self.download_path = self.download_path.replace('~/', f'/home/{self.name}/')


        if not os.path.exists(self.download_path):
            print("Invalid")
            time.sleep(1)
            print("Creating dir...")
            time.sleep(3)
            os.makedirs(self.download_path)
        elif os.path.exists(self.download_path):
            pass

    def download_vid(self, url, codec):
        
        # Setting the downloader options
        ydl_opts = {
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'), # The output template of the downloaded file of the media
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', # Extracts the audio from the video
                'preferredcodec': codec,
                'preferredquality': '320',
            }],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading video from {url}...")
                ydl.download([url])
        except Exception as e:
            # Raised exception is caught as e, prints 'Error Downloading link: <error_message>'
            print(f"Error Downloading link: {e}")

    def run(self):
    # UI interface/Prompts
        print("Welcome to EDL")
        while True:
            self.download_path
            self.ensure_download_path()
            url = input("Input url (or 'exit' to quit): ")
            if url.lower() == 'exit':
                print("Leaving program...")
                break
            codec = input("Input Media format: ")
            if url:
                self.download_vid(url, codec)


if __name__ == "__main__":
    proks = Proksesor()
    proks.run()





