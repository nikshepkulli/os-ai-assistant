#!/usr/bin/env python3
"""Create GitHub labels for the project."""

import requests
import json
import sys

# Usage: python create_labels.py USERNAME TOKEN
if len(sys.argv) < 3:
    print("Usage: python create_labels.py USERNAME TOKEN")
    sys.exit(1)

USERNAME = sys.argv[1]
TOKEN = sys.argv[2]
REPO = f"{USERNAME}/os-ai-assistant"
API_URL = f"https://api.github.com/repos/{REPO}/labels"

LABELS = [
    # Priority
    {"name": "priority: high", "color": "d73a4a", "description": "High priority"},
    {"name": "priority: medium", "color": "fb8500", "description": "Medium priority"},
    {"name": "priority: low", "color": "ffd60a", "description": "Low priority"},

    # Type
    {"name": "feature", "color": "0e8a16", "description": "New feature"},
    {"name": "bug", "color": "d73a4a", "description": "Bug fix"},
    {"name": "documentation", "color": "0075ca", "description": "Documentation"},
    {"name": "testing", "color": "7057ff", "description": "Testing"},
    {"name": "setup", "color": "d4c5f9", "description": "Setup and configuration"},
    {"name": "security", "color": "b60205", "description": "Security related"},
    {"name": "performance", "color": "e99695", "description": "Performance improvement"},

    # Phase
    {"name": "phase: foundation", "color": "bfdaff", "description": "Foundation phase"},
    {"name": "phase: automation", "color": "0e8a16", "description": "Automation phase"},
    {"name": "phase: ui", "color": "7057ff", "description": "UI phase"},
    {"name": "phase: integration", "color": "fb8500", "description": "Integration phase"},
    {"name": "phase: optimization", "color": "ffd60a", "description": "Optimization phase"},
    {"name": "phase: launch", "color": "d73a4a", "description": "Launch phase"},

    # Platform
    {"name": "platform: macos", "color": "cccccc", "description": "macOS specific"},
    {"name": "platform: linux", "color": "fb8500", "description": "Linux specific"},
    {"name": "platform: windows", "color": "0075ca", "description": "Windows specific"},

    # Component
    {"name": "voice-input", "color": "006b75", "description": "Voice input component"},
    {"name": "stt", "color": "0075ca", "description": "Speech-to-text"},
    {"name": "nlu", "color": "0e8a16", "description": "Natural language understanding"},
    {"name": "automation", "color": "fb8500", "description": "OS automation"},
    {"name": "tts", "color": "7057ff", "description": "Text-to-speech"},
    {"name": "ui", "color": "e99695", "description": "User interface"},
    {"name": "core", "color": "cccccc", "description": "Core system"},
]

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

print(f"Creating {len(LABELS)} labels for {REPO}...\n")

created = 0
failed = 0

for label in LABELS:
    try:
        response = requests.post(API_URL, headers=headers, json=label)
        if response.status_code == 201:
            print(f"✓ Created: {label['name']}")
            created += 1
        else:
            print(f"✗ Failed: {label['name']} - {response.status_code}")
            failed += 1
    except Exception as e:
        print(f"✗ Error creating {label['name']}: {e}")
        failed += 1

print(f"\n{'='*60}")
print(f"Summary: {created} created, {failed} failed")
print(f"{'='*60}")
