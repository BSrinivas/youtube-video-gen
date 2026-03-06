#!/usr/bin/env python3
"""
YouTube Video Generator - Demo & Testing Script
Demonstrates all features of the application
"""

import logging
from youtube_generator import (
    VideoConfig, VideoProject, CloudServices, VideoScript, AssetManager
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def demo_1_basic_project():
    """Demo 1: Create a basic video project"""
    print("\n" + "=" * 70)
    print("DEMO 1: CREATE A BASIC VIDEO PROJECT")
    print("=" * 70)
    
    # Create configuration
    config = VideoConfig(
        title="Getting Started with Python",
        topic="Python programming for beginners",
        description="Learn Python basics in 10 minutes",
        duration=600,
        style="educational",
        music_vibe="calm",
        include_voiceover=True
    )
    
    # Create project
    project = VideoProject(config)
    project.initialize_project()
    
    print(f"\n✅ Project created: {config.title}")
    print(f"   Duration: {config.duration} seconds")
    print(f"   Style: {config.style}")
    print(f"   Voiceover: {'Yes' if config.include_voiceover else 'No'}")


def demo_2_script_generation():
    """Demo 2: Generate video script"""
    print("\n" + "=" * 70)
    print("DEMO 2: GENERATE VIDEO SCRIPT")
    print("=" * 70)
    
    config = VideoConfig(
        title="Web Design Fundamentals",
        topic="Introduction to web design",
        duration=720,
        style="educational",
        music_vibe="calm"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Generate script
    script = project.script.generate_script_template()
    
    print("\n📝 Script Template Generated:")
    print("-" * 70)
    print(script[:500] + "...\n")
    print(f"Total script length: {len(script)} characters")


def demo_3_scene_management():
    """Demo 3: Manage video scenes"""
    print("\n" + "=" * 70)
    print("DEMO 3: MANAGE VIDEO SCENES")
    print("=" * 70)
    
    config = VideoConfig(
        title="Digital Marketing Tutorial",
        topic="Digital marketing basics",
        duration=900,
        style="educational",
        music_vibe="upbeat"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Add multiple scenes
    scenes = [
        ("Introduction", 60, "Introduce the topic"),
        ("Module 1: SEO Basics", 300, "Search engine optimization"),
        ("Module 2: Social Media", 240, "Social media marketing"),
        ("Module 3: Email Marketing", 240, "Email campaign strategies"),
        ("Conclusion & CTA", 60, "Wrap up and call to action")
    ]
    
    for name, duration, description in scenes:
        project.script.add_scene(name, duration, description)
    
    # Get scenes summary
    summary = project.script.get_scenes_summary()
    
    print(f"\n✅ Scenes Created: {summary['total_scenes']}")
    print(f"   Total Duration: {summary['total_duration']} seconds")
    print("\nScene List:")
    for i, scene in enumerate(summary['scenes'], 1):
        print(f"   {i}. {scene['name']} ({scene['duration']}s)")


def demo_4_asset_management():
    """Demo 4: Manage video assets"""
    print("\n" + "=" * 70)
    print("DEMO 4: MANAGE VIDEO ASSETS")
    print("=" * 70)
    
    config = VideoConfig(
        title="My First Video",
        topic="testing",
        duration=600,
        style="casual",
        music_vibe="upbeat"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Add video assets
    project.assets.add_video_asset(
        "intro.mp4",
        "https://example.com/intro.mp4",
        {"duration": 30, "resolution": "1080p"}
    )
    
    project.assets.add_video_asset(
        "main_content.mp4",
        "https://example.com/content.mp4",
        {"duration": 300, "resolution": "4K"}
    )
    
    # Add image assets
    project.assets.add_image_asset(
        "thumbnail.jpg",
        "https://example.com/thumbnail.jpg",
        {"width": 1280, "height": 720}
    )
    
    # Add audio assets
    project.assets.add_audio_asset(
        "background_music.mp3",
        "https://example.com/music.mp3",
        duration=600,
        metadata={"genre": "upbeat", "bpm": 120}
    )
    
    project.assets.add_audio_asset(
        "voiceover.mp3",
        "https://example.com/voiceover.mp3",
        duration=120,
        metadata={"voice": "female", "language": "en-US"}
    )
    
    # Get summary
    summary = project.assets.get_assets_summary()
    
    print("\n✅ Assets Added:")
    print(f"   Videos: {summary['videos']}")
    print(f"   Images: {summary['images']}")
    print(f"   Audio Files: {summary['audio']}")
    print(f"   Music Tracks: {summary['music']}")
    print(f"   Total Assets: {summary['videos'] + summary['images'] + summary['audio'] + summary['music']}")


def demo_5_workflow_guide():
    """Demo 5: View workflow guide"""
    print("\n" + "=" * 70)
    print("DEMO 5: VIDEO CREATION WORKFLOW")
    print("=" * 70)
    
    config = VideoConfig(
        title="My Awesome Video",
        topic="test",
        duration=600,
        style="casual",
        music_vibe="upbeat"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Get workflow steps
    steps = project.get_workflow_steps()
    
    print("\n📋 Complete Workflow:")
    for step in steps:
        print(f"\n   Step {step['step']}: {step['title']}")
        print(f"   └─ {step['description']}")
        print(f"   └─ Tools: {', '.join(step['tools'])}")
        print(f"   └─ Time: {step['estimated_time']}")


def demo_6_best_practices():
    """Demo 6: View best practices"""
    print("\n" + "=" * 70)
    print("DEMO 6: BEST PRACTICES FOR YOUTUBE")
    print("=" * 70)
    
    config = VideoConfig(
        title="Demo Video",
        topic="test",
        duration=600,
        style="casual",
        music_vibe="upbeat"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Get best practices
    practices = project.get_best_practices()
    
    print("\n✨ ENGAGEMENT TIPS:")
    for tip in practices['engagement']:
        print(f"   ✓ {tip}")
    
    print("\n📈 SEO OPTIMIZATION:")
    for tip in practices['seo'][:3]:
        print(f"   ✓ {tip}")
    
    print("\n❌ MISTAKES TO AVOID:")
    for mistake in practices['mistakes_to_avoid'][:3]:
        print(f"   • {mistake}")
    
    print("\n💰 MONETIZATION:")
    for step in practices['monetization'][:3]:
        print(f"   ✓ {step}")


def demo_7_cloud_services():
    """Demo 7: Explore cloud services"""
    print("\n" + "=" * 70)
    print("DEMO 7: AVAILABLE CLOUD SERVICES")
    print("=" * 70)
    
    # List all services
    all_services = CloudServices.list_all_services()
    
    print(f"\n📚 Total Services Available: {len(all_services)}\n")
    
    # Group by type
    services_by_type = {}
    for service in all_services:
        service_type = service['type']
        if service_type not in services_by_type:
            services_by_type[service_type] = []
        services_by_type[service_type].append(service)
    
    # Display by type
    for service_type in sorted(services_by_type.keys()):
        services = services_by_type[service_type]
        print(f"\n   📁 {service_type} ({len(services)} services):")
        for service in services:
            print(f"      • {service['name']}")
            print(f"        {service['description']}")


def demo_8_resource_recommendations():
    """Demo 8: Get resource recommendations"""
    print("\n" + "=" * 70)
    print("DEMO 8: RESOURCE RECOMMENDATIONS")
    print("=" * 70)
    
    config = VideoConfig(
        title="Recommendation Test",
        topic="test",
        duration=600,
        style="educational",
        music_vibe="calm"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Get recommendations
    recommendations = project.get_resource_recommendations()
    
    print("\n💡 RECOMMENDED RESOURCES:")
    
    print(f"\n   📝 For Scripts ({len(recommendations['for_script'])} services):")
    for tool in recommendations['for_script'][:2]:
        print(f"      • {tool['name']} - {tool['url']}")
    
    print(f"\n   🎨 For Visuals ({len(recommendations['for_visuals'])} services):")
    for tool in recommendations['for_visuals'][:2]:
        print(f"      • {tool['name']} - {tool['url']}")
    
    print(f"\n   🎤 For Voiceover ({len(recommendations['for_voiceover'])} services):")
    for tool in recommendations['for_voiceover'][:2]:
        print(f"      • {tool['name']} - {tool['url']}")
    
    print(f"\n   🎵 For Audio ({len(recommendations['for_audio'])} services):")
    for tool in recommendations['for_audio'][:2]:
        print(f"      • {tool['name']} - {tool['url']}")


def demo_9_project_export():
    """Demo 9: Export project"""
    print("\n" + "=" * 70)
    print("DEMO 9: EXPORT PROJECT SUMMARY")
    print("=" * 70)
    
    config = VideoConfig(
        title="Project Export Demo",
        topic="testing project export",
        duration=600,
        style="educational",
        music_vibe="calm"
    )
    
    project = VideoProject(config)
    project.initialize_project()
    
    # Add some data
    project.script.add_scene("Scene 1", 300, "First scene")
    project.assets.add_audio_asset("music.mp3", "https://example.com/music.mp3")
    
    # Export
    summary = project.export_project_summary("/tmp/demo_project.json")
    
    print("\n✅ Project exported successfully!")
    print(f"   Location: /tmp/demo_project.json")
    print(f"   Metadata: {summary['metadata']['title']}")
    print(f"   Scenes: {summary['script']['scenes_count']}")
    print(f"   Workflow Steps: {len(summary['workflow'])}")


def demo_10_complete_workflow():
    """Demo 10: Complete workflow example"""
    print("\n" + "=" * 70)
    print("DEMO 10: COMPLETE WORKFLOW EXAMPLE")
    print("=" * 70)
    
    print("\n🎬 Creating a complete video project...\n")
    
    # Step 1: Configuration
    print("   Step 1: Creating configuration...")
    config = VideoConfig(
        title="Complete Workflow Demo",
        topic="video production",
        description="Complete workflow demonstration",
        duration=900,
        style="educational",
        music_vibe="calm",
        include_voiceover=True
    )
    
    # Step 2: Initialize
    print("   Step 2: Initializing project...")
    project = VideoProject(config)
    project.initialize_project()
    
    # Step 3: Generate script
    print("   Step 3: Generating script template...")
    project.script.generate_script_template()
    
    # Step 4: Add scenes
    print("   Step 4: Adding video scenes...")
    for i in range(3):
        project.script.add_scene(f"Scene {i+1}", 300, f"Content for scene {i+1}")
    
    # Step 5: Add assets
    print("   Step 5: Adding assets...")
    project.assets.add_video_asset(f"video_{i}.mp4", "https://example.com/video.mp4")
    project.assets.add_audio_asset("music.mp3", "https://example.com/music.mp3", 600)
    
    # Step 6: Get summary
    print("   Step 6: Generating summary...")
    summary = project.get_workflow_steps()
    
    print("\n✅ Workflow Completed:")
    print(f"   Project: {config.title}")
    print(f"   Duration: {config.duration}s")
    print(f"   Scenes: 3")
    print(f"   Assets: 2")
    print(f"   Workflow Steps: {len(summary)}")


def run_all_demos():
    """Run all demonstrations"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " YOUTUBE VIDEO GENERATOR - COMPLETE DEMO & TESTING ".center(68) + "║")
    print("╚" + "=" * 68 + "╝")
    
    demos = [
        ("Basic Project Creation", demo_1_basic_project),
        ("Script Generation", demo_2_script_generation),
        ("Scene Management", demo_3_scene_management),
        ("Asset Management", demo_4_asset_management),
        ("Workflow Guide", demo_5_workflow_guide),
        ("Best Practices", demo_6_best_practices),
        ("Cloud Services", demo_7_cloud_services),
        ("Resource Recommendations", demo_8_resource_recommendations),
        ("Project Export", demo_9_project_export),
        ("Complete Workflow", demo_10_complete_workflow)
    ]
    
    for i, (name, demo_func) in enumerate(demos, 1):
        try:
            demo_func()
        except Exception as e:
            print(f"\n❌ Error in Demo {i}: {e}")
            logger.error(f"Error in demo: {e}")
    
    # Final summary
    print("\n" + "=" * 70)
    print("DEMO COMPLETE!")
    print("=" * 70)
    print("\n✅ All 10 demos completed successfully!")
    print("\n📚 Next Steps:")
    print("   1. Run: python youtube_cli.py")
    print("   2. Create your first video project")
    print("   3. Follow the generated workflow")
    print("   4. Start creating amazing YouTube videos!")
    print("\n💡 Resources:")
    print("   • README.md - Complete documentation")
    print("   • QUICKSTART.md - Practical examples")
    print("   • youtube_cli.py - Interactive interface")
    print("\n🎉 Happy Creating!\n")


if __name__ == "__main__":
    run_all_demos()
