from django.http.response import HttpResponse
import hashlib
import random
from wechatpy import *
from django.views.decorators.csrf import csrf_exempt
import json
from wechat import auto_reply


# Create your views here.
def check_signature(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'namespacexp'

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        print('hashstr befor sha1', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1', hashstr)
        if hashstr ==signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('error')
    elif request.method == 'POST':
        msg = parse_message(request.body)
        if msg.type == "event":

            reply_word = auto_reply.reply_data["subscribe"]["content"]
            reply = create_reply(reply_word, message=msg)
            response = HttpResponse(reply.render(), content_type="application/xml")
            return response
        if msg.type == "text":
            reply_word = "我不知道该回复什么因为我只是一个小公众号"
            for i in auto_reply.reply_data["keyword"]:
                if i["type"] == "partial":
                    if msg.content.find(i["word"]) != -1:
                        rand = random.random()
                        total = 0
                        for j in i["content"]:
                            total = total + j["probability"]
                            if rand <= total:
                                reply_word = j["text"]
                                break
                    else:
                        pass
                else:
                    if i["word"] == msg.content:
                        rand = random.random()
                        total = 0
                        for j in i["content"]:
                            total = total + j["probability"]
                            if rand <= total:
                                reply_word = j["text"]
                                break
                    else:
                        pass
            reply = create_reply(reply_word, message=msg)
            response = HttpResponse(reply.render(), content_type="application/xml")
            return response
        elif msg.type == "image":
            reply = create_reply('我不知道该怎么回复你因为我只是一个自动回复的公众号', message=msg)
            response = HttpResponse(reply.render(), content_type="application/xml")
            return response
        else:
            reply = create_reply('我不知道该回复什么因为我只是一个小公众号', message=msg)
            response = HttpResponse(reply.render(), content_type="application/xml")
            return response
    else:
        pass



