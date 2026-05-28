# /// script
# dependencies = [
#   "supabase",
#   "python-dotenv",
# ]
# ///

import os
from dotenv import load_dotenv
from supabase import create_client, Client

def main():
    # 載入本地 .env 檔案
    load_dotenv()
    
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    # 驗證憑證是否已填寫
    if not supabase_url or "your-project-id" in supabase_url:
        print("[錯誤] 請先在根目錄的 .env 檔案中填入正確的 SUPABASE_URL！")
        return
        
    if not supabase_key or "your-anon-key" in supabase_key:
        print("[錯誤] 請先在根目錄的 .env 檔案中填入正確的 SUPABASE_KEY！")
        return

    print("正在連線至 Supabase 資料庫...")
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
    except Exception as e:
        print(f"[錯誤] 連線初始化失敗: {e}")
        return

    # 作品集儲存庫的原始資料
    repos_data = [
        {
            "name": "Agentic-Coding",
            "emoji": "🤖",
            "url": "https://github.com/OoallenoO123123123/Agentic-Coding",
            "description": "探索 Agentic AI 程式設計的專案，運用 JavaScript 實現智能代理程式（Agent）的程式撰寫技術。這是一個以自動化代理為核心的程式設計實驗專案，展示如何利用 AI 輔助完成複雜的程式任務。此儲存庫獲得了 ⭐ 1 顆星的認可。",
            "is_fork": False,
            "language": "JavaScript",
            "feature": "1 星",
            "card_color_1": "#0969da",
            "card_color_2": "#8250df"
        },
        {
            "name": "AI",
            "emoji": "🧠",
            "url": "https://github.com/OoallenoO123123123/AI",
            "description": "從原始作者 Fork 而來的人工智慧相關儲存庫，包含豐富的 AI 學習資源與實作範例。儲存庫大小達 65,589 KB，顯示這是一個內容相當豐富的 AI 資料集或學習材料。適合作為 AI 學習與研究的參考資源。",
            "is_fork": True,
            "language": "多語言",
            "feature": "Forked",
            "card_color_1": "#8250df",
            "card_color_2": "#bc4c00"
        },
        {
            "name": "AI-",
            "emoji": "📚",
            "url": "https://github.com/OoallenoO123123123/AI-",
            "description": "人工智慧課程相關的作業與實作儲存庫（B11090033 陳俊維）。包含課堂學習內容、程式作業及 AI 相關實驗，共有 8 個開放議題（Issues），代表此專案持續活躍開發中。這是學習 AI 領域技術的重要記錄。",
            "is_fork": False,
            "language": "學術專案",
            "feature": "8 Issues",
            "card_color_1": "#bc4c00",
            "card_color_2": "#9a6700"
        },
        {
            "name": "php",
            "emoji": "🐘",
            "url": "https://github.com/OoallenoO123123123/php",
            "description": "PHP 後端開發相關的專案儲存庫，展示伺服器端腳本語言的應用。包含 PHP 程式設計的實踐與練習，涵蓋網頁後端開發、資料庫互動等核心技術。最後更新於 2024 年 6 月，是掌握 PHP 開發技術的良好範例。",
            "is_fork": False,
            "language": "PHP",
            "feature": "後端開發",
            "card_color_1": "#9a6700",
            "card_color_2": "#1a7f37"
        },
        {
            "name": "html-",
            "emoji": "🌐",
            "url": "https://github.com/OoallenoO123123123/html-",
            "description": "HTML 前端開發相關的儲存庫，展示網頁設計與前端技術的應用。包含 HTML 結構設計、網頁布局與互動效果的實作練習，展示了扎實的前端開發基礎能力。儲存庫大小 233 KB，包含完整的網頁範例。",
            "is_fork": False,
            "language": "HTML",
            "feature": "前端設計",
            "card_color_1": "#1a7f37",
            "card_color_2": "#0969da"
        },
        {
            "name": "-",
            "emoji": "📂",
            "url": "https://github.com/OoallenoO123123123/-",
            "description": "這是一個新建立的儲存庫，目前尚在初始化階段。名稱為「-」，預計作為新專案的起點或實驗性開發用途。期待未來這個儲存庫會展現更多精彩內容！",
            "is_fork": False,
            "language": "待定",
            "feature": "初始化中",
            "card_color_1": "#64748b",
            "card_color_2": "#475569"
        }
    ]

    print("正在清空舊有 repositories 資料...")
    try:
        # 清空資料庫內原有的儲存庫資料
        supabase.table("repositories").delete().neq("id", 0).execute()
        print("原有資料清除成功！")
    except Exception as e:
        print(f"[警告] 清除舊資料時發生異常，可能資料表為空或尚未建立 Table: {e}")
        print("將直接嘗試插入資料...")

    print(f"正在匯入 {len(repos_data)} 筆儲存庫資料...")
    try:
        response = supabase.table("repositories").insert(repos_data).execute()
        print("🎉 資料匯入成功！已成功上傳至 Supabase。")
        print("詳細寫入記錄:")
        for idx, row in enumerate(response.data):
            print(f"  [{idx+1}] {row.get('emoji')} {row.get('name')} (ID: {row.get('id')})")
    except Exception as e:
        print(f"[錯誤] 資料寫入失敗: {e}")
        print("請確認您已在 Supabase 執行 SQL 建立資料表，且欄位名稱正確。")

if __name__ == "__main__":
    main()
