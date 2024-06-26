from tkinter import *

class GUI:
    @staticmethod
    def gui(title, geometry):
        """
        Builds the main window

        Args:
            title (String): Title of the window
            geometry (string): Geometry of the window
        """

        gui = Tk()
        gui.title(title)
        gui.geometry(geometry)
        return gui

    @staticmethod
    def display(gui, textvariable, columnspan, row, width):
        """
        Builds a display

        Args:
            gui (GUI): the main window
            textvariable (StringVar): the variable to be displayed
            columnspan (int): the number of columns in the display
            row (int): the number of rows in the display
            width (int): the width of the display
        """

        display = Label(
            gui,
            textvariable=textvariable,
            width=width,
            height=2,
            borderwidth=1,
            relief="solid",
            anchor="e",
            padx=5,
        )
        display.grid(columnspan=columnspan, row=row, padx=5, pady=10)
        return display

    @staticmethod
    def button(gui, command, text, options):
        """
        Builds a button

        Args:
            text (str): The text to display
            command (function): A command callback function
            options (dict): A dictionary of options
        """

        button = Button(
            gui,
            command=command,
            text=text,
            fg=options["fg"],
            bg=options["bg"],
            height=options["height"],
            width=options["width"]
        )

        button.grid(row=options["row"], column=options["column"])

        return button
