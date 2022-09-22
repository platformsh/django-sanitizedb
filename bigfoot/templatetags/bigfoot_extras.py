from django import template

register = template.Library()

@register.filter(name='user_activity_text')
def user_activity_text(user):
    comment_count = user.get_recent_comments_count()

    if (comment_count > 50):
        return 'bigfoot fanatic'
    elif (comment_count > 30):
        return 'believer'
    elif (comment_count > 20):
        return 'hobbyist'

    return 'skeptic'
