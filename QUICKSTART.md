# YouTube Video Generator - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Installation (2 minutes)

```bash
# Install Python packages
pip install -r requirements.txt

# Optional: Set up API keys
cp .env.example .env
# Edit .env with your API keys (optional but recommended)
```

### 2. Run the CLI (1 minute)

```bash
python youtube_cli.py
```

### 3. Create Your First Project (2 minutes)

Choose option "1" from the menu and fill in:
- Video Title: "My First YouTube Video"
- Topic: "Digital Marketing"
- Duration: 600 (10 minutes)
- Style: Educational
- Music: Upbeat
- Voiceover: Yes

### 4. Start Creating!

Follow the generated workflow step-by-step.

---

## 📝 Example 1: Educational Tutorial Video

### Scenario
Creating a tutorial on "How to Learn Python for Beginners"

### Code Example
```python
from youtube_generator import VideoConfig, VideoProject
from cloud_apis import CloudAPIManager

# Step 1: Create project configuration
config = VideoConfig(
    title="Python Basics for Beginners",
    topic="Learn Python programming",
    description="Complete guide to Python fundamentals",
    duration=1200,  # 20 minutes
    style="educational",
    music_vibe="calm",
    include_voiceover=True
)

# Step 2: Initialize project
project = VideoProject(config)
project.initialize_project()

# Step 3: Generate script template
script_template = project.script.generate_script_template()
print("Script Template:")
print(script_template)

# Step 4: Add scenes
project.script.add_scene(
    "Introduction",
    duration=30,
    description="Introduce Python and what we'll cover",
    visual="Title card with Python logo",
    audio="Calm background music"
)

project.script.add_scene(
    "Variables & Data Types",
    duration=600,
    description="Explain variables, integers, strings, lists",
    visual="Screen recording of code examples",
    audio="Voiceover with background music"
)

project.script.add_scene(
    "Functions",
    duration=420,
    description="How to create and use functions",
    visual="Code examples with animations",
    audio="Voiceover"
)

project.script.add_scene(
    "Call to Action",
    duration=150,
    description="Subscribe and next steps",
    visual="End screen with subscribe button",
    audio="Uplifting music outro"
)

# Step 5: Search for assets
manager = CloudAPIManager()

# Search for background music
music = manager.search_audio("calm educational background music", limit=5)
for m in music[:3]:
    print(f"Music: {m.title} - {m.url}")

# Step 6: Add assets to project
for i, track in enumerate(music[:1]):
    project.assets.add_audio_asset(
        f"background_music_{i}.mp3",
        track.url,
        duration=track.duration
    )

# Step 7: Export project summary
summary = project.export_project_summary("python_tutorial.json")
print("\n✅ Project exported successfully!")
```

### Workflow Checklist
- [ ] Write full script using ChatGPT or Claude
- [ ] Record screen recordings of Python code
- [ ] Download background music from YouTube Audio Library
- [ ] Generate voiceover using ElevenLabs or Google TTS
- [ ] Edit video using DaVinci Resolve or CapCut
- [ ] Create thumbnail in Canva
- [ ] Upload to YouTube

---

## 🎬 Example 2: Vlog/Lifestyle Video

### Scenario
Creating a vlog about "My Day as a Software Engineer"

