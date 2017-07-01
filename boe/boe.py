import requests

page = requests.get('http://www.bankofengland.co.uk/about/Pages/default.aspx')
contents = page.content
