import sys
import urllib2
from bs4 import BeautifulSoup

#conn_page = sys.argv[1]

content_link = []
for i in range(1, 230):
	conn = 'https://www.natgeomedia.com/category/news/page/'
	conn_page = conn + str(i)
	page = urllib2.urlopen(conn_page)
	soup = BeautifulSoup(page, 'html.parser')

	#name_box = soup.find('div', attrs = {'class':'td-post-content'})
	#h3 = soup.find_all('h3', {'itemprop':"name"})
	#link = soup.find_all("a", href="https://www.natgeomedia.com/news/ngnews")
	link = soup.select('h3[itemprop="name"] > a[itemprop="url"]')
	#content = list(set(content))

	#content = name_box.text.strip()
	#content = h3.strip()
	#print type(link)
	for h in link:
		content_link.append(h.get('href'))

content_link_news = []
content_link = list(set(content_link))
for c in content_link:
	hope_ngnews = c[-12:-6]
	### result(1:15): 96
	if hope_ngnews == 'ngnews':
		content_link_news.append(c)
	### Why couldn't I use the belowing code?? result(1:15): 121
'''	
	if hope_ngnews != 'ngnews':
		content_link.remove(c)
'''	
		#print i
		#print c[-12:-6]
		#i += 1

i = 1
for c in content_link_news:
	print i
	print c
	i += 1


i = 1
for page_content in content_link_news:
	page = urllib2.urlopen(page_content)
	soup = BeautifulSoup(page, 'html.parser')
	
	page_title_box = soup.find('title')
	title = page_title_box.text.strip()
	page_content_box = soup.find('div', attrs = {'class':'td-post-content'})
	if page_content_box is None:
		i += 1
		continue
	content = page_content_box.text.strip()
	title_content = title + '\n' + content
	'''
	conn_page = 'https://www.natgeomedia.com/news/ngews/19424'
	page = urllib2.urlopen(conn_page)
	soup = BeautifulSoup(page, 'html.parser')

	page_title_box = soup.find('title')
	title = page_title_box.text.strip()
	page_content_box = soup.find('div', attrs = {'class':'td-post-content'})
	content = page_content_box.text.strip()
	title_content = title + '\n' + content
	'''

	# detect the link of the next page
	page_nav_checker = soup.find('div', attrs = {'class':'page-nav'})
	if page_nav_checker is not None:
		page_nav = page_nav_checker.text.strip()
		print(page_nav)
		if page_nav is not None:
			for n in range(2, len(page_nav)):
				next_conn_page = page_content + '/' + str(n)
				next_page = urllib2.urlopen(next_conn_page)
				next_soup = BeautifulSoup(next_page, 'html.parser')

				next_page_content_box = next_soup.find('div', attrs = {'class':'td-post-content'})
				if next_page_content_box is None:
					break
				next_content = next_page_content_box.text.strip()
				title_content = title_content + '\n\n' + next_content

	'''
	next_a = soup.select('div[class="page-nav page-nav-post td-pb-padding-side"] > a')
	print(next_a)
	next_link = next_a[0].get('href')
	next_page = urllib2.urlopen(next_link)
	next_soup = BeautifulSoup(next_page, 'html,paser')

	next_page_content_box = soup.find('div', attrs = {'class':'td-post-content'})
	next_content = next_page_content_box.text.strip()
	title_content = title_content + next_content

	page_nav_checker = next_soup.find('page_nav')
	page_nav = page_nav_checker.text.strip()
	'''

	filename = 'post' + str(i) + '.txt'
	#filename = 'test_nav.txt'
	fp = open(filename, "w")
	fp.write(title_content.encode('utf8'))
	fp.close()

	print(i)
	i += 1

#fp = open("test.txt", "w")
#fp.write(content.encode('utf8'))
#fp.close()