### Code Example
```python
from youtube_generator import VideoConfig, VideoProject
from cloud_apis import CloudAPIManager

# Configuration for casual vlog
config = VideoConfig(
    title="Day in My Life as a Software Engineer",
    topic="software engineer lifestyle vlog",
    description="Follow me through a typical workday",
    duration=900,  # 15 minutes
    style="casual",
    music_vibe="upbeat",
    include_voiceover=False  # Direct commentary
)

project = VideoProject(config)
project.initialize_project()

# Generate script (casual outline)
script = project.script.generate_script_template()

# Add scenes
project.script.add_scene(
    "Morning Routine",
    duration=120,
    description="Wake up, breakfast, commute",
    visual="Personal footage",
    audio="Upbeat background music"
)

project.script.add_scene(
    "Office & Coding",
    duration=420,
    description="Work at desk, coding, meetings",
    visual="Office footage + screen recording",
    audio="Upbeat music with commentary"
)

project.script.add_scene(
    "Lunch Break",
    duration=180,
    description="Lunch with coworkers",
    visual="Casual lunch footage",
    audio="Upbeat music"
)

project.script.add_scene(
    "Evening Project",
    duration=120,
    description="Side project work",
    visual="Personal project footage",
    audio="Upbeat music"
)

project.script.add_scene(
    "Outro & Subscribe",
    duration=60,
    description="Thank viewers",
    visual="Personal outro",
    audio="Music outro"
)

# Search for background music
manager = CloudAPIManager()
upbeat_music = manager.search_audio("upbeat vlog music", limit=10)

# Export project
project.export_project_summary("vlog_project.json")
```

### Content Tips
- Film throughout the day with your phone
- Keep footage natural and authentic
- Add text overlays for context
- Use quick transitions
- Include some B-roll from stock footage

---

## 💰 Example 3: Product Review Video

### Scenario
Reviewing a new smartphone

### Code Example
```python
from youtube_generator import VideoConfig, VideoProject

config = VideoConfig(
    title="iPhone 15 Pro Max Review - Worth Buying?",
    topic="smartphone review",
    description="Honest review of the latest iPhone with pros and cons",
    duration=600,  # 10 minutes
    style="casual",
    music_vibe="upbeat",
    include_voiceover=True
)

project = VideoProject(config)
project.initialize_project()

# Scene structure for product review
project.script.add_scene(
    "Unboxing",
    duration=120,
    description="Show product unboxing",
    visual="Unboxing footage",
    audio="Upbeat music"
)

project.script.add_scene(
    "Design & Build",
    duration=150,
    description="Review design and materials",
    visual="Product shots from different angles",
    audio="Voiceover + music"
)

project.script.add_scene(
    "Features & Performance",
    duration=180,
    description="Demonstrate key features",
    visual="Feature demonstrations",
    audio="Voiceover + music"
)

project.script.add_scene(
    "Camera Performance",
    duration=120,
    description="Test camera in different conditions",
    visual="Sample photos and videos",
    audio="Voiceover + music"
)

project.script.add_scene(
    "Pros & Cons",
    duration=90,
    description="List advantages and disadvantages",
    visual="Text overlays with graphics",
    audio="Voiceover + music"
)

project.script.add_scene(
    "Final Verdict",
    duration=60,
    description="Final recommendation",
    visual="Product shot",
    audio="Music outro"
)

# Export
project.export_project_summary("phone_review.json")
```

### Filming Tips
- Use natural lighting
- Film in 4K if possible
- Get product shots from multiple angles
- Test features in different environments
- Be honest about pros and cons

---

## 🎨 Example 4: Animation/Motion Graphics Video

### Scenario
Explaining a concept with animations

### Code Example
```python
from youtube_generator import VideoConfig, VideoProject
from cloud_apis import CloudAPIManager

config = VideoConfig(
    title="How Neural Networks Work - Explained with Animation",
    topic="artificial intelligence machine learning",
    description="Visual explanation of how neural networks function",
    duration=720,  # 12 minutes
    style="educational",
    music_vibe="dramatic",
    include_voiceover=True
)

project = VideoProject(config)
project.initialize_project()

# Scene structure with animations
project.script.add_scene(
    "Concept Introduction",
    duration=60,
    description="Introduce neural networks concept",
    visual="Animated title sequence",
    audio="Dramatic music"
)

project.script.add_scene(
    "Neural Network Basics",
    duration=180,
    description="Explain nodes and connections",
    visual="Animated neural network diagram",
    audio="Voiceover + background music"
)

project.script.add_scene(
    "Training Process",
    duration=240,
    description="How networks learn",
    visual="Animated training visualization",
    audio="Voiceover + music"
)

project.script.add_scene(
    "Real World Examples",
    duration=180,
    description="Show practical applications",
    visual="Animated examples",
    audio="Voiceover + music"
)

project.script.add_scene(
    "Conclusion & Resources",
    duration=60,
    description="Summary and next steps",
    visual="Animated conclusion",
    audio="Dramatic music outro"
)

# Search for background music
manager = CloudAPIManager()
dramatic_music = manager.search_audio("dramatic educational music", limit=5)

# Export project
project.export_project_summary("animation_project.json")
```

