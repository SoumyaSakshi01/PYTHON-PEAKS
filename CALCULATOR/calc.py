import customtkinter as ctk
import sys

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Error in {func.__name__}: {str(e)}')
            sys.exit(1)
    return wrapper

class ExportedApp(ctk.CTk):
    @handle_error
    def __init__(self):
        super().__init__()
        self._initialize_widgets()
        self._create_widgets()
        self._place_widgets()

    @handle_error
    def _initialize_widgets(self):
        self.title('Calculator')
        self.geometry('700x800')
        self.resizable(1, 1)
        ctk.set_appearance_mode('dark')
        ctk.set_widget_scaling(1.0)

        # Widget placeholders
        self.widget_d99e18c7 = None
        self.buttons = {}

    @handle_error
    def _create_widgets(self):
        # Display
        self.widget_d99e18c7 = ctk.CTkEntry(self, width=620, height=100, font=('Inter', 30),
                                            fg_color='#c9f1f5', text_color='black', border_width=0,
                                            corner_radius=19, bg_color="#015053")
        self.widget_d99e18c7.place(x=40, y=30)

        # Button layout config: text, x, y
        buttons_config = [
            ('C', 40, 180), ('+/-', 203, 180), ('+', 529, 180), ('=', 366, 180),
            ('1', 40, 300), ('2', 203, 300), ('3', 366, 300), ('-', 529, 300),
            ('4', 40, 420), ('5', 203, 420), ('6', 366, 420), ('*', 529, 420),
            ('7', 40, 540), ('8', 203, 540), ('9', 366, 540), ('/', 530, 540),
            ('0', 40, 660), ('.', 203, 660), ('%', 366, 660), ('//', 529, 660),
        ]

        for text, x, y in buttons_config:
            btn = ctk.CTkButton(self, text=text, width=111, height=70, fg_color='#04adbb',
                                hover_color='#80ffff', text_color='black', border_width=0,
                                corner_radius=26, font=('Inter', 26), bg_color="#002A2A")
            btn.place(x=x, y=y)
            self.buttons[text] = btn

        # Assign commands
        for char in '0123456789.+-*/%//':
            self.buttons[char].configure(command=lambda ch=char: self._on_button_click(ch))

        self.buttons['C'].configure(command=self._clear)
        self.buttons['='].configure(command=self._evaluate)
        self.buttons['+/-'].configure(command=self._toggle_sign)

    @handle_error
    def _place_widgets(self):
        pass  # Already placed in _create_widgets

    def _on_button_click(self, value):
        current = self.widget_d99e18c7.get()
        self.widget_d99e18c7.delete(0, "end")
        self.widget_d99e18c7.insert(0, current + str(value))

    def _clear(self):
        self.widget_d99e18c7.delete(0, "end")

    def _evaluate(self):
        expression = self.widget_d99e18c7.get()
        try:
            result = str(eval(expression))
            self.widget_d99e18c7.delete(0, "end")
            self.widget_d99e18c7.insert(0, result)
        except Exception:
            self.widget_d99e18c7.delete(0, "end")
            self.widget_d99e18c7.insert(0, "Error")

    def _toggle_sign(self):
        text = self.widget_d99e18c7.get()
        if text:
            try:
                if text.startswith("-"):
                    self.widget_d99e18c7.delete(0, "end")
                    self.widget_d99e18c7.insert(0, text[1:])
                else:
                    self.widget_d99e18c7.delete(0, "end")
                    self.widget_d99e18c7.insert(0, "-" + text)
            except Exception:
                self.widget_d99e18c7.delete(0, "end")
                self.widget_d99e18c7.insert(0, "Error")

if __name__ == '__main__':
    app = ExportedApp()
    app.mainloop()

