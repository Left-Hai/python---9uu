# @Time : 2020/4/2 18:32 

# @Author : xx

# @File : 9uu分类.py 

# @Software: PyCharm

from Crypto.Cipher import AES

import pprint

import hashlib

import requests

import base64

import random

import json

import time

timestamp = str(time.time() * 1000)[0:13]

key = 'AG+BwcnekYZy$9f7X#b2zdB93brfFMmz'

ramde = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

c = random.sample(ramde, 6)

v_I = ''.join(c)

# 密钥（key）, 密斯偏移量（iv） CBC模式加密

def AES_Encrypt(key, data, vi):

    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    data = pad(data)

    # 字符串补位

    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))

    encryptedbytes = cipher.encrypt(data.encode('utf8'))

    # 加密后得到的是bytes类型的数据

    encodestrs = base64.b64encode(encryptedbytes)

    #

    enctext = encodestrs.decode('utf8')

    # 对byte字符串按utf-8进行解码

    return enctext

def AES_Decrypt(key, data, ivs):

    data = data.encode('utf8')

    encodebytes = base64.decodebytes(data)

    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, ivs.encode('utf8'))

    text_decrypted = cipher.decrypt(encodebytes)

    unpad = lambda s: s[0:-s[-1]]

    text_decrypted = unpad(text_decrypted)

    # 去补位

    text_decrypted = text_decrypted.decode('utf8')

    return text_decrypted

def md5(sig):

    word = sig.encode()

    result = hashlib.md5(word)

    return result.hexdigest()

def with_open():

    a = open('分类.json','r')

    b = a.read()

    c = json.loads(b)['data']

    for v in c:

        tag = v['key']

        name = v['name']['zh-cn']

        file_type = '''

<style>

.chain{

text-align:center;

display: inline-block;

padding: 15px 0;

text-decoration: none;

overflow: hidden;

text-overflow: ellipsis;

white-space: nowrap;

background-color: #888;

border-radius: 15px;

font-size: 15px;

color: #eee;

}

.txt{

text-align:center;

margin: 0px 0% 0 0%;

<!--居中-->}

.chain{

width: 20%;

margin: 15px 2% 0 2%;

<!--控件大小-->} 

.boss div{

width:49%;

border:solid 3px gray;

float:left;}

.boss div img{

display:block;

width:100%;

height:40%;}

</style>

<body>

<div class="boss">'''

        with open(name + '.html', 'w+')as fl:

            fl.write('<title>%s</title>'%name + file_type + '\n')

        get_html(tag,name)

def get_html(tag,name):

    try:

        url = 'https://alipaydatabase.com/video/lists'

        sign = md5("devicetype=pc&page={}&tag={}&timestamp={}&6Bf2_kh*P?4tuB*C#@WEVf752x8beCE@uB-Z".format("1", tag , timestamp))

        data = '{"tag":"%s","timestamp":%s,"devicetype":"pc","page":%s,"encode_sign":"%s"}' % (tag,timestamp, "1", sign)

        data_enctext = AES_Encrypt(key, str(data), 'f%Z4F+qtFh' + v_I)

        response_page = requests.post(url, data={"post-data": data_enctext}, headers={'suffix': v_I}).json()

        deced_i_v = 'f%Z4F+qtFh' + str(response_page['suffix'])

        decrypt_page = AES_Decrypt(key, str(response_page["data"]), deced_i_v)  # 解密

        json_page = (json.loads(decrypt_page))['last_page']

        pga = int(json_page) + 1

        for i in range(1,pga):

            pga -= 1

            responses = requests.post(url, data={"post-data": data_enctext}, headers={'suffix': v_I}).json()

            data = responses['data']

            decrypted_i_v = 'f%Z4F+qtFh' + str(responses['suffix'])

            text_decrypted = AES_Decrypt(key, data, decrypted_i_v)  # 解密

            json_Text = (json.loads(text_decrypted))['data']

            print("\033[31m=\033[0m" * 25, '\033[0;36m正在爬{}第{}页,剩余{}页\033[0m'.format(name,i,pga), "\033[31m=\033[0m" * 25)

            if json_Text != []:

                for json_text in json_Text:

                    i_d = json_text['id']

                    preview = json_text['thumb_raw']  # 动态图preview

                    nickname = json_text['title']

                    json_parser(i_d ,preview , nickname ,name)

            else:

                print('到底了',name, responses)

    except Exception as l:

        print(l)

def json_parser(i_d, img, name,file_name):

    try:

        '''

        sig = channel=shipin&devicetype=pc&timestamp={}&vid={}&6Bf2_kh*P?4tuB*C#@WEVf752x8beCE@uB-Z

        data = {"vid": "%s", "channel": "shipin", "timestamp": %s, "devicetype": "pc", "encode_sign": "%s"}

        sig = devicetype=pc&timestamp={}&vid={}&6Bf2_kh*P?4tuB*C#@WEVf752x8beCE@uB-Z

        data = {"vid":"%s","timestamp":%s,"devicetype":"pc","encode_sign":"%s"}

        '''

        url = 'https://alipaydatabase.com/video/getVideoUrl'

        sign = md5("devicetype=pc&timestamp={}&vid={}&6Bf2_kh*P?4tuB*C#@WEVf752x8beCE@uB-Z".format(timestamp, i_d))

        data = '{"vid":"%s","timestamp":%s,"devicetype":"pc","encode_sign":"%s"}' % (i_d, timestamp, sign)

        data_enctext = AES_Encrypt(key, str(data), 'f%Z4F+qtFh' + v_I)

        response = requests.post(url, data={"post-data": data_enctext}, headers={'suffix': v_I}).json()

        decrypted_i_v = 'f%Z4F+qtFh' + str(response['suffix'])

        href = json.loads(AES_Decrypt(key, str(response['data']), decrypted_i_v))['data']['video_url']  # 解密

        analysis_tsa = url.split('/')

        analysis_tsb = analysis_tsa[0:3]

        analysis_tsc = '/'.join(analysis_tsb)

        api = '<a class="chain" href = "{}"target="_blank">接口2</a>'.format(href.replace(analysis_tsc, 'https://9uu66.com'))

        api_1 = '<a class="chain" href = "{}"target="_blank">接口3</a>'.format(href.replace(analysis_tsc, 'https://daqqzz.com'))

        api_2 = '<a class="chain" href = "{}"target="_blank">接口4</a></div></h2>'.format(href.replace(analysis_tsc, 'https://moshequan.com'))

        aggregate = '<h2><div><p class="txt">{}</p><img src="{}"><a class="chain" href = "{}"target="_blank">接口1</a>'.format(name, img, href) + api + api_1 + api_2

    

        deep(file_name,aggregate)

        

    except Exception as g:

        pass

def deep(file_name,aggregate):

    f = open(file_name + '.html', 'a')#as f:

    f.write(aggregate + '\n')

        

    print("\033[31m*\033[0m"*80)

    print(aggregate)

with_open()
