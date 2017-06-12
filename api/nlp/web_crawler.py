from pattern.web import Google, Bing, SEARCH, plaintext
from pattern.web import Bing
from pattern.en import sentiment


# TO IMPLEMENT: SentiWordNet

#  [X, Y] = [Goodness, Subjectivity]
def get_google_sentiment(topic_name):

    sentiment_list = []
    engine = Google(license=None)

    for result in engine.search(topic_name, cached=False):
        article_text = result.text
        sentiment_list.append(sentiment(article_text))

    return sentiment_list


print get_google_sentiment("YHOO")
    

