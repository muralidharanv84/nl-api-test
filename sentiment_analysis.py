from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                                 '$discovery/rest?version={apiVersion}')

def analyze_sentiment(review_text):
    '''Run a sentiment analysis request on text within a passed filename'''

    credentials = GoogleCredentials.get_application_default().create_scoped(
            ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    service = discovery.build('language', 'v1beta1',
                              http=http, discoveryServiceUrl=DISCOVERY_URL)
    
    service_request = service.documents().analyzeSentiment(
        body={
            'document': {
                 'type': 'PLAIN_TEXT',
                 'content': review_text,
            }
        })

    response = service_request.execute()
    polarity = response['documentSentiment']['polarity']
    magnitude = response['documentSentiment']['magnitude']
    print('Sentiment: polarity of %s with magnitude of %s' % (polarity, magnitude))
    return (polarity, magnitude)
