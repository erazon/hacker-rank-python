from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        lines = comment.split('\n')
        if len(lines) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        for line in lines:
            print(line)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ""
for _ in range(int(input())):
    html += input() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
