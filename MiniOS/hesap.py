import math
import tkinter as tk
from tkinter import messagebox, ttk


class GelismisHesapMakinesi:

  def __init__(self, root):
    self.root = root
    self.root.title("Kutuk Efe - Gelişmiş Hesap Makinesi")
    self.root.geometry("420x680")
    self.root.config(bg="#1e1e2e")
    self.root.resizable(False, False)

    # İfade değişkeni
    self.expression = ""
    self.input_text = tk.StringVar()

    # Arayüz Bileşenlerini Oluştur
    self.create_widgets()

  def create_widgets(self):
    # Üst Ekran (Giriş ve Sonuç Alanı)
    display_frame = tk.Frame(self.root, bg="#1e1e2e", bd=0)
    display_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=15, pady=15)

    self.input_field = tk.Entry(
        display_frame,
        font=("Consolas", 24, "bold"),
        textvariable=self.input_text,
        bg="#252538",
        fg="#ffffff",
        bd=0,
        justify=tk.RIGHT,
        insertbackground="white",
    )
    self.input_field.pack(fill=tk.BOTH, ipady=15)

    # Geçmiş / Log Paneli (Hataları ve geçmişi görmek için)
    history_frame = tk.Frame(self.root, bg="#1e1e2e")
    history_frame.pack(fill=tk.BOTH, padx=15, pady=5)

    self.history_label = tk.Label(
        history_frame,
        text="Geçmiş: İşlem bekleniyor...",
        font=("Arial", 10),
        bg="#1e1e2e",
        fg="#a6adc8",
        anchor="e",
    )
    self.history_label.pack(fill=tk.BOTH)

    # Tuş Takımı Paneli
    btn_frame = tk.Frame(self.root, bg="#1e1e2e")
    btn_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

    # Buton yerleşimi (Metin, Satır, Sütun, Arka Plan Rengi)
    buttons = [
        ("C", 0, 0, "#f38ba8"),
        ("(", 0, 1, "#45475a"),
        (")", 0, 2, "#45475a"),
        ("/", 0, 3, "#fab387"),
        ("7", 1, 0, "#313244"),
        ("8", 1, 1, "#313244"),
        ("9", 1, 2, "#313244"),
        ("*", 1, 3, "#fab387"),
        ("4", 2, 0, "#313244"),
        ("5", 2, 1, "#313244"),
        ("6", 2, 2, "#313244"),
        ("-", 2, 3, "#fab387"),
        ("1", 3, 0, "#313244"),
        ("2", 3, 1, "#313244"),
        ("3", 3, 2, "#313244"),
        ("+", 3, 3, "#fab387"),
        ("0", 4, 0, "#313244"),
        (".", 4, 1, "#313244"),
        ("√", 4, 2, "#89b4fa"),
        ("=", 4, 3, "#a6e3a1"),
        ("^", 5, 0, "#89b4fa"),
        ("Mod", 5, 1, "#89b4fa"),
        ("Pi", 5, 2, "#89b4fa"),
        ("Del", 5, 3, "#eba0ac"),
    ]

    for text, row, col, color in buttons:
      btn = tk.Button(
          btn_frame,
          text=text,
          font=("Arial", 14, "bold"),
          bg=color,
          fg="#1e1e2e" if color in ["#a6e3a1", "#fab387", "#89b4fa"] else "#fff",
          bd=0,
          activebackground="#585b70",
          activeforeground="#fff",
          command=lambda t=text: self.on_button_click(t),
      )
      btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    # Izgara ağırlıklarını ayarla (esnek butonlar için)
    for i in range(6):
      btn_frame.rowconfigure(i, weight=1)
    for j in range(4):
      btn_frame.columnconfigure(j, weight=1)

  def on_button_click(self, char):
    if char == "C":
      self.expression = ""
      self.input_text.set("")
      self.history_label.config(text="Geçmiş: Temizlendi")

    elif char == "Del":
      self.expression = self.expression[:-1]
      self.input_text.set(self.expression)

    elif char == "=":
      self.hesapla()

    elif char == "√":
      try:
        if self.expression:
          val = float(eval(self.expression))
          if val < 0:
            raise ValueError("Negatif sayıların karekökü alınamaz!")
          result = math.sqrt(val)
          self.history_label.config(text=f"√({self.expression}) = {result}")
          self.expression = str(result)
          self.input_text.set(self.expression)
        else:
          self.show_error("Önce bir sayı girmelisiniz!")
      except Exception as e:
        self.show_error(f"Karakök Hatası: {str(e)}")

    elif char == "Pi":
      self.expression += str(math.pi)
      self.input_text.set(self.expression)

    elif char == "^":
      self.expression += "**"
      self.input_text.set(self.expression)

    elif char == "Mod":
      self.expression += "%"
      self.input_text.set(self.expression)

    else:
      self.expression += str(char)
      self.input_text.set(self.expression)

  def hesapla(self):
    try:
      if not self.expression.strip():
        return

      temiz_ifade = self.expression
      sonuc = eval(temiz_ifade)

      if isinstance(sonuc, float):
        sonuc = round(sonuc, 10)

      self.history_label.config(text=f"{self.expression} = {sonuc}")
      self.expression = str(sonuc)
      self.input_text.set(self.expression)

    except ZeroDivisionError:
      self.show_error("Matematiksel Hata: Bir sayı sıfıra bölünemez!")
    except SyntaxError:
      self.show_error("Sözdizimi Hatası: Yanlış işlem veya eksik karakter!")
    except NameError:
      self.show_error("Geçersiz İfade: Tanımlanmayan karakter kullanıldı!")
    except Exception as e:
      self.show_error(f"Beklenmeyen Hata: {str(e)}")

  def show_error(self, message):
    self.history_label.config(text=f"HATA: {message}")
    messagebox.showerror("Hata Yakalandı", message)


if __name__ == "__main__":
  root = tk.Tk()
  app = GelismisHesapMakinesi(root)
  root.mainloop()
