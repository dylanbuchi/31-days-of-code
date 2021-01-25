import tkinter as tk

MILES_TO_KM_VALUE = 1.60934


def create_screen(title):
    screen = tk.Tk()
    screen.title(title)
    screen.minsize(width=400, height=200)
    screen.config(padx=100, pady=20)
    return screen


def convert_miles_to_km(miles):
    return miles * MILES_TO_KM_VALUE


def clear_text_area(text_area):
    """clears input text area """
    text_area.delete(0, tk.END)


def click_calculate_button(result_label, text_area):
    try:
        miles = float(text_area.get())
    except Exception:
        text_area.delete(0, tk.END)
        return
    else:
        result = convert_miles_to_km(miles)
        result_label['text'] = f"{result:.2f}"


def main():
    screen = create_screen('Mile to Km')

    # text area
    text_area = tk.Entry(width=6)
    text_area.focus()
    text_area.grid(row=0, column=2, padx=20)

    # bind the enter key to the calculate button
    text_area.bind(
        "<Return>",
        lambda event: click_calculate_button(result_label, text_area))

    # bind the backspace key to the calculate button
    text_area.bind("<BackSpace>", lambda event: clear_text_area(text_area))

    # miles label
    miles_label = tk.Label(text="Mile")
    miles_label.grid(row=0, column=3)

    # converter result label
    result_label = tk.Label(text='0')
    result_label.grid(row=1, column=2)

    # calculate button
    calculate_button = tk.Button(
        text="Calculate",
        command=lambda: click_calculate_button(result_label, text_area))
    calculate_button.grid(row=2, column=2)

    # km label
    Km_label = tk.Label(text='Km')
    Km_label.grid(row=1, column=3)

    screen.mainloop()


if __name__ == "__main__":
    main()
