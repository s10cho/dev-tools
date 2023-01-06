import requests
from bs4 import BeautifulSoup

fakdrop_url = 'http://172.16.120.132:9000'
topic_id = 'command.mocha.member'

topic_detail_url = '%s/topic/%s' % (fakdrop_url, topic_id)
topic_message_url = '%s/topic/%s/messages?partition={}&offset={}&count=100' % (fakdrop_url, topic_id)

def getResponse(url):
    return requests.get(url)

topic_detail_response = getResponse(topic_detail_url)

topic_detail_response.raise_for_status()  # status 200
soup = BeautifulSoup(topic_detail_response.text, "lxml")

for row in soup.find(id='partition-detail-table').find('tbody').find_all('tr'):
    partition = row.find_all_next('a')[0].text
    size = row.find_all_next('td')[3].text
    print('partition: {}, size: {}'.format(partition, size))

    topic_detail_response = getResponse(topic_detail_url)



