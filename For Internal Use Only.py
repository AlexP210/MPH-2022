from wsgiref.util import request_uri
import praw
import wget
import csv
import os
import time
reddit = praw.Reddit(
    client_id='Cj9-71XrLwKx-f6yh1xBXQ',
    client_secret='31l_JzqFAjGzl_IfVsCuOktlUImZOA',
    user_agent="windows:Crawler2:V1(by u/watercress97)"
)
print(reddit.read_only)
g = 0
sub_list = open("MPH-2022\\subreddits_list.txt", 'r')
for i in sub_list.readlines():
    i = i.strip()
    filefolder = "MPH-2022\\Data\\" + str(i)
    if not os.path.exists(filefolder): 
        os.mkdir(filefolder)
    with open(filefolder + "\\" + str(i) + '.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "URL", "POSTID", "Upvotes", "Type", 'Title'])
        try:
            for submission in reddit.subreddit(i).top(limit=10):
                print(submission.subreddit)
                g = g + 1
                print(submission.url)
                url = submission.url
                urls = submission.url
                a = urls.split('.') [-1]
                if a in 'jpg' 'png':
                    print(a)
                    response = wget.download (url, filefolder + "\\" + str(submission.subreddit) + '_' + str(g) + '.' + str(a))
                else:
                    print("invalid filetype")
                writer.writerow([int(g), str(submission.url), str(submission.id), str(submission.ups), str(submission.post_hint), str(submission.title)])
        except:
            pass
    time.sleep(2)