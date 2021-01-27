from django.utils.timezone import make_aware

from facebook_scraper import get_posts
from api.models import FacebookPost


def get_reaction_value(post, react_type):
    try:
        return post['reactions'][react_type]
    except:
        return 0


def scrape_posts():
    fb_posts = []
    page = 'samatv.net'
    for post in get_posts(page, pages=20000, extra_info=True, timeout=60):
        fb_post = FacebookPost(
            page_name=page,
            post_id=post['post_id'] if post['post_id'] is not None else '',
            text=post['text'] if post['text'] is not None else '',
            shared_text=post['shared_text'] if post['shared_text'] is not None else '',
            time=make_aware(post['time']),
            image=post['image'] if post['image'] is not None else '',
            video=post['video'] if post['video'] is not None else '',
            num_reacts=post['likes'] if post['likes'] is not None else 0,
            like_react=get_reaction_value(
                post, 'like') if 'reactions' in post is not None else 0,
            sorry_react=get_reaction_value(
                post, 'sorry') if 'reactions' in post is not None else 0,
            anger_react=get_reaction_value(
                post, 'anger') if 'reactions' in post is not None else 0,
            love_react=get_reaction_value(
                post, 'love') if 'reactions' in post is not None else 0,
            wow_react=get_reaction_value(
                post, 'wow') if 'reactions' in post is not None else 0,
            support_react=get_reaction_value(
                post, 'support') if 'reactions' in post is not None else 0,
            haha_react=get_reaction_value(
                post, 'haha') if 'reactions' in post is not None else 0,
            comments=post['comments'] if post['comments'] is not None else 0,
            shares=post['shares'] if post['shares'] is not None else 0,
            post_url=post['post_url'] if post['post_url'] is not None else ''
        )
        fb_posts.append(fb_post)
        if len(fb_posts) > 30:
            print("saving facebook posts")
            print("latest one:")
            print(fb_post.post_id)
            print(fb_post.time)
            FacebookPost.objects.bulk_create(fb_posts)
            fb_posts = []
    FacebookPost.objects.bulk_create(fb_posts)
