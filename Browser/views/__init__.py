from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render

from Browser.models import UserInfo
from Browser.views import cellar, administrator

def simple_response(request, *args, **kwargs):
    template_name = kwargs["path"]
    if kwargs["type"] :
        template_name = kwargs["type"] + "/" + template_name
        
    userInfo = UserInfo.getUserInfo(request)
    context = {
        "isMetic"   : userInfo.isMetic(),
        "isYeoman"  : userInfo.isYeoman(),
        "isAdmin"   : userInfo.isAdmin(),
        "isSuper"   : userInfo.isSuper()
    }
        
    return HttpResponse(render(request, template_name, context))