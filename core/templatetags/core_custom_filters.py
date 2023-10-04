from django import template
from bs4 import BeautifulSoup

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
    soup = BeautifulSoup(value, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    words = text.split()

    truncated_words = words[:num_words]
    truncated_text = ' '.join(truncated_words)

    if len(words) > num_words:
        truncated_text += '...'

    return truncated_text

# Register the filter
register = template.Library()
register.filter('truncate_html_words', truncate_html_words)

