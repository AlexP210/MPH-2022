import praw
reddit = praw.Reddit(
    client_id='Cj9-71XrLwKx-f6yh1xBXQ',
    client_secret='31l_JzqFAjGzl_IfVsCuOktlUImZOA',
    user_agent="windows:Crawler2:V1(by u/watercress97)"
)
print(reddit.read_only)
for submission in reddit.subreddit("itookapicture").hot(limit=10):
    print(submission.title)
