# Quick Start Guide

Get up and running with OS AI Assistant in 5 minutes!

## Prerequisites

- macOS 12 or later (for MVP - Linux/Windows support coming soon)
- Python 3.10+
- Microphone
- OpenAI API key (for MVP)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/os-ai-assistant.git
cd os-ai-assistant
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure

```bash
# Copy default config
cp config/default_config.yaml config/config.yaml

# Edit config.yaml and add your OpenAI API key
nano config/config.yaml
```

Set your API key:
```yaml
nlu:
  api_key: "sk-your-openai-api-key-here"
```

Or use environment variable:
```bash
export OPENAI_API_KEY="sk-your-openai-api-key-here"
```

### 5. Grant macOS Permissions

The assistant needs these permissions:

1. **Microphone Access**
   - System Settings → Privacy & Security → Microphone
   - Enable for Terminal (or your app)

2. **Accessibility Access**
   - System Settings → Privacy & Security → Accessibility
   - Enable for Terminal

3. **Screen Recording** (for screenshots)
   - System Settings → Privacy & Security → Screen Recording
   - Enable for Terminal

### 6. Run the Assistant

```bash
python main.py
```

## First Commands

Once running, try these commands:

### Basic Commands
```
"Hey Assistant, open Chrome"
"Hey Assistant, what can you do?"
"Hey Assistant, take a screenshot"
```

### File Operations
```
"Hey Assistant, create a file called test.txt on Desktop"
"Hey Assistant, create a folder called Projects"
"Hey Assistant, show me files in Documents"
```

### System Controls
```
"Hey Assistant, set volume to 50"
"Hey Assistant, increase brightness"
```

### Web
```
"Hey Assistant, search for Python tutorials"
"Hey Assistant, go to github.com"
```

## Keyboard Shortcut

Don't want to use voice activation? Use:
- **macOS**: `Cmd + Shift + Space`
- **Windows**: `Ctrl + Shift + Space`
- **Linux**: `Ctrl + Shift + Space`

Then speak your command!

## Troubleshooting

### "Microphone not working"
- Check System Settings permissions
- Make sure microphone is not muted
- Test with another app first

### "Wake word not detected"
- Speak clearly and at normal pace
- Adjust sensitivity in config.yaml
- Use keyboard shortcut as alternative

### "Commands not executing"
- Check accessibility permissions
- Verify API key is set correctly
- Check logs: `~/.os-ai-assistant/logs/assistant.log`

### "ModuleNotFoundError"
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

## Configuration Tips

### Adjust Wake Word Sensitivity

In `config/config.yaml`:
```yaml
voice:
  sensitivity: 0.7  # Higher = more sensitive (0-1)
```

### Change STT Provider

```yaml
stt:
  provider: "google"  # Instead of "whisper"
  google_api_key: "your-key"
```

### Disable Voice Feedback

```yaml
tts:
  enabled: false  # No voice responses
```

### Change Default Browser

```yaml
automation:
  default_browser: "chrome"  # or "safari", "firefox"
```

## Next Steps

- Read the [full README](../README.md)
- Check out [all available commands](COMMANDS.md)
- Learn about [security features](SECURITY.md)
- Explore [advanced configuration](CONFIGURATION.md)
- [Contributing guidelines](../CONTRIBUTING.md)

## Getting Help

- **Issues**: GitHub Issues
- **Questions**: GitHub Discussions
- **Bugs**: File a bug report
- **Feature requests**: Open an issue

## Updating

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstalling

```bash
# Remove application
cd ..
rm -rf os-ai-assistant

# Remove user data (optional)
rm -rf ~/.os-ai-assistant
```

---

Happy automating! 🎤🤖
