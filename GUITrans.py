import easygui as g
import sys
import urllib.parse
import json
import time
import urllib.request

while True:
    g.msgbox("简单的在线英汉互译Beat",'简单的在线翻译','请点击')

    if g.ccbox('继续翻译？','选择',choices=('继续','退出')): 
            pass         # user chose to continue
    else: 
        sys.exit(0)     # user chose to cancel
    trans = g.enterbox('请输入需要翻译的内容','输入')
    while trans == '':
        g.msgbox('输入不能为空!','注意','好的')
        trans = g.enterbox('请输入需要翻译的内容','输入')
    if trans == None:
        sys.exit(0)
    #if trans =='2333':
     #   break
 
    url  = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'


    head = {}

    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = trans
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'

    #data格式转换
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    urlresponse = urllib.request.urlopen(req)

    html = urlresponse.read().decode('utf-8')

    result = json.loads(html)
   # print('翻译结果： %s' % (result['translateResult'][0][0]['tgt']))

    g.textbox('翻译结果如下','结果',result['translateResult'][0][0]['tgt'])
