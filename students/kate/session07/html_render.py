#! usr/bin/env python3
"""
html render activity
"""

class Element():
    tag = 'html'
    indent = '  '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]
    # python 3 "object" is assumed
    # none is handy default value bc it is immutable

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj):
        file_obj.write('<')

class Body(Element):
    tag = 'body'

class Para(Element):
    tag = 'p'

class HTML(Element):
    tag = 'HTML'
