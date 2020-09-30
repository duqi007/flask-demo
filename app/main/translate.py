# -*- coding: utf-8 -*-
import json
import requests
from flask_babel import _
import random
from hashlib import md5
from flask import current_app

def translate(q, source_language, dest_language):
    url = current_app.config['TRANSLATE_URL'] 
    appid = current_app.config['BD_APP_ID'] 
    secretKey = current_app.config['BD_TRANSLATOR_KEY'] 
    salt = random.randint(32768, 65536)
    if 'BD_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['BD_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    sign =  appid + q + str(salt) + secretKey
    sign = md5(sign.encode()).hexdigest()
    data = {
        'appid' : appid,
        'q' : q,
        'from' : source_language,
        'to' : dest_language,
        'salt': str(salt),
        'sign' : sign,
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    res = requests.post(url = url, data=data)
    res_content = json.loads(res.content.decode('utf-8'))
    if 'error_code' in res_content.keys():
        return _('Error: the translation service failed.')
    return res_content['trans_result'][0]['dst']

    