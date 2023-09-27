class CheckMixin:
    def check(self, username, password):
        if self.password == password and self.username == username:
            self.posts += 1
            return 'Successfully created'
        return 'Wrong username or password'


class Instagram(CheckMixin):
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.posts = 0

    def post_post(self, post_name, username, password):
        return self.check(username, password)


class TikTok(CheckMixin):
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.posts = 0

    def post_video(self, post_name, username, password):
        return self.check(username, password)
    

inst = Instagram('loadeng', 'qwe123')
tk = TikTok('therock', 'zxc123')

print(inst.post_post('Pancakes recipe', 'loadeng', 'qwe123'))
print(inst.post_post('Это я на море, щас я дома уже', 'load', 'q123'))
print(inst.posts)


