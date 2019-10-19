import argparse
import os

import praw


def write_comment_to_database(comment):
    print('-' * 20)
    print(comment.body)


def stream_subreddit_comments(reddit, subreddit, callback=None):
    for comment in reddit.subreddit(subreddit).stream.comments():
        if callback:
            callback(comment)

def authenticate_with_reddit():
    return praw.Reddit(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        user_agent='iPython:u/somea_interface'
    )


def get_subreddit_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--subreddit', help='Subreddit to stream')
    args = parser.parse_args()
    return args.subreddit


if __name__ == '__main__':
    subreddit = get_subreddit_from_args()
    reddit = authenticate_with_reddit()
    stream_subreddit_comments(reddit, subreddit, callback=write_comment_to_database)
