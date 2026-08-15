# Nose-Controlled Mouse 🖱️👃

A Python project that lets you control your computer mouse using **nose movements** detected via webcam.  
The cursor moves with **super-high sensitivity**, inverted horizontally (right ↔ left), and only responds when your **mouth is closed**.

---

## 🚀 Features

- Tracks nose tip using FaceMesh (via `cvzone`).
- Moves mouse pointer instantly with **super-high sensitivity**.
- Inverted horizontal movement (move nose right → cursor left).
- Cursor freezes when mouth is open.
- Simple quit option (`q` key).

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
