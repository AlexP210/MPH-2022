# Compiles a list of subreddits and exports to subreddits_list.txt

from wsgiref.util import request_uri
import praw
import wget
reddit = praw.Reddit(
    client_id='Cj9-71XrLwKx-f6yh1xBXQ',
    client_secret='31l_JzqFAjGzl_IfVsCuOktlUImZOA',
    user_agent="windows:Crawler2:V1(by u/watercress97)"
)
print(reddit.read_only)


topics = ["art","politics","nature","sports","technology","animals","finance","literature","music","science","physics"]
all_sbrs = []
all_sbrs_title = []

for i in topics:
    sbrs = reddit.subreddits.search(i)
    for j in sbrs:
        if j not in all_sbrs:
            all_sbrs.append(j)
            all_sbrs_title.append(j.display_name.split('/')[-1])


f = open("subreddits_list.txt", "w")
for i in range(len(all_sbrs_title)):
    towrite = all_sbrs_title[i]
    try:
        f.write(towrite)
        f.write("\n")
    except Exception as e:
        print('missed one')
f.close()