### Animation Tools
- Blender (free 3D animation)
- Manim (Python animation library)
- Powtoon (template-based)
- Animaker (free tier)

---

## 📊 Step-by-Step Workflow Example

### Complete Project Flow

```python
#!/usr/bin/env python3
"""
Complete YouTube Video Generation Workflow
"""

from youtube_generator import VideoConfig, VideoProject
from cloud_apis import CloudAPIManager
import json

def create_complete_video_project():
    """Step-by-step complete project creation"""
    
    print("=" * 60)
    print("YOUTUBE VIDEO GENERATOR - COMPLETE WORKFLOW")
    print("=" * 60)
    
    # STEP 1: Create Configuration
    print("\n📝 STEP 1: Creating project configuration...")
    config = VideoConfig(
        title="The Ultimate Guide to Remote Work",
        topic="remote work productivity",
        description="Complete guide to working from home effectively",
        duration=1200,
        style="educational",
        music_vibe="calm",
        include_voiceover=True
    )
    print("✅ Configuration created")
    
    # STEP 2: Initialize Project
    print("\n🎬 STEP 2: Initializing project...")
    project = VideoProject(config)
    project.initialize_project()
    print("✅ Project initialized")
    
    # STEP 3: Generate Script
    print("\n✍️ STEP 3: Generating script template...")
    script = project.script.generate_script_template()
    print("✅ Script template generated")
    
    # STEP 4: Add Scenes
    print("\n🎞️ STEP 4: Adding video scenes...")
    scenes_data = [
        {
            "name": "Introduction",
            "duration": 60,
            "description": "Hook and intro to remote work benefits"
        },
        {
            "name": "Setting Up Workspace",
            "duration": 240,
            "description": "How to create a productive home office"
        },
        {
            "name": "Daily Routine Tips",
            "duration": 300,
            "description": "Time management and routine building"
        },
        {
            "name": "Tools & Technology",
            "duration": 300,
            "description": "Best free and paid tools for remote workers"
        },
        {
            "name": "Health & Wellness",
            "duration": 240,
            "description": "Staying healthy while working from home"
        },
        {
            "name": "Conclusion & CTA",
            "duration": 60,
            "description": "Summary and call to action"
        }
    ]
    
    for scene in scenes_data:
        project.script.add_scene(
            scene["name"],
            scene["duration"],
            scene["description"]
        )
    
    print(f"✅ Added {len(scenes_data)} scenes")
    
    # STEP 5: Search for Assets
    print("\n🔍 STEP 5: Searching for assets...")
    manager = CloudAPIManager()
    
    # Search for background music
    print("  Searching for music...")
    music_results = manager.search_audio("calm productivity music", limit=3)
    print(f"  ✅ Found {len(music_results)} music tracks")
    
    # Add music to project
    for i, music in enumerate(music_results[:1]):
        project.assets.add_audio_asset(
            f"background_music_{i}.mp3",
            music.url,
            music.duration
        )
    
    # Step 6: View Workflow
    print("\n🎯 STEP 6: Workflow steps:")
    workflow = project.get_workflow_steps()
    for step in workflow:
        print(f"  {step['step']}. {step['title']} ({step['estimated_time']})")
    
    # STEP 7: View Best Practices
    print("\n💡 STEP 7: Best practices:")
    practices = project.get_best_practices()
    print("  Engagement Tips:")
    for tip in practices['engagement'][:3]:
        print(f"    • {tip}")
    
    # STEP 8: Export Project
    print("\n💾 STEP 8: Exporting project...")
    summary = project.export_project_summary("remote_work_guide.json")
    print("✅ Project exported to remote_work_guide.json")
    
    # STEP 9: Display Summary
    print("\n" + "=" * 60)
    print("PROJECT SUMMARY")
    print("=" * 60)
    print(f"Title: {config.title}")
    print(f"Duration: {config.duration} seconds ({config.duration // 60} min)")
    print(f"Total Scenes: {len(scenes_data)}")
    print(f"Assets: {len(project.assets.base_dir.glob('**/*'))}")
    print(f"\nEstimated Production Time: 4-6 hours")
    print(f"Total Cost: $0 (100% FREE)")
    
    # STEP 10: Next Steps
    print("\n" + "=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    print("1. ✍️ Write your full script using ChatGPT or Claude")
    print("2. 🎥 Record your video or find screen recordings")
    print("3. 📸 Download stock footage and images")
    print("4. 🎵 Download background music from YouTube Audio")
    print("5. 🎤 Generate voiceover using ElevenLabs or Google TTS")
    print("6. ✂️ Edit video using DaVinci Resolve or CapCut")
    print("7. 🎨 Design thumbnail in Canva")
    print("8. 🚀 Upload to YouTube Studio")
    print("9. 📊 Monitor analytics and engage with comments")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    create_complete_video_project()
```

