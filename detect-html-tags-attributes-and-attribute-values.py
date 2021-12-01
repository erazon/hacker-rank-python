from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print("->", element[0], ">", element[1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print("->", element[0], ">", element[1])


html = ""
for _ in range(int(input())):
    html += input()

parser = MyHTMLParser()
parser.feed(html)
parser.close()
