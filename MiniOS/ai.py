import os
from groq import Groq

# Terminal için ANSI Renk Kodları ve Biçimlendirmeler
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

api_key = os.environ.get("GROQ_KEY")
if not api_key:
    api_key = "GROQ_KEY"

try:
    client = Groq(api_key=api_key)
    
    # Şık Karşılama Ekranı
    print(f"{CYAN}{BOLD}")
    print("╔══════════════════════════════════════════════════╗")
    print("║            MINI OS - AI ASİSTANİ (v2.0)          ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{RESET}")
    print(f"{YELLOW}💡 İpucu: Çıkış yapmak için 'q' veya 'cikis' yazabilirsin.\n{RESET}")

    # Sohbet Geçmişi
    messages = [
        {
            "role": "system",
            "content": "Sen bir Mini OS içerisinde çalışan teknik ve yazılımcı dostu bir yapay zeka asistanısın. Yanıtları kısa, net ve kod odaklı ver."
        }
    ]

    while True:
        try:
            # Şık kullanıcı prompt satırı
            user_prompt = input(f"{GREEN}{BOLD}Sen ❯ {RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{RED}Asistan sonlandırıldı.{RESET}")
            break
            
        # Çıkış koşulu
        if user_prompt.lower() in ["q", "cikis", "çıkış"]:
            print(f"\n{RED}🤖 AI Asistan kapatılıyor. İyi kodlamalar!{RESET}")
            break
            
        if not user_prompt.strip():
            continue

        messages.append({"role": "user", "content": user_prompt})

        print(f"{YELLOW}⏳ Yapay zeka düşünüyor...{RESET}")
        
        # API İstegi
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-20b", # Çalışan modelin
        )

        ai_response = chat_completion.choices[0].message.content
        
        # Şık Yanıt Kutusu
        print(f"\n{CYAN}{BOLD}┌─ AI Asistan ─────────────────────────────────────┐{RESET}")
        print(f"{CYAN}{ai_response}{RESET}")
        print(f"{CYAN}{BOLD}└──────────────────────────────────────────────────┘{RESET}\n")

        messages.append({"role": "assistant", "content": ai_response})

except Exception as e:
    print(f"\n{RED}❌ Bir hata oluştu: {e}{RESET}")
