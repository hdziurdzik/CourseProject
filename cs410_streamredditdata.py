
import praw

reddit = praw.Reddit(client_id='6_qit9bTgw0cNaqHEcCwDA', client_secret='zG5M9WEkJw__o1Ia-Z9sp-J4-2XTFw', user_agent='CS 410 Final Project Test', check_for_async=False)

import json
from datetime import datetime

posts = []
ids = [] # keep track of post ids that have been visited
uiuc_subreddit = reddit.subreddit('UIUC')
keywords = ["restaurant", "eating out", "coffee shop", "dining", "pub", "bar"]
for keyword in keywords:
  for post in uiuc_subreddit.search(keyword, limit=50):
      if post.id in ids: # avoid duplicates
        continue
      else:
        ids.append(post.id)
      
      # post data
      body = post.selftext
      title = post.title
      created = datetime.fromtimestamp(post.created).strftime('%Y-%m-%d')

      submission = post
      submission.comments.replace_more(limit=0)
      comments = []

      for comm in submission.comments.list():
        comments.append(comm.body)
      
      post_dict = {'title':title, 'created':created, 'body':body, 'comments':comments}
      posts.append(post_dict)

posts

json_object = json.dumps(posts, indent=4) # convert posts list to json
with open("reddit_data_big.json", "w") as outfile: #save as json file
    outfile.write(json_object)