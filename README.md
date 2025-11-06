# OS AI Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub issues](https://img.shields.io/github/issues/nikshepkulli/os-ai-assistant)](https://github.com/nikshepkulli/os-ai-assistant/issues)
[![GitHub stars](https://img.shields.io/github/stars/nikshepkulli/os-ai-assistant)](https://github.com/nikshepkulli/os-ai-assistant/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

An AI-powered voice assistant that enables complete OS control through natural language commands - no mouse or keyboard required.

> **🌟 Open Source Project** - We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Vision

Enable users to control their entire operating system (Windows, macOS, Linux) through voice commands powered by AI. Inspired by Perplexity's Comet browser, but for the entire OS.

## Core Capabilities

- **Voice Control**: Hands-free OS interaction through natural speech
- **Cross-Platform**: Windows, macOS, and Linux support
- **Natural Language Understanding**: Execute complex tasks through conversational commands
- **Visual Feedback**: Real-time display of actions and confirmations
- **Secure**: Permission system for sensitive operations

## MVP Features

### Phase 1: Foundation (v0.1)
- ✅ Voice activation system (hotword detection)
- ✅ Speech-to-Text integration
- ✅ Basic command execution (open/close apps, file operations)
- ✅ Simple overlay UI for feedback
- ✅ Single OS support (macOS/Linux first)

### Phase 2: Enhanced Control (v0.2)
- Window management (resize, move, switch)
- System controls (volume, brightness, network)
- Web search and browsing control
- Multi-OS support

### Phase 3: Intelligence (v0.3)
- Context awareness across commands
- Task automation and workflows
- Learning user preferences
- Advanced NLU with LLM integration

## Tech Stack

### Core
- **Language**: Python 3.10+
- **Voice Input**: PyAudio, SpeechRecognition
- **STT**: OpenAI Whisper (local) / Google Speech API
- **NLU**: LangChain + GPT-4 / Claude
- **TTS**: pyttsx3 / ElevenLabs

### OS Automation
- **macOS**: pyobjc, AppleScript
- **Linux**: python-xlib, pyautogui
- **Windows**: pywin32, UI Automation

### UI
- **Overlay**: tkinter / PyQt6
- **System Tray**: pystray

## Architecture

```
┌─────────────────────────────────────────────┐
│            Voice Input Layer                 │
│  (Microphone → Hotword Detection → STT)     │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│         NLU & Intent Processing              │
│     (LLM → Intent Classification)            │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│         OS Automation Engine                 │
│  (Platform-specific Command Execution)       │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│         Feedback Layer (TTS + UI)            │
└─────────────────────────────────────────────┘
```

## Project Structure

```
os-ai-assistant/
├── src/
│   ├── core/
│   │   ├── voice_input.py      # Audio capture and hotword
│   │   ├── stt.py              # Speech-to-text
│   │   ├── nlu.py              # Natural language understanding
│   │   ├── tts.py              # Text-to-speech
│   │   └── orchestrator.py     # Main coordinator
│   ├── automation/
│   │   ├── base.py             # Base automation interface
│   │   ├── macos.py            # macOS automation
│   │   ├── linux.py            # Linux automation
│   │   └── windows.py          # Windows automation
│   ├── ui/
│   │   ├── overlay.py          # Visual feedback overlay
│   │   └── tray.py             # System tray icon
│   └── utils/
│       ├── config.py           # Configuration management
│       ├── security.py         # Permission handling
│       └── logger.py           # Logging utilities
├── tests/
├── docs/
├── config/
│   └── default_config.yaml
├── requirements.txt
├── setup.py
└── main.py
```

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Microphone access
- OS-specific dependencies (see docs)

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd os-ai-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Configure
cp config/default_config.yaml config/config.yaml
# Edit config.yaml with your API keys and preferences

# Run
python main.py
```

## Usage

### Basic Commands

```
"Hey Assistant, open Chrome"
"Hey Assistant, create a new folder called Projects"
"Hey Assistant, search for Python tutorials"
"Hey Assistant, close all windows"
"Hey Assistant, increase volume to 50%"
"Hey Assistant, take a screenshot"
```

### Configuration

Edit `config/config.yaml`:

```yaml
voice:
  hotword: "hey assistant"
  language: "en-US"

stt:
  provider: "whisper"  # or "google"
  model: "base"

nlu:
  provider: "openai"
  model: "gpt-4"
  api_key: "your-key-here"

security:
  require_confirmation:
    - delete_file
    - run_script
    - system_command
```

## Development

### Running Tests
```bash
pytest tests/
```

### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## Roadmap

- [ ] MVP v0.1 - Basic voice control (macOS)
- [ ] v0.2 - Enhanced commands + Linux support
- [ ] v0.3 - Windows support
- [ ] v0.4 - LLM integration for complex tasks
- [ ] v0.5 - Workflow automation
- [ ] v1.0 - Full multi-OS release

## Security & Privacy

- Local speech processing option (Whisper)
- No command history sent to cloud by default
- Explicit consent for sensitive operations
- Open source and auditable

**Security Vulnerability?** See [SECURITY.md](SECURITY.md) for responsible disclosure.

## Community

We welcome contributions from everyone! Here's how to get involved:

### Contributing

- 📖 Read our [Contributing Guidelines](CONTRIBUTING.md)
- 🐛 Report bugs via [GitHub Issues](https://github.com/nikshepkulli/os-ai-assistant/issues)
- 💡 Suggest features via [Feature Requests](https://github.com/nikshepkulli/os-ai-assistant/issues/new?template=feature_request.md)
- 🔧 Submit pull requests to improve the code
- ⭐ Star the repo if you find it useful!

### Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone. Please read our [Code of Conduct](CODE_OF_CONDUCT.md).

### Getting Help

- 📚 Check the [Documentation](docs/)
- 💬 Open a [Discussion](https://github.com/nikshepkulli/os-ai-assistant/discussions)
- ❓ Ask questions in [Issues](https://github.com/nikshepkulli/os-ai-assistant/issues/new?template=question.md)

## License

MIT License - see [LICENSE](LICENSE) file

This project is free and open-source software. You are free to use, modify, and distribute it under the terms of the MIT license.

## Acknowledgments

Inspired by Perplexity's Comet AI Browser
