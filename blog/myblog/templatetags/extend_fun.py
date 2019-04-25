from django import template
from ..models import Article
import markdown

register = template.Library()

@register.filter(name='markdown_content')
def markdown_content(value):
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    value.content = md.convert(value.content)
    value.toc = md.toc
    return value.content



