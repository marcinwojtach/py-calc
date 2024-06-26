"""Application main file"""

from gui import GUI
from tkinter import StringVar


button_common_options = {
    "fg": "black",
    "bg": "white",
    "height": 1,
    "width": 6
}

calculator_gui = {
    1: [     "display"      ],
    2: [  7,   8,   9,   "+"],
    3: [  4,   5,   6,   "-"],
    4: [  1,   2,   3,   "*"],
    5: [0, "=", "/", "CLEAR"]
}

calculator_geometry = [360, 180]

class Main:
    def __init__(self):
        self.gui = GUI.gui("Calculator", f"{calculator_geometry[0]}x{calculator_geometry[1]}")
        self.expression = ""
        self.equation = StringVar()
        self._build_gui()

    def run(self):
        self.gui.mainloop()

    def _button_press(self, value):
        if value == "CLEAR":
            self._clear()
            return
        if value == "=":
            self._equals()
            return

        self.expression = self.expression + str(value)
        self.equation.set(self.expression)

    def _equals(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except ValueError:
            self.equation.set("Unexpected error occurred")
            self.expression = ""

    def _clear(self):
        self.expression = ""
        self.equation.set("")

    def _build_gui(self):
        for row in calculator_gui:
            for column, gui_element in enumerate(calculator_gui[row]):
                if gui_element == "display":
                    colspan = len(calculator_gui[row - 1] if row == len(calculator_gui) else calculator_gui[row + 1])
                    self.display = GUI.display(self.gui, self.equation, colspan, row, int(calculator_geometry[0] / 10))
                else:
                    GUI.button(
                        self.gui,
                        lambda val=gui_element: self._button_press(val),
                        gui_element,
                        { **button_common_options, **{ "row": row, "column": column } }
                    )

def boot():
    """Application boot"""

    print("Booting calculator up...")
    Main().run()


boot()
