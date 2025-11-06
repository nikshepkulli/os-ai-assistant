"""Setup script for OS AI Assistant."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="os-ai-assistant",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Voice-controlled OS automation powered by AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/os-ai-assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pyaudio>=0.2.13",
        "openai-whisper>=20230918",
        "langchain>=0.1.0",
        "openai>=1.12.0",
        "pyttsx3>=2.90",
        "pystray>=0.19.5",
        "PyYAML>=6.0.1",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.3.0",
            "pylint>=2.17.0",
            "mypy>=1.4.0",
        ],
        "macos": [
            "pyobjc>=9.2",
        ],
    },
    entry_points={
        "console_scripts": [
            "os-ai-assistant=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["config/*.yaml"],
    },
)
