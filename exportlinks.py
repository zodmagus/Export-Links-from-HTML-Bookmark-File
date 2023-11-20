import os
import re
import sys

def extract_links_from_bookmark_file(bookmark_file_path, output_file_path):
    if not bookmark_file_path.endswith(".html"):
        print("Error: Bookmark file must be an HTML file")
        sys.exit(1)

    with open(bookmark_file_path, "r", encoding="utf-8") as bookmark_file:
        bookmark_file_content = bookmark_file.read()

    # Updated regex to match the provided HTML snippet structure
    links = re.findall(r'<A HREF=["\'](https?://[^"\']+)', bookmark_file_content)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for link in links:
            output_file.write(link + "\n")

    print(f"Links extracted from {bookmark_file_path} and saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 exportlinks.py <bookmark_file_path>")
        sys.exit(1)

    bookmark_file_path = sys.argv[1]
    output_file_path = "links.txt"

    extract_links_from_bookmark_file(bookmark_file_path, output_file_path)


#z0ds3c
