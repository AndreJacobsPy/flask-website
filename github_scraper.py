from requests import get
from bs4 import BeautifulSoup


def get_pinned_repo_links() -> list[str]:
    # first get html
    html = get("https://github.com/AndreJacobsPy").text
    soup = BeautifulSoup(html, "html.parser")
    ordered_list = soup.find("ol")

    # find links for all pinned repos
    links = [link.get("href") for link in ordered_list.find_all("a")]
    quality_filter = filter(lambda x: len(x.split("/")) == 3, links)
    filtered_links = list(quality_filter)
    filtered_links = [f"https://github.com/{link}" for link in filtered_links]

    return filtered_links
