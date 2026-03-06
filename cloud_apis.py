"""
Cloud Service API Integrations
Handlers for connecting to and using free cloud APIs
"""

import os
import json
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
import requests
from urllib.parse import urlencode

logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    """Represents a search result from a cloud service"""
    title: str
    url: str
    source: str
    media_type: str  # video, image, audio
    duration: Optional[int] = None  # in seconds
    credit: Optional[str] = None
    license: Optional[str] = None
    metadata: Dict = None
    
    def to_dict(self) -> Dict:
        return asdict(self)


class CloudServiceAPI(ABC):
    """Abstract base class for cloud service APIs"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.service_name = self.__class__.__name__
    
    @abstractmethod
    def search_videos(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for videos"""
        pass
    
    @abstractmethod
    def search_images(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for images"""
        pass
    
    @abstractmethod
    def search_audio(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for audio/music"""
        pass


class PexelsAPI(CloudServiceAPI):
    """Pexels API Integration - Free stock videos and images"""
    
    API_BASE = "https://api.pexels.com/v1"
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.api_key = api_key or os.getenv('PEXELS_API_KEY')
    
    def _make_request(self, endpoint: str, params: Dict) -> Dict:
        """Make API request to Pexels"""
        headers = {"Authorization": self.api_key} if self.api_key else {}
        url = f"{self.API_BASE}{endpoint}"
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Pexels API error: {e}")
            return {}
    
    def search_videos(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for videos on Pexels"""
        params = {"query": query, "per_page": limit}
        data = self._make_request("/videos/search", params)
        
        results = []
        for video in data.get("videos", []):
            result = SearchResult(
                title=query,
                url=video.get("url"),
                source="Pexels",
                media_type="video",
                duration=video.get("duration"),
                credit=video.get("photographer"),
                license="Free (CC0)",
                metadata={
                    "width": video.get("width"),
                    "height": video.get("height"),
                    "video_files": video.get("video_files")
                }
            )
            results.append(result)
        
        return results
    
    def search_images(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for images on Pexels"""
        params = {"query": query, "per_page": limit}
        data = self._make_request("/search", params)
        
        results = []
        for photo in data.get("photos", []):
            result = SearchResult(
                title=photo.get("alt"),
                url=photo.get("src", {}).get("medium"),
                source="Pexels",
                media_type="image",
                credit=photo.get("photographer"),
                license="Free (CC0)",
                metadata={
                    "width": photo.get("width"),
                    "height": photo.get("height"),
                    "download_url": photo.get("url")
                }
            )
            results.append(result)
        
        return results
    
    def search_audio(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Pexels does not provide audio search"""
        logger.warning("Pexels API does not support audio search")
        return []


class PixabayAPI(CloudServiceAPI):
    """Pixabay API Integration - Free videos and images"""
    
    API_BASE = "https://pixabay.com/api"
    VIDEO_API_BASE = "https://pixabay.com/api/videos"
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.api_key = api_key or os.getenv('PIXABAY_API_KEY')
    
    def _make_request(self, url: str, params: Dict) -> Dict:
        """Make API request to Pixabay"""
        params["key"] = self.api_key
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Pixabay API error: {e}")
            return {}
    
    def search_videos(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for videos on Pixabay"""
        params = {"q": query, "per_page": limit}
        data = self._make_request(self.VIDEO_API_BASE, params)
        
        results = []
        for video in data.get("hits", []):
            result = SearchResult(
                title=query,
                url=video.get("pageURL"),
                source="Pixabay",
                media_type="video",
                credit=video.get("user"),
                license="Free (Pixabay License)",
                metadata={
                    "videos": video.get("videos"),
                    "views": video.get("views")
                }
            )
            results.append(result)
        
        return results
    
    def search_images(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for images on Pixabay"""
        params = {"q": query, "per_page": limit, "image_type": "photo"}
        data = self._make_request(self.API_BASE, params)
        
        results = []
        for image in data.get("hits", []):
            result = SearchResult(
                title=image.get("tags"),
                url=image.get("webformatURL"),
                source="Pixabay",
                media_type="image",
                credit=image.get("user"),
                license="Free (Pixabay License)",
                metadata={
                    "download_url": image.get("download"),
                    "views": image.get("views"),
                    "downloads": image.get("downloads")
                }
            )
            results.append(result)
        
        return results
    
    def search_audio(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Pixabay does not provide audio search"""
        logger.warning("Pixabay API does not support audio search")
        return []


class FreesoundAPI(CloudServiceAPI):
    """Freesound API Integration - Free sound effects and music"""
    
    API_BASE = "https://freesound.org/apiv2"
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.api_key = api_key or os.getenv('FREESOUND_API_KEY')
    
    def _make_request(self, endpoint: str, params: Dict) -> Dict:
        """Make API request to Freesound"""
        headers = {"Authorization": f"Token {self.api_key}"} if self.api_key else {}
        url = f"{self.API_BASE}{endpoint}"
        params["format"] = "json"
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Freesound API error: {e}")
            return {}
    
    def search_audio(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Search for audio/sound effects on Freesound"""
        params = {"query": query, "page_size": limit, "sort": "rating"}
        data = self._make_request("/search/text/", params)
        
        results = []
        for sound in data.get("results", []):
            result = SearchResult(
                title=sound.get("name"),
                url=sound.get("url"),
                source="Freesound",
                media_type="audio",
                duration=int(sound.get("duration", 0)),
                credit=sound.get("username"),
                license=sound.get("license"),
                metadata={
                    "download_url": sound.get("download"),
                    "rating": sound.get("rating"),
                    "views": sound.get("num_downloads")
                }
            )
            results.append(result)
        
        return results
    
    def search_videos(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Freesound does not provide video search"""
        logger.warning("Freesound API does not support video search")
        return []
    
    def search_images(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Freesound does not provide image search"""
        logger.warning("Freesound API does not support image search")
        return []


class ElevenlabsAPI(CloudServiceAPI):
    """ElevenLabs API Integration - AI Voiceover generation"""
    
    API_BASE = "https://api.elevenlabs.io"
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY')
    
    def get_available_voices(self) -> List[Dict]:
        """Get list of available voices"""
        headers = {"xi-api-key": self.api_key} if self.api_key else {}
        
        try:
            response = requests.get(
                f"{self.API_BASE}/v1/voices",
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json().get("voices", [])
        except requests.exceptions.RequestException as e:
            logger.error(f"ElevenLabs API error: {e}")
            return []
    
    def generate_speech(self, text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM",
                       model_id: str = "eleven_monolingual_v1") -> Optional[bytes]:
        """Generate speech from text"""
        if not self.api_key:
            logger.warning("ElevenLabs API key not configured")
            return None
        
        headers = {"xi-api-key": self.api_key, "Content-Type": "application/json"}
        data = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        
        try:
            response = requests.post(
                f"{self.API_BASE}/v1/text-to-speech/{voice_id}",
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"ElevenLabs speech generation error: {e}")
            return None
    
    def search_videos(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Not applicable for ElevenLabs"""
        return []
    
    def search_images(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Not applicable for ElevenLabs"""
        return []
    
    def search_audio(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Not applicable for ElevenLabs"""
        return []


class GoogleTTSAPI(CloudServiceAPI):
    """Google Text-to-Speech API Integration"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
    
    def get_available_voices(self) -> List[Dict]:
        """Get list of available voices from Google"""
        return [
            {"name": "en-US-Standard-A", "language": "English (US)", "gender": "Female"},
            {"name": "en-US-Standard-B", "language": "English (US)", "gender": "Male"},
            {"name": "en-GB-Standard-A", "language": "English (UK)", "gender": "Female"},
            {"name": "en-AU-Standard-A", "language": "English (AU)", "gender": "Female"},
        ]
    
    def generate_speech(self, text: str, voice_name: str = "en-US-Standard-A") -> Optional[bytes]:
        """Generate speech using Google TTS"""
        if not self.api_key:
            logger.warning("Google API key not configured")
            return None
        
        url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={self.api_key}"
        
        body = {
            "input": {"text": text},
            "voice": {
                "languageCode": "en-US",
                "name": voice_name
            },
            "audioConfig": {
                "audioEncoding": "MP3"
            }
        }
        
        try:
            response = requests.post(url, json=body, timeout=30)
            response.raise_for_status()
            
            audio_content = response.json().get("audioContent")
            if audio_content:
                import base64
                return base64.b64decode(audio_content)
        except requests.exceptions.RequestException as e:
            logger.error(f"Google TTS error: {e}")
        
        return None
    
    def search_videos(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Not applicable for Google TTS"""
        return []
    
    def search_images(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Not applicable for Google TTS"""
        return []
    
    def search_audio(self, query: str, limit: int = 10) -> List[SearchResult]:
        """Not applicable for Google TTS"""
        return []


class CloudAPIManager:
    """Manager for multiple cloud service APIs"""
    
    def __init__(self):
        self.services: Dict[str, CloudServiceAPI] = {}
        self._initialize_apis()
    
    def _initialize_apis(self) -> None:
        """Initialize all available API clients"""
        self.services["pexels"] = PexelsAPI()
        self.services["pixabay"] = PixabayAPI()
        self.services["freesound"] = FreesoundAPI()
        self.services["elevenlabs"] = ElevenlabsAPI()
        self.services["google_tts"] = GoogleTTSAPI()
    
    def search_stock_videos(self, query: str, service: str = "pexels",
                           limit: int = 10) -> List[SearchResult]:
        """Search for stock videos"""
        if service in self.services:
            return self.services[service].search_videos(query, limit)
        return []
    
    def search_stock_images(self, query: str, service: str = "pexels",
                           limit: int = 10) -> List[SearchResult]:
        """Search for stock images"""
        if service in self.services:
            return self.services[service].search_images(query, limit)
        return []
    
    def search_audio(self, query: str, service: str = "freesound",
                    limit: int = 10) -> List[SearchResult]:
        """Search for audio/music"""
        if service in self.services:
            return self.services[service].search_audio(query, limit)
        return []
    
    def search_all_services(self, query: str, media_type: str = "video") -> Dict[str, List[SearchResult]]:
        """Search across all available services"""
        results = {}
        
        if media_type in ["video", "all"]:
            for service_name, service in self.services.items():
                try:
                    video_results = service.search_videos(query, limit=5)
                    if video_results:
                        results[f"{service_name}_videos"] = video_results
                except Exception as e:
                    logger.error(f"Error searching {service_name}: {e}")
        
        if media_type in ["image", "all"]:
            for service_name, service in self.services.items():
                try:
                    image_results = service.search_images(query, limit=5)
                    if image_results:
                        results[f"{service_name}_images"] = image_results
                except Exception as e:
                    logger.error(f"Error searching {service_name}: {e}")
        
        if media_type in ["audio", "all"]:
            for service_name, service in self.services.items():
                try:
                    audio_results = service.search_audio(query, limit=5)
                    if audio_results:
                        results[f"{service_name}_audio"] = audio_results
                except Exception as e:
                    logger.error(f"Error searching {service_name}: {e}")
        
        return results
    
    def generate_voiceover(self, text: str, service: str = "google_tts",
                          voice: Optional[str] = None) -> Optional[bytes]:
        """Generate voiceover using specified service"""
        if service == "elevenlabs" and "elevenlabs" in self.services:
            voice_id = voice or "21m00Tcm4TlvDq8ikWAM"
            return self.services["elevenlabs"].generate_speech(text, voice_id)
        elif service == "google_tts" and "google_tts" in self.services:
            voice_name = voice or "en-US-Standard-A"
            return self.services["google_tts"].generate_speech(text, voice_name)
        
        logger.warning(f"Service {service} not available")
        return None


def demo_api_usage():
    """Demonstrate API usage"""
    logger.info("=" * 60)
    logger.info("Cloud API Integration Demo")
    logger.info("=" * 60)
    
    manager = CloudAPIManager()
    
    # Search for stock videos
    logger.info("\n📹 Searching for stock videos...")
    videos = manager.search_stock_videos("nature", service="pixabay", limit=3)
    logger.info(f"Found {len(videos)} videos")
    for video in videos[:2]:
        logger.info(f"  • {video.title} - {video.source}")
    
    # Search for stock images
    logger.info("\n📷 Searching for stock images...")
    images = manager.search_stock_images("sunset", service="pexels", limit=3)
    logger.info(f"Found {len(images)} images")
    for image in images[:2]:
        logger.info(f"  • {image.title} - {image.source}")
    
    # Search for audio
    logger.info("\n🎵 Searching for audio/music...")
    audio = manager.search_audio("upbeat", service="freesound", limit=3)
    logger.info(f"Found {len(audio)} audio files")
    for sound in audio[:2]:
        logger.info(f"  • {sound.title} - {sound.source}")
    
    # Get available voices
    logger.info("\n🎤 Available Google TTS Voices:")
    tts = GoogleTTSAPI()
    voices = tts.get_available_voices()
    for voice in voices:
        logger.info(f"  • {voice['name']} ({voice['gender']})")
    
    logger.info("\n" + "=" * 60)
    logger.info("Demo completed successfully!")
    logger.info("=" * 60)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    demo_api_usage()
