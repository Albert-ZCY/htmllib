import os
import json
from .Tool import *

class HtmlWidget():
    def __init__(self, content='', **args):
        self.args = args
        self.content = ''
        if isinstance(content, list):
            for item in content:
                if isinstance(item, str):
                    self.content += '\n'+item
                else:
                    self.content += '\n'+item.code
        else:
            self.content = content
        self.name = ''

    def setup(self):
        arg_span = dictToArgs(self.args)
        self.code = f'<{self.name}{arg_span}>{self.content}</{self.name}>'
    
    def render(self):
        self.web_lines = loadWebLines()
        _head_line = getPos('/body')
        self.web_lines.insert(_head_line, self.code)
        writeWebLines(self.web_lines)
    
    def addItem(self, item):
        if isinstance(item, str):
            self.content += '\n'+item
        else:
            self.content += '\n'+item.code
        self.setup()


class HtmlComment():
    def __init__(self, content=''):
        self.content = content
        self.setup()

    def setup(self):
        self.code = f'<!--{self.content}-->'
    
    def render(self):
        self.web_lines = loadWebLines()
        _head_line = getPos('/body')
        self.web_lines.insert(_head_line, self.code)
        writeWebLines(self.web_lines)


class AnchorLink(HtmlWidget):
    def __init__(self, content='', href='', **args):
        args['href'] = href
        super().__init__(content, **args)
        self.name = 'a'
        self.setup()


class Navigation(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'nav'
        self.setup()


class Heading(HtmlWidget):
    def __init__(self, content='', size=1, **args):
        super().__init__(content, **args)
        if 1 <= size <= 6:
            self.name = f'h{size}'
            self.setup()


class Acronym(HtmlWidget):
    def __init__(self, content='', title='', **args):
        args['title'] = title
        super().__init__(content, **args)
        self.name = 'acronym'
        self.setup()


class Abbreviation(HtmlWidget):
    def __init__(self, content='', title='', **args):
        args['title'] = title
        super().__init__(content, **args)
        self.name = 'abbr'
        self.setup()


class Address(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'address'
        self.setup()


class Br(HtmlWidget):
    def __init__(self, **args):
        super().__init__('', **args)
        self.name = 'br'
        self.setup()


class Hr(HtmlWidget):
    def __init__(self, **args):
        super().__init__('', **args)
        self.name = 'hr'
        self.setup()
    

class Bold(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'b'
        self.setup()


class Bdi(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'bdi'
        self.setup()


class Bdo(HtmlWidget):
    def __init__(self, content='', dir='', **args):
        args['dir'] = dir
        super().__init__(content, **args)
        self.name = 'bdo'
        self.setup()


class Big(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'big'
        self.setup()


class Typewriter(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'tt'
        self.setup()


class Italics(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'i'
        self.setup()


class Small(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'small'
        self.setup()


class Center(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'center'
        self.setup()


class BlockQuote(HtmlWidget):
    def __init__(self, content='', cite='', **args):
        args['cite'] = cite
        super().__init__(content, **args)
        self.name = 'blockquote'
        self.setup()


class Emphasize(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'em'
        self.setup()


class Strong(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'strong'
        self.setup()


class Define(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'dfn'
        self.setup()


class Code(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'code'
        self.setup()


class Sample(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'samp'
        self.setup()
    

class Keyboard(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'kbd'
        self.setup()


class Variable(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'var'
        self.setup()


class Preset(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'pre'
        self.setup()


class Cite(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'cite'
        self.setup()


class Delete(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'del'
        self.setup()


class Font(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'font'
        self.setup()


class Insert(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'ins'
        self.setup()


class Mark(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'mark'
        self.setup()


class Quote(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'q'
        self.setup()


class Meter(HtmlWidget):
    def __init__(self, value=1, min=0, max=1, **args):
        args['value'] = value
        args['min'] = min
        args['max'] = max
        super().__init__('', **args)
        self.name = 'meter'
        self.setup()


class Progress(HtmlWidget):
    def __init__(self, value=1, max=1, **args):
        args['value'] = value
        args['max'] = max
        super().__init__('', **args)
        self.name = 'progress'
        self.setup()


class Rp(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'rp'
        self.setup()


class Rt(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'rt'
        self.setup()


class Ruby(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'ruby'
        self.setup()


class Sup(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'sup'
        self.setup()


class Sub(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'sub'
        self.setup()


class Time(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'time'
        self.setup()


class UnderLine(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'u'
        self.setup()


class WordBreak(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'wbr'
        self.setup()


class Div(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'div'
        self.setup()


class Phrase(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'p'
        self.setup()


class Span(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'span'
        self.setup()


class Header(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'header'
        self.setup()


class Footer(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'footer'
        self.setup()


class Section(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'section'
        self.setup()


class Article(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'article'
        self.setup()


class Aside(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'aside'
        self.setup()


class Details(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'details'
        self.setup()


class Dialog(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'dialog'
        self.setup()


class Summary(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'summary'
        self.setup()


class Image(HtmlWidget):
    def __init__(self, src='', alt='', **args):
        args['src'] = src
        args['alt'] = alt
        super().__init__('', **args)
        self.name = 'img'
        self.setup()


class Map(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'map'
        self.setup()


class Area(HtmlWidget):
    def __init__(self, **args):
        super().__init__('', **args)
        self.name = 'area'
        self.setup()


class Canvas(HtmlWidget):
    def __init__(self, **args):
        super().__init__('', **args)
        self.name = 'canvas'
        self.setup()


class Figure(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'figure'
        self.setup()


class FigureCaption(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'figcaption'
        self.setup()


class Audio(HtmlWidget):
    def __init__(self, content='', src='', **args):
        args['src'] = src
        super().__init__(content, **args)
        self.name = 'audio'
        self.setup()


class AudioSource(HtmlWidget):
    def __init__(self, src='', type='', **args):
        args['src'] = src
        args['type'] = type
        super().__init__('', **args)
        self.name = 'source'
        self.setup()


class Video(HtmlWidget):
    def __init__(self, content='', src='', **args):
        args['src'] = src
        super().__init__(content, **args)
        self.name = 'video'
        self.setup()


class VideoTrack(HtmlWidget):
    def __init__(self, src='', **args):
        args['src'] = src
        super().__init__('', **args)
        self.name = 'track'
        self.setup()


class srcipt(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'srcipt'
        self.setup()


class srciptWarning(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'nosrcipt'
        self.setup()


class Embed(HtmlWidget):
    def __init__(self, src='', **args):
        args['src'] = src
        super().__init__('', **args)
        self.name = 'embed'


class Object(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'object'
        self.setup()


class Param(HtmlWidget):
    def __init__(self, **args):
        args['src'] = src
        super().__init__('', **args)
        self.name = 'param'
        self.setup()


class UnorderedList(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'ul'
        self.setup()


class OrderedList(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'ol'
        self.setup()


class DefinedList(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'dl'
        self.setup()


class NormalListItem(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'li'
        self.setup()


class DefinedListItem(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'dt'
        self.setup()


class DefinedListInformation(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'dd'
        self.setup()


class Menu(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'menu'
        self.setup()


class MenuItem(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'menuitem'
        self.setup()


class Table(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'table'
        self.setup()


class TableCaption(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'caption'
        self.setup()


class TableHeadCell(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'th'
        self.setup()


class TableRow(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'tr'
        self.setup()


class TableCell(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'td'
        self.setup()


class TableHead(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'thead'
        self.setup()


class TableBody(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'tbody'
        self.setup()


class TableFoot(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'tfoot'
        self.setup()


class TableColumnAttribute(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'col'
        self.setup()


class TableColumnAttributeGroup(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'colgroup'
        self.setup()


class Form(HtmlWidget):
    def __init__(self, content='', action='', **args):
        super().__init__(content, **args)
        args['action'] = action
        args['method'] = method
        self.name = 'form'
        self.setup()


class FormInput(HtmlWidget):
    def __init__(self, type='', value='', **args):
        super().__init__('', **args)
        args['type'] = type
        args['value'] = value
        self.name = 'input'
        self.setup()


class FormTextBox(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'textarea'
        self.setup()


class FormButton(HtmlWidget):
    def __init__(self, content='', type='', **args):
        super().__init__(content, **args)
        args['type'] = type
        self.name = 'button'
        self.setup()


class FormSelect(HtmlWidget):
    def __init__(self, content='', value='', **args):
        super().__init__(content, **args)
        args['value'] = value
        self.name = 'select'
        self.setup()


class FormSelectOption(HtmlWidget):
    def __init__(self, content='', value='', **args):
        super().__init__(content, **args)
        args['value'] = value
        self.name = 'option'
        self.setup()


class FormSelectOptionGroup(HtmlWidget):
    def __init__(self, content='', label='', **args):
        super().__init__(content, **args)
        args['label'] = label
        self.name = 'optgroup'
        self.setup()


class FormLabel(HtmlWidget):
    def __init__(self, content='', for_='', **args):
        super().__init__(content, **args)
        args['for'] = for_
        self.name = 'label'
        self.setup()


class FormFieldSet(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'fieldset'
        self.setup()


class FormLegend(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'legend'
        self.setup()


class FormDatalist(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'datalist'
        self.setup()


class FormKeygen(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'keygen'
        self.setup()


class FormOutput(HtmlWidget):
    def __init__(self, content='', for_='', **args):
        super().__init__(content, **args)
        args['for'] = for_
        self.name = 'label'
        self.setup()


class Frame(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'frame'
        self.setup()


class FrameSet(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'frameset'
        self.setup()


class FrameInline(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'iframe'
        self.setup()


class Style(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'style'
        self.setup()
        self.render()


class Script(HtmlWidget):
    def __init__(self, content='', **args):
        super().__init__(content, **args)
        self.name = 'script'
        self.setup()
        self.render()