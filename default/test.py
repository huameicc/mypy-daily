from aiohttp import web

resp = web.BaseRequest(None,None, None, None,None, None)
print(resp.items())