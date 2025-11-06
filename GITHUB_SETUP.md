# GitHub Repository Setup Instructions

Since the GitHub CLI (`gh`) is not available, follow these steps to create your GitHub repository and push the code.

## Step 1: Create GitHub Repository

### Option A: Via GitHub Website (Recommended)

1. Go to https://github.com/new
2. Fill in the repository details:
   - **Repository name**: `os-ai-assistant`
   - **Description**: "Voice-controlled OS automation powered by AI - Control your computer hands-free"
   - **Visibility**: Public (or Private if you prefer)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

### Option B: Using GitHub API (if you have a personal access token)

```bash
# Create repo using curl
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     -d '{"name":"os-ai-assistant","description":"Voice-controlled OS automation powered by AI","private":false}' \
     https://api.github.com/user/repos
```

## Step 2: Push to GitHub

After creating the repository, run these commands:

```bash
cd /home/user/os-ai-assistant

# Set main as default branch (instead of master)
git branch -M main

# Add GitHub remote (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/os-ai-assistant.git

# Push to GitHub
git push -u origin main
```

## Step 3: Set Up Repository Settings

### Add Repository Topics/Tags

Go to your repository on GitHub and add these topics:
- `ai`
- `voice-assistant`
- `voice-control`
- `automation`
- `macos`
- `python`
- `whisper`
- `gpt-4`
- `accessibility`
- `hands-free`

### Enable Issues

1. Go to repository Settings → Features
2. Ensure "Issues" is enabled

### Set Up Branch Protection (Optional but Recommended)

1. Settings → Branches → Add rule
2. Branch name pattern: `main`
3. Enable:
   - Require pull request reviews before merging
   - Require status checks to pass before merging

## Step 4: Create GitHub Issues

You have two options:

### Option A: Manual Creation

Open `docs/issues/ISSUES.md` and manually create each issue on GitHub:
1. Go to your repo's Issues tab
2. Click "New Issue"
3. Copy title and description from ISSUES.md
4. Add appropriate labels
5. Assign to milestone "v0.1 MVP Foundation"

### Option B: Use GitHub API Script

We've created a script to automate issue creation. First, create a GitHub Personal Access Token:

1. GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` scope
3. Save the token

Then run:

```bash
cd /home/user/os-ai-assistant
python scripts/create_github_issues.py YOUR_GITHUB_USERNAME YOUR_TOKEN
```

## Step 5: Create Milestones

1. Go to Issues → Milestones → New Milestone
2. Create these milestones:

**Milestone 1: v0.1 MVP Foundation**
- Due date: 6 weeks from today
- Description: "Core voice control functionality for macOS"

**Milestone 2: v0.2 Enhanced Control**
- Due date: 14 weeks from today
- Description: "Linux support and advanced features"

**Milestone 3: v0.3 Windows Support**
- Due date: 20 weeks from today
- Description: "Full cross-platform support"

**Milestone 4: v1.0 Public Release**
- Due date: 28 weeks from today
- Description: "Production-ready release"

## Step 6: Create Labels

Go to Issues → Labels and create these labels:

### Priority Labels
- `priority: high` - #d73a4a (red)
- `priority: medium` - #fb8500 (orange)
- `priority: low` - #ffd60a (yellow)

### Type Labels
- `feature` - #0e8a16 (green)
- `bug` - #d73a4a (red)
- `documentation` - #0075ca (blue)
- `testing` - #7057ff (purple)
- `setup` - #d4c5f9 (gray)
- `security` - #b60205 (dark red)
- `performance` - #e99695 (pink)

### Phase Labels
- `phase: foundation` - #bfdaff (light blue)
- `phase: automation` - #0e8a16 (green)
- `phase: ui` - #7057ff (purple)
- `phase: integration` - #fb8500 (orange)
- `phase: optimization` - #ffd60a (yellow)
- `phase: launch` - #d73a4a (red)

### Platform Labels
- `platform: macos` - #cccccc (gray)
- `platform: linux` - #fb8500 (orange)
- `platform: windows` - #0075ca (blue)

### Component Labels
- `voice-input` - #006b75 (teal)
- `stt` - #0075ca (blue)
- `nlu` - #0e8a16 (green)
- `automation` - #fb8500 (orange)
- `tts` - #7057ff (purple)
- `ui` - #e99695 (pink)
- `core` - #cccccc (gray)

## Step 7: Set Up GitHub Actions (Optional)

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: macos-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov

    - name: Run tests
      run: pytest
```

## Step 8: Add Repository Description and Website

1. Go to your repository homepage
2. Click the gear icon next to "About"
3. Add:
   - Description: "Voice-controlled OS automation powered by AI - Control your computer hands-free"
   - Website: Link to docs or demo (if available)
   - Topics: (add the topics from Step 3)

## Verification Checklist

- [ ] Repository created on GitHub
- [ ] Code pushed to `main` branch
- [ ] Repository description and topics set
- [ ] Issues enabled
- [ ] Milestones created
- [ ] Labels created
- [ ] Issues created (at least the first few)
- [ ] README displays correctly
- [ ] License file present

## Next Steps

After setup is complete:

1. **Star your own repo** - To keep track of it!
2. **Share with team** - Invite collaborators
3. **Start development** - Pick your first issue and start coding!
4. **Set up project board** (optional) - For better task management

## Need Help?

If you encounter issues:
- Check GitHub documentation: https://docs.github.com
- Ensure git is configured: `git config --list`
- Verify you have push access to the repository
- Check your GitHub token has correct permissions

---

Once everything is set up, you'll have a professional, well-organized repository ready for development! 🚀
