# GitHub Issues for MVP

This file contains all the issues to create for the OS AI Assistant MVP. Copy each issue to GitHub with the specified labels and milestones.

---

## Milestone: v0.1 MVP Foundation

---

### Issue #1: Set up project structure and development environment

**Labels**: `setup`, `priority: high`, `phase: foundation`

**Description**:
Initialize the project with proper structure, dependencies, and development tools.

**Tasks**:
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

**Acceptance Criteria**:
- Project structure matches architecture docs
- All developers can clone and run `pip install -r requirements.txt`
- Tests can be run with `pytest`
- Code quality tools configured (black, pylint, mypy)

**Estimated Time**: 1 day

---

### Issue #2: Implement microphone audio capture system

**Labels**: `feature`, `voice-input`, `priority: high`, `phase: foundation`

**Description**:
Create a robust audio capture system that continuously listens for voice input in the background.

**Technical Details**:
- Use PyAudio for cross-platform audio capture
- Implement background threading to avoid blocking
- Handle audio device selection
- Implement error handling for missing/disconnected microphones
- Add noise gate to filter background noise

**Tasks**:
- [ ] Set up PyAudio audio stream
- [ ] Implement continuous audio capture in background thread
- [ ] Add audio device selection and configuration
- [ ] Implement circular buffer for audio storage
- [ ] Add basic noise filtering
- [ ] Handle microphone disconnection gracefully
- [ ] Create unit tests for audio capture
- [ ] Add configuration for sample rate, channels, chunk size

**Acceptance Criteria**:
- Audio captures at 16kHz, mono, 16-bit
- Runs in background without blocking main thread
- Handles microphone errors gracefully
- CPU usage < 5% during capture
- Can be started/stopped programmatically

**Dependencies**: None

**Estimated Time**: 2-3 days

---

### Issue #3: Implement hotword detection (wake word)

**Labels**: `feature`, `voice-input`, `priority: high`, `phase: foundation`

**Description**:
Detect the wake word "Hey Assistant" to activate voice command listening.

**Technical Details**:
- Evaluate options: Porcupine, Snowboy, Picovoice
- Recommendation: Porcupine (good accuracy, free tier available)
- Custom wake word: "Hey Assistant" or "Computer"
- Low false positive rate required

**Tasks**:
- [ ] Research and select hotword detection library
- [ ] Integrate Porcupine or alternative
- [ ] Create custom wake word model
- [ ] Implement detection in audio stream
- [ ] Add callback system for wake word events
- [ ] Test accuracy with various voice types
- [ ] Add sensitivity configuration
- [ ] Measure and optimize detection latency
- [ ] Add visual/audio confirmation of activation

**Acceptance Criteria**:
- 90%+ detection accuracy in quiet environments
- < 500ms latency from wake word to activation
- < 1% false positive rate
- Works with different voice tones
- Configurable sensitivity

**Dependencies**: Issue #2

**Estimated Time**: 2 days

---

### Issue #4: Add push-to-talk alternative activation

**Labels**: `feature`, `voice-input`, `priority: medium`, `phase: foundation`

**Description**:
Provide keyboard shortcut alternative to voice activation for noisy environments.

**Technical Details**:
- Global hotkey: Cmd+Shift+Space (macOS), Ctrl+Shift+Space (Win/Linux)
- Must work when app is in background
- Use pynput for cross-platform keyboard listening

**Tasks**:
- [ ] Integrate pynput for global hotkey detection
- [ ] Implement hotkey registration
- [ ] Add hotkey callback to trigger listening
- [ ] Make hotkey configurable
- [ ] Add visual feedback when activated
- [ ] Test hotkey doesn't conflict with system shortcuts
- [ ] Document hotkey in README

**Acceptance Criteria**:
- Hotkey works when app is in background
- < 100ms activation latency
- User can customize hotkey in config
- No conflicts with system shortcuts

**Dependencies**: Issue #2

**Estimated Time**: 1 day

---

### Issue #5: Integrate OpenAI Whisper for speech-to-text

**Labels**: `feature`, `stt`, `priority: high`, `phase: foundation`

**Description**:
Convert captured audio to text using OpenAI Whisper (local, offline).

**Technical Details**:
- Use whisper package (local inference)
- Start with "base" model (balanced speed/accuracy)
- Option to upgrade to "small" or "medium" for better accuracy
- Implement chunked processing for real-time feel

