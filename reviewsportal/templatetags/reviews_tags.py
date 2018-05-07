from __future__ import absolute_import, unicode_literals
from urllib.parse import urlparse, ParseResult
from django import template

register = template.Library()

@register.simple_tag
def modify_site_name(site):
    if not site:
        return
    site = urlparse(site)
    if not site.scheme:
        site = ParseResult('http', *site[1:])
    return site.geturl()
