from typing import Optional

from requests import Request, Response

from kucoin_universal_sdk.model.transport_option import Interceptor


class LoggingInterceptor(Interceptor):

    def before(self, req: Request) -> Request:
        return req

    def after(self, req: Request, resp: Optional[Response], err: Optional[Exception]) -> Response:
        if req is not None:
            print(f'request url: {req.url}, err:{err}')
        return resp