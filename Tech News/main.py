import requests
import tkinter as tk
from tkinter import ttk
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# --- Fetch Data Function ---
def fetch_data():
    global dev_articles, hn_stories, github_repos

    dev_response = requests.get("https://dev.to/api/articles?per_page=5")
    dev_articles = dev_response.json()

    hn_response = requests.get("https://hn.algolia.com/api/v1/search?tags=front_page")
    hn_stories = hn_response.json()["hits"][:5]

    github_url = "https://api.github.com/search/repositories?q=stars:>1000&sort=stars"
    github_response = requests.get(github_url, headers={"User-Agent": "MyDashboardApp"})
    github_repos = github_response.json()["items"][:5]

# --- Open Link ---
def open_link(url):
    webbrowser.open(url)

# --- Build Dashboard ---
def build_dashboard():
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Dev.to Tab
    dev_frame = tk.Frame(notebook)
    notebook.add(dev_frame, text="Dev.to Articles")
    for article in dev_articles:
        link = tk.Label(dev_frame, text=article['title'], fg="blue", cursor="hand2", wraplength=700, justify="left")
        link.pack(anchor="w")
        link.bind("<Button-1>", lambda e, url=article['url']: open_link(url))

    # Hacker News Tab
    hn_frame = tk.Frame(notebook)
    notebook.add(hn_frame, text="Hacker News")
    for story in hn_stories:
        link = tk.Label(hn_frame, text=story['title'], fg="blue", cursor="hand2", wraplength=700, justify="left")
        link.pack(anchor="w")
        link.bind("<Button-1>", lambda e, url=story['url']: open_link(url))

    # --- GitHub Tab with Chart ---
    gh_frame = tk.Frame(notebook)
    notebook.add(gh_frame, text="GitHub Repos")

    names = [repo["full_name"] for repo in github_repos]
    stars = [repo["stargazers_count"] for repo in github_repos]

    fig, ax = plt.subplots(figsize=(8, 6))  # bigger figure
    ax.barh(names, stars, color="skyblue")

    # Larger font sizes
    ax.set_title("Top GitHub Repos by Stars", fontsize=16)
    ax.set_xlabel("Stars", fontsize=14)
    ax.set_ylabel("Repositories", fontsize=14)

    # Increase tick label size
    ax.tick_params(axis="y", labelsize=12)
    ax.tick_params(axis="x", labelsize=12)

    # Adjust layout so labels fit
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=gh_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add scrollable list of repo names + URLs
    scroll_frame = tk.Frame(gh_frame)
    scroll_frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(scroll_frame)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(scroll_frame, yscrollcommand=scrollbar.set, font=("Arial", 12))
    for repo in github_repos:
        listbox.insert(tk.END, f"{repo['full_name']} ({repo['language']}) - {repo['html_url']}")
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=listbox.yview)

# --- Main Window ---
root = tk.Tk()
root.title("Mini Tech Dashboard")
root.geometry("900x600")

# Refresh Button
refresh_btn = tk.Button(root, text="Refresh Data", command=lambda: [fetch_data(), build_dashboard()])
refresh_btn.pack(pady=10)

# Initial Load
fetch_data()
build_dashboard()

root.mainloop()
