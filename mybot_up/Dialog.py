# -*- coding:utf-8 -*-
import json
import urllib2

def dialog(text_input):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"

    req = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },

            "selfInfo":
            {
                "location":
                {
                    "city": "上海",
                    "province": "上海",
                    "street": "文汇路"
                }
            }
        },

        "userInfo": 
        {
            "apiKey": "7bd01dac044b40c3b3e40f1ae2419574",
            "userId": "18676661594"
        }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib2.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib2.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']

    return intent_code,results_text
