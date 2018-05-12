from __future__ import absolute_import, unicode_literals
from urllib.parse import urlparse, ParseResult
from django import template

register = template.Library()


# modified from https://stackoverflow.com/questions/21659044/how-can-i-prepend-http-to-a-url-if-it-doesnt-begin-with-http
@register.simple_tag
def modify_site_name(site):
    if not site:
        return
    site = urlparse(site, 'http')
    netloc = site.netloc or site.path
    path = site.path if site.netloc else ''
    site = ParseResult(site.scheme, netloc, path, *site[3:])
    return site.geturl()
