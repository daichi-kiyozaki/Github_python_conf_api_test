from atlassian import Confluence
import config
import re

confluence = Confluence(url=config.CONFLUENCE_URL, username=config.CONFLUENCE_USERNAME, password=config.CONFLUENCE_TOKEN)

# idでページ情報を取得
loaded_page_id = "16318465"
res = confluence.get_page_by_id(
    page_id=loaded_page_id,
    expand="space,body.storage"  # スペース情報やページの本文を取得
)
# 取得したページの本文を抜き出す。resは多重な辞書型として引っ張られてくるので以下の様になる。
conf_page_content = res['body']['storage']['value']
# ```uml xxxxx ```から、xxxxxの部分 を抽出
puml_blocks = re.findall(r"```uml\s*([^/`]+)```", conf_page_content)
print(puml_blocks)