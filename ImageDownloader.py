import requests

class ImageDownloader:
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def download_image(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            with open(self.output_path, 'wb') as f:
                f.write(response.content)
            print(f"Image downloaded successfully. Saved as {self.output_path}")
        else:
            print("Failed to download the image.")

def main():
    url = "https://example.com/image.jpg"
    output_path = "image.jpg"

    downloader = ImageDownloader(url, output_path)
    downloader.download_image()

if __name__ == "__main__":
    main()
