def get_valid_input(min_val, max_val):
    """
    接收使用者輸入，並檢查是否為整數且在指定範圍內。
    
    參數:
        min_val (int): 猜數字範圍的最小值
        max_val (int): 猜數字範圍的最大值
        
    回傳:
        int: 經過驗證的合法數字
    """
    while True:
        # 1. 負責寫 input()
        user_input = input(f"請猜一個數字 ({min_val} ~ {max_val}): ")
        
        # 2. 檢查使用者輸入的是不是數字
        try:
            guess = int(user_input)
            
            # 3. 檢查有沒有在範圍內
            if min_val <= guess <= max_val:
                return guess # 完全符合條件，回傳數字結束這個函式
            else:
                print(f"⚠️ 提示：數字不在範圍內！請輸入介於 {min_val} 到 {max_val} 之間的數字。\n")
                
        except ValueError:
            # 如果 int(user_input) 失敗（例如輸入英文字母或符號），就會跑到這裡
            print("⚠️ 錯誤：格式不對！請輸入純數字（整數）。\n")

# ==========================================
# 下方這段是給你（開發者 A）自己在本機測試用的
# 整合者 D (main 分支) 不會用到下面這段，只會 import 上面的 get_valid_input 函式
# ==========================================
if __name__ == "__main__":
    print("--- 測試開發者 A 的功能開始 ---")
    
    # 假設我們現在的範圍是 1 到 100
    valid_number = get_valid_input(1, 100)
    
    print(f"✅ 成功！你輸入的合法數字是：{valid_number}")
    print("--- 測試開發者 A 的功能結束 ---")