<<<<<<< HEAD
def print_hedz(url='https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)
    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)
def extract_headline_text(txt):
	mystr = parse_headline_tags(txt)
	xlist = mystr.split('>')
def parse_headline_tags(txt):
	fetch_html(url)
	myList = []
	lines = fetch_html.splitlines()
	for line in lines:
		if '<h3><a' in line:
			myList.append(line)
	return myList
def fetch_html(url):
	import requests
	url = 'https://wgetsnaps.github.io/stanford-edu-news/news/'
	resp=requests.get(url)
=======
def print_hedz(url='https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)
    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)
def extract_headline_text(txt):
	mystr = parse_headline_tags(txt)
	xlist = mystr.split('>')
def parse_headline_tags(txt):
	fetch_html(url)
	myList = []
	lines = fetch_html.splitlines()
	for line in lines:
		if '<h3><a' in line:
			myList.append(line)
	return myList
def fetch_html(url):
	import requests
	url = 'https://wgetsnaps.github.io/stanford-edu-news/news/'
	resp=requests.get(url)
>>>>>>> 8ca8f4c5a16b1245613c8cd625edf7d70d9d2c60
	print(resp.text)