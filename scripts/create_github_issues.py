#!/usr/bin/env python3
"""
Script to create GitHub issues from ISSUES.md file.

Usage:
    python scripts/create_github_issues.py YOUR_USERNAME YOUR_TOKEN

Requirements:
    pip install requests
"""

import sys
import json
import requests
from typing import List, Dict


# Define all issues for MVP
ISSUES = [
    {
        "title": "Set up project structure and development environment",
        "body": """Initialize the project with proper structure, dependencies, and development tools.

**Tasks:**
- [ ] Create project directory structure (src/, tests/, docs/, config/)
- [ ] Set up Python virtual environment
- [ ] Create requirements.txt with core dependencies
- [ ] Create setup.py for package installation
- [ ] Set up .gitignore for Python projects
- [ ] Initialize git repository
- [ ] Create README.md with project overview
- [ ] Set up pytest for testing
- [ ] Create logging configuration
- [ ] Set up CI/CD basics (GitHub Actions)

**Acceptance Criteria:**
- Project structure matches architecture docs
- All developers can clone and run `pip install -r requirements.txt`
- Tests can be run with `pytest`
- Code quality tools configured (black, pylint, mypy)

**Estimated Time:** 1 day""",
        "labels": ["setup", "priority: high", "phase: foundation"],
        "milestone": 1
    },
    {
        "title": "Implement microphone audio capture system",
        "body": """Create a robust audio capture system that continuously listens for voice input in the background.

**Technical Details:**
- Use PyAudio for cross-platform audio capture
- Implement background threading to avoid blocking
- Handle audio device selection
- Implement error handling for missing/disconnected microphones
- Add noise gate to filter background noise

**Tasks:**
- [ ] Set up PyAudio audio stream
- [ ] Implement continuous audio capture in background thread
- [ ] Add audio device selection and configuration
- [ ] Implement circular buffer for audio storage
- [ ] Add basic noise filtering
- [ ] Handle microphone disconnection gracefully
- [ ] Create unit tests for audio capture
- [ ] Add configuration for sample rate, channels, chunk size

**Acceptance Criteria:**
- Audio captures at 16kHz, mono, 16-bit
- Runs in background without blocking main thread
- Handles microphone errors gracefully
- CPU usage < 5% during capture
- Can be started/stopped programmatically

**Estimated Time:** 2-3 days""",
        "labels": ["feature", "voice-input", "priority: high", "phase: foundation"],
        "milestone": 1
    },
    {
        "title": "Implement hotword detection (wake word)",
        "body": """Detect the wake word "Hey Assistant" to activate voice command listening.

**Technical Details:**
- Evaluate options: Porcupine, Snowboy, Picovoice
- Recommendation: Porcupine (good accuracy, free tier available)
- Custom wake word: "Hey Assistant" or "Computer"
- Low false positive rate required

**Tasks:**
- [ ] Research and select hotword detection library
- [ ] Integrate Porcupine or alternative
- [ ] Create custom wake word model
- [ ] Implement detection in audio stream
- [ ] Add callback system for wake word events
- [ ] Test accuracy with various voice types
- [ ] Add sensitivity configuration
- [ ] Measure and optimize detection latency
- [ ] Add visual/audio confirmation of activation

**Acceptance Criteria:**
- 90%+ detection accuracy in quiet environments
- < 500ms latency from wake word to activation
- < 1% false positive rate
- Works with different voice tones
- Configurable sensitivity

**Dependencies:** #2

**Estimated Time:** 2 days""",
        "labels": ["feature", "voice-input", "priority: high", "phase: foundation"],
        "milestone": 1
    },
    {
        "title": "Integrate OpenAI Whisper for speech-to-text",
        "body": """Convert captured audio to text using OpenAI Whisper (local, offline).

**Technical Details:**
- Use whisper package (local inference)
- Start with "base" model (balanced speed/accuracy)
- Option to upgrade to "small" or "medium" for better accuracy
- Implement chunked processing for real-time feel

**Tasks:**
- [ ] Install and test Whisper models
- [ ] Implement audio preprocessing for Whisper
- [ ] Create transcription function
- [ ] Add model selection (tiny, base, small)
- [ ] Implement streaming/chunked transcription
- [ ] Add language detection
- [ ] Handle transcription errors gracefully
- [ ] Optimize for speed (GPU if available)
- [ ] Add confidence scores
- [ ] Create unit tests with sample audio

**Acceptance Criteria:**
- 95%+ accuracy on clear speech
- < 1 second transcription time for 5-second audio
- Works offline
- Handles 10-15 second commands
- Graceful degradation for unclear audio

**Dependencies:** #2

**Estimated Time:** 2-3 days""",
        "labels": ["feature", "stt", "priority: high", "phase: foundation"],
        "milestone": 1
    },
    {
        "title": "Build intent classification system",
        "body": """Classify user commands into 20 MVP intents using LLM or pattern matching.

**Technical Details:**
- Use LangChain for LLM integration
- Start with OpenAI GPT-4-mini or Claude Haiku
- Implement prompt engineering for intent extraction
- Fallback to regex patterns for common commands
- Return intent + confidence score

**MVP Intents (20 total):**
1. open_application
2. close_application
3. search_web
4. create_file
5. create_folder
6. delete_file
7. move_file
8. list_files
9. take_screenshot
10. volume_control
11. brightness_control
12. open_url
13. copy_file
14. rename_file
15. find_file
16. system_info
17. wifi_control
18. lock_screen
19. sleep_system
20. help_command

**Tasks:**
- [ ] Set up LangChain framework
- [ ] Create intent classification prompt
- [ ] Define intent schema (JSON)
- [ ] Implement LLM-based classifier
- [ ] Add regex fallback patterns
- [ ] Create confidence threshold logic
- [ ] Handle ambiguous intents
- [ ] Add unit tests for each intent
- [ ] Measure classification accuracy
- [ ] Optimize prompt for cost/speed

**Acceptance Criteria:**
- 90%+ intent classification accuracy
- < 1 second response time
- Handles natural language variations
- Returns confidence scores
- Falls back to clarification questions

**Dependencies:** #5

**Estimated Time:** 3-4 days""",
        "labels": ["feature", "nlu", "priority: high", "phase: foundation"],
        "milestone": 1
    },
    {
        "title": "Set up macOS application control automation",
        "body": """Implement launching, quitting, and focusing applications on macOS.

**Technical Details:**
- Use osascript (AppleScript) via subprocess
- Use macOS Accessibility API for advanced control
- Support top 20 common applications

**Tasks:**
- [ ] Create macOS automation base class
- [ ] Implement app launching via osascript
- [ ] Implement app quitting
- [ ] Implement app focusing (bring to front)
- [ ] Build application name resolver (fuzzy matching)
- [ ] Add error handling for missing apps
- [ ] Test with common apps (Chrome, Safari, VSCode, etc.)
- [ ] Add app state detection (is running?)
- [ ] Create unit tests with mock apps
- [ ] Document required macOS permissions

**Acceptance Criteria:**
- Can launch any installed application
- Can quit running applications
- Can bring apps to foreground
- Handles app not found errors
- Works with both app names and bundle IDs

**Estimated Time:** 3 days""",
        "labels": ["feature", "automation", "priority: high", "platform: macos", "phase: automation"],
        "milestone": 1
    },
    {
        "title": "Build text-to-speech feedback system",
        "body": """Provide audio feedback for all actions using natural-sounding voice.

**Technical Details:**
- Use pyttsx3 for offline TTS
- Optional: ElevenLabs API for high-quality voice

**Tasks:**
- [ ] Integrate pyttsx3
- [ ] Select default voice
- [ ] Implement response generation
- [ ] Add voice speed/pitch configuration
- [ ] Create response templates for common actions
- [ ] Implement TTS queue (handle multiple responses)
- [ ] Add volume control (respect system settings)
- [ ] Add option to disable TTS
- [ ] Test voice quality
- [ ] (Optional) Integrate ElevenLabs API

**Acceptance Criteria:**
- Clear, natural voice output
- < 500ms latency for short responses
- Non-blocking (doesn't freeze UI)
- Volume respects system settings
- Can be disabled in config

**Estimated Time:** 2 days""",
        "labels": ["feature", "tts", "priority: high", "phase: foundation"],
        "milestone": 1
    },
    {
        "title": "Create system tray icon and menu",
        "body": """Add persistent system tray icon showing assistant status with menu options.

**Technical Details:**
- Use pystray for cross-platform system tray
- Icon states: idle, listening, processing, error
- Menu: Enable/Disable, Settings, Quit

**Tasks:**
- [ ] Integrate pystray
- [ ] Create icon assets (SVG or PNG)
- [ ] Implement state changes (idle, listening, processing, error)
- [ ] Add animated listening indicator
- [ ] Create tray menu
- [ ] Add "Enable/Disable" toggle
- [ ] Add "Settings" menu item
- [ ] Add "Quit" menu item
- [ ] Add tooltips showing current state
- [ ] Test on macOS

**Acceptance Criteria:**
- Icon visible in system tray
- Icon animates during listening
- Menu items functional
- Can quit app from tray

**Estimated Time:** 2 days""",
        "labels": ["feature", "ui", "priority: high", "phase: ui"],
        "milestone": 1
    },
]


