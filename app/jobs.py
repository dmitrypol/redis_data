import logging
import pandas as pd
import requests
import redis
from . import APP, RQ_CLIENT


REDIS_CLIENT = redis.Redis(host=APP.config.get('REDIS_HOST'), db=0)
GH_HEADERS = {'Authorization': 'token ' + APP.config.get('GITHUB_TOKEN', '')}


#   https://stackoverflow.com/questions/17622439/how-to-use-github-api-token-in-python-for-requesting
#   https://github.com/pandas-dev/pandas/issues/10526
@RQ_CLIENT.job()
def github_users(since=0, counter=0):
    ''' get users data from github api '''
    req = requests.get(f'https://api.github.com/users?since={since}', headers=GH_HEADERS)
    df = pd.DataFrame(req.json())
    for _, v in df.iterrows():
        github_each_user.queue(v['login'])
        since = v['id']
    #  queue next job request
    if counter+1 < 10:
        github_users.queue(since=since, counter=counter+1)


@RQ_CLIENT.job()
def github_each_user(login):
    ''' get data for specific user '''
    req = requests.get(f'https://api.github.com/users/{login}', headers=GH_HEADERS)
    ds = pd.Series(req.json()).to_dict()
    keys = ['public_repos', 'public_gists', 'followers', 'following']
    ds2 = {key: ds[key] for key in keys}
    logging.info(ds2)
    REDIS_CLIENT.hmset(login, ds2)