**Tasks**:
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

**Acceptance Criteria**:
- 95%+ accuracy on clear speech
- < 1 second transcription time for 5-second audio
- Works offline
- Handles 10-15 second commands
- Graceful degradation for unclear audio

**Dependencies**: Issue #2

**Estimated Time**: 2-3 days

---

### Issue #6: Add Google Speech API as STT fallback

**Labels**: `feature`, `stt`, `priority: low`, `phase: foundation`

**Description**:
Provide cloud-based STT option for better accuracy or when local resources are limited.

**Tasks**:
- [ ] Integrate Google Speech-to-Text API
- [ ] Add API key configuration
- [ ] Implement streaming recognition
- [ ] Add provider selection in config
- [ ] Handle API errors and rate limits
- [ ] Measure latency vs Whisper
- [ ] Document API setup in README

**Acceptance Criteria**:
- User can switch between Whisper and Google STT
- API errors handled gracefully
- Similar latency to Whisper
- Clear docs on API key setup

**Dependencies**: Issue #5

**Estimated Time**: 1-2 days

---

### Issue #7: Build intent classification system

**Labels**: `feature`, `nlu`, `priority: high`, `phase: foundation`

**Description**:
Classify user commands into 20 MVP intents using LLM or pattern matching.

**Technical Details**:
- Use LangChain for LLM integration
- Start with OpenAI GPT-4-mini or Claude Haiku
- Implement prompt engineering for intent extraction
- Fallback to regex patterns for common commands
- Return intent + confidence score

**MVP Intents** (20 total):
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

**Tasks**:
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

**Acceptance Criteria**:
- 90%+ intent classification accuracy
- < 1 second response time
- Handles natural language variations
- Returns confidence scores
- Falls back to clarification questions

**Dependencies**: Issue #5

**Estimated Time**: 3-4 days

---

### Issue #8: Build entity extraction system

**Labels**: `feature`, `nlu`, `priority: high`, `phase: foundation`

**Description**:
Extract parameters from user commands (app names, file paths, search terms, etc.).

**Technical Details**:
- Use LLM for complex entity extraction
- Combine with regex for common patterns
- Entity types: application, file_path, folder_path, url, search_query, number, percentage

**Tasks**:
- [ ] Define entity schema for all intents
- [ ] Implement LLM-based entity extraction
- [ ] Add regex patterns for common entities
- [ ] Create entity validation logic
- [ ] Handle missing required entities
- [ ] Implement entity resolution (e.g., "Chrome" -> "Google Chrome.app")
- [ ] Add fuzzy matching for app names
- [ ] Create entity extraction tests
- [ ] Handle ambiguous entities (ask for clarification)

**Acceptance Criteria**:
- Correctly extracts entities from 90%+ of commands
- Handles variations ("Chrome" vs "Google Chrome")
- Validates entity formats (URLs, paths)
- Requests clarification for ambiguous cases

**Dependencies**: Issue #7

**Estimated Time**: 3 days

---

### Issue #9: Implement context awareness for multi-turn commands

**Labels**: `feature`, `nlu`, `priority: medium`, `phase: foundation`

**Description**:
Remember context from previous commands to handle references like "close it", "delete that file".

**Technical Details**:
- Maintain conversation context (last 5 commands)
- Resolve pronouns and references
- Track active entities (files, apps, windows)

