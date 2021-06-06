"""Data Science Blogs Aggregator with Feedparser and Streamlit"""
# Necessary Library Imports:
import feedparser
import streamlit as st

st.title("WELCOME TO YOUR WEEKLY DOSE OF DATA SCIENCE DIGEST")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1487147264018-f937fba0c817")
    }
    </style>
    """,
    unsafe_allow_html=True
)


#-------------------------------------------------------------------------------------------------------------
def rss_feed_url(url):

    """given an RSS feed url, extract it's entities"""

    rss_feed_contents = feedparser.parse(url)
    news = rss_feed_contents.entries
    
    for idx, curr_news in enumerate(news):
        id = str(idx+1)
        title = curr_news['title']
        actual_link = curr_news['link']
        content = curr_news['summary'].split('<')[0] if curr_news['summary'].split('<')[0] != '' else 'No article summary available, click on the link to read'

        st.header(f"\n({id}) {title}")
        st.write(f"{content}")
        st.write(f"Read full story here: {actual_link}")
        #st.write(f"\n({id}) {title}\n02. News source: {actual_link}\n03. News Summary: {content}")
        st.write("---------------------------------------------------------")

        if idx>10:
            break
    
#-------------------------------------------------------------------------------------------------------------



# Our RSS news feeds look-up table
# dict_rss_news_feeds = {'CNN': "http://rss.cnn.com/rss/cnn_topstories.rss",
#                        'Huffington Post': "https://www.huffpost.com/section/front-page/feed?x=1"}

dict_rss_news_feeds = { 'KDnuggets': "https://www.kdnuggets.com/feed",
                        'Towards Data Science': "https://towardsdatascience.com/feed",                
                        'Dataquest': "https://www.dataquest.io/blog/feed/"}
                 

#-------------------------------------------------------------------------------------------------------------
# Fetching news summary for you:
#print("Let us fetch the headlines and summary from CNN news:")
for channel, webpage in dict_rss_news_feeds.items():
    st.title(f"From {channel}: \n")
    #print(f"Your news summary from {channel} are: \n")
    rss_feed_url(webpage)
    print("###########################################################################")
