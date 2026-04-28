import fitz
from PIL import Image

class MusicService:
    """Luokka musiikkisävellyksiä varten, jolla on nimi, kuvaus ja uniikki id."""
    def __init__(self):
        self._doc = None

    def get_music_score_image(self, file_path):

        if not file_path:
            return None

        try:
            doc = fitz.open(file_path)
            page = doc.load_page(0)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            return img

        except Exception as e:
            print(f"Error loading music score image: {e}")
            return None