### Run Complete Workflow
```bash
python workflow_example.py
```

---

## 🎯 Quick Command Reference

### Using CLI
```bash
# Start interactive CLI
python youtube_cli.py

# Create project
Select option "1" from menu

# Search assets
Select option "3" from menu

# View workflow
Select option "4" from menu
```

### Using Python
```python
# Import modules
from youtube_generator import VideoConfig, VideoProject
from cloud_apis import CloudAPIManager

# Create project
config = VideoConfig(...)
project = VideoProject(config)

# Initialize
project.initialize_project()

# Search assets
manager = CloudAPIManager()
results = manager.search_audio("query")

# Export
project.export_project_summary()
```

---

## 📚 Common Tasks

### Task: Create a Tutorial Video
```bash
python youtube_cli.py
→ Choose "1" (Create Project)
→ Style: Educational
→ Music: Calm
→ Follow CLI workflow
```

### Task: Search for Free Music
```python
from cloud_apis import CloudAPIManager
manager = CloudAPIManager()
results = manager.search_audio("upbeat vlog music")
for r in results:
    print(r.title, r.url)
```

### Task: Generate Voiceover
```python
from cloud_apis import CloudAPIManager
manager = CloudAPIManager()
audio = manager.generate_voiceover(
    "Hello and welcome to my channel!",
    service="google_tts"
)
# Save audio to file
```

---

## 🆘 Troubleshooting

### Issue: API errors
**Solution:** Make sure you have internet connection and API keys if using optional features.

### Issue: No results in search
**Solution:** Try different search terms or check if API key is configured.

### Issue: Can't generate voiceover
**Solution:** Make sure Google API key is configured in .env file.

### Issue: File not found
**Solution:** Make sure output directory exists and has write permissions.

---

## ✅ Your First Video Checklist

- [ ] Install Python and dependencies
- [ ] Clone/download this project
- [ ] Run `python youtube_cli.py`
- [ ] Create a new project
- [ ] Generate script template
- [ ] Write your full script
- [ ] Search for stock footage
- [ ] Search for background music
- [ ] Create/record video content
- [ ] Edit using free tool (CapCut/DaVinci)
- [ ] Generate voiceover
- [ ] Create thumbnail
- [ ] Upload to YouTube
- [ ] Promote on social media

---

**You're all set! Start creating your first YouTube video now! 🎬🚀**
