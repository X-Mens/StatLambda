from app.handlers.Handler import Handler


class DefaultHandler(Handler):

    def __init__(self, event):
        pass

    def process(self):
        return 405, {"message": "Method not allowed."}
