import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackTemplateAction, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, VideoSendMessage 

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_highlight(reply_token):
    message = VideoSendMessage(
        original_content_url='https://www.youtube.com/embed/l0sSxqSUXJY',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/p720x720/78642628_2854360461262817_5363181969536450560_o.jpg?_nc_cat=100&_nc_ohc=kgNOhq7ewyAAQn419aRrnxRITRFTRSHhSZz0yNB5DxAKPqd_0RP_uI_CQ&_nc_ht=scontent.fkhh1-1.fna&oh=bfc80f3e242fb2a8f91d75f4c314dc1f&oe=5E8A7C5F'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/sugwLW4.jpg',
                    action=PostbackTemplateAction(
                        label='西區',
                        text='west',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/f3d2DJb.jpg',
                    action=PostbackTemplateAction(
                        label='東區',
                        text='east',
                        data='action=buy&itemid=2'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_west_team(reply_token):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/sugwLW4.jpg',
            title='西區',
            text='請選擇一組',
            actions=[
                MessageTemplateAction(
                    label='西北組(金塊、爵士、灰狼、雷霆、拓荒者)',
                    text='northwest divition'
                ),
                MessageTemplateAction(
                    label='太平洋組(湖人、快艇、太陽、國王、勇士)',
                    text='pacific divition'
                ),
                MessageTemplateAction(
                    label='西南組(小牛、火箭、馬刺、灰熊、鵜鶘)',
                    text='southwest divition'
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_northwest_divition_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
               ImageCarouselColumn(
                    image_url='https://i.imgur.com/Za8Kg4H.png',
                    action=PostbackTemplateAction(
                        label='爵士',
                        text='jazz',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/2lUGdbv.png',
                    action=PostbackTemplateAction(
                        label='金塊',
                        text='nuggets',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/2ie9dVz.png',
                    action=PostbackTemplateAction(
                        label='雷霆',
                        text='thunders',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/ZZrjJed.png',
                    action=PostbackTemplateAction(
                        label='灰狼',
                        text='timberwolves',
                        data='action=buy&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/2rokfHw.png',
                    action=PostbackTemplateAction(
                        label='拓荒者',
                        text='trail blazers',
                        data='action=buy&itemid=5'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_jazz(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79241279_2852476418117888_3201914190935621632_n.jpg?_nc_cat=104&_nc_ohc=azTDc86ZDHMAQmz02QSGpb1Gdha0cT6TNF0T0z6c7FXFvAnVeorP6L_Yg&_nc_ht=scontent.fkhh1-2.fna&oh=91391dc3e1235625530062e1bc71f5c4&oe=5E7CF90D',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79241279_2852476418117888_3201914190935621632_n.jpg?_nc_cat=104&_nc_ohc=azTDc86ZDHMAQmz02QSGpb1Gdha0cT6TNF0T0z6c7FXFvAnVeorP6L_Yg&_nc_ht=scontent.fkhh1-2.fna&oh=91391dc3e1235625530062e1bc71f5c4&oe=5E7CF90D'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_nuggets(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79222466_2854171671281696_5975948711753154560_n.jpg?_nc_cat=111&_nc_ohc=a_LXSuxhkgcAQnjNZVHSz42ex_CqvqX5XCHr9xrl5Qsz1XCDbpNJqtRtw&_nc_ht=scontent.fkhh1-2.fna&oh=ad3caa93912920e1397b16a11b99168d&oe=5E3F4E45',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79222466_2854171671281696_5975948711753154560_n.jpg?_nc_cat=111&_nc_ohc=a_LXSuxhkgcAQnjNZVHSz42ex_CqvqX5XCHr9xrl5Qsz1XCDbpNJqtRtw&_nc_ht=scontent.fkhh1-2.fna&oh=ad3caa93912920e1397b16a11b99168d&oe=5E3F4E45'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    
def send_thunders(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78507393_2854172781281585_191698989014319104_n.jpg?_nc_cat=100&_nc_ohc=a0Ty1UNdKl4AQlGyWGlZdkZUWY2JIpHuQTQZTYDKad3z8WmLEJ0hIv0Kw&_nc_ht=scontent.fkhh1-1.fna&oh=ab1c3053961eaa4635587b8ebc0e21c8&oe=5E893E48',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78507393_2854172781281585_191698989014319104_n.jpg?_nc_cat=100&_nc_ohc=a0Ty1UNdKl4AQlGyWGlZdkZUWY2JIpHuQTQZTYDKad3z8WmLEJ0hIv0Kw&_nc_ht=scontent.fkhh1-1.fna&oh=ab1c3053961eaa4635587b8ebc0e21c8&oe=5E893E48'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_timberwolves(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78674037_2854174244614772_873020517446057984_n.jpg?_nc_cat=107&_nc_ohc=YmxNxH1kOn4AQmiekt_opJcBC4yHDx7x0iOi63vWYgGGOr5oOi0Hz4A8w&_nc_ht=scontent.fkhh1-2.fna&oh=f951500413a725fc5d1edde2558dc961&oe=5E405CC5',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78674037_2854174244614772_873020517446057984_n.jpg?_nc_cat=107&_nc_ohc=YmxNxH1kOn4AQmiekt_opJcBC4yHDx7x0iOi63vWYgGGOr5oOi0Hz4A8w&_nc_ht=scontent.fkhh1-2.fna&oh=f951500413a725fc5d1edde2558dc961&oe=5E405CC5'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_trail_blazers(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78248143_2854175341281329_8704820122444890112_n.jpg?_nc_cat=101&_nc_ohc=Jqel_GcZMW8AQn3158ehAGE7cEqb1R8BIhE6hHRDk8FC-BRR4cX8upvyA&_nc_ht=scontent.fkhh1-1.fna&oh=eb2b4099f1521a436fc283581785f33e&oe=5E89A698',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78248143_2854175341281329_8704820122444890112_n.jpg?_nc_cat=101&_nc_ohc=Jqel_GcZMW8AQn3158ehAGE7cEqb1R8BIhE6hHRDk8FC-BRR4cX8upvyA&_nc_ht=scontent.fkhh1-1.fna&oh=eb2b4099f1521a436fc283581785f33e&oe=5E89A698'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)           

def send_pacific_divition_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
               ImageCarouselColumn(
                    image_url='https://i.imgur.com/NjIZPvy.png',
                    action=PostbackTemplateAction(
                        label='快艇',
                        text='clippers',
                        data='action=buy&itemid=1'
                    )
                ),                
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/hLTYqcQ.png',
                    action=PostbackTemplateAction(
                        label='國王',
                        text='kings',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/2zTrz4Z.png',
                    action=PostbackTemplateAction(
                        label='湖人',
                        text='lakers',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/6FdkdEf.png',
                    action=PostbackTemplateAction(
                        label='太陽',
                        text='suns',
                        data='action=buy&itemid=4'
                    )
                ),                
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/YRwCVJl.png',
                    action=PostbackTemplateAction(
                        label='勇士',
                        text='warriors',
                        data='action=buy&itemid=5'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_clippers(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78598811_2854190081279855_4219443225267535872_n.jpg?_nc_cat=100&_nc_ohc=2GYW4XWV-bcAQkPvrPEJTJbQ4EfzeNxaUYmcsICtNCkxddQhRofemauRg&_nc_ht=scontent.fkhh1-1.fna&oh=d31f1b200bbc2fe155027b6775d02a8a&oe=5E880E19',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78598811_2854190081279855_4219443225267535872_n.jpg?_nc_cat=100&_nc_ohc=2GYW4XWV-bcAQkPvrPEJTJbQ4EfzeNxaUYmcsICtNCkxddQhRofemauRg&_nc_ht=scontent.fkhh1-1.fna&oh=d31f1b200bbc2fe155027b6775d02a8a&oe=5E880E19'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_kings(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79147824_2854191094613087_1261112697160728576_n.jpg?_nc_cat=108&_nc_ohc=mXY65FMq2jcAQl6C-H-4jluRFu9XPXPZBYnZ4u_XCPj1cTJ1KWKEacVMw&_nc_ht=scontent.fkhh1-2.fna&oh=788f203fc894fb5aaa458934d3abaab5&oe=5E8396E9',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79147824_2854191094613087_1261112697160728576_n.jpg?_nc_cat=108&_nc_ohc=mXY65FMq2jcAQl6C-H-4jluRFu9XPXPZBYnZ4u_XCPj1cTJ1KWKEacVMw&_nc_ht=scontent.fkhh1-2.fna&oh=788f203fc894fb5aaa458934d3abaab5&oe=5E8396E9'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    
def send_lakers(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78627810_2854192217946308_5289299933520723968_n.jpg?_nc_cat=100&_nc_ohc=QlbYzcOtavUAQnt-kasnatl8iKjrKF_Vdx80Ppsf8rQ0d3Cgu021jxYNw&_nc_ht=scontent.fkhh1-1.fna&oh=7a02b5aaded3816169428242997aa104&oe=5E85A63D',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78627810_2854192217946308_5289299933520723968_n.jpg?_nc_cat=100&_nc_ohc=QlbYzcOtavUAQnt-kasnatl8iKjrKF_Vdx80Ppsf8rQ0d3Cgu021jxYNw&_nc_ht=scontent.fkhh1-1.fna&oh=7a02b5aaded3816169428242997aa104&oe=5E85A63D'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_suns(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78846140_2854193884612808_4568018029367001088_n.jpg?_nc_cat=105&_nc_ohc=oNO1kSV872QAQkm6BjMumg66hA8nfSDbgc3LDBk9CVz1vVrKAlnh5wePg&_nc_ht=scontent.fkhh1-1.fna&oh=a385bb5afcd81c2ba9b108b4a27829f4&oe=5E7DBB22',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78846140_2854193884612808_4568018029367001088_n.jpg?_nc_cat=105&_nc_ohc=oNO1kSV872QAQkm6BjMumg66hA8nfSDbgc3LDBk9CVz1vVrKAlnh5wePg&_nc_ht=scontent.fkhh1-1.fna&oh=a385bb5afcd81c2ba9b108b4a27829f4&oe=5E7DBB22'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_warriors(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/s960x960/78639443_2854194867946043_4159670375862501376_o.jpg?_nc_cat=102&_nc_ohc=fPVsLVDQ_xYAQll-NYJxnDS2LqaDjxjh96AHdCdmyBtWF0MxrxwXdt8HA&_nc_ht=scontent.fkhh1-1.fna&oh=fef666693d593e12bcd447a5dbd8c95c&oe=5E76DBF6',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/s960x960/78639443_2854194867946043_4159670375862501376_o.jpg?_nc_cat=102&_nc_ohc=fPVsLVDQ_xYAQll-NYJxnDS2LqaDjxjh96AHdCdmyBtWF0MxrxwXdt8HA&_nc_ht=scontent.fkhh1-1.fna&oh=fef666693d593e12bcd447a5dbd8c95c&oe=5E76DBF6'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_southwest_divition_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/KfhWlHX.png',
                    action=PostbackTemplateAction(
                        label='獨行俠',
                        text='mavericks',
                        data='action=buy&itemid=1'
                    )
                ),                
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/MwZ7gOG.png',
                    action=PostbackTemplateAction(
                        label='灰熊',
                        text='grizzles',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/rSfD5It.png',
                    action=PostbackTemplateAction(
                        label='鵜鶘',
                        text='pelicans',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/VakO1Td.png',
                    action=PostbackTemplateAction(
                        label='火箭',
                        text='rockets',
                        data='action=buy&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/76CbfhM.png',
                    action=PostbackTemplateAction(
                        label='馬刺',
                        text='spurs',
                        data='action=buy&itemid=5'
                    )
                )                
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"    

def send_mavericks(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/79158998_2854206964611500_8025932066648489984_n.jpg?_nc_cat=100&_nc_ohc=dF7VJLHL5A8AQnuJ4CCvaJHLZNF4K0sPOjiQSdZdwBHqC9wUOvb7VFd3Q&_nc_ht=scontent.fkhh1-1.fna&oh=46506ed7ce5b4474173f71faea00fc7d&oe=5E7E04D8',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/79158998_2854206964611500_8025932066648489984_n.jpg?_nc_cat=100&_nc_ohc=dF7VJLHL5A8AQnuJ4CCvaJHLZNF4K0sPOjiQSdZdwBHqC9wUOvb7VFd3Q&_nc_ht=scontent.fkhh1-1.fna&oh=46506ed7ce5b4474173f71faea00fc7d&oe=5E7E04D8'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_grizzles(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/78492877_2854207961278067_4570258391682777088_n.jpg?_nc_cat=103&_nc_ohc=hiEEjRbymnQAQm94XtW9z1u43IN0OTJRexjYvyEmAkDYQ3W2gh8yRKGeA&_nc_ht=scontent-tpe1-1.xx&oh=df5a438fad9f0cd0c7014f7e9a80de3c&oe=5E8C1CD3',
        preview_image_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/78492877_2854207961278067_4570258391682777088_n.jpg?_nc_cat=103&_nc_ohc=hiEEjRbymnQAQm94XtW9z1u43IN0OTJRexjYvyEmAkDYQ3W2gh8yRKGeA&_nc_ht=scontent-tpe1-1.xx&oh=df5a438fad9f0cd0c7014f7e9a80de3c&oe=5E8C1CD3'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    
def send_pelicans(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/76710870_2854209761277887_4514777872463822848_n.jpg?_nc_cat=102&_nc_ohc=U_G-IuHMEFsAQmFAbRwPuYY4mOnaJ0CxesXMjs_F3_h6YmDyhQxDJrBaw&_nc_ht=scontent.fkhh1-1.fna&oh=85964d333d15c062b51ad59320b8a5b5&oe=5E717772',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/76710870_2854209761277887_4514777872463822848_n.jpg?_nc_cat=102&_nc_ohc=U_G-IuHMEFsAQmFAbRwPuYY4mOnaJ0CxesXMjs_F3_h6YmDyhQxDJrBaw&_nc_ht=scontent.fkhh1-1.fna&oh=85964d333d15c062b51ad59320b8a5b5&oe=5E717772'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_rockets(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/s960x960/79293456_2854210514611145_3651039071402196992_o.jpg?_nc_cat=108&_nc_ohc=1FE42XJB1RgAQlwqZN8yee-DL8_vs3LHOnZQ3eW-fVqK5JIhTpVa8_sHQ&_nc_ht=scontent.fkhh1-2.fna&oh=a807753a38afd2b6908e82b92c942640&oe=5E4015B8',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/s960x960/79293456_2854210514611145_3651039071402196992_o.jpg?_nc_cat=108&_nc_ohc=1FE42XJB1RgAQlwqZN8yee-DL8_vs3LHOnZQ3eW-fVqK5JIhTpVa8_sHQ&_nc_ht=scontent.fkhh1-2.fna&oh=a807753a38afd2b6908e82b92c942640&oe=5E4015B8'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_spurs(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78383820_2854211487944381_5884107639356391424_n.jpg?_nc_cat=103&_nc_ohc=MJtlPegDsaQAQmItb38Pc0BeMTzMRqMFhqeKhsHyUNaIADhAxsQely8aQ&_nc_ht=scontent.fkhh1-1.fna&oh=b8f477a7dab5ff1097b31383cfa1cc25&oe=5E6BFA1C',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78383820_2854211487944381_5884107639356391424_n.jpg?_nc_cat=103&_nc_ohc=MJtlPegDsaQAQmItb38Pc0BeMTzMRqMFhqeKhsHyUNaIADhAxsQely8aQ&_nc_ht=scontent.fkhh1-1.fna&oh=b8f477a7dab5ff1097b31383cfa1cc25&oe=5E6BFA1C'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_east_team(reply_token):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/f3d2DJb.jpg',
            title='東區',
            text='請選擇一組',
            actions=[
                MessageTemplateAction(
                    label='大西洋組(暴龍、賽爾提克、76人、)',
                    text='atalantic divition'
                ),
                MessageTemplateAction(
                    label='中部組(公鹿、溜馬、活塞、公牛、騎士)',
                    text='central divition'
                ),
                MessageTemplateAction(
                    label='東南組(熱火、魔術、黃蜂、巫師、老鷹)',
                    text='southeast divition'
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_atalantic_divition_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
               ImageCarouselColumn(
                    image_url='https://i.imgur.com/hQV1mql.png',
                    action=PostbackTemplateAction(
                        label='暴龍',
                        text='raptors',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/MNlnQcA.png',
                    action=PostbackTemplateAction(
                        label='賽爾提克',
                        text='celtics',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/DPFhrrX.png',
                    action=PostbackTemplateAction(
                        label='76人',
                        text='76ers',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/vo4yWWw.png',
                    action=PostbackTemplateAction(
                        label='籃網',
                        text='nets',
                        data='action=buy&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/RMKhZxx.png',
                    action=PostbackTemplateAction(
                        label='尼克',
                        text='knics',
                        data='action=buy&itemid=5'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_raptors(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78628760_2854224254609771_5964230262853206016_n.jpg?_nc_cat=108&_nc_ohc=S-E4xWOSUMcAQmpuWRzUds7l09EmvnO_tNp2P5OQXsNEKNHG2qLWjWyNw&_nc_ht=scontent.fkhh1-2.fna&oh=69bba450e63331f39c3e658ae4783244&oe=5E708A86',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78628760_2854224254609771_5964230262853206016_n.jpg?_nc_cat=108&_nc_ohc=S-E4xWOSUMcAQmpuWRzUds7l09EmvnO_tNp2P5OQXsNEKNHG2qLWjWyNw&_nc_ht=scontent.fkhh1-2.fna&oh=69bba450e63331f39c3e658ae4783244&oe=5E708A86'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_celtics(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78377042_2854225147943015_6832237544147517440_n.jpg?_nc_cat=107&_nc_ohc=7RakpO0IJ1AAQlxbMQm7dCFt0F36Maph5bCY-Uddwqt-gtxixCYhExMeg&_nc_ht=scontent.fkhh1-2.fna&oh=95267fd249c3832c2144da0bd8f6c027&oe=5E76875D',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78377042_2854225147943015_6832237544147517440_n.jpg?_nc_cat=107&_nc_ohc=7RakpO0IJ1AAQlxbMQm7dCFt0F36Maph5bCY-Uddwqt-gtxixCYhExMeg&_nc_ht=scontent.fkhh1-2.fna&oh=95267fd249c3832c2144da0bd8f6c027&oe=5E76875D'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    
def send_76ers(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/76646879_2854226264609570_788926672698081280_n.jpg?_nc_cat=100&_nc_ohc=aoHovmYnoUEAQnYx6bHbOHdTt5BojiOhEY8IKZKa8ovFeKK8BZ3a94tCw&_nc_ht=scontent.fkhh1-1.fna&oh=b1ed97319d45930cc34b3fc1cd5fe30e&oe=5E78CFF8',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/76646879_2854226264609570_788926672698081280_n.jpg?_nc_cat=100&_nc_ohc=aoHovmYnoUEAQnYx6bHbOHdTt5BojiOhEY8IKZKa8ovFeKK8BZ3a94tCw&_nc_ht=scontent.fkhh1-1.fna&oh=b1ed97319d45930cc34b3fc1cd5fe30e&oe=5E78CFF8'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_nets(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78321645_2854227064609490_4518626669967179776_n.jpg?_nc_cat=101&_nc_ohc=UJ-jW1JUdo0AQkMAd5wMxbRh8hmRjenZyxG6IB8QkZ2IHxUT8q1utXK6w&_nc_ht=scontent.fkhh1-1.fna&oh=4722e83cae478b286424a0de0274dd53&oe=5E81B18A',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78321645_2854227064609490_4518626669967179776_n.jpg?_nc_cat=101&_nc_ohc=UJ-jW1JUdo0AQkMAd5wMxbRh8hmRjenZyxG6IB8QkZ2IHxUT8q1utXK6w&_nc_ht=scontent.fkhh1-1.fna&oh=4722e83cae478b286424a0de0274dd53&oe=5E81B18A'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_knics(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/s960x960/78831819_2854228211276042_8423881071753428992_o.jpg?_nc_cat=101&_nc_ohc=udMp5dXUgokAQlzoAGvCGwLn_VwHoHHkG8g8QSBhx9ubVLaD-okmzSpuQ&_nc_ht=scontent-tpe1-1.xx&oh=41c3f6f7cd75da329766eb1ea65baf9c&oe=5E7A02DC',
        preview_image_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/s960x960/78831819_2854228211276042_8423881071753428992_o.jpg?_nc_cat=101&_nc_ohc=udMp5dXUgokAQlzoAGvCGwLn_VwHoHHkG8g8QSBhx9ubVLaD-okmzSpuQ&_nc_ht=scontent-tpe1-1.xx&oh=41c3f6f7cd75da329766eb1ea65baf9c&oe=5E7A02DC'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_central_divition_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
               ImageCarouselColumn(
                    image_url='https://i.imgur.com/Vq9uSfw.png',
                    action=PostbackTemplateAction(
                        label='公鹿',
                        text='bucks',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/49Py8da.png',
                    action=PostbackTemplateAction(
                        label='溜馬',
                        text='pacers',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/ccm79f8.png',
                    action=PostbackTemplateAction(
                        label='活塞',
                        text='pistons',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/jgM2e8T.png',
                    action=PostbackTemplateAction(
                        label='公牛',
                        text='bulls',
                        data='action=buy&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/9j4vObi.png',
                    action=PostbackTemplateAction(
                        label='騎士',
                        text='caveliers',
                        data='action=buy&itemid=5'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_bucks(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78900032_2854235861275277_4444509750779969536_n.jpg?_nc_cat=101&_nc_ohc=JwFu7UnX1bAAQke4z21MU02rpfI72ncSQx00gNhmgYZ9Pesuftiz8fEHA&_nc_ht=scontent.fkhh1-1.fna&oh=21255b92a56e66ae17a0d320930210ed&oe=5E416B0D',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78900032_2854235861275277_4444509750779969536_n.jpg?_nc_cat=101&_nc_ohc=JwFu7UnX1bAAQke4z21MU02rpfI72ncSQx00gNhmgYZ9Pesuftiz8fEHA&_nc_ht=scontent.fkhh1-1.fna&oh=21255b92a56e66ae17a0d320930210ed&oe=5E416B0D'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_pacers(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/74406650_2854236727941857_6693694732540837888_n.jpg?_nc_cat=101&_nc_ohc=IpPmQg5C-5gAQmXgEr_Qa5RQElkx8lU5uRXA3h3Plb973rkTn2JNWRN9w&_nc_ht=scontent.fkhh1-1.fna&oh=d9cfb8723fedeca8b7fe0a16aee8c974&oe=5E827CD6',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/74406650_2854236727941857_6693694732540837888_n.jpg?_nc_cat=101&_nc_ohc=IpPmQg5C-5gAQmXgEr_Qa5RQElkx8lU5uRXA3h3Plb973rkTn2JNWRN9w&_nc_ht=scontent.fkhh1-1.fna&oh=d9cfb8723fedeca8b7fe0a16aee8c974&oe=5E827CD6'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    
def send_pistons(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78426819_2854237474608449_1907988626533253120_n.jpg?_nc_cat=105&_nc_ohc=JyqZkQDfGr0AQl3283l-b7-3xB6E4xrG88-Y5gNtfFSww14lZNtEeR3rQ&_nc_ht=scontent.fkhh1-1.fna&oh=1efb295289744a34f8052eececa88421&oe=5E887755',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78426819_2854237474608449_1907988626533253120_n.jpg?_nc_cat=105&_nc_ohc=JyqZkQDfGr0AQl3283l-b7-3xB6E4xrG88-Y5gNtfFSww14lZNtEeR3rQ&_nc_ht=scontent.fkhh1-1.fna&oh=1efb295289744a34f8052eececa88421&oe=5E887755'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_bulls(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79409191_2854238864608310_2455477092825956352_n.jpg?_nc_cat=109&_nc_ohc=tBEM4NvpsDcAQnK26piemLYa39xGEZjeWGi50AcScceVca_fwQrJ9Thpg&_nc_ht=scontent.fkhh1-2.fna&oh=a7a3cd79461e2fb23c16e1f47586eac2&oe=5E742AD7',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79409191_2854238864608310_2455477092825956352_n.jpg?_nc_cat=109&_nc_ohc=tBEM4NvpsDcAQnK26piemLYa39xGEZjeWGi50AcScceVca_fwQrJ9Thpg&_nc_ht=scontent.fkhh1-2.fna&oh=a7a3cd79461e2fb23c16e1f47586eac2&oe=5E742AD7'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_caveliers(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78373442_2854239771274886_6584265429764538368_n.jpg?_nc_cat=107&_nc_ohc=FUu0rWxv85gAQmTRzg7-iQbI7mdUUGFkwQsI6jO8zSKDq13oAZH7ki4Sw&_nc_ht=scontent.fkhh1-2.fna&oh=64dd8fd206496e3cd1aebac240654b1f&oe=5E789A19',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78373442_2854239771274886_6584265429764538368_n.jpg?_nc_cat=107&_nc_ohc=FUu0rWxv85gAQmTRzg7-iQbI7mdUUGFkwQsI6jO8zSKDq13oAZH7ki4Sw&_nc_ht=scontent.fkhh1-2.fna&oh=64dd8fd206496e3cd1aebac240654b1f&oe=5E789A19'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_southeast_divition_team(reply_token):
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
               ImageCarouselColumn(
                    image_url='https://i.imgur.com/JlSkgo1.png',
                    action=PostbackTemplateAction(
                        label='熱火',
                        text='heats',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/ofJ4VgI.png',
                    action=PostbackTemplateAction(
                        label='魔術',
                        text='magic',
                        data='action=buy&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/qerCfYv.png',
                    action=PostbackTemplateAction(
                        label='黃蜂',
                        text='hornets',
                        data='action=buy&itemid=3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/BE37OBk.png',
                    action=PostbackTemplateAction(
                        label='巫師',
                        text='wizards',
                        data='action=buy&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/QxmRbDF.png',
                    action=PostbackTemplateAction(
                        label='老鷹',
                        text='hawks',
                        data='action=buy&itemid=5'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_heats(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79134841_2854250167940513_5434643117171015680_n.jpg?_nc_cat=104&_nc_ohc=7QuQ4mkvIJcAQk7LkVajM0SOiCSP-A0rV1bd7leEmkLYfBhYQyzYMEH-w&_nc_ht=scontent.fkhh1-2.fna&oh=dbff531d800ae85b3a1a7134ea350929&oe=5E6BEA51',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/79134841_2854250167940513_5434643117171015680_n.jpg?_nc_cat=104&_nc_ohc=7QuQ4mkvIJcAQk7LkVajM0SOiCSP-A0rV1bd7leEmkLYfBhYQyzYMEH-w&_nc_ht=scontent.fkhh1-2.fna&oh=dbff531d800ae85b3a1a7134ea350929&oe=5E6BEA51'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_magic(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78483894_2854250764607120_7100869872858431488_n.jpg?_nc_cat=103&_nc_ohc=6AGauk-wDhoAQkys7x7-OLGfOXHsQIkN6mCmTidENk52SVbL8rVEiYe2A&_nc_ht=scontent.fkhh1-1.fna&oh=0124ea20d18f0bd4b4a53f7f931b633e&oe=5E7BFD33',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78483894_2854250764607120_7100869872858431488_n.jpg?_nc_cat=103&_nc_ohc=6AGauk-wDhoAQkys7x7-OLGfOXHsQIkN6mCmTidENk52SVbL8rVEiYe2A&_nc_ht=scontent.fkhh1-1.fna&oh=0124ea20d18f0bd4b4a53f7f931b633e&oe=5E7BFD33'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    
def send_hornets(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78594147_2854251781273685_232763493453922304_n.jpg?_nc_cat=109&_nc_ohc=CI_9ld0KEdEAQm3zRUMpAmAQmqSep4yPlRcqRvadbLVsIiQIBetkchEMg&_nc_ht=scontent.fkhh1-2.fna&oh=ff73617332524870f423bf38dc53fa98&oe=5E6F5938',
        preview_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/78594147_2854251781273685_232763493453922304_n.jpg?_nc_cat=109&_nc_ohc=CI_9ld0KEdEAQm3zRUMpAmAQmqSep4yPlRcqRvadbLVsIiQIBetkchEMg&_nc_ht=scontent.fkhh1-2.fna&oh=ff73617332524870f423bf38dc53fa98&oe=5E6F5938'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_wizards(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78470828_2854252431273620_5148310008462573568_n.jpg?_nc_cat=103&_nc_ohc=NY8v4Bn4b2QAQkJ_X2MARzwp24MydVnaW6B10UOZByXiwCKDmTYdWP8pQ&_nc_ht=scontent.fkhh1-1.fna&oh=b4c2960fb863e92d0c89452542502ac4&oe=5E7D0F27',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78470828_2854252431273620_5148310008462573568_n.jpg?_nc_cat=103&_nc_ohc=NY8v4Bn4b2QAQkJ_X2MARzwp24MydVnaW6B10UOZByXiwCKDmTYdWP8pQ&_nc_ht=scontent.fkhh1-1.fna&oh=b4c2960fb863e92d0c89452542502ac4&oe=5E7D0F27'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

def send_hawks(reply_token):
    message = ImageSendMessage(
        original_content_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78599513_2854253307940199_8763806507503452160_n.jpg?_nc_cat=103&_nc_ohc=MZtcE43_4zYAQmMuwCUo6_fOoUwh_AoZgnDROEZyqDZ4Mn-qeNEujHT4w&_nc_ht=scontent.fkhh1-1.fna&oh=bfe2888cdace8c1e79967b0cfb341765&oe=5E6FF695',
        preview_image_url='https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/78599513_2854253307940199_8763806507503452160_n.jpg?_nc_cat=103&_nc_ohc=MZtcE43_4zYAQmMuwCUo6_fOoUwh_AoZgnDROEZyqDZ4Mn-qeNEujHT4w&_nc_ht=scontent.fkhh1-1.fna&oh=bfe2888cdace8c1e79967b0cfb341765&oe=5E6FF695'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
