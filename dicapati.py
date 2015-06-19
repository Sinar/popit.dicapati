import requests
import json
import dateutil
import datetime


def dewan_rakyat_posts(url='http://sinar-malaysia.popit.mysociety.org',
                       popit_id='53633b5a19ee29270d8a9ecf',
                       total=222):
    """
    Checks if posts in popit_id organization matches total
    popit_id str
    total int
    url str eg. http://sinar-malaysia.popit.mysociety.org
    """

    org_req = requests.get(url + '/api/v0.1/posts/?q=organization_id:' + popit_id)
    org_json = json.loads(org_req.content)
    org_total = org_json['total']
    if org_total == total:
        msg = str(org_total) + '/' + str(total)
        status = 'OK!'
    else:
        msg = str(org_total) + '/' + str(total)
        status = 'Fail!'

    return (status,msg)

def current_post_limit(url='http://sinar-malaysia.popit.mysociety.org',
                       popit_id='53633b5a19ee29270d8a9ecf',
                       ):

    posts_req = requests.get(url + '/api/v0.1/organizations/' + popit_id)
    posts = json.loads(posts_req.content)['result']['memberships']
    
