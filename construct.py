from tkinter import *

# a method to create multiple Labels
def construct_lables(window, texts, x, y, font, bg, fg, anchor, isBold=False, x_increment=0, y_increment=0):
    # let font be a list of all font attributes
    if type(font) != list:
        font = ["Inter", 10, 'normal']

    for text in texts:
        Label(
            window,
            text=text,
            bg=bg,
            fg=fg,
            font=(font[0], font[1], font[2] if isBold else ''),
            anchor=anchor
        ).place(x=x, y=y)
        y += y_increment
        x += x_increment


# a method to create multiple Radiobuttons
def construct_radio_buttons(window, texts, x, y, font, bg, fg, anchor, x_increment=0, y_increment=0):
    for text in texts:
        Radiobutton(
            window,
            text=text,
            bg=bg,
            fg=fg,
            font=font,
            anchor=anchor
        ).place(x=x, y=y)
        y += y_increment
        x += x_increment

        

def construct_buttons(window, texts, x, y, width, height, font, bg, fg, highlightbg, hightlight_thickness, bwidth, anchor, x_increment=0, y_increment=0):
    buttons = []
    if type(font) != list:
        font = ["Inter", 10, 'normal']
    for text in texts:
        label = Label(
            window,
            text=text,
            bg=bg,
            width=width,
            height=height,
            fg=fg,
            font=font,
            borderwidth=bwidth,
            highlightthickness=hightlight_thickness,
            highlightbackground=highlightbg, 
            anchor=anchor,
        )
        label.place(x=x, y=y)
        y += y_increment
        x += x_increment

        buttons += [label]
    return buttons