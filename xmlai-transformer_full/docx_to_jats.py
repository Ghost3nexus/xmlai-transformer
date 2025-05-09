from docx import Document
from io import BytesIO

def convert_docx_to_jats(file_bytes):
    doc = Document(BytesIO(file_bytes))
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]

    body = ""
    for para in paragraphs:
        body += f"<p>{para}</p>\n"

    jats_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE article PUBLIC "-//NLM//DTD JATS (Z39.96) Journal Publishing DTD v1.3 20150301//EN"
  "http://jats.nlm.nih.gov/publishing/1.3/JATS-journalpublishing1.dtd">
<article xmlns:xlink="http://www.w3.org/1999/xlink"
         article-type="research-article"
         xml:lang="ja">
  <front>
    <journal-meta>
      <journal-id journal-id-type="publisher-id">xmlai-journal</journal-id>
      <journal-title>XML AI 自動変換</journal-title>
    </journal-meta>
    <article-meta>
      <article-id pub-id-type="doi">10.1234/xmlai.00002</article-id>
      <title-group>
        <article-title>自動JATS変換出力</article-title>
      </title-group>
      <contrib-group>
        <contrib contrib-type="author">
          <name>
            <surname>テスト</surname>
            <given-names>ユーザー</given-names>
          </name>
        </contrib>
      </contrib-group>
      <pub-date><year>2025</year></pub-date>
    </article-meta>
  </front>
  <body>
    <sec>
      <title>本文</title>
      {body}
    </sec>
  </body>
</article>
"""
    return jats_template
