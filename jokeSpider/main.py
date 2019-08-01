import re,requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

def parse_url(url):
    res = requests.get(url,headers)
    text = res.text
    authors = []
    names = re.findall(r'<div class="author clearfix">.*?<h2>(.*?)</h2>',text,re.DOTALL)
    for name in names:
        name = name.strip()
        authors.append(name)

    contents = []
    contents_text = re.findall(r'<div class="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    for content in contents_text:
        content = content.strip()
        content = re.sub('<.*?>','',content)
        contents.append(content)

    joke = []
    for value in zip(authors,contents):
        author,content = value
        joke.append({
            'author': author,
            'content': content
        })
    return joke

def main():
    for x in range(1,11):
        url = "https://www.qiushibaike.com/text/page/{}/".format(x)
        parse_url(url)

if __name__ == "__main__":
    main()