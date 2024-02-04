import os
from datetime import datetime

from googleapiclient.discovery import build

from langchain.tools import BaseTool


from dotenv import find_dotenv, load_dotenv
path_to_env = find_dotenv()
load_dotenv(path_to_env)

ggl_api_key = os.environ.get("GOOGLE_SEARCH_CLIENT_KEY")
ggl_cse_id = os.environ.get("GOOGLE_CSE_ID")


class DateTimeTool(BaseTool):
     name="Get Today's Date and Current Time"
     description="use this tool to get today's date and current time in 12-hour format"

     def _run(self):
          
          return datetime.today().strftime("%a %d %b %Y, %I:%M%p")
     
     def _arun(self):
          raise NotImplementedError("This tool does not support async")


class GoogleSearchTool(BaseTool):
    name="Perform google search for provided query"
    description="Use this tool to get google search results."

    def google_search(self, search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=ggl_api_key)
        res = service.cse().list(q=search_term, cx=ggl_cse_id, gl='in', **kwargs).execute()
        return res['items']
     
    def _run(self, search_query):
        
        results = self.google_search(search_query, num=5)
        results = [{'title':ele['title'],'link':ele['link'],'snippet':ele['snippet']} for ele in results]
        return results
     
    def _arun(self):
        raise NotImplementedError("This tool does not support async")


if __name__ == "__main__":
    temp = GoogleSearchTool()

    print(temp.run("Life"))
