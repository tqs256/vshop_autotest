import requests



class BizResponse:
    """
    业务响应对象
    """

    def __init__(self,resp:requests.Response):
        self.code = resp.status_code
        self.json = None

        try:
            self.json = resp.json()
        except ValueError:
            self.json = None

        self.code = self.json.get("code",-1) if self.json else None
        self.message = self.json.get('message','') if self.json else None
        self.data = self.json.get("data") if self.json else None

    @property
    def success(self,i:int = 0) -> bool:
        return self.code == i

    @property
    def raw(self) ->dict:
        return self.data or {}

    def __repr__(self):
        return f"BizResponse(code={self.code},message={self.message!r})"