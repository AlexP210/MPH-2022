import praw
import requests

# Grab a read-only reddit instance
reddit = praw.Reddit(
    client_id='Cj9-71XrLwKx-f6yh1xBXQ',
    client_secret='31l_JzqFAjGzl_IfVsCuOktlUImZOA',
    user_agent="windows:Crawler2:V1(by u/TheAlexinatorinator)"
)

# Accepted filetypes
filetypes = ["jpg", "png", "jpeg"]

print(reddit.read_only)
for submission in reddit.subreddit("itookapicture").hot(limit=10):
    url = submission.url
    if "png" in url or "jpg" in url:    
        name, filetype = url.split("/")[-1].split(".")
        if filetype in filetypes:
            r = requests.get(url, allow_redirects=True)
            open(f'{name}.{filetype}', 'wb').write(r.content)