#! usr/bin/env python3
"""
test html render activity
"""

import html_render
import pytest
from html_render import Element, Body, Para, HTML

def test_new_element():
    el_object = html_render.Element()
    el_object = html_render.Element('hedgweena')

def test_add_content():
    el_object = html_render.Element('hedgie')
    el_object = html_render.Element()
    print(el_object)
    assert el_object.content == []
    # if an assertion fails pytest will fail and spit out info

def test_adding_empty_string():
    el_object = html_render.Element('')
    assert el_object.content == ['']

def test_append_string():
    el_object = html_render.Element('Hedgie')
    el_object.append(' Hugs!')
    assert el_object.content == ['Hedgie Hugs!']

def test_tag_exists():
    assert html_render.Element.tag == 'html'
    el_object = html_render.Element.tag('spam, spam, spam')
    assert el_object.tag == 'html'

def test_indent_exists():
    assert html_render.Element.indent == '  '

def test_body_tag():
    assert Body.tag == 'body'

def test_para_tag():
    assert Para.tag == 'p'

def test_html_tag():
    assert HTML.tag == 'HTML'

def test_render_non_strings():
    el_object - Element(Body('a neat string'))
