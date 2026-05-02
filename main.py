import os
import random
from colorama import Fore, Style, init

# --- 初始化與環境設定 ---
init(autoreset=True)

def clear_screen():
    # 支援 Windows (cls) 與 Linux/Mac (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

# --- 1. 核心邏輯 (來自分支二) ---
def generate_answer(start=1, end=100):
    return random.randint(start, end)

def check_guess(guess, answer):
    if guess > answer:
        return "TOO HIGH"
    elif guess < answer:
        return "TOO LOW"
    else:
        return "CORRECT"

# --- 2. 輸入驗證 (來自分支三，並優化以適應 UI) ---
def get_valid_input(min_val, max_val, attempts, current_feedback):
    while True:
        # 呼叫 UI 顯示目前的狀態，並取得輸入
        user_input = display_input_page(attempts, current_feedback)
        
        try:
            guess = int(user_input)
            if min_val <= guess <= max_val:
                return guess
            else:
                current_feedback = "OUT OF RANGE"
        except ValueError:
            current_feedback = "INVALID INPUT"

# --- 3. UI 頁面控制 (來自分支一) ---
def display_welcome_page():
    clear_screen()
    banner = f"""
    {Fore.CYAN}┌───────────────────────────────────────────────────────────────────┐
    │                                                                   │
    │  {Fore.YELLOW} ██████╗ ██╗   ██╗███████╗███████╗███████╗                       {Fore.CYAN}│
    │  {Fore.YELLOW}██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝                       {Fore.CYAN}│
    │  {Fore.YELLOW}██║  ███╗██║   ██║█████╗  ███████╗███████╗                       {Fore.CYAN}│
    │  {Fore.YELLOW}██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║                       {Fore.CYAN}│
    │  {Fore.YELLOW}╚██████╔╝╚██████╔╝███████╗███████║███████║                       {Fore.CYAN}│
    │  {Fore.YELLOW} ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝                       {Fore.CYAN}│
    │                                                                   │
    │  {Fore.YELLOW}      ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      {Fore.CYAN}│
    │  {Fore.YELLOW}      ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗     {Fore.CYAN}│
    │  {Fore.YELLOW}      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝     {Fore.CYAN}│
    │  {Fore.YELLOW}      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗     {Fore.CYAN}│
    │  {Fore.YELLOW}      ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║     {Fore.CYAN}│
    │  {Fore.YELLOW}      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     {Fore.CYAN}│
    │                                                                   │
    │                   {Fore.WHITE}SYSTEM STATUS: ONLINE                           {Fore.CYAN}│
    └───────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}
    """
    print(banner)
    print(f"\n{Fore.GREEN}             >>> [ PRESS ENTER TO START SYSTEM ] <<<{Style.RESET_ALL}")
    input()

# --- 2. 輸入頁面修正 (狀態列對齊) ---
def display_input_page(attempts=0, feedback="AWAITING INPUT"):
    clear_screen()
    # 這裡將格式化稍微簡化，確保邊框不會爆開
    header = f"{Fore.WHITE}CORE MODULE {Fore.CYAN}│ {Fore.WHITE}ATTEMPTS: {Fore.YELLOW}{attempts:02d} {Fore.CYAN}│ {Fore.WHITE}STATUS: {Fore.MAGENTA}{feedback:<15}"
    
    print(f"{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════╗")
    print(f"║ {header} {Fore.CYAN}             ║")
    print(f"╚═══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}  INPUT TARGET NUMBER (1-100):{Style.RESET_ALL}")
    guess = input(f"  {Fore.CYAN}>> {Style.RESET_ALL}")
    return guess

# --- 3. 結算頁面修正 (終極對齊版) ---
def display_final_page(target=0, total_attempts=0):
    clear_screen()
    # 這裡調整了空格，確保在顏色控制碼存在的情況下，右側的 # 依然能對齊
    success_art = f"""
    {Fore.GREEN}#####################################################################
    #                                                                   #
    #                 {Fore.WHITE}✨ MISSION ACCOMPLISHED ✨{Fore.GREEN}                        #
    #                                                                   #
    #                 {Fore.YELLOW}IDENTIFIED: {target:<21}{Fore.GREEN}                 #
    #                 {Fore.YELLOW}ATTEMPTS  : {total_attempts:<21}{Fore.GREEN}                 #
    #                                                                   #
    #####################################################################{Style.RESET_ALL}
    """
    print(success_art)
    print(f"\n{Fore.CYAN}              [ 'R' ] RESTART  |  [ ANY ] EXIT{Style.RESET_ALL}")
    return input().upper()
# --- 4. 主執行流程 (Main Game Loop) ---
def main():
    while True:
        display_welcome_page()
        
        target_number = generate_answer(1, 100)
        attempts = 0
        current_feedback = "AWAITING INPUT"
        
        while True:
            # 取得驗證過的輸入
            user_guess = get_valid_input(1, 100, attempts, current_feedback)
            attempts += 1
            
            # 檢查結果
            result = check_guess(user_guess, target_number)
            
            if result == "CORRECT":
                break
            else:
                current_feedback = result # 更新狀態為 TOO HIGH 或 TOO LOW

        # 遊戲結束頁面
        choice = display_final_page(target_number, attempts)
        if choice != 'R':
            print(f"{Fore.WHITE}SYSTEM SHUTDOWN. GOODBYE.")
            break

if __name__ == "__main__":
    main()
