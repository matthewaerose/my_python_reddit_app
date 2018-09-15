import requests
import requests.auth
import praw
import re

class PythonRedditApp:

    def __init__(self):
        self.CLIENT_ID = ""
        self.SECRET = ""
        self.PASSWORD = ""
        self.USERNAME = ''
        self.TOKEN = ''
        self.subject_redditor = ''

    def read_file(self):
        f = open("text", "r")

        lines = f.readlines()

        for line in lines:
            if "id" in line:
                self.CLIENT_ID = line.split(':')[-1].strip()
            if "secret" in line:
                self.SECRET = line.split(':')[-1].strip()
            if "username" in line:
                self.USERNAME = line.split(':')[-1].strip()
            if "password" in line:
                self.PASSWORD = line.split(':')[-1].strip()

    def get_client_id(self):
        return self.CLIENT_ID

    def get_secret(self):
        return self.SECRET

    def get_password(self):
        return self.PASSWORD

    def get_username(self):
        return self.USERNAME

    def get_token(self):
        return self.TOKEN

    def generate_token(self):
        client_auth = requests.auth.HTTPBasicAuth(app.get_client_id(), app.get_secret())
        post_data = {"grant_type": "password", "username": app.get_username(), "password": app.get_password()}
        headers = {"User-Agent": f"ChangeMeClient/0.1 by {app.get_username()}"}
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                                 headers=headers)
        res = response.json()
        self.TOKEN = res['access_token']




app = PythonRedditApp()
app.read_file()
app.generate_token()
reddit = praw.Reddit(client_id=app.get_client_id(),
            client_secret=app.get_secret(),
            password=app.get_password(),
            user_agent="USERAGENT",
            username=app.get_username())

comment_dictionary = []

for comment in reddit.redditor('').comments.new(limit=None):
    result = re.sub('([^\w\s/]|_)+', '', comment.body)
    comment_dictionary.append(result)

comment_dictionary.
print(f"number of comments: {len(comment_dictionary)}")

# print(app.get_token())
