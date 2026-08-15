import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def scrape_meaning(word):
    """Scrape Vocabulary.com for word meaning"""
    try:
        url = f"https://www.vocabulary.com/dictionary/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            meaning_tag = soup.find("p", {"class": "short"})
            if meaning_tag:
                return meaning_tag.text.strip()
        return "Meaning not found."
    except Exception as e:
        return f"Error: {e}"

def search_word():
    word = entry.get().strip()
    if not word:
        messagebox.showwarning("Input Error", "Please enter a word!")
        return
    meaning = scrape_meaning(word)
    result_label.config(text=f"{word.capitalize()}:\n{meaning}")

# Tkinter UI
root = tk.Tk()
root.title("📖 Real-Time Dictionary")
root.geometry("600x400")
root.config(bg="#1e1e2f")

title_label = tk.Label(root, text="📖 Real-Time Dictionary", 
                       font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2f")
title_label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 16), width=25, 
                 bg="#2e2e3f", fg="white", insertbackground="white")
entry.pack(pady=10)

search_btn = tk.Button(root, text="Search Meaning", command=search_word,
                       font=("Helvetica", 14, "bold"), bg="#39FF14", fg="black")
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="white", 
                        bg="#1e1e2f", wraplength=500, justify="left")
result_label.pack(pady=20)

root.mainloop()
