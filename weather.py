import urllib.request
import gzip
import json
import easygui as g

g.msgbox("------天气查询------")
def get_weather_data() :
    msg = "请输入要查询的城市名称："
    title = "天气查询器"
    city_name = g.enterbox(msg, title)
    #city_name = input('请输入要查询的城市名称：')
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #网址1只需要输入城市名，网址2需要输入城市代码
    #print(url1)
    weather_data = urllib.request.urlopen(url1).read()
    #读取网页数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def query_weather(weather_dict):
        weather_dict.get('desc') =='OK'
        forecast = weather_dict.get('data').get('forecast')
        msg = "查询天气信息如下"
        title = "查询结果"
        text = "城市："+weather_dict.get('data').get('city')+\
               "\n"+"温度："+ weather_dict.get('data').get('wendu')+'℃ '+\
               "\n"+"感冒："+ weather_dict.get('data').get('ganmao')+\
               "\n"+"风向："+ forecast[0].get('fengxiang')+\
               "\n"+"风级："+ forecast[0].get('fengli')+\
               "\n"+"高温："+ forecast[0].get('high')+\
               "\n"+"低温："+ forecast[0].get('low')+\
               "\n"+"天气："+ forecast[0].get('type')+\
               "\n"+"日期："+ forecast[0].get('date')
        g.textbox(msg,title,text)
        
        msg = "是否要显示未来四天天气，是/否："
        title = "未来天气"
        four_day_forecast = g.enterbox(msg, title)
        if four_day_forecast == '是':
            text = ''
            for i in range(1,5):
                msg = "查询天气信息如下"
                title = "查询结果"
                text += '日期：'+forecast[i].get('date')+\
                "\n"+'风向：'+forecast[i].get('fengxiang')+\
                "\n"+'风级：'+forecast[i].get('fengli')+\
                "\n"+'高温：'+forecast[i].get('high')+\
                "\n"+'低温：'+forecast[i].get('low')+\
                "\n"+'天气：'+forecast[i].get('type')+\
                "\n"+'******************************'+"\n"
            g.textbox(msg,title,text)
        elif four_day_forecast == '否':
            g.msgbox('您请求不查询未来四天天气')
        else:
            g.msgbox('您输入的信息有误')

def show_weather(weather_data):
    weather_dict = weather_data 
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        g.msgbox("你输入的城市名有误，或者天气中心未收录你所在城市")
        weather_dict = get_weather_data()
        query_weather(weather_dict)

    else:
        query_weather(weather_dict)
            

show_weather(get_weather_data())
