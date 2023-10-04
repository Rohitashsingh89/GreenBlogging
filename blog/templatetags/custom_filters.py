import os
from django import template

register = template.Library()

@register.filter
def truncate_html_lines(value, num_lines):
    from html import unescape
    from django.utils.html import strip_tags, linebreaks

    # Unescape HTML entities, strip HTML tags, and convert line breaks to newlines
    text = unescape(strip_tags(linebreaks(value)))

    # Split the text into lines
    lines = text.split('\n')

    # Take the specified number of lines
    truncated_lines = lines[:num_lines]

    # Join the lines back together with line breaks
    return '\n'.join(truncated_lines)

@register.filter
def truncate_html_words(value, num_words):
    from html import unescape
    from django.utils.html import strip_tags

    # Unescape HTML entities and strip HTML tags
    text = unescape(strip_tags(value))

    # Split the text into words
    words = text.split()

    # Take the specified number of words
    truncated_words = words[:num_words]

    # Join the words back together with spaces
    truncated_text = ' '.join(truncated_words)

    # Add an ellipsis (...) if the text was truncated
    if len(words) > num_words:
        truncated_text += '...'

    return truncated_text