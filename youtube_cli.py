"""
YouTube Video Generator CLI
Command-line interface for managing video projects
"""

import sys
import json
import logging
from pathlib import Path
from typing import Optional
from youtube_generator import (
    VideoConfig, VideoProject, CloudServices, VideoScript
)
from cloud_apis import CloudAPIManager, SearchResult

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class VideoGeneratorCLI:
    """Command-line interface for video generator"""
    
    def __init__(self):
        self.api_manager = CloudAPIManager()
        self.current_project: Optional[VideoProject] = None
    
    def print_header(self, text: str) -> None:
        """Print formatted header"""
        print("\n" + "=" * 70)
        print(f"  {text}")
        print("=" * 70 + "\n")
    
    def print_menu(self, title: str, options: dict) -> str:
        """Print menu and get user choice"""
        print(f"\n{title}")
        print("-" * 50)
        for key, value in options.items():
            print(f"  {key}) {value}")
        print("-" * 50)
        return input("Choose an option: ").strip()
    
    def create_new_project(self) -> None:
        """Create a new video project"""
        self.print_header("CREATE NEW VIDEO PROJECT")
        
        # Get project details
        title = input("📝 Video Title: ").strip()
        topic = input("🎯 Topic/Keyword: ").strip()
        description = input("📄 Description: ").strip()
        
        # Duration
        print("\nDuration options: 30, 60, 90, 120 seconds")
        duration = int(input("⏱️  Duration (seconds): "))
        
        # Style
        styles = {"1": "cinematic", "2": "casual", "3": "educational", "4": "energetic"}
        style = styles[self.print_menu("Choose video style:", 
                                      {k: v for k, v in styles.items()})]
        
        # Music vibe
        vibes = {"1": "upbeat", "2": "calm", "3": "dramatic", "4": "ambient"}
        music_vibe = vibes[self.print_menu("Choose music vibe:",
                                          {k: v for k, v in vibes.items()})]
        
        # Voiceover
        voiceover = input("Include voiceover? (y/n): ").lower() == 'y'
        
        # Create config and project
        config = VideoConfig(
            title=title,
            topic=topic,
            description=description,
            duration=duration,
            style=style,
            music_vibe=music_vibe,
            include_voiceover=voiceover
        )
        
        self.current_project = VideoProject(config)
        self.current_project.initialize_project()
        
        logger.info(f"✅ Project created: {title}")
        print(f"\n✅ Project '{title}' created successfully!")
    
    def view_script(self) -> None:
        """View generated script"""
        if not self.current_project:
            print("❌ No project loaded. Create a project first.")
            return
        
        self.print_header("VIDEO SCRIPT")
        print(self.current_project.script.script)
        
        # Save option
        if input("\nSave script to file? (y/n): ").lower() == 'y':
            filename = f"script_{self.current_project.config.title.replace(' ', '_')}.txt"
            self.current_project.script.export_script(filename)
            print(f"✅ Script saved to {filename}")
    
    def search_assets(self) -> None:
        """Search for video assets"""
        if not self.current_project:
            print("❌ No project loaded. Create a project first.")
            return
        
        self.print_header("SEARCH FOR ASSETS")
        
        asset_type = self.print_menu(
            "What type of asset are you looking for?",
            {"1": "Video", "2": "Image", "3": "Audio/Music"}
        )
        
        query = input("\n🔍 Search query: ").strip()
        
        if not query:
            print("❌ Query cannot be empty")
            return
        
        print(f"\n⏳ Searching for {['video', 'image', 'audio'][int(asset_type)-1]}s...")
        
        if asset_type == "1":  # Video
            results = self.api_manager.search_stock_videos(query, service="pixabay", limit=5)
        elif asset_type == "2":  # Image
            results = self.api_manager.search_stock_images(query, service="pexels", limit=5)
        else:  # Audio
            results = self.api_manager.search_audio(query, service="freesound", limit=5)
        
        if not results:
            print("❌ No results found. Try a different search query.")
            return
        
        self.print_header("SEARCH RESULTS")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result.title}")
            print(f"   Source: {result.source}")
            print(f"   Type: {result.media_type}")
            if result.duration:
                print(f"   Duration: {result.duration}s")
            print(f"   License: {result.license}")
            print(f"   Link: {result.url}")
        
        # Add to project
        if input("\nAdd selected asset to project? (y/n): ").lower() == 'y':
            asset_idx = int(input("Enter asset number: ")) - 1
            if 0 <= asset_idx < len(results):
                result = results[asset_idx]
                metadata = result.metadata or {}
                
                if result.media_type == "video":
                    self.current_project.assets.add_video_asset(
                        f"asset_{asset_idx}.mp4",
                        result.url,
                        metadata
                    )
                elif result.media_type == "image":
                    self.current_project.assets.add_image_asset(
                        f"asset_{asset_idx}.jpg",
                        result.url,
                        metadata
                    )
                else:
                    self.current_project.assets.add_audio_asset(
                        f"asset_{asset_idx}.mp3",
                        result.url,
                        result.duration,
                        metadata
                    )
                
                print(f"✅ Asset added to project")
    
    def view_workflow(self) -> None:
        """View complete workflow"""
        if not self.current_project:
            print("❌ No project loaded. Create a project first.")
            return
        
        self.print_header("VIDEO CREATION WORKFLOW")
        
        steps = self.current_project.get_workflow_steps()
        for step in steps:
            print(f"\n{'Step ' + str(step['step'])}: {step['title']}")
            print(f"  Description: {step['description']}")
            print(f"  Tools: {', '.join(step['tools'])}")
            print(f"  Estimated Time: {step['estimated_time']}")
    
    def view_best_practices(self) -> None:
        """View best practices"""
        if not self.current_project:
            print("❌ No project loaded. Create a project first.")
            return
        
        self.print_header("BEST PRACTICES FOR YOUTUBE VIDEOS")
        
        practices = self.current_project.get_best_practices()
        
        for category, items in practices.items():
            category_name = category.replace('_', ' ').title()
            print(f"\n{category_name}:")
            for item in items:
                print(f"  ✓ {item}")
    
    def view_resources(self) -> None:
        """View available cloud resources"""
        self.print_header("FREE CLOUD SERVICES")
        
        # Group by type
        services = CloudServices.list_all_services()
        services_by_type = {}
        
        for service in services:
            service_type = service['type']
            if service_type not in services_by_type:
                services_by_type[service_type] = []
            services_by_type[service_type].append(service)
        
        for service_type, items in services_by_type.items():
            print(f"\n📁 {service_type}:")
            for service in items:
                print(f"  • {service['name']}")
                print(f"    {service['description']}")
                print(f"    → {service['url']}")
    
    def view_project_summary(self) -> None:
        """View project summary"""
        if not self.current_project:
            print("❌ No project loaded. Create a project first.")
            return
        
        self.print_header("PROJECT SUMMARY")
        
        print(f"Title: {self.current_project.config.title}")
        print(f"Topic: {self.current_project.config.topic}")
        print(f"Duration: {self.current_project.config.duration} seconds")
        print(f"Style: {self.current_project.config.style}")
        print(f"Music Vibe: {self.current_project.config.music_vibe}")
        print(f"Voiceover: {'Yes' if self.current_project.config.include_voiceover else 'No'}")
        
        # Assets summary
        assets = self.current_project.assets.get_assets_summary()
        print(f"\n📦 Assets:")
        print(f"  Videos: {assets['videos']}")
        print(f"  Images: {assets['images']}")
        print(f"  Audio: {assets['audio']}")
        print(f"  Music: {assets['music']}")
        
        # Script summary
        script_summary = self.current_project.script.get_scenes_summary()
        print(f"\n📝 Script:")
        print(f"  Scenes: {script_summary['total_scenes']}")
        print(f"  Total Duration: {script_summary['total_duration']}s")
    
    def export_project(self) -> None:
        """Export project summary"""
        if not self.current_project:
            print("❌ No project loaded. Create a project first.")
            return
        
        filename = input("\nEnter filename (without extension): ").strip()
        if not filename:
            filename = "project_summary"
        
        filepath = f"{filename}.json"
        summary = self.current_project.export_project_summary(filepath)
        print(f"✅ Project exported to {filepath}")
    
    def show_resource_links(self) -> None:
        """Show direct links to all resources"""
        self.print_header("QUICK LINKS TO FREE TOOLS")
        
        categories = {
            'Script Writing': CloudServices.get_services_by_type('Script Writing'),
            'Stock Videos/Images': CloudServices.get_services_by_type('Stock Video/Images'),
            'AI Generation': CloudServices.get_services_by_type('AI Image Generation'),
            'AI Voiceover': CloudServices.get_services_by_type('Voiceover'),
            'Music & SFX': [
                *CloudServices.get_services_by_type('Music & SFX'),
                *CloudServices.get_services_by_type('Sound Effects & Music')
            ],
            'Video Editing': CloudServices.get_services_by_type('Video Editing'),
            'Design': CloudServices.get_services_by_type('Thumbnail Design')
        }
        
        for category, services in categories.items():
            if services:
                print(f"\n{category}:")
                for service in services:
                    print(f"  • {service['name']}")
                    print(f"    {service['url']}")
    
    def main_menu(self) -> None:
        """Main menu loop"""
        self.print_header("YOUTUBE VIDEO GENERATOR")
        print("Welcome to the YouTube Video Generator CLI!")
        print("Create professional videos using 100% free cloud tools.\n")
        
        while True:
            menu_options = {
                "1": "Create New Project",
                "2": "View Script",
                "3": "Search for Assets",
                "4": "View Workflow",
                "5": "Best Practices",
                "6": "View Resources",
                "7": "Project Summary",
                "8": "Export Project",
                "9": "Quick Links",
                "0": "Exit"
            }
            
            choice = self.print_menu("MAIN MENU", menu_options)
            
            if choice == "1":
                self.create_new_project()
            elif choice == "2":
                self.view_script()
            elif choice == "3":
                self.search_assets()
            elif choice == "4":
                self.view_workflow()
            elif choice == "5":
                self.view_best_practices()
            elif choice == "6":
                self.view_resources()
            elif choice == "7":
                self.view_project_summary()
            elif choice == "8":
                self.export_project()
            elif choice == "9":
                self.show_resource_links()
            elif choice == "0":
                print("\n👋 Thank you for using YouTube Video Generator!")
                print("Happy creating! 🎬\n")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please try again.")


def main():
    """Main entry point"""
    cli = VideoGeneratorCLI()
    
    try:
        cli.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting... Goodbye!")
        sys.exit(0)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
