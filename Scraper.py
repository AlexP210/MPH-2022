import praw
import wget
import csv
import os
import time
import urllib

reddit = praw.Reddit(
    client_id='Cj9-71XrLwKx-f6yh1xBXQ',
    client_secret='31l_JzqFAjGzl_IfVsCuOktlUImZOA',
    user_agent="windows:Crawler2:V1(by u/watercress97)"
)

# Specify where to download the data
data_folder = "D:\MPH-2022-Data"

# Specify allowed file extensions
allowed_file_extensions = {
    "jpg": "image", 
    "png": "image", 
    "jpeg": "image"
}

# Go through the list of subreddits and download the top 100 posts
with open("subreddits_list.txt", 'r') as subreddits_list_file:
    subreddit_name_list = [subreddit.strip() for subreddit in subreddits_list_file.readlines()]
   
    for subreddit_name in subreddit_name_list:
        print(f"Downloading from {subreddit_name}")
        subreddit_folder = os.path.join(data_folder, subreddit_name)

        # Create the subreddit folder if it doesn't exist
        if not os.path.exists(subreddit_folder): 
            os.mkdir(subreddit_folder)
        
        # Create the index file specifying the type and statistics of each post
        with open(os.path.join(subreddit_folder, f"{subreddit_name}.csv"), 'w', newline = '') as index_file:
            writer = csv.writer(index_file, delimiter=";")
            writer.writerow(["Number", "URL", "PostID", "Upvotes", "Type", 'Title', "Content File"])
            g = 0
            for submission in reddit.subreddit(subreddit_name).top(limit=200):
                if not submission.stickied:
                    try:
                        url = submission.url
                        print(f"    {url}")

                        # Get the file extension to see if we should download the post content
                        file_extension = url.split('.')[-1]
                        sanitized_submission_title = "".join([c for c in submission.title.lower() if c in "abcdefghijklmnopqrstuvwxyz '-,?!."])
                        sanitized_submission_title = sanitized_submission_title.split("]")[-1].strip()
                        if file_extension in allowed_file_extensions:
                            content_file_path = os.path.join(subreddit_folder, f"{submission.id}.{file_extension}")
                            response = wget.download (url, content_file_path)
                            row = [
                                int(g), 
                                str(submission.url), 
                                str(submission.id), 
                                str(submission.ups), 
                                allowed_file_extensions[file_extension], 
                                sanitized_submission_title,
                                content_file_path
                            ]
                            writer.writerow(row)

                        # Check if it's a text post
                        if submission.is_self:
                            content_file_path = os.path.join(subreddit_folder, f"{submission.id}.txt")
                            with open(content_file_path, "w") as content_file:
                                content_file.write(submission.selftext)
                            row = [
                                int(g), 
                                str(submission.url), 
                                str(submission.id), 
                                str(submission.ups), 
                                "text", 
                                sanitized_submission_title,
                                content_file_path
                            ]
                            writer.writerow(row)

                        else:
                            print(f"Invalid filetype: {url}")
                    except:
                        pass
            
            time.sleep(2)

                

# sub_list = open("subreddits_list.txt", 'r')
# for i in sub_list.readlines():
#     i = i.strip()
#     filefolder = "Data\\" + str(i)
#     if not os.path.exists(filefolder): 
#         os.mkdir(filefolder)
#     with open(filefolder + "\\" + str(i) + '.csv', 'w', newline = '') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Number", "URL", "POSTID", "Upvotes", "Type", 'Title'])
#         try:
#             for submission in reddit.subreddit(i).top(limit=100):
#                 print(submission.subreddit)
#                 g = g + 1
#                 print(submission.url)
#                 url = submission.url
#                 urls = submission.url
#                 a = urls.split('.') [-1]
#                 if a in ['jpg', 'png']:
#                     print(a)
#                     response = wget.download (url, filefolder + "\\" + str(submission.subreddit) + '_' + str(g) + '.' + str(a))
#                 else:
#                     print("invalid filetype")
#                 writer.writerow([int(g), str(submission.url), str(submission.id), str(submission.ups), str(submission.post_hint), str(submission.title).split("]")[-1].strip()])
#         except:
#             print("Failed to download.")
#             pass
#     # time.sleep(2)