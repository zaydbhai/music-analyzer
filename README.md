# 🎵 Music Library Analyzer

A high-performance Python application designed to scan your music directories, extract metadata from MP3 files, and generate a clean, structured spreadsheet of your library.

## ✨ Features

* **Targeted Scanning:** Recursively scans your folders specifically for `.mp3` files.
* **Smart Metadata Extraction:** Automatically pulls Title, Artist, Album, and Release Year.
* **Playlist Awareness:** Automatically identifies the parent folder of every song and labels it as a "Playlist" in your report.
* **Intelligent Filtering:** Automatically ignores non-music files (like game assets or system sounds) by verifying ID3 metadata.
* **Modern GUI:** Built with Tkinter for a simple, intuitive user experience.

## 🚀 Getting Started

### Prerequisites
* Python 3.7+
* `tinytag` library

### Installation & Usage

1. **Clone or Download the project:**
   ```bash
   git clone [your-repository-url]
   cd Music-Analyzer
2. **Setup Virtual Environment (Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. **Install Dependencies:**
   ```bash
   pip install tinytag
4. **Launch the App:**
   ```bash
   python music_analyzer.py


📊 **Output Structure**

The application generates a Music_Library_By_Playlist.csv file, which is compatible with Microsoft Excel, LibreOffice Calc, and Google Sheets.
