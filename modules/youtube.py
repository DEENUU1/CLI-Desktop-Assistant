from pytube import YouTube
from rich.table import Table 


class YoutubeDownloader:
    def __init__(self, url):
        self.url = url 
        
    def download_file(self, type):
        if type == "video":
            video = YouTube(self.url).streams.download(output_path=".")
            return video 
        elif type == "audio":
            audio = YouTube(self.url).streams.filter(only_audio=True).first().download(output_path=".")
            return audio
        else:
            return "Invalid type"
    
    def return_video_thumbnail(self):
        video = YouTube(self.url)
        return f"Thumbnail url -> {video.thumbnail_url}"
