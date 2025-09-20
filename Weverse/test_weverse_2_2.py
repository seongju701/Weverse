from time import sleep
from pages.login_page import LoginPage

id_value = "seongju701@naver.com"
pw_value = "dnlqjtm1!"

def test_community_join(page):
    login_page = LoginPage(page)
    login_page.login(id_value, pw_value)
    page.get_by_role("button").filter(has_text="커뮤니티 찾기").click()
    page.get_by_role("textbox", name="search").fill("bts")
    page.locator(".global-search-community-list-item-_-community_name").first.click()
    page.locator("#iwma").get_by_role("button", name="가입하기").click()
    page.get_by_label("wev3 modal").locator("button").filter(has_text="가입하기").click()
    title = page.locator(".community-meta-description-_-joined").inner_text()
    print(title)
    assert title in "가입 완료"

def test_create_post(page):

    login_page = LoginPage(page)
    login_page.login(id_value, pw_value)
    page.get_by_role("link").filter(has_text="BTS").first.click()
    page.locator(".global-header-profile-_-profile").click()
    page.locator(".wev-editor-input-v3-_-text").click()
    page.locator("#wev-editor").fill("BTS!!!!!!!!!!!!  Let's Go")
    page.get_by_label("attach photo", exact=True).set_input_files("/Users/seongjucho/Desktop/BTS_WE.jpeg")
    page.get_by_text("확인").click()
    page.locator("button").filter(has_text="등록").click()
    # src 속성 가져오기
    img_element = page.locator(".post-module-_-image_wrap > span > img").first
    src_value = img_element.get_attribute("src")
    print(src_value)
    assert "BTS_WE.jpeg" in src_value


def test_modify_post(page):

    login_page = LoginPage(page)
    login_page.login(id_value, pw_value)
    page.get_by_role("link").filter(has_text="BTS").first.click()
    page.locator(".global-header-profile-_-profile").click()
    page.locator(".toolbar-_-more").first.click()
    page.get_by_role("button", name="수정하기 수정하기", exact=True).click()
    page.locator("button").filter(has_text="delete image").click()
    page.locator("#wev-editor > p").first.fill("BBBBBTTTTSSSSS!!!")
    page.get_by_label("attach video", exact=True).set_input_files("/Users/seongjucho/Desktop/JImin.mov")
    page.locator("button").filter(has_text="확인").click()
    page.locator("button").filter(has_text="등록").click()
    page.locator("//*[@id=\"Rectangle 502\"]").click()
    text = page.locator("div.community-fanpost-postId-_-wrap_weverse_viewer > div > div > p").inner_text()
    print(text)
    assert "text" in "BBBBBTTTTSSSSS!!!"
    sleep(5)



def test_login_delete(page):

    login_page = LoginPage(page)
    login_page.login(id_value, pw_value)
    page.get_by_role("link").filter(has_text="BTS").first.click()
    page.locator(".global-header-profile-_-profile").click()
    sleep(1)
    posts = page.locator(".profile-content-post-list-_-item")
    post_count = posts.count()  # 게시글 수
    print(post_count)
    for i in range(post_count):
        page.locator(".toolbar-_-more").first.click()
        page.get_by_role("button", name="삭제하기 삭제하기", exact=True).click()
        page.locator("button").filter(has_text="확인").click()
        sleep(1)
    not_post = page.locator(".empty-module-view-_-description").inner_text()
    print(not_post)
    assert not_post in "아직 작성한 포스트가 없습니다."
