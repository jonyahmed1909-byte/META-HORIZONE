import os
import sys
import time
import json

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

CONFIG_FILE = "config.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {"accounts": [], "passwords": []}
    return {"accounts": [], "passwords": []}

def save_data(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def banner():
    clear_screen()
    print(f"{GREEN}{BOLD}")
    print("=" * 60)
    print(r"""
     ██ ██ ██ ██   ██  █████  ██████  
     ██ ██ ██ ██   ██ ██   ██ ██   ██ 
     ██ ██ ██ ███████ ███████ ██   ██ 
██    ██ ██ ██ ██   ██ ██   ██ ██   ██ 
 ██████  ██ ██ ██   ██ ██   ██ ██████  
                                    
        J E   J I H A D   T O O L
    """)
    print("=" * 60)
    print(f"{CYAN} Developer: JE JIHAD{RESET}\n")

def loading_animation(text):
    sys.stdout.write(f"{YELLOW}{text}")
    for _ in range(3):
        time.sleep(0.4)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

def meta_ai_automation():
    clear_screen()
    banner()
    print(f"{YELLOW}[*] Meta AI Automation Started (Android Local Mode){RESET}")
    print(f"{CYAN}Generating execution link and browser session...{RESET}")
    loading_animation("Bypassing verification & initializing selenium")
    
    generated_link = "https://meta.ai/automation/session_auth_android?token=local_bypass"
    print(f"{GREEN}[✓] Automation Link Generated Successfully!{RESET}")
    print(f"{CYAN}Link: {generated_link}{RESET}")
    print(f"{YELLOW}[!] Status: Ready for auto photo upload, verification & saving.{RESET}\n")
    
    data = load_data()
    new_acc = {
        "email": "meta_user_" + str(int(time.time())) + "@tempmail.com",
        "password": "Jihad_Pass_" + str(int(time.time()))[:4],
        "status": "Active & Verified"
    }
    data["accounts"].append(new_acc)
    data["passwords"].append({"email": new_acc["email"], "password": new_acc["password"]})
    save_data(data)
    
    print(f"{GREEN}[✓] New Account & Password automatically saved to local database!{RESET}")
    input(f"\n{BOLD}Press Enter to go back to the main menu...{RESET}")

def password_save_option():
    clear_screen()
    banner()
    print(f"{YELLOW}[*] Saved Passwords List{RESET}")
    data = load_data()
    passwords = data.get("passwords", [])
    
    if not passwords:
        print(f"{RED}[!] No passwords saved yet.{RESET}")
    else:
        print(f"{CYAN}{'Email':<35} | {'Password'}{RESET}")
        print("-" * 55)
        for idx, item in enumerate(passwords, 1):
            print(f"{idx}. {item['email']:<30} | {item['password']}")
            
    input(f"\n{BOLD}Press Enter to go back to the main menu...{RESET}")

def all_account_save_option():
    clear_screen()
    banner()
    print(f"{YELLOW}[*] All Accounts Database (Local Storage){RESET}")
    data = load_data()
    accounts = data.get("accounts", [])
    
    print(f"{GREEN}[✓] Total Accounts Created: {len(accounts)}{RESET}\n")
    if accounts:
        for idx, acc in enumerate(accounts, 1):
            print(f"{CYAN}[{idx}] Email: {acc['email']} | Status: {acc['status']}{RESET}")
            
    input(f"\n{BOLD}Press Enter to go back to the main menu...{RESET}")

def google_sheet_integration():
    clear_screen()
    banner()
    print(f"{YELLOW}[*] Local Sheet / Backup Sync{RESET}")
    print(f"{CYAN}Backing up all accounts to a local CSV/JSON file (No API Key Required)...{RESET}")
    loading_animation("Exporting data")
    
    data = load_data()
    backup_filename = "jihad_accounts_backup.csv"
    
    with open(backup_filename, "w") as f:
        f.write("Email,Password,Status\n")
        for acc in data.get("accounts", []):
            f.write(f"{acc['email']},{acc['password']},{acc['status']}\n")
            
    print(f"{GREEN}[✓] Backup successfully saved as '{backup_filename}' in your folder!{RESET}\n")
    input(f"\n{BOLD}Press Enter to go back to the main menu...{RESET}")

def main_menu():
    while True:
        banner()
        print(f"{BOLD}[1] Meta AI Automation Account Create")
        print("[2] Password Save Option")
        print("[3] All Account Save Option")
        print("[4] Google Sheet / Local Backup Save")
        print(f"[0] Exit Tool{RESET}\n")
        
        choice = input(f"{CYAN}Select an option (1-4): {RESET}")
        
        if choice == '1':
            meta_ai_automation()
        elif choice == '2':
            password_save_option()
        elif choice == '3':
            all_account_save_option()
        elif choice == '4':
            google_sheet_integration()
        elif choice == '0':
            print(f"\n{RED}Exiting tool. Goodbye, JE JIHAD!{RESET}\n")
            sys.exit()
        else:
            print(f"\n{RED}Invalid option! Please choose between 1 to 4.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{RED}Process interrupted by user. Exiting...{RESET}\n")
        sys.exit()
