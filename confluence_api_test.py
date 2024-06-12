# on GithubActions
from atlassian import Confluence
import re
import os


# secretsに登録した環境変数の呼び出し
CONFLUENCE_URL = os.environ.get("CONFLUENCE_URL")
CONFLUENCE_USERNAME = os.environ.get("CONFLUENCE_USERNAME ")
CONFLUENCE_TOKEN = os.environ.get("CONFLUENCE_TOKEN")

print(CONFLUENCE_URL)
confluence = Confluence(url=CONFLUENCE_URL, username=CONFLUENCE_USERNAME, password=CONFLUENCE_TOKEN)

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