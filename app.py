import os
import json
from datetime import datetime

# --- CONSTANTS ---
FILE_NAME = "gorevler.txt"

# --- DATA AND FILE MANAGEMENT (VERİ VE DOSYA YÖNETİMİ) ---
def load_tasks() -> list:
    """Görevleri utf-8 formatındaki dosyadan okur. Dosya yoksa veya hatalıysa boş liste döner."""
    if not os.path.exists(FILE_NAME):
        print("Görev dosyası bulunamadı. Yeni bir liste oluşturuldu.")
        return []
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("Uyarı: Dosya formatı bozuk, temiz bir başlangıç yapılıyor.")
        return []
    except Exception as e:
        print(f"Okuma hatası oluştu: {e}")
        return []

def save_tasks(tasks: list) -> None:
    """Mevcut görev listesini dosyaya kaydeder."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        print("Görevler başarıyla kaydedildi.")
    except Exception as e:
        print(f"Kayıt işlemi sırasında hata: {e}")

# --- UTILS (YARDIMCI FONKSİYONLAR) ---
def get_valid_date(prompt_message: str, default_value: str = "Belirtilmedi") -> str:
    """Kullanıcıdan GG.AA.YYYY formatında geçerli bir tarih alır."""
    while True:
        user_input = input(prompt_message).strip()
        if not user_input:
            return default_value
        
        try:
            valid_date = datetime.strptime(user_input, "%d.%m.%Y")
            return valid_date.strftime("%d.%m.%Y")
        except ValueError:
            print("\nHata: Geçersiz tarih formatı! Lütfen GG.AA.YYYY şeklinde girin (Örn: 15.04.2026).")

def clear_screen() -> None:
    """Konsol ekranını temizleyerek profesyonel bir arayüz deneyimi sunar."""
    # Windows için 'cls', macOS/Linux için 'clear' komutunu çalıştırır
    os.system('cls' if os.name == 'nt' else 'clear')

# --- BUSINESS LOGIC (İŞ MANTIĞI) ---
def list_tasks(tasks: list) -> None:
    """Mevcut görevleri numaralandırılmış ve detaylı formatta listeler."""
    if not tasks:
        print("\nHenüz görev bulunmamaktadır.")
        return
    
    print("\n--- GÖREV LİSTESİ ---")
    for i, task in enumerate(tasks, 1):
        status_icon = "✅" if task.get("tamamlandi", False) else "❌"
        priority = task.get("oncelik", "Normal")
        due_date = task.get("son_tarih", "Belirtilmedi")
        text = task.get("metin", "")
        
        print(f"{i}. {status_icon} {text} (Öncelik: {priority} | Son Tarih: {due_date})")

def add_task(tasks: list) -> None:
    """Yeni görev alır, doğrular ve listeye ekler."""
    text = input("Yeni görev: ").strip()
    
    if not text:
        print("\nHata: Boş görev eklenemez!")
        return
        
    print("Öncelik Seviyeleri: 1-Yüksek, 2-Normal, 3-Düşük")
    priority_choice = input("Seçiminiz (Varsayılan 2): ").strip()
    priority_map = {"1": "Yüksek", "2": "Normal", "3": "Düşük"}
    priority = priority_map.get(priority_choice, "Normal")
    due_date = get_valid_date("Son Tarih (Örn: 15.04.2026 veya boş bırakmak için Enter): ")

    if not due_date:
        due_date = "Belirtilmedi"
    
    new_task = {
        "metin": text,
        "tamamlandi": False,
        "oncelik": priority,
        "son_tarih": due_date
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\n'{text}' görevi eklendi.")

def edit_task(tasks: list) -> None:
    """Belirtilen indexteki görevi düzenler ve durumunu günceller."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("\nDüzenlemek istediğiniz görevin numarası: "))
        index = task_no - 1
        
        if 0 <= index < len(tasks):
            current_task = tasks[index]
            
            # 1. METİN DÜZENLEME
            print(f"\nMevcut görev metni: {current_task['metin']}")
            new_text = input("Yeni metin (Değiştirmemek için sadece Enter'a basın): ").strip()
            
            if new_text:
                tasks[index]["metin"] = new_text
            
            # 2. TARİH DÜZENLEME
            current_date = current_task.get('son_tarih', 'Belirtilmedi')
            print(f"\nMevcut Son Tarih: {current_date}")
            new_date = get_valid_date("Yeni Son Tarih (Değiştirmemek için sadece Enter'a basın): ", default_value=current_date)
            tasks[index]["son_tarih"] = new_date

            # 3. DURUM DÜZENLEME
            current_status_text = "Tamamlandı" if current_task.get("tamamlandi", False) else "Tamamlanmadı"
            print(f"\nMevcut Tamamlanma Durumu: {current_status_text}")
            update_status = input("Bu görev tamamlandı mı? (Evet için 'e', Hayır için 'h', Değiştirmemek için Enter): ").strip().lower()
            
            if update_status == 'e':
                tasks[index]["tamamlandi"] = True
            elif update_status == 'h':
                tasks[index]["tamamlandi"] = False
                
            save_tasks(tasks)
            print("\nGörev başarıyla güncellendi.")
        else:
            print("Hata: Geçersiz görev numarası!")
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")

def delete_task(tasks: list) -> None:
    """Belirtilen indexteki görevi listeden siler."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("\nSilmek istediğiniz görevin numarası: "))
        index = task_no - 1
        
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"\n'{deleted_task['metin']}' görevi silindi.")
        else:
            print("Hata: Geçersiz görev numarası!")
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")

def sort_tasks(tasks: list) -> None:
    """Görevleri öncelik seviyesine göre (Yüksek -> Normal -> Düşük) sıralar."""
    if not tasks:
        print("\nSıralanacak görev bulunmamaktadır.")
        return

    priority_order = {"Yüksek": 1, "Normal": 2, "Düşük": 3}
    tasks.sort(key=lambda x: priority_order.get(x.get("oncelik", "Normal"), 2))
    save_tasks(tasks)
    
    print("\n Görevler öncelik seviyesine göre (Yüksekten Düşüğe) başarıyla sıralandı!")
    list_tasks(tasks)

# --- UI LAYER (ARAYÜZ) ---
def main_menu():
    """Kullanıcı arayüzünü başlatan ve yönlendiren ana döngü."""
    clear_screen()
    print("To-Do List Uygulamasına Hoş Geldiniz!")
    tasks = load_tasks()

    while True:
        print("\n" + "="*25)
        print("TO-DO LIST UYGULAMASI")
        print("="*25)
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Görevleri Sırala (Önceliğe Göre)")
        print("6. Çıkış")
        print("="*25)
        
        choice = input("Seçiminiz (1-6): ").strip()
        clear_screen() # Her seçimden sonra ekranı temizler

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen 1 ile 6 arasında bir değer girin.")

# --- PROGRAM ENTRY POINT ---
if __name__ == "__main__":
    main_menu()