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

# Specify where to download the data
data_folder = "Data"
# Go through the list of subreddits and download the top 100 posts
with open("subreddits_list.txt", 'r') as subreddits_list_file:
    subreddit_name_list = [subreddit.strip() for subreddit in subreddits_list_file.readlines()]
    for subreddit_name in subreddit_name_list:
        subreddit_folder = os.path.join(data_folder, subreddit_name)
        if not os.path.exists(subreddit_folder): os.mkdir(subreddit_folder)
        with open(filefolder + "\\" + str(i) + '.csv', 'w', newline = '') as index_file:
            writer = csv.writer(index_file)
            writer.writerow(["Number", "URL", "PostID", "Upvotes", "Type", 'Title', "Content"])

sub_list = open("subreddits_list.txt", 'r')
for i in sub_list.readlines():
    i = i.strip()
    filefolder = "Data\\" + str(i)
    if not os.path.exists(filefolder): 
        os.mkdir(filefolder)
    with open(filefolder + "\\" + str(i) + '.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "URL", "POSTID", "Upvotes", "Type", 'Title'])
        try:
            for submission in reddit.subreddit(i).top(limit=100):
                print(submission.subreddit)
                g = g + 1
                print(submission.url)
                url = submission.url
                urls = submission.url
                a = urls.split('.') [-1]
                if a in ['jpg', 'png']:
                    print(a)
                    response = wget.download (url, filefolder + "\\" + str(submission.subreddit) + '_' + str(g) + '.' + str(a))
                else:
                    print("invalid filetype")
                writer.writerow([int(g), str(submission.url), str(submission.id), str(submission.ups), str(submission.post_hint), str(submission.title).split("]")[-1].strip()])
        except:
            print("Failed to download.")
            pass
    # time.sleep(2)