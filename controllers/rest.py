# -*- coding: utf-8 -*-
from api.key import APIKey, APIKeyPermissions
from api.request import APIRequest
try:
    import httplib as http
except ImportError:
    import http.client as http


def index():
    api_key = APIKey(db, request.vars.API_KEY)
    if api_key.auth:
        permissions = APIKeyPermissions(request)
        if permissions.can_perform_api_call():
            api_request = APIRequest(api_key, request)
            return api_request.perform_request()
    else:
        raise HTTP(http.UNAUTHORIZED, "API Key inválida ou inativa")
