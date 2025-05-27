from abc import ABC, abstractmethod
from typing import Optional

class BaseAPI(ABC):
    """Tüm API sınıfları için temel sınıf."""
    
    @abstractmethod
    def search(self, query: str) -> Optional[str]:
        """Verilen sorgu için arama yapar ve sonuç döndürür."""
        pass

    @abstractmethod
    def get_cover_url(self, item_id: Optional[str]) -> Optional[str]:
        """Verilen ID için kapak URL'sini döndürür."""
        pass 