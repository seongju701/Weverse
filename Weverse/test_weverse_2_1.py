from time import sleep


def test_signup(page):
    email_value = "whtjdwn3000@daum.net"
    k_id_value = "seongju701@naver.com"
    k_pw_value = "whtjdwn1@"
    # 회원가입 인증번호 받기
    page.get_by_role("button", name="로그인").click()
    page.get_by_role("button", name="회원가입").click()
    page.get_by_role("button", name="이메일로 가입하기").click()
    page.get_by_role("textbox", name="이메일 required").click()
    page.get_by_role("textbox", name="이메일 required").fill(email_value)
    page.get_by_role("button", name="인증코드 받기").click()
    # 인증코드 발송 대기 시간 지정
    sleep(5)
    # 다음 메일 내 인증코드 확인 절차
    page1 = page.context.new_page()
    page1.goto("https://www.daum.net/")
    page1.get_by_role("link", name="카카오계정으로 로그인").click()
    page1.get_by_role("textbox", name="계정정보 입력").fill(k_id_value)
    page1.get_by_role("textbox", name="비밀번호 입력").fill(k_pw_value)
    page1.get_by_role("button", name="로그인", exact=True).click()
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="메일 안 읽은 메일").click()
    page2 = page2_info.value
    page2.get_by_role("link", name="[Weverse Account]").first.click()
    mail_code = page2.locator(
        "//*[@id=\"mailViewer\"]/div[2]/div[2]/div[1]/table/tbody/tr/td/div/table/tbody/tr/td[2]/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/table/tbody/tr[5]/td/table/tbody/tr[4]").inner_text()
    print(mail_code)
    #첫번째 탭 이동
    page.bring_to_front()
    #인증번호 입력
    page.get_by_placeholder("인증코드 6자리").fill(mail_code)
    page.get_by_role("button", name="인증코드 확인").click()
    page.get_by_role("textbox", name="비밀번호 required").fill("whtjdwn1!")
    page.get_by_role("textbox", name="비밀번호 확인 required").fill("whtjdwn1!")
    page.get_by_role("textbox", name="닉네임 required").fill("윤이아빠")
    page.get_by_role("button", name="다음").click()

def test_login_check(page):
    id_value = "seongju701@naver.com"
    pw_value = "dnlqjtm1!"
    # 로그인 과정
    page.get_by_role("button", name="로그인").click()
    page.get_by_role("button", name="이메일로 로그인").click()
    page.get_by_role("textbox", name="your@email.com").fill(id_value)
    page.get_by_role("textbox", name="비밀번호").fill(pw_value)
    with page.expect_response(lambda r: "users/me" in r.url) as response_info:
        page.get_by_role("button", name="로그인").click()
    response = response_info.value
    data = response.json()
    print(data)
    wid_value = data["wid"]
    print("ID:", id_value)
    print("PW:", pw_value)
    print("WID:", wid_value)

