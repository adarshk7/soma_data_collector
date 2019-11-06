import argparse
import os

import praw

from db import db


LOGGING_ENABLED = bool(os.environ.get('LOGGING_ENABLED', False))


def write_comment_to_database(comment):
    if LOGGING_ENABLED:
        print(f'Comment by {comment.author}: "{comment.body}" at {comment.created_utc}')
    db.comments.insert_one({
        'author': comment.author.name,
        'body': comment.body,
        'created_utc': comment.created_utc,
        'id': comment.id,
        'parent_id': comment.parent_id,
        'subreddit': comment.subreddit.display_name,
        'subreddit_id': comment.subreddit_id,
    })


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
