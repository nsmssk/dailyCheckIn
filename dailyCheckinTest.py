import re
import requests
from datetime import datetime
import schedule
import random
import json
import os
from discordwebhook import Discord
def checkin(game_name,ltoken_v2,ltuid_v2):
    url_zzz="https://sg-act-nap-api.hoyolab.com/event/luna/os/sign"
    url_gi="https://sg-hk4e-api.hoyolab.com/event/sol/sign"
    url_hsr="https://sg-public-api.hoyolab.com/event/luna/os/sign"
    url_hi3="https://sg-public-api.hoyolab.com/event/mani/sign"
    url_userInfo="https://api-account-os.hoyoverse.com/binding/api/getUserGameRolesByLtoken"
    headers={'Content-type':'application/json'}
    cookies={'ltoken_v2':str(ltoken_v2),'ltuid_v2':str(ltuid_v2)}
    #game_name='zzz'
    if game_name=='hi3':
        url_checkin=url_hi3
        gameBiz='bh3_global'
    elif game_name=='gi':
        url_checkin=url_gi
        gameBiz='hk4e_global'
    elif game_name=='hsr':
        url_checkin=url_hsr
        gameBiz='hkrpg_global'
    elif game_name=='zzz':
        url_checkin=url_zzz
        gameBiz='nap_global'
    r=requests.post(url_checkin,cookies=cookies,headers=headers,json={"act_id":"e202406031448091"} )
    data=r.json()
    print(data)
    response_message=data.get('message')
    retcode=data.get('retcode')

    r2=requests.get(url_userInfo,cookies=cookies,headers=headers)
    responsedata=r2.json()
    responsedata2=responsedata['data']
    listAccountName=responsedata2['list']
    level=0
    accountName='accountNameHolder'
#from gameBiz get level => accountname
    for i in range(len(listAccountName)):
        if str(listAccountName[i].get('game_biz'))==gameBiz and int(listAccountName[i].get('level'))>level:
            accountName=listAccountName[i].get('nickname')

    discord = Discord(url="https://discord.com/api/webhooks/1260432062570168413/dll1sbVkfT_aC5Hp59avYjoSKuLc0xEc3jASrLXvQKDDiUK2oBxkat7euChekdTUEMFK")
    discord.post(
        embeds=[{
            "author":{"name":"authorname","url":"https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"},
            "title":"Daily check in task ["+accountName+"]",
            "description":str(response_message),
            "fields":[
                {"name":"Game","value":"ZZZ"},
                ],
            #"timestamp":datetime.now().strftime("%H:%M:%S"),
            }],
        )
ltoken_v2=os.environ['USER_1_TOKEN']
luid_v2=os.environ['USER_1_ID']
checkin('zzz',ltoken_v2,luid_v2)    
