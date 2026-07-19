from ddgs import DDGS


def get_live_news(sport):
    query = f"{sport} latest news"

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))

    return results