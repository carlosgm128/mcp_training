#feed mcp
from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="Feed MCP")

@mcp.tool(name="fetch_rss_feed")
def fetch_rss_feed(query: str, max_results: int = 3):
    """Fetch and parse an RSS feed from the given query"""
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss")
    query_lower = query.lower()
    results = []
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description:
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
        if len(results) >= max_results:
            break

    return results or [{"message": "No Results found"}]

@mcp.tool()
def fcc_yt_search(query:str, max_results: int = 3 ,channel_id: str = "UC1gKBgknwlQagEnq4Q-UnCg"):
    """Search Kiskeya Life YouTube channel for videos matching the query"""
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UC1gKBgknwlQagEnq4Q-UnCg")
    query_lower = query.lower()
    results = []
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("media_description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "description":description,
                "link":entry.get("link","")
            })
        if len(results) >= max_results:
            break

    return results or [{"message": "No Results found"}]


if __name__ == "__main__":
    mcp.run(transport="http")