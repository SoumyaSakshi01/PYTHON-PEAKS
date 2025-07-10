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
  pip install customtkinter
  
#📂 File Structure<br>
CALCULATOR<br>
calc.py     # Main application file<br>
README.md         # This documentation<br>
<br>
#▶️ How to Run<br>
Clone the repo or copy the script.<br>
Ensure customtkinter is installed.<br>
Run the Python file:
python calc.py
<br>
#🧠 Code Overview<br>
ExportedApp class inherits from ctk.CTk (CustomTkinter window).<br>
Entry widget acts as the calculator display.<br>
Buttons created dynamically using a layout configuration list.<br>
<br>
Functions:<br>
_on_button_click: Appends character to display.<br>
_evaluate: Computes result using eval().<br>
_clear: Clears display.<br>
_toggle_sign: Toggles sign of current input.<br>
<br>
#⚠️ Note<br>
This calculator uses eval() to evaluate expressions, which is not secure for untrusted inputs. It is safe here as a local app.<br>
<br>
🧑‍💻 Author<br>
Made with ❤️ by [SOUMYA SAKSHI]<br>
