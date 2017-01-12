import newspaper, json, re

from newspaper import news_pool

from .models import Source, Article

def buildSources(query_text):
  context = Source.objects.values()
  data = { 'articles' : {} }
  regex = buildRegex(query_text)
  size = 0
  for index, source in enumerate(context):
    data['articles'].update(scrapeArticleUrls(source, regex, index + 1))

  data['total_articles'] = size

  return data

def scrapeArticleUrls(source, regex, count):
  scraped = newspaper.build(source['url'], memoize_articles=False)
  data = {}
  i = 1 * count
  for index, article in enumerate(scraped.articles):
    if checkRelevance(article, regex):
      data[i - 1] = {
        'url': article.url,
        'source_url': article.source_url,
        'source_position': source['position'],
        'source_brand': source['brand']
      }
      if article.title:
        title = re.sub(r' [[{(~`!@#$%^*-_=+\|)}] ', ' ', article.title).strip()
        data[i - 1]['title'] = title
      i += 1

  return data

def buildRegex(query_text):
  q = query_text.split()
  x = ''
  for index, t in enumerate(q):
    x += t
    if index != len(q) - 1:
      x += ' | '
  return x

def checkRelevance(article, regex):
  relevant = False

  r = re.compile(regex, flags=re.I | re.X)
  u = r.findall(str(article.url))
  t = r.findall(str(article.title))

  if len(u) or len(t) > 0:
    relevant = True

  return relevant

