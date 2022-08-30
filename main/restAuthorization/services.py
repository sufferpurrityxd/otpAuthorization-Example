from config.settings import sms_ru_apikey
import random
import requests


def send_otp_code(phonenumber=None):
    code = str(random.randint(99999, 999999))
    api = f'https://sms.ru/sms/send?api_id={sms_ru_apikey}&to={phonenumber}&msg={code}&json=1'
    with requests.get(api) as _request:
        resp = _request.json()
        if resp["status"] == "OK" and resp["sms"][phonenumber]["status"] == "OK":
            return code
