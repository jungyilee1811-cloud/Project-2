import google.generativeai as genai
from web_search import web_search
import json
import requests

def web_search(query):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = []
    
    if "RelatedTopics" in data:
        for item in data["RelatedTopics"][:5]:
            if "Text" in item and "FirstURL" in item:
                results.append({
                    "title": item["Text"],
                    "url": item["FirstURL"]
                })
    return results





genai.configure(api_key="AIzaSyCIsLvPKLi9abhh6k3I9ZWFbHhSXww3j_w")
model = genai.GenerativeModel("gemini-2.5-flash")

def smart_answer(question):
    check = model.generate_content(f"問題是：「{question}」。請回答：是否需要查詢網路才能回答？只回答 是 或 否。")
    need_search = "是" in check.text

    if need_search:
        print("\n 需要搜尋網路，正在查詢中...")
        results = web_search(question)
        if results:
            summary_text = "\n".join([f"{r['title']} ({r['url']})" for r in results])
            full_prompt = f"使用以下資料回答問題：\n{summary_text}\n\n問題：{question}\n請產生一個清晰簡潔的回答。"
            answer = model.generate_content(full_prompt)
            return answer.text
        else:
            return "查不到相關資料。"
    else:
        answer = model.generate_content(question)
        return answer.text

if __name__ == "__main__":
    while True:
        question = input("\n 請輸入問題（或輸入 'exit' 離開）：")
        if question.lower() == "exit":
            break
        print("\n 機器人回答：", smart_answer(question))