**Tasks**:
- [ ] Create context manager class
- [ ] Store last N commands and their entities
- [ ] Implement reference resolution ("it", "that", "the file")
- [ ] Add entity tracking (what's currently open/active)
- [ ] Implement context timeout (clear after 5 mins)
- [ ] Test multi-turn conversations
- [ ] Handle context conflicts

**Acceptance Criteria**:
- Can handle "open Chrome", then "close it"
- Remembers files just created or accessed
- Context persists for 5 minutes
- Clears context appropriately

**Dependencies**: Issue #7, Issue #8

**Estimated Time**: 2 days

---

### Issue #10: Set up macOS application control automation

**Labels**: `feature`, `automation`, `priority: high`, `platform: macos`, `phase: automation`

**Description**:
Implement launching, quitting, and focusing applications on macOS.

**Technical Details**:
- Use osascript (AppleScript) via subprocess
- Use macOS Accessibility API for advanced control
- Support top 20 common applications

**Tasks**:
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

**Acceptance Criteria**:
- Can launch any installed application
- Can quit running applications
- Can bring apps to foreground
- Handles app not found errors
- Works with both app names and bundle IDs

**Dependencies**: None

**Estimated Time**: 3 days

---

### Issue #11: Implement macOS file system operations

**Labels**: `feature`, `automation`, `priority: high`, `platform: macos`, `phase: automation`

**Description**:
Create, delete, move, copy, and list files/folders on macOS.

**Technical Details**:
- Use Python pathlib and shutil
- Implement safety checks for dangerous operations
- Support common paths (Desktop, Documents, Downloads)

**Tasks**:
- [ ] Implement file creation (touch)
- [ ] Implement folder creation (mkdir)
- [ ] Implement file/folder deletion (with confirmation)
- [ ] Implement file/folder move
- [ ] Implement file/folder copy
- [ ] Implement file listing (ls)
- [ ] Implement file search (find)
- [ ] Add path expansion (~, relative paths)
- [ ] Add safety checks (prevent system file deletion)
- [ ] Handle permission errors
- [ ] Add undo capability for deletions (trash instead of rm)
- [ ] Create comprehensive tests

**Acceptance Criteria**:
- All file operations work correctly
- Dangerous operations require confirmation
- Deleted files go to trash, not permanent deletion
- Handles permission errors gracefully
- Supports relative and absolute paths

**Dependencies**: None

**Estimated Time**: 3 days

---

### Issue #12: Implement macOS system controls

**Labels**: `feature`, `automation`, `priority: medium`, `platform: macos`, `phase: automation`

**Description**:
Control volume, brightness, WiFi, and other system settings on macOS.

**Technical Details**:
- Use osascript for volume control
- Use macOS APIs for brightness (PyObjC)
- Use networksetup for WiFi

**Tasks**:
- [ ] Implement volume control (get, set, mute, unmute)
- [ ] Implement brightness control (get, set, increase, decrease)
- [ ] Implement WiFi control (on, off, status)
- [ ] Implement Bluetooth control
- [ ] Implement Do Not Disturb toggle
- [ ] Implement display sleep
- [ ] Add system info queries (battery, WiFi status)
- [ ] Test on different macOS versions
- [ ] Handle permission requirements

**Acceptance Criteria**:
- Volume adjusts to specific level or relative amount
- Brightness adjusts smoothly
- WiFi can be toggled
- System info returns accurate data
- Works on macOS 12+

**Dependencies**: None

**Estimated Time**: 3 days

---

### Issue #13: Implement web search and browser automation

**Labels**: `feature`, `automation`, `priority: medium`, `platform: macos`, `phase: automation`

**Description**:
Open URLs and perform web searches in default or specified browser.

**Technical Details**:
- Use webbrowser module for basic opening
- Use osascript for browser-specific control
- Support Chrome, Safari, Firefox

**Tasks**:
- [ ] Implement URL opening in default browser
- [ ] Implement web search (Google, DuckDuckGo)
- [ ] Add browser selection
- [ ] Implement new tab/window opening
- [ ] Add browser control (close tab, navigate back/forward)
- [ ] Handle URL validation
- [ ] Add search engine configuration
- [ ] Test with multiple browsers

**Acceptance Criteria**:
- Opens URLs in default browser
- Performs web searches with query
- Can specify browser
- Handles invalid URLs gracefully

**Dependencies**: None

**Estimated Time**: 2 days

---

### Issue #14: Implement screenshot capture

**Labels**: `feature`, `automation`, `priority: low`, `platform: macos`, `phase: automation`

**Description**:
Capture screenshots of full screen, window, or selection.

**Technical Details**:
- Use macOS screencapture command
- Support different capture modes
- Save to configurable location

**Tasks**:
- [ ] Implement full screen capture
- [ ] Implement window capture
- [ ] Implement selection capture (interactive)
- [ ] Add save location configuration
- [ ] Add filename customization (timestamp)
- [ ] Handle permissions for screen recording
- [ ] Return screenshot path after capture

**Acceptance Criteria**:
- Can capture full screen
- Can capture specific window
- Saves with timestamp filename
- Returns path to saved screenshot

**Dependencies**: None

**Estimated Time**: 1 day

---

### Issue #15: Implement window management

**Labels**: `feature`, `automation`, `priority: low`, `platform: macos`, `phase: automation`

**Description**:
Resize, move, minimize, and maximize windows.

**Technical Details**:
- Use macOS Accessibility API
- Requires accessibility permissions

**Tasks**:
- [ ] Request accessibility permissions
- [ ] Implement window resize
- [ ] Implement window move (to position)
- [ ] Implement window minimize
- [ ] Implement window maximize/zoom
- [ ] Implement window close
- [ ] Add window listing (get all windows)
- [ ] Test with multiple apps

**Acceptance Criteria**:
- Can resize/move active window
- Can minimize/maximize windows
- Works with standard macOS apps
- Handles permission errors

**Dependencies**: None

**Estimated Time**: 2-3 days

---

### Issue #16: Build text-to-speech feedback system

**Labels**: `feature`, `tts`, `priority: high`, `phase: foundation`

**Description**:
Provide audio feedback for all actions using natural-sounding voice.

**Technical Details**:
- Use pyttsx3 for offline TTS
- Optional: ElevenLabs API for high-quality voice

**Tasks**:
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

**Acceptance Criteria**:
- Clear, natural voice output
- < 500ms latency for short responses
- Non-blocking (doesn't freeze UI)
- Volume respects system settings
- Can be disabled in config

**Dependencies**: None

**Estimated Time**: 2 days

---

### Issue #17: Create system tray icon and menu

**Labels**: `feature`, `ui`, `priority: high`, `phase: ui`

**Description**:
Add persistent system tray icon showing assistant status with menu options.

**Technical Details**:
- Use pystray for cross-platform system tray
- Icon states: idle, listening, processing, error
- Menu: Enable/Disable, Settings, Quit

**Tasks**:
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

**Acceptance Criteria**:
- Icon visible in system tray
- Icon animates during listening
- Menu items functional
- Can quit app from tray

**Dependencies**: None

**Estimated Time**: 2 days

---

### Issue #18: Build visual overlay for transcription and feedback

**Labels**: `feature`, `ui`, `priority: high`, `phase: ui`

**Description**:
Create on-screen overlay showing real-time transcription and action confirmations.

**Technical Details**:
- Use tkinter for lightweight overlay
- Transparent window, always-on-top
- Position: top-center of screen
- Auto-hide after 3 seconds

**Tasks**:
- [ ] Create transparent overlay window
- [ ] Position window top-center
- [ ] Implement always-on-top behavior
- [ ] Display transcription text (real-time)
- [ ] Display action confirmations
- [ ] Display error messages
- [ ] Add fade-in/fade-out animations
- [ ] Auto-hide after 3 seconds
- [ ] Add manual dismiss option
- [ ] Style with rounded corners, shadow
- [ ] Make colors/position configurable

**Acceptance Criteria**:
- Overlay appears during voice input
- Shows transcription in real-time
- Shows action being performed
- Auto-hides after completion
- Non-intrusive, doesn't block work
- Visually appealing

**Dependencies**: None

**Estimated Time**: 3 days

---

### Issue #19: Build settings/preferences window

**Labels**: `feature`, `ui`, `priority: medium`, `phase: ui`

**Description**:
Create GUI for configuring assistant settings.

**Technical Details**:
- Use tkinter or PyQt6
- Tabbed interface for different settings categories
- Opened from system tray menu

**Settings Categories**:
- Voice: Hotword, language, STT provider
- Automation: Confirmation settings, allowed commands
- UI: Overlay position, TTS voice
- Privacy: Logging, command history
- About: Version, help, licenses

**Tasks**:
- [ ] Create settings window UI
- [ ] Add tabs for categories
- [ ] Implement voice settings
- [ ] Implement automation settings
- [ ] Implement UI settings
- [ ] Implement privacy settings
- [ ] Add save/cancel buttons
- [ ] Persist settings to config file
- [ ] Validate settings input
- [ ] Add reset to defaults option

**Acceptance Criteria**:
- Settings window opens from tray menu
- All settings can be modified
- Changes persist after restart
- Input validation works
- Cancel discards changes

**Dependencies**: Issue #17

**Estimated Time**: 3-4 days

---

### Issue #20: Implement security and permission system

**Labels**: `feature`, `security`, `priority: high`, `phase: foundation`

**Description**:
Protect user from dangerous operations with confirmation prompts and permission system.

**Technical Details**:
- YAML config for permission rules
- Dialog prompts for confirmation
- Action logging for audit

**Dangerous Operations** (require confirmation):
- File/folder deletion
- System shutdown/restart
- Running shell scripts
- Modifying system settings

**Tasks**:
- [ ] Create permission configuration schema
- [ ] Implement permission checker
- [ ] Build confirmation dialog UI
- [ ] Add whitelist/blacklist for commands
- [ ] Implement action logging
- [ ] Add command history viewer
- [ ] Sanitize logged data (no passwords)
- [ ] Add "always allow" option (persistent)
- [ ] Test with dangerous operations
- [ ] Document security features

**Acceptance Criteria**:
- Deletion requires confirmation by default
- System commands require confirmation
- User can customize permission rules
- All actions logged with timestamps
- Logs don't contain sensitive data
- Confirmation dialogs are clear

**Dependencies**: None

**Estimated Time**: 3 days

---

### Issue #21: Build main orchestrator/coordinator

**Labels**: `feature`, `core`, `priority: high`, `phase: foundation`

**Description**:
Create main controller that coordinates all components (voice, NLU, automation, feedback).

**Technical Details**:
- Main event loop
- Component lifecycle management
- Error handling and recovery
- State management

**Tasks**:
- [ ] Create Orchestrator class
- [ ] Implement component initialization
- [ ] Build event loop
- [ ] Implement state machine (idle, listening, processing, executing)
- [ ] Add component communication
- [ ] Implement error handling
- [ ] Add graceful shutdown
- [ ] Create startup checks (permissions, dependencies)
- [ ] Add logging throughout
- [ ] Create integration tests

**Acceptance Criteria**:
- All components initialize correctly
- State transitions work properly
- Errors handled gracefully
- Clean shutdown when quitting
- Comprehensive logging

**Dependencies**: All component issues

**Estimated Time**: 3-4 days

---

### Issue #22: Create configuration management system

**Labels**: `feature`, `core`, `priority: medium`, `phase: foundation`

**Description**:
Manage application configuration with defaults and user overrides.

**Technical Details**:
- YAML configuration files
- Default config + user config
- Validation and migration

**Tasks**:
- [ ] Create config schema
- [ ] Create default_config.yaml
- [ ] Implement config loader
- [ ] Add config validation
- [ ] Implement user config override
- [ ] Add config migration (version updates)
- [ ] Create config documentation
- [ ] Add environment variable support
- [ ] Implement hot-reload (optional)

**Acceptance Criteria**:
- Default config loads correctly
- User config overrides defaults
- Invalid config shows clear errors
- Config documented in README
- Environment variables work

**Dependencies**: None

**Estimated Time**: 2 days

---

### Issue #23: Set up comprehensive logging system

**Labels**: `feature`, `core`, `priority: medium`, `phase: foundation`

**Description**:
Implement structured logging for debugging and monitoring.

**Technical Details**:
- Use Python logging module
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Log to file and console
- Rotate log files

**Tasks**:
- [ ] Configure logging framework
- [ ] Create log formatters
- [ ] Implement file logging with rotation
- [ ] Add console logging (development)
- [ ] Create logger instances for each module
- [ ] Add contextual logging (user command, session ID)
- [ ] Implement log sanitization (remove sensitive data)
- [ ] Add log viewer in settings
- [ ] Configure log levels per module
- [ ] Test log rotation

**Acceptance Criteria**:
- Logs written to file
- Log rotation works (max 10MB per file)
- Sensitive data not logged
- Log levels configurable
- Logs help with debugging

**Dependencies**: None

**Estimated Time**: 2 days

---

### Issue #24: Create comprehensive test suite

**Labels**: `testing`, `priority: high`, `phase: foundation`

**Description**:
Build unit and integration tests for all components.

**Test Coverage Goals**:
- Unit tests: 80%+ coverage
- Integration tests for critical paths
- E2E tests for complete workflows

**Tasks**:
- [ ] Set up pytest framework
- [ ] Create test fixtures and mocks
- [ ] Write unit tests for voice input
- [ ] Write unit tests for STT
- [ ] Write unit tests for NLU
- [ ] Write unit tests for automation (each platform)
- [ ] Write unit tests for TTS
- [ ] Write unit tests for UI components
- [ ] Write integration tests for end-to-end flows
- [ ] Add test audio samples
- [ ] Set up coverage reporting
- [ ] Add tests to CI/CD

**Acceptance Criteria**:
- 80%+ code coverage
- All critical paths tested
- Tests run in CI
- Tests documented
- Easy to run locally

**Dependencies**: All component issues

**Estimated Time**: 5-7 days (ongoing)

---

### Issue #25: macOS accessibility permissions setup

**Labels**: `setup`, `platform: macos`, `priority: high`, `phase: foundation`

**Description**:
Create guided setup for macOS accessibility permissions required for automation.

**Required Permissions**:
- Microphone access
- Accessibility API access
- Screen recording (for screenshots)

**Tasks**:
- [ ] Detect missing permissions on startup
- [ ] Show clear permission request dialogs
- [ ] Provide step-by-step instructions
- [ ] Add deep links to System Preferences
- [ ] Test permission flows on macOS 12, 13, 14
- [ ] Handle permission denials gracefully
- [ ] Create troubleshooting guide
- [ ] Add permission reset instructions

**Acceptance Criteria**:
- Clear instructions for each permission
- Direct links to settings
- Graceful handling of denied permissions
- Works on macOS 12+

**Dependencies**: None

**Estimated Time**: 2 days

---

### Issue #26: Create packaging and distribution

**Labels**: `setup`, `priority: medium`, `phase: foundation`

**Description**:
Package application for easy installation and distribution on macOS.

**Technical Details**:
- Create standalone executable (PyInstaller)
- Create .app bundle for macOS
- Create installer DMG
- Code signing (optional for MVP)

**Tasks**:
- [ ] Set up PyInstaller configuration
- [ ] Create executable build script
- [ ] Create macOS .app bundle
- [ ] Include all dependencies
- [ ] Test on clean macOS installation
- [ ] Create DMG installer
- [ ] Add application icon
- [ ] (Optional) Set up code signing
- [ ] Create installation instructions
- [ ] Test auto-start on login

**Acceptance Criteria**:
- One-click installation on macOS
- All dependencies included
- Launches on login (optional)
- Icon shows in Applications folder

**Dependencies**: All component issues

**Estimated Time**: 3-4 days

---

### Issue #27: Write user documentation

**Labels**: `documentation`, `priority: medium`, `phase: foundation`

**Description**:
Create comprehensive user and developer documentation.

**Documents Needed**:
- README.md (overview, installation, usage)
- USER_GUIDE.md (detailed usage, commands)
- DEVELOPER.md (architecture, contributing)
- API.md (for future extensions)
- FAQ.md
- TROUBLESHOOTING.md

**Tasks**:
- [ ] Write clear README with quick start
- [ ] Document all 20 MVP commands
- [ ] Create usage examples
- [ ] Document configuration options
- [ ] Write troubleshooting guide
- [ ] Create FAQ
- [ ] Document architecture for developers
- [ ] Add contribution guidelines
- [ ] Create video demos (optional)
- [ ] Add screenshots/GIFs

**Acceptance Criteria**:
- New users can install and use with docs alone
- All commands documented with examples
- Common issues covered in troubleshooting
- Developer docs enable contributions

**Dependencies**: All component issues

**Estimated Time**: 3-4 days

---

### Issue #28: End-to-end integration testing

**Labels**: `testing`, `priority: high`, `phase: integration`

**Description**:
Test complete workflows from voice input to action execution.

**Test Scenarios**:
1. "Hey Assistant, open Chrome" - full flow
2. "Hey Assistant, create a file called test.txt on Desktop" - full flow
3. "Hey Assistant, what's my battery level" - info query
4. "Hey Assistant, search for Python tutorials" - web search
5. "Hey Assistant, set volume to 50" - system control
6. Multi-turn: "open VSCode", then "close it"
7. Error handling: "open NonexistentApp"
8. Confirmation: "delete my file.txt"

**Tasks**:
- [ ] Create E2E test framework
- [ ] Implement test scenarios above
- [ ] Add performance benchmarks
- [ ] Test on real hardware (various Macs)
- [ ] Test in different environments (quiet, noisy)
- [ ] Measure end-to-end latency
- [ ] Test error recovery
- [ ] Test resource usage (CPU, RAM)
- [ ] Create test report template

**Acceptance Criteria**:
- All test scenarios pass
- End-to-end latency < 2 seconds
- Resource usage within targets
- Error handling works correctly

**Dependencies**: All component issues

**Estimated Time**: 3-4 days

---

### Issue #29: Performance optimization

**Labels**: `performance`, `priority: medium`, `phase: optimization`

**Description**:
Optimize for latency, resource usage, and battery life.

**Performance Targets**:
- Voice activation latency: < 500ms
- STT latency: < 1s for 5s audio
- NLU latency: < 1s
- Total latency: < 2s
- Idle CPU: < 5%
- Active CPU: < 30%
- RAM usage: < 300MB

**Tasks**:
- [ ] Profile application performance
- [ ] Optimize STT (model selection, batching)
- [ ] Optimize NLU (caching, prompt optimization)
- [ ] Reduce memory usage
- [ ] Optimize wake word detection
- [ ] Add performance monitoring
- [ ] Test battery impact
- [ ] Implement lazy loading
- [ ] Add performance tests to CI

**Acceptance Criteria**:
- Meets all performance targets
- No performance regressions in CI
- Battery life impact < 5%
- Smooth user experience

**Dependencies**: All component issues

**Estimated Time**: 3-5 days

---

### Issue #30: Security audit and hardening

**Labels**: `security`, `priority: high`, `phase: optimization`

**Description**:
Audit security, fix vulnerabilities, and implement best practices.

**Security Checklist**:
- Input validation (all user inputs)
- Path traversal prevention
- Command injection prevention
- Secure credential storage
- Dependency vulnerability scanning
- Privacy compliance

**Tasks**:
- [ ] Run security audit (bandit, safety)
- [ ] Fix all high/critical vulnerabilities
- [ ] Implement input validation everywhere
- [ ] Add path sanitization
- [ ] Prevent command injection
- [ ] Secure API key storage
- [ ] Review and minimize permissions
- [ ] Add rate limiting for API calls
- [ ] Implement secure logging (no secrets)
- [ ] Create security documentation
- [ ] Set up automated vulnerability scanning

**Acceptance Criteria**:
- No high/critical vulnerabilities
- All inputs validated
- Secrets stored securely
- Security best practices followed
- Documented security features

**Dependencies**: All component issues

**Estimated Time**: 3-4 days

---

### Issue #31: MVP launch preparation

**Labels**: `release`, `priority: high`, `phase: launch`

**Description**:
Prepare for MVP launch with final testing, documentation, and release.

**Tasks**:
- [ ] Final end-to-end testing
- [ ] User acceptance testing (5-10 beta users)
- [ ] Fix critical bugs from testing
- [ ] Finalize documentation
- [ ] Create demo video
- [ ] Prepare launch announcement
- [ ] Set up GitHub releases
- [ ] Create changelog
- [ ] Prepare support channels
- [ ] Launch MVP v0.1!

**Acceptance Criteria**:
- All MVP features working
- No critical bugs
- Documentation complete
- Demo video published
- Release notes ready

**Dependencies**: All issues above

**Estimated Time**: 5-7 days

---

## Additional Labels to Create

Create these labels in your GitHub repo:

**Priority**:
- `priority: high` - Red
- `priority: medium` - Orange
- `priority: low` - Yellow

**Type**:
- `feature` - Green
- `bug` - Red
- `documentation` - Blue
- `testing` - Purple
- `setup` - Gray
- `security` - Dark red
- `performance` - Pink

**Phase**:
- `phase: foundation` - Light blue
- `phase: automation` - Green
- `phase: ui` - Purple
- `phase: integration` - Orange
- `phase: optimization` - Yellow
- `phase: launch` - Red

**Platform**:
- `platform: macos` - Gray
- `platform: linux` - Orange
- `platform: windows` - Blue

**Component**:
- `voice-input` - Teal
- `stt` - Blue
- `nlu` - Green
- `automation` - Orange
- `tts` - Purple
- `ui` - Pink
- `core` - Gray

---

## Milestones to Create

**Milestone 1**: v0.1 MVP Foundation (Week 1-6)
- All issues above
- Due date: 6 weeks from start

**Milestone 2**: v0.2 Enhanced Control (Week 7-14)
- Linux support
- Advanced automation
- Workflow features

**Milestone 3**: v0.3 Windows Support (Week 15-20)
- Windows automation
- Cross-platform polish

**Milestone 4**: v1.0 Public Release (Week 21-28)
- Enterprise features
- Full documentation
- Public launch
