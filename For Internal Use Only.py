from wsgiref.util import request_uri
import praw
import wget
reddit = praw.Reddit(
    client_id='Cj9-71XrLwKx-f6yh1xBXQ',
    client_secret='31l_JzqFAjGzl_IfVsCuOktlUImZOA',
    user_agent="windows:Crawler2:V1(by u/watercress97)"
)
print(reddit.read_only)
i = 0
for submission in reddit.subreddit("noncredibledefense").top(limit=10):
    i = i + 1
    # img_data = requests.get(submission.url).content
    print(submission.url)
# response = wget.download(submission.url, "yoda.gif")
    url = submission.url
    urls = submission.url
    a = urls.split('.') [-1]
    if a in 'jpg' 'png':
        print(a)
        response = wget.download(url, str(i)+ '.' + str(a))
    else:
        print("invalid filetype")
print(i)