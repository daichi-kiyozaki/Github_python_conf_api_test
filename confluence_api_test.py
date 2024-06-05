from atlassian import Confluence
import config

confluence = Confluence(url=config.CONFLUENCE_URL, username=config.CONFLUENCE_USERNAME, password=config.CONFLUENCE_TOKEN)

# idでページ情報を取得
page_id = "11993089"
res = confluence.get_page_by_id(
    page_id=page_id,
    expand="space,body.view"  # スペース情報やページの本文を取得
)

print(res["space"]["key"])
print(res["id"])
print(res["title"])
print(res["body"]["view"]["value"])  # 本文 (HTML) の先頭 100 文字

# タイトルでページ情報を取得
page_title = "conv_check_test_2"
res2 = confluence.get_page_by_title(
    space=config.CONFLUENCE_SPACE_KEY,
    title=page_title
)

print(res2)