def create_issues(username: str, token: str, repo_name: str = "os-ai-assistant"):
    """Create GitHub issues via API."""
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    print(f"Creating {len(ISSUES)} issues for {username}/{repo_name}...")
    print(f"API URL: {api_url}\n")

    created = 0
    failed = 0

    for i, issue in enumerate(ISSUES, 1):
        print(f"[{i}/{len(ISSUES)}] Creating: {issue['title'][:60]}...")

        data = {
            "title": issue["title"],
            "body": issue["body"],
            "labels": issue.get("labels", [])
        }

        # Note: Milestone assignment requires milestone to exist first
        # Skipping milestone assignment in this version

        try:
            response = requests.post(api_url, headers=headers, json=data)

            if response.status_code == 201:
                issue_num = response.json()["number"]
                print(f"  ✓ Created issue #{issue_num}")
                created += 1
            else:
                print(f"  ✗ Failed: {response.status_code} - {response.text}")
                failed += 1

        except Exception as e:
            print(f"  ✗ Error: {e}")
            failed += 1

    print(f"\n{'='*60}")
    print(f"Summary: {created} created, {failed} failed")
    print(f"{'='*60}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_github_issues.py USERNAME TOKEN [REPO_NAME]")
        print("\nExample:")
        print("  python create_github_issues.py myusername ghp_xxxxx")
        print("\nCreate a GitHub Personal Access Token with 'repo' scope:")
        print("  https://github.com/settings/tokens")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    repo_name = sys.argv[3] if len(sys.argv) > 3 else "os-ai-assistant"

    create_issues(username, token, repo_name)


if __name__ == "__main__":
    main()
