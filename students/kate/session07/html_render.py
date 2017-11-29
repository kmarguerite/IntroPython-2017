#! usr/bin/env python3
"""
html render activity
"""

class Element():
    """ Class for rendering html element
    # """
    tag = 'html'
    indent = '  '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
    # python 3 "object" is assumed
    # none is handy default value bc it is immutable

    def append(self, content):
        self.content.append(content)

    def render(self, file_obj, cur_ind=""):
        
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

class OneLineTag(Element):

    def render(self, out_file, ind=""):
        out_file.write('\n' + ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file)
            except AttributeError:
                out_file.write(str(each))
        out_file.write('</' + self.tag + '>')


class SelfClosingTag(Element):

    def render(self, out_file, ind = "", depth=1):
        out_file.write("{}<{} />\n".format(ind*depth, self.tag))

class A(Element):
    def __init__(self,link, text):
        super(A, self).__init__()
        self.link = link
        self.text = text

    def render(self, out_file, ind="", depth=1):
        out_file.write('{}<a href="{}">{}</a>\n'.format(ind*depth, self.link, self.text))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Title(OneLineTag):
    tag = 'title'

class Body(Element):
    tag = 'body'

class Para(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'

class Head(Element):
    tag = 'head'

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"
