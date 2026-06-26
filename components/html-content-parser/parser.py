from bs4 import BeautifulSoup

def parse_html(html_content: str) -> dict:
    """
    Parse HTML and return a dict with title and body text.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    return {
        "title": soup.title.string if soup.title else None,
        "body": soup.get_text(separator=" ", strip=True)
    }