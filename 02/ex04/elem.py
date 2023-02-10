#!/usr/bin/python3


class Text(str):


    def __str__(self):
        return super().__str__().replace(
                '<', '&lt;').replace(
                    '>', '&gt;').replace(
                        '"', '&quot;').replace("\&quot;", '"').replace(
                            '\n', '\n<br />\n')
        


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    [...]

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        
        if content:
            self.add_content(content)
        elif content != None and not isinstance(content, Text):
            raise Elem.ValidationError
        self.tag_type = tag_type
        
    def __str__(self):
        if self.tag_type == 'double':
            result = "<" + self.tag + self.__make_attr() + ">" + self.__make_content() + "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            result = "<" + self.tag + self.__make_attr() + "/>"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  '
            result += str(elem).replace('\n', '\n  ') + '\n'

        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    class ValidationError(Exception):
            def __init__(self):
                super().__init__(self, "Invalid input")

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    elem = Elem('html', 
    content = [Elem( 'head', 
    content = Elem('title', 
    content = Text('\\"Hello ground\\"'))),
    Elem( 'body',
    content = [Elem('h1', 
    content = Text('\\"Oh on, not again!\\"')), 
    Elem('img', attr= {"src=" : "http://i.imgur.com/pfp3T.jpg"})])])

    print(elem)
