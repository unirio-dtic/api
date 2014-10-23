# -*- coding: utf-8 -*-
from APIKey import APIKey
from APIRequest import APIRequest
from APIKeyPermissions import APIKeyPermissions


@service.json
@service.xml
def index():
    apiKey = APIKey(request.vars.API_KEY)
    if apiKey.auth_key:
        keyPermissions = APIKeyPermissions(request)
        if keyPermissions.canPerformAPICall():
            apiRequest = APIRequest(apiKey, request)
            resp = apiRequest.performRequest()
            return resp
    else:
        return dict(error="API Key Inválida ou Inativa")


def call():
    session.forget()
    return service()
