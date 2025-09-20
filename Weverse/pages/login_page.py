class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, email, password):
        self.page.get_by_role("button", name="로그인").click()
        self.page.get_by_role("button", name="이메일로 로그인").click()
        self.page.get_by_role("textbox", name="your@email.com").fill(email)
        self.page.get_by_role("textbox", name="비밀번호").fill(password)
        self.page.get_by_role("button", name="로그인").click()
