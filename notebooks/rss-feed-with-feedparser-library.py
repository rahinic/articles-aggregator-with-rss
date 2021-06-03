"""RSS feed aggregator using feedparser library"""

# Necessary Library Imports:
import feedparser

#-------------------------------------------------------------------------------------------------------------
def rss_feed_url(url):

    """given an RSS feed url, extract it's entities"""

    rss_feed_contents = feedparser.parse(url)
    news = rss_feed_contents.entries
    
    for idx, curr_news in enumerate(news):
        id = str(idx+1)
        title = curr_news['title']
        actual_link = curr_news['link']
        content = curr_news['summary'].split('<')[0] if curr_news['summary'].split('<')[0] != '' else 'No news summary available'
        print("---------------------------------------------------------")
        print(f"\nNews #:{id}\n01. News Headlines: {title}\n02. News source: {actual_link}\n03. News Summary: {content}")
        print("---------------------------------------------------------")
    
#-------------------------------------------------------------------------------------------------------------
# Our RSS news feeds look-up table
dict_rss_news_feeds = {'CNN': "http://rss.cnn.com/rss/cnn_topstories.rss",
                       'Huffington Post': "https://www.huffpost.com/section/front-page/feed?x=1"}

#-------------------------------------------------------------------------------------------------------------
# Fetching news summary for you:
print("Let us fetch the headlines and summary from CNN news:")
for channel, webpage in dict_rss_news_feeds.items():
    print(f"Your news summary from {channel} are: \n")
    rss_feed_url(webpage)
    print("###########################################################################")