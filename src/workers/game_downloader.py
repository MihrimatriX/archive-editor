import os
from typing import List, Optional, Set
from PySide6.QtWidgets import QWidget
from src.workers.base import BaseDownloaderThread
from src.api.twitch import TwitchAPI
from src.api.steam import SteamAPI

class GameDownloaderThread(BaseDownloaderThread):
    def __init__(self, games: List[str], twitch_api: TwitchAPI, steam_api: SteamAPI, parent: Optional[QWidget] = None) -> None:
        super().__init__(games, twitch_api, parent)
        self.twitch_api: TwitchAPI = twitch_api
        self.steam_api: SteamAPI = steam_api
        self.output_dir: str = "Oyunlar"

    def run(self) -> None:
        failed_items: List[str] = []
        downloaded_hashes: Set[str] = set()
        self.log_signal.emit("Oyun kapak indirme işlemi başladı...", "normal")

        for game_name in self.items:
            game_id: Optional[str] = self.twitch_api.search(game_name)
            cover_url: Optional[str] = self.twitch_api.get_cover_url(game_id)

            if not cover_url:
                self.log_signal.emit(f"Twitch'te bulunamadı, Steam deneniyor: {game_name}", "normal")
                game_id = self.steam_api.search(game_name)
                if game_id:
                    self.log_signal.emit(f"Steam'de bulundu (ID: {game_id}), kapak aranıyor...", "normal")
                cover_url = self.steam_api.get_cover_url(game_id)

            if not cover_url or not self._download_cover(game_name, cover_url):
                self.log_signal.emit(f"× {game_name} için kapak bulunamadı.", "kirmizi")
                failed_items.append(game_name)
                continue

            file_path: str = os.path.join(self.output_dir, f"{game_name}.jpg")
            hash_value: str = self._create_hash(file_path)

            if hash_value in downloaded_hashes:
                os.remove(file_path)
                self.log_signal.emit(f"× {game_name} tekrar eden görsel.", "kirmizi")
                failed_items.append(game_name)
            else:
                downloaded_hashes.add(hash_value)
                self.log_signal.emit(f"✓ {game_name} indirildi.", "normal")

        self.finished_signal.emit(failed_items)