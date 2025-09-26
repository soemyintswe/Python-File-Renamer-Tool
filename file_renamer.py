import os
import shutil

# --- Folder လမ်းကြောင်းများ သတ်မှတ်ခြင်း ---
INPUT_FOLDER = "input_files"
OUTPUT_FOLDER = "output_files"

def ensure_dirs(folders):
    """Folders များရှိ/မရှိ စစ်ဆေးပြီး မရှိရင် အသစ်ဖန်တီးပေးသည်။"""
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def get_new_filename(original_name, option, user_input):
    """ရွေးချယ်မှုအလိုက် ဖိုင်အမည်အသစ်ကို ပြန်ပေးသည်။"""
    
    name_only, extension = os.path.splitext(original_name)
    
    # ရွေးချယ်မှုအလိုက် နာမည်အသစ် ပြောင်းလဲခြင်း
    if option == '1':
        # ၁။ နာမည်အသစ်လုံးဝ အစားထိုးခြင်း (Overwrite)
        return user_input + extension
        
    elif option == '2':
        # ၂။ ရှေ့ဆုံး (Prefix) တွင် စာလုံးထပ်ထည့်ခြင်း (Space ခြားမည်)
        text_to_add = user_input.strip() 
        return f"{text_to_add} {name_only}" + extension
        
    elif option == '3':
        # ၃။ နောက်ဆုံး (Suffix) တွင် စာလုံးထပ်ထည့်ခြင်း (Space ခြားမည်)
        text_to_add = user_input.strip()
        return f"{name_only} {text_to_add}" + extension
        
    elif option == '4':
        # ၄။ ကြားနေရာ (Position) တွင် စာလုံးထပ်ထည့်ခြင်း (Space ခြားမည်)
        try:
            position = int(user_input['position'])
            text_to_add = user_input['text'].strip()
            
            position = min(position, len(name_only)) 
            
            # Space နှစ်ခုလုံး ခံထားသည်
            new_name = name_only[:position] + f" {text_to_add} " + name_only[position:]
            
            # နာမည်ရဲ့ အစမှာ/အဆုံးမှာ မလိုအပ်ဘဲ ဖြစ်နေတဲ့ space များကို ဖြုတ်ခြင်း
            return new_name.strip() + extension
            
        except ValueError:
            # Position ဂဏန်း မဟုတ်ရင် မပြောင်းလဲဘဲ မူရင်းအတိုင်း ပြန်ပေး
            return original_name 
            
    elif option == '5':
        # ၅။ တစ်စိတ်တစ်ပိုင်း (Substring) ကို အခြားစာလုံးဖြင့် အစားထိုးခြင်း
        find_text = user_input['find']
        replace_text = user_input['replace']
        
        if find_text in name_only:
            return name_only.replace(find_text, replace_text) + extension
        else:
            return original_name
            
    elif option == '6':
        # ၆။ မလိုချင်တဲ့ စာလုံးအစုအဝေး (Substring) ကို ဖယ်ထုတ်ခြင်း (Remove Substring)
        text_to_remove = user_input
        new_name = name_only.replace(text_to_remove, "")
        
        # ဖယ်ရှားပြီးနောက် မလိုလားအပ်သော Space များအား ထပ်မံ ဖြုတ်ခြင်း
        new_name = new_name.replace("  ", " ").strip() 
        return new_name + extension
    
    elif option == '7':
        # ၇။ ဘာမှ မပြောင်းလဲခြင်း (မူရင်းအတိုင်း Output သို့ ရွှေ့ခြင်း)
        return original_name
    
    return original_name

def get_user_choice():
    """ရွေးချယ်မှု နံပါတ်ကို မှန်ကန်စွာ ရိုက်ထည့်သည်အထိ စစ်ဆေးမေးမြန်းခြင်း"""
    VALID_CHOICES = ['1', '2', '3', '4', '5', '6', '7']
    
    while True:
        print("\n" + "="*50)
        print("      📁 ဖိုင်အမည် ပြောင်းလဲမှုပုံစံ ရွေးချယ်ပါ 📁")
        print("="*50)
        print("  1. နာမည်အသစ်လုံးဝ အစားထိုးမည်။")
        print("  2. ရှေ့ဆုံး (Prefix) တွင် စာလုံးထပ်ထည့်မည်။")
        print("  3. နောက်ဆုံး (Suffix) တွင် စာလုံးထပ်ထည့်မည်။")
        print("  4. ကြားနေရာတစ်ခုခု (Position) တွင် စာလုံးထပ်ထည့်မည်။")
        print("  5. နာမည်ရဲ့ တစ်စိတ်တစ်ပိုင်း (Substring) ကို အခြားစာလုံးဖြင့် အစားထိုးမည်။")
        print("  6. မလိုချင်တဲ့ စာလုံးအစုအဝေးကို ဖယ်ထုတ်ပစ်မည်။")
        print("  7. **ဘာမှ မပြောင်းလဲဘဲ Output Folder သို့ ရွှေ့ပြောင်းမည်။**")
        print("-" * 50)
        
        choice = input("ကျေးဇူးပြု၍ နံပါတ်တစ်ခု (1-7) ကို ရွေးချယ်ပါ: ")
        
        if choice in VALID_CHOICES:
            return choice
        else:
            print("\n" + "#"*50)
            print(f"❌ ရွေးချယ်မှု နံပါတ် '{choice}' သည် မမှန်ကန်ပါ။ (1 မှ 7 အတွင်းသာ ရွေးချယ်ပါ)")
            
            # ဆက်လုပ်မလား ရပ်မလား မေးခြင်း
            continue_choice = input("မှန်ကန်သော နံပါတ်ကို ပြန်ရွေးချင်ပါသလား (Y/y)၊ သို့မဟုတ် ရပ်နားချင်ပါသလား (N/n)။: ").strip().lower()
            
            if continue_choice in ['n', 'no']:
                return None # ရပ်နားရန်
            # Y/y သို့မဟုတ် အခြားရိုက်ထည့်ပါက loop ပြန်စပြီး မှန်တာပြန်ရွေးခိုင်းမည်

