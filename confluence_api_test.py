from atlassian import Confluence
import config

confluence = Confluence(url=config.CONFLUENCE_URL, username=config.CONFLUENCE_USERNAME, password=config.CONFLUENCE_TOKEN)

# idでページ情報を取得
page_id = "7340033"
res = confluence.get_page_by_id(
    page_id=page_id,
    expand="space,body.storage"  # スペース情報やページの本文を取得
)
print("---res---")
print(res)
'''
# タイトルでページ情報を取得
page_title = "conv_check_test_2"
res2 = confluence.get_page_by_title(
    space=config.CONFLUENCE_SPACE_KEY,
    title=page_title
)
print("---res2---")
print(res2)
'''
# ページが存在する場合、本文をbodyの内容で更新
page_id = "15007859"
title = "更新時に書式が反映されるかのテスト_更新後"
body = res["body"]["storage"]["value"]
update_res = confluence.update_page(
    page_id=page_id,
    title=title,
    body=body,
    full_width=True
)
print("---update_res---")
print(update_res)
'''
# タイトル指定でページ内容を更新（指定したページがない場合は新規作成）、必ず子ページになる
parent_id = "15040513"
title = "API_update_test1_6/7_更新後2_width-test"
body = "更新後2_width-test"
update_res2 = confluence.update_or_create(
    parent_id=parent_id,
    title=title,
    body=body,
    full_width=True
)
print("---update_res2---")
print(update_res2)

# 添付ファイルをアップロードしたい場合
page_id = "15040573"
filename = "images/boy01_laugh.png"
upload_res = confluence.attach_file(
    filename=filename,
    page_id=page_id
)
print("---upload_res---")
print(upload_res)
'''
'''
# 添付コンテンツをアップロードしたい場合
page_id = "15040595"
content = "images/boy01_laugh.png"
upload_res2 = confluence.attach_content(
    content=content,
    name="irasutoya_boy",
    page_id=page_id
)
print("---upload_res2---")
print(upload_res2)
'''

# ページを移動させたい場合
page_id = "11993089"
parent_title = "readme.md"
move_res = confluence.move_page(
    space_key=config.CONFLUENCE_SPACE_KEY,
    page_id=page_id,
    target_title=parent_title
)
print("---move_res---")
print(move_res)
