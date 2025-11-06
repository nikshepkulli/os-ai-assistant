# Contributing to OS AI Assistant

Thank you for your interest in contributing to OS AI Assistant! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites
- Python 3.10 or higher
- macOS (for MVP development - Linux/Windows coming later)
- Git

### Getting Started

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/os-ai-assistant.git
   cd os-ai-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install dev dependencies
   ```

4. **Configure the application**
   ```bash
   cp config/default_config.yaml config/config.yaml
   # Edit config/config.yaml with your API keys
   ```

5. **Run tests**
   ```bash
   pytest
   ```

## Development Workflow

### Branching Strategy

- `main` - Stable releases only
- `develop` - Main development branch
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation updates

### Making Changes

1. Create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
   - Follow the code style (use `black` for formatting)
   - Add tests for new functionality
   - Update documentation as needed

3. Run quality checks
   ```bash
   # Format code
   black src/ tests/

   # Run linter
   pylint src/

   # Type checking
   mypy src/

   # Run tests
   pytest
   ```

4. Commit your changes
   ```bash
   git add .
   git commit -m "feat: Add new feature description"
   ```

   **Commit message format:**
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `test:` - Test changes
   - `refactor:` - Code refactoring
   - `perf:` - Performance improvements
   - `chore:` - Build/tooling changes

5. Push and create a pull request
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- Follow PEP 8 style guide
- Use type hints for function signatures
- Write docstrings for all public functions/classes
- Keep functions small and focused
- Prefer composition over inheritance

### Example Code Style

```python
"""Module docstring describing the module."""

import logging
from typing import Optional, List


class ExampleClass:
    """Class docstring describing the class."""

    def __init__(self, config: dict):
        """Initialize the class."""
        self.config = config
        self.logger = logging.getLogger(__name__)

    def example_method(self, param: str) -> Optional[str]:
        """
        Method docstring describing what it does.

        Args:
            param: Description of parameter

        Returns:
            Description of return value
        """
        try:
            # Implementation
            return result
        except Exception as e:
            self.logger.error(f"Error: {e}", exc_info=True)
            return None
```

## Testing

- Write unit tests for all new functionality
- Aim for 80%+ code coverage
- Test both success and failure cases
- Use meaningful test names

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_nlu.py

# Run specific test
pytest tests/test_nlu.py::test_intent_classification
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all public APIs
- Update MVP_PLAN.md when changing roadmap
- Add examples for new features

## Pull Request Process

1. Update documentation
2. Add tests
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Create PR with clear description
6. Link related issues
7. Wait for review

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Added/updated tests
- [ ] All tests pass
- [ ] Updated documentation
- [ ] No breaking changes (or documented)
```

## Issue Reporting

### Bug Reports

Include:
- OS and version
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs
- Screenshots if applicable

### Feature Requests

Include:
- Clear use case
- Expected behavior
- Why it's useful
- Proposed implementation (optional)

## Architecture Guidelines

### Adding a New Intent

1. Add to `NaturalLanguageUnderstanding.INTENTS`
2. Update NLU prompt
3. Implement handler in automation engine
4. Add tests
5. Document in README

### Adding a New Platform

1. Create new file in `src/automation/`
2. Inherit from `AutomationEngine`
3. Implement all abstract methods
4. Add platform detection in `get_automation_engine()`
5. Add platform-specific dependencies to `requirements.txt`
6. Test thoroughly
7. Update documentation

### Adding a New Component

1. Create module in appropriate directory
2. Follow existing patterns
3. Add logging
4. Handle errors gracefully
5. Write tests
6. Document API

## Getting Help

- Open an issue for bugs/features
- Join discussions for questions
- Check existing issues/PRs first
- Be respectful and patient

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
