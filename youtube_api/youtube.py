from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class Yt:

    def __init__(self):
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                             developerKey=DEVELOPER_KEY)

    def youtube_search(self, query):
        # Call the search.list method to retrieve results matching the specified
        # query term.

        part_string = 'snippet'

        response = self.youtube.videos().list(
            part=part_string,
            id=query
        ).execute()

        for item in response.get('items', []):
            try:
                return item['snippet']['title']
            except HttpError as e:
                print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
