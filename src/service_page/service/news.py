import os
import datetime
import requests
from resources.global_resources.variables import *
from resources.global_resources.log_vars import logPass, logFail
from log.log import log_outbound


def createPage_news(service):
    #
    resources = '<link rel="stylesheet" href="/resource/css/jarvis.service_page.news.css">'
    #
    html_buttons = ''
    html_body = ''
    #
    # Top Headlines
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='12',
                                        service_id=service['service_id'],
                                        function_id='top_headlines',
                                        function_name='Top Headlines',
                                        btn_class='service_function_btn_active')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='top_headlines',
                                     function_body=_html_articles(service, 'sources'),
                                     body_class='service_function_body_active')
    #
    args = {'service_id': service['service_id'],
            'resources': resources,
            'html_buttons': html_buttons,
            'html_body': html_body}
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_container.html'), 'r') as f:
        page_body = f.read().format(**args)
    #
    return page_body


def _html_articles(service, option):
    #
    timestamp = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    html_articles = '<p style="text-align: right">Last updated {timestamp}</p>'.format(timestamp=timestamp)
    #
    data = _get_headlines(service, option)
    dict_html = _create_dict_of_article_html(data)
    #
    for html_key in sorted(dict_html.keys(), reverse=True):
        html_articles += dict_html[html_key]
    #
    return html_articles


def _get_headlines(service, option):
    #
    uri = service_uri_news_headlines.format(option=option)
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=uri)
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get(service_url, headers=headers)
    #
    if r.status_code == requests.codes.ok:
        log_outbound(logPass,
                     service['ip'], service['port'], 'GET', uri,
                     '-', '-',
                     r.status_code)
        return r.json()
    else:
        log_outbound(logFail,
                     service['ip'], service['port'], 'GET', uri,
                     '-', '-',
                     r.status_code)
        return []


def _create_dict_of_article_html(data):
    #
    dict_html = {}
    #
    for article in data['articles']:
        #
        try:
            #
            if article['description'] is None or article['description'] is None:
                raise Exception
            #
            if not article['publishedAt'] is None:
                #
                try:
                    publish_datetime = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%Sz")
                except:
                    try:
                        publish_datetime = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%Sz.%f")
                    except:
                        pass
                #
                #
                try:
                    publish_string = publish_datetime.strftime('%d-%m-%Y %H:%M')
                except:
                    publish_datetime = datetime.datetime.now()
                    publish_string = '-'
                    #
            else:
                publish_datetime = datetime.datetime.now()
                publish_string = '-'
            #
            if article['urlToImage']:
                image_url = article['urlToImage'].encode('utf-8')
            else:
                image_url = ''
            #
            args_item = {'source_name': article['source']['name'],
                         'article_link': article['url'],
                         'article_title': article['title'],
                         'article_description': article['description'],
                         'article_date': publish_string,
                         'article_image': image_url.decode('UTF-8')}
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/news/article_item.html'), 'r') as f:
                dict_html[publish_datetime] = f.read().format(**args_item)
            #
        except Exception as e:
            pass
    #
    return dict_html

def removeUnicodeChars(text):
    text = text.replace('\\u2019', '\'')
    text = text.replace('\u2019', '\'')
    return text