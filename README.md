Python File Renamer Utility

တစ်နေရာတည်းမှာရှိတဲ့ ဖိုင်များစွာရဲ့ နာမည်ကို အလိုအလျောက်၊ စိတ်ကြိုက် ပြောင်းလဲပေးနိုင်တဲ့ Python Script ဖြစ်ပါတယ်။ အသုံးပြုသူရဲ့ လိုအပ်ချက်ပေါ်မူတည်ပြီး Prefix, Suffix, ဖိုင် Extension ပြောင်းလဲခြင်း စတဲ့ လုပ်ဆောင်ချက် ၇ မျိုးကို ရွေးချယ်နိုင်ပါတယ်။

✨ Features (ထူးခြားချက်များ)

Bulk Renaming: Folder တစ်ခုအတွင်းရှိ ဖိုင်အားလုံးကို တစ်ပြိုင်တည်း အမည်ပြောင်းလဲနိုင်ခြင်း။

Multiple Options: ဖိုင်အမည်ရှေ့ဆုံး (Prefix)၊ နောက်ဆုံး (Suffix) ထည့်သွင်းခြင်း၊ နာမည်အသစ် အစားထိုးခြင်း စတဲ့ ရွေးချယ်မှု (၇) မျိုး ပါဝင်ခြင်း။

Sequential Numbering: ဖိုင်တွေကို အစဉ်လိုက် နံပါတ်စဉ် (e.g., file-001.jpg, file-002.jpg) တပ်ပေးနိုင်ခြင်း။

Case Conversion: နာမည်အားလုံးကို အကြီးစာလုံး (UPPERCASE) သို့မဟုတ် အသေးစာလုံး (lowercase) သို့ ပြောင်းလဲနိုင်ခြင်း။

Input Validation: အသုံးပြုသူရဲ့ Input တွေကို စစ်ဆေးပြီး မှားယွင်းမှုမရှိအောင် ကာကွယ်ပေးထားခြင်း။

🛠️ Prerequisites (ကြိုတင်ပြင်ဆင်ရန်)

ဒီ Script ကို အသုံးပြုဖို့အတွက် သင့်ကွန်ပျူတာမှာ အောက်ပါတို့ ရှိနေရပါမယ်။



Python 3: Python Official Website မှ နောက်ဆုံး Version ကို Install လုပ်ပါ။

Command Line Access: Windows (Command Prompt / PowerShell) သို့မဟုတ် Mac/Linux (Terminal) ကို အသုံးပြုနိုင်ရပါမယ်။

🚀 Setup (စတင်အသုံးပြုနည်း)

Project Folder ဖန်တီးပါ:

သင့်ကွန်ပျူတာမှာ Project အတွက် Folder အသစ်တစ်ခု (ဥပမာ- Renamer-Project) ဖန်တီးပါ။

Script ထည့်သွင်းပါ:renamer.py ဖိုင်ကို အဲဒီ Folder ထဲကို ကူးထည့်ပါ။

ဖိုင်များ ထည့်သွင်းပါ:

နာမည်ပြောင်းလဲလိုတဲ့ ဖိုင်အားလုံးကိုလည်း renamer.py ဖိုင်နှင့် တူညီသော Folder ထဲမှာ ထည့်ထားပါ။

Terminal ဖွင့်ပါ:

Command Line (သို့မဟုတ် VS Code Terminal) ကိုဖွင့်ပြီး အောက်ပါ Command ဖြင့် သက်ဆိုင်ရာ Folder သို့ သွားပါ။



Bash



cd /path/to/Renamer-Project

Script ကို Run ပါ:

အောက်ပါ Command ဖြင့် Script ကို စတင် အသုံးပြုနိုင်ပါပြီ။



Bash



python renamer.py

⚙️ Command Line Options (လုပ်ဆောင်ချက်များ)

Script ကို စတင် Run ပြီးနောက် အသုံးပြုသူအား ရွေးချယ်ရန် လုပ်ဆောင်ချက် (၇) မျိုးကို မေးပါလိမ့်မယ်။

နံပါတ်ရွေးချယ်မှုလုပ်ဆောင်ချက်ဥပမာ (Original: photo.jpg)1Add Prefixဖိုင်အမည်ရှေ့ဆုံးတွင် စာသားထည့်ပါ။NEW_photo.jpg2Add Suffixဖိုင်အမည်နောက်ဆုံးတွင် စာသားထည့်ပါ။photo_OLD.jpg3Replace Substringဖိုင်အမည်ရှိ စာသားတစ်စိတ်တစ်ပိုင်းကို အခြားစာသားဖြင့် အစားထိုးပါ။(_v1 ကို _final ဖြင့်အစားထိုး)4Change Extensionဖိုင် Extension ကို ပြောင်းလဲပါ။photo.png5Sequential Numberingဖိုင်အမည်ရှေ့ဆုံးတွင် အစဉ်လိုက် နံပါတ်စဉ် (001, 002...) တပ်ပါ။001_photo.jpg6Convert to LOWERCASEဖိုင်အမည်တစ်ခုလုံးကို စာလုံးအသေးသို့ ပြောင်းလဲပါ။photo.jpg7Convert to UPPERCASEဖိုင်အမည်တစ်ခုလုံးကို စာလုံးအကြီးသို့ ပြောင်းလဲပါ။PHOTO.JPG

Export to Sheets

📁 Output Structure (ရလဒ် ပုံစံ)

Original Files: နာမည်မပြောင်းလဲမီ ဖိုင်များ

Renamed Files: Script မှ အောင်မြင်စွာ ပြောင်းလဲပေးလိုက်သော ဖိုင်များ

Console Output: Terminal တွင် နာမည်ပြောင်းလဲခြင်း လုပ်ငန်းစဉ် အောင်မြင်မှု/မအောင်မြင်မှုကို အဆင့်ဆင့် ဖော်ပြပေးပါမည်။

⚠️ Troubleshooting (ပြဿနာဖြေရှင်းနည်း)

ပြဿနာဖြစ်နိုင်ခြေ အကြောင်းရင်းဖြေရှင်းနည်းpython: command not foundPython ကို Install မလုပ်ရသေးခြင်း သို့မဟုတ် Path ထဲတွင် မရှိခြင်း။Python ကို စနစ်တကျ Install လုပ်ပြီး Terminal အသစ် ပြန်ဖွင့်ပါ။File Renamer: Permission deniedပြောင်းလဲလိုသော ဖိုင်ကို အခြား Program တစ်ခုမှ ဖွင့်ထားခြင်း။ဖွင့်ထားသော Program (e.g., Image Viewer, Video Editor) ကို ပိတ်ပါ။No files found in directoryScript Folder ထဲမှာ ပြောင်းလဲလိုသော ဖိုင်များ လုံးဝ မရှိခြင်း။Script နဲ့ တူညီသော Folder ထဲမှာ ဖိုင်အနည်းဆုံး ၁ ဖိုင် ထည့်သွင်းပါ။

Export to Sheets

🙋‍♂️ Support & Contribution

ဒီ Script ကို အသုံးပြုရာမှာ အဆင်မပြေမှု တစ်စုံတစ်ရာ ရှိခဲ့ရင် သို့မဟုတ် အကြံပြုချက် ပေးလိုရင် GitHub Issues ကနေတဆင့် ဆက်သွယ်နိုင်ပါတယ်။