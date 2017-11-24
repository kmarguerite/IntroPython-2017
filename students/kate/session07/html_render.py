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
        all_content = ('<' + self.tag + '>')
        for each in self.content:
            try:
                all_content += each
            except TypeError:
                each.render(file_obj)
        all_content += '</' + self.tag + '>'

        self.write_to_file(file_obj, all_content)

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)

class Body(Element):
    tag = 'body'

class Para(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):

    def render(self, out_file, ind=""):
        out_file.write('\n' + ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file)
            except AttributeError:
                out_file.write(str(each))
        out_file.write('</' + self.tag + '>')

class Title(OneLineTag):
    tag = 'title'
