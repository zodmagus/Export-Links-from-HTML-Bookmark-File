# Export Links from HTML Bookmark File

This script extracts links from an HTML bookmark file and saves them to a text file.

## How It Works

The script reads an HTML bookmark file and uses a regular expression to extract links from anchor tags (`<a>`). It then writes the extracted links to a text file.

## Installation

1. Clone the repository:
   git clone https://github.com/zodmagus/exportlinks.git
2. Navigate to the project directory:
   cd exportlinks
3. Run script
   python3 exportlinks.py path/to/your/bookmarks.html

Requirements
Python 3.x
Note
Ensure that your bookmark file is in HTML format (ends with .html).
The script uses a regular expression to extract links. While it should work for common cases, consider using an HTML parser for more robust handling of various HTML structures.
