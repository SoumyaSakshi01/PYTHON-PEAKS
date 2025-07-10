# 🧮 CustomTkinter Calculator

This is a simple, elegant **desktop calculator app** built using **Python** and **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** — a modern UI framework built on top of Tkinter. It supports **basic arithmetic**, **percentage**, **floor division**, and **sign toggle**.

---

## 📸 Preview

> _A dark-themed calculator with round buttons, clean layout, and responsive design._

---

## 🚀 Features

- ✅ Basic operations: `+`, `-`, `*`, `/`
- 🧮 Extra operations: `%`, `//`, `+/-` (sign toggle)
- 🧼 Clear entry
- 🟰 Evaluate expression using `eval()`
- 💅 Custom rounded buttons with hover effect
- 🎨 Dark mode with light-colored display and modern fonts

---

## 🛠 Requirements

- Python `>=3.7`
- `customtkinter`  
  Install via pip:

  ```bash
  pip install customtkinter```
  
📂 File Structure
calculator
calc.py     # Main application file
README.md         # This documentation

▶️ How to Run
Clone the repo or copy the script.

Ensure customtkinter is installed.

Run the Python file:
python calc.py

🧠 Code Overview
ExportedApp class inherits from ctk.CTk (CustomTkinter window).

Entry widget acts as the calculator display.

Buttons created dynamically using a layout configuration list.

Functions:

_on_button_click: Appends character to display.

_evaluate: Computes result using eval().

_clear: Clears display.

_toggle_sign: Toggles sign of current input.

⚠️ Note
This calculator uses eval() to evaluate expressions, which is not secure for untrusted inputs. It is safe here as a local app.

📌 To Do (Optional)
 Add keyboard bindings

 Improve error handling with math-safe parsing

 Add scientific calculator features (sin, cos, log, etc.)

 Add themes or light mode toggle

🧑‍💻 Author
Made with ❤️ by [SOUMYA SAKSHI]
Let me know if you want to save this as a `.md` file or convert it into a GitHub-ready project!
