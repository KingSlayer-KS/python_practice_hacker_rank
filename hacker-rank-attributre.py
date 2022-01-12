from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print((tag))
        for key, val in attrs:
            print("->",key+" > "+val)
   
parser = MyHTMLParser()
n = int(input()) 
for i in range(n):
    parser.feed(input())

