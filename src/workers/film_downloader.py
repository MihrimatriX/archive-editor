import os
from typing import List, Optional, Set
from PySide6.QtWidgets import QWidget
from src.workers.base import BaseDownloaderThread
from src.api.omdb import OMDbAPI

class FilmDownloaderThread(BaseDownloaderThread):
    def __init__(self, films: List[str], api: OMDbAPI, parent: Optional[QWidget] = None) -> None:
        super().__init__(films, api, parent)
        self.output_dir: str = "Filmler"

    def run(self) -> None:
        failed_items: List[str] = []
        downloaded_hashes: Set[str] = set()
        self.log_signal.emit("Film kapak indirme işlemi başladı...", "normal")

        for film_name in self.items:
            cover_url: Optional[str] = self.api.get_cover_url(film_name)
            if not cover_url or not self._download_cover(film_name, cover_url):
                self.log_signal.emit(f"× {film_name} için kapak bulunamadı.", "kirmizi")
                failed_items.append(film_name)
                continue

            file_path: str = os.path.join(self.output_dir, f"{film_name}.jpg")
            hash_value: str = self._create_hash(file_path)

            if hash_value in downloaded_hashes:
                os.remove(file_path)
                self.log_signal.emit(f"× {film_name} tekrar eden görsel.", "kirmizi")
                failed_items.append(film_name)
            else:
                downloaded_hashes.add(hash_value)
                self.log_signal.emit(f"✓ {film_name} indirildi.", "normal")

        self.finished_signal.emit(failed_items) 