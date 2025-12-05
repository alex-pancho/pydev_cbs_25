# xml xpath testing and parsing
# https://www.guru99.com/xpath-selenium.html
from lxml import html, etree
import requests


def get_html_content(url:str = 'https://example.com') -> str:
    """ Get html from source """
    response = requests.get(url)
    return response.text


def get_tree(html_text:str):
    return html.fromstring(html_text)


def find_by(tree: html, locator, by_text=True):
    if by_text:
        return tree.xpath(f'//p[contains(., "{locator}")]')[0]
    else:
        return tree.xpath(locator)[0]


def broken_html():
    return """<html><head>
    <title>test<body><h1>page title</h1>
    <a href='mailto:my@mail.com' rel='my@mail.com'>click me</a>
    <p class='abc' > some text
    <div id="xyz"> text </div>  <p class="">невірний, покоцаний html
    """ # невірний покоцаний хтмл


def clean_html(broken_html:str) -> str:
    parser = etree.HTMLParser()
    html_root = etree.fromstring(broken_html, parser)
    return etree.tostring(html_root, pretty_print=True, method="html", encoding="utf-8")


if __name__ == "__main__":
    url = "https://lxml.de/"
    html_content = get_html_content(url)
    print(html_content)
    tree = get_tree(html_content)
    print(tree)
    xpath = '//div[@id="support-the-project"]/p[@class="center"][3]'
    
    donate_button = find_by(tree, xpath, False)
    print(donate_button.text)

    xpath2 = '//div[@id="support-the-project"]/p[contains(., "Support lxml")]'
    text = "Support lxml"
    donate_button = find_by(tree, text)
    print(donate_button.text)
    print("="*8)
    out = clean_html(broken_html()).decode("utf-8")
    print(out)

