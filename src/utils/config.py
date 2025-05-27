from dataclasses import dataclass

@dataclass
class APIConfig:
    """API anahtarlarını ve yapılandırmalarını içeren sınıf."""
    twitch_client_id: str = "sdqx8fqnx9es32nd19zom0a082yqoa"
    twitch_client_secret: str = "u8163disiork64ao2iaz6wopogmfp7"
    steam_api_key: str = "F19D2670BA278623B577D2202411AFA7"
    omdb_api_key: str = "1d794710" 