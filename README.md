googleAI.py是結合 Gemini 模型與 DuckDuckGo 搜尋 API 的簡易問答程式。
它會自動判斷問題是否需要查詢網路，並在必要時進行搜尋後生成回答。
功能
判斷問題是否需要網路搜尋
DuckDuckGo API 搜尋前 5 筆結果
使用 Gemini 生成清晰回答
命令列互動式問答
安裝
pip install google-generativeai requests
設定 Gemini API 金鑰：
genai.configure(api_key="YOUR_API_KEY")
使用方式
python main.py
輸入問題即可開始使用，輸入 exit 可離開。
