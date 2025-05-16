from ezmcp import ezmcp, TextContent
import logging
import requests
from typing import List
# ..custom
from env_config import (
    YOTUBE_API_KEY,
    APP_VERSION,
    APP_PORT
)


# logging config
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s[%(filename)s:%(lineno)s-%(funcName)s()]-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

# Create an ezmcp application
app = ezmcp(f"youtube-mcp-server - v{APP_VERSION}")

# Define a tool
@app.tool(description="about mcp server")
async def about():
    """Echo back mcp server functionality"""
    return [TextContent(type="text", text="mcp sse server to query youtube videos based on video title or topic")]

@app.tool(description="search youtube video by topic")
async def query_youtube_video_by_topic(topic: str):
    """search a youtube video based on a topic or video title"""
    logging.debug(f"Search: querying video using topic: {topic}")
    try:
        url = (
            'https://www.googleapis.com/youtube/v3/search'
            '?part=snippet&type=video&maxResults=5'
            f'&q={topic}&key={YOTUBE_API_KEY}'
        )
        # consolidate video ids
        video_id_list: List[str] = []
        response = requests.get(url)
        data = response.json()
        # edge case - if data is empty
        if data is None or (data is not None and "items" not in data.keys()):
            raise ValueError("invalid topic / search returned empty response")
        for item in data['items']:
            video_id_list.append(item['id']['videoId'])
        logging.debug(f"video id list is: {str(video_id_list)}")
        vids_list: List[str] = []
        # provide a csv list of youtube urls with video ids
        for id in video_id_list:
            vids_list.append(f'https://www.youtube.com/watch?v={id}')
        return [TextContent(type="text", text=f'{",".join(vids_list)}')]
    # error handling
    except Exception as err:
        logging.error(f"Search: Error {err.__class__} - {str(err)}")
        error_msg: str = f"Search: An Error occurred when searching for topic: {topic}"
        return [TextContent(type="text", text=error_msg)]
        
# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(APP_PORT))