# --- Main Function ---
def run_file_renamer():
    ensure_dirs([INPUT_FOLDER, OUTPUT_FOLDER])
    
    files_to_rename = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    
    if not files_to_rename:
        print(f"**'{INPUT_FOLDER}' folder ထဲတွင် ဖိုင်များ မတွေ့ပါ။ ရွှေ့ပြောင်း/နာမည်ပြောင်းရန် ဖိုင်များ ထည့်ပေးပါ။**")
        return

    # ရွေးချယ်မှုရယူခြင်း (မှန်ကန်မှသာ ဆက်သွားမည်)
    choice = get_user_choice()
    
    if choice is None:
        print("\n👋 အသုံးပြုသူ၏ တောင်းဆိုမှုအရ Script ကို ရပ်နားလိုက်ပါပြီ။")
        return

    # --- ရွေးချယ်မှုအလိုက် လိုအပ်သော Input များ ထပ်မံရယူခြင်း ---
    new_input = {}
    if choice == '1':
        print("\n**သတိပြုရန်။ ဖိုင်အားလုံးကို နာမည်တစ်ခုတည်းဖြင့် အစားထိုးပါက ဖိုင်ဟောင်းများ ပျက်စီးနိုင်ပါသည်။**")
        new_input = input("ဖိုင်အသစ်၏ နာမည်အပြည့်အစုံကို ထည့်ပါ (ဥပမာ: photo_new): ")
        
    elif choice == '2':
        new_input = input("ရှေ့ဆုံးတွင် ထပ်ထည့်မည့် စာလုံး (Prefix) ကို ထည့်ပါ (ဥပမာ: FINAL): ")
        
    elif choice == '3':
        new_input = input("နောက်ဆုံးတွင် ထပ်ထည့်မည့် စာလုံး (Suffix) ကို ထည့်ပါ (ဥပမာ: VER2): ")
        
    elif choice == '4':
        text = input("ထည့်သွင်းလိုသော စာလုံးကို ထည့်ပါ: ")
        pos = input("ထည့်သွင်းလိုသော နေရာ (Position - 0 ကနေစသည်) ကို ဂဏန်းဖြင့် ထည့်ပါ: ")
        new_input = {'text': text, 'position': pos}
        
    elif choice == '5':
        find_text = input("အစားထိုးမည့် မူရင်းစာလုံး (Substring) ကို ထည့်ပါ (ဥပမာ: IMG_): ")
        replace_text = input("အစားထိုးမည့် စာလုံးအသစ်ကို ထည့်ပါ (ဥပမာ: PIC_): ")
        new_input = {'find': find_text, 'replace': replace_text}
        
    elif choice == '6':
        new_input = input("ဖိုင်နာမည်ထဲမှ ဖယ်ထုတ်လိုသော စာလုံးအစုအဝေး (Substring) ကို တိကျစွာ ထည့်ပါ (ဥပမာ: copy of): ")
        
    elif choice == '7':
        print("\n**မူရင်းဖိုင်နာမည်အတိုင်း Output Folder သို့ ရွှေ့ပြောင်းပါမည်။**")
        pass

    # --- ဖိုင်များ လည်ပတ်ခြင်းနှင့် နာမည်ပြောင်း/ရွှေ့ပြောင်းခြင်း ---
    print("\n--- လုပ်ဆောင်နေပါသည် ---")
    for filename in files_to_rename:
        old_path = os.path.join(INPUT_FOLDER, filename)
        
        # နာမည်အသစ် တွက်ချက်ခြင်း
        new_filename = get_new_filename(filename, choice, new_input)
        
        # နာမည်အသစ်နှင့် ဖိုင်လမ်းကြောင်းအသစ်
        new_path = os.path.join(OUTPUT_FOLDER, new_filename)
        
        try:
            # ဖိုင်ကို နာမည်ပြောင်းပြီး ရွှေ့ပြောင်းခြင်း
            shutil.move(old_path, new_path)
            print(f"✅ {filename}  ->  {new_filename}")
        except Exception as e:
            print(f"❌ Error! {filename} ကို မပြောင်းလဲနိုင်ခဲ့ပါ။ ({e})")

    print("\n" + "="*50)
    print(f"            🎉 အောင်မြင်စွာ ပြီးဆုံးပါပြီ 🎉")
    print(f"      ဖိုင်များကို '{OUTPUT_FOLDER}' ထဲတွင် စစ်ဆေးနိုင်ပါသည်။")
    print("="*50)

if __name__ == "__main__":
    run_file_renamer()