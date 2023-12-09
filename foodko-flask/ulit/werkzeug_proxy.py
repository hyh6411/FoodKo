from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Response


class DDoSProtection(ProxyFix):
    def __init__(self, app, whitelist=None, num_requests=100):
        super().__init__(app)
        self.whitelist = whitelist or []
        self.num_requests = num_requests
        self.counters = {}

    def __call__(self, environ, start_response):
        remote_addr = environ.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip() or environ.get('REMOTE_ADDR')
        if remote_addr in self.whitelist:
            return self.app(environ, start_response)

        if remote_addr not in self.counters:
            self.counters[remote_addr] = 1
        else:
            self.counters[remote_addr] += 1

        if self.counters[remote_addr] > self.num_requests:
            # 封禁 IP
            return Response('逼崽子搞我服务器，别让我顺着网线打你.', status=403)(environ, start_response)

        return self.app(environ, start_response)
