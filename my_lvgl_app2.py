
# Initialize

import display_driver
import lvgl as lv

# CORE OBJECTS (the ones you will use most)
# 1. lv.obj
#The base of all objects.
#Everything inherits from this.
#Useful when you want:
#a simple container
#to group objects
#to create layout regions
# Create screen object
scr = lv.obj()
lv.screen_load(scr)
# Create a style
scr_style = lv.style_t()
scr_style.init()
# Set background color to blue:
scr_style.set_bg_color(lv.color_hex(0x3498db))
scr.add_style(scr_style, 0)

# 2. lv.label
# Shows text.
# Create label on screen
label = lv.label(scr)
label.set_text('Hello LGVL!')
label.align(lv.ALIGN.TOP_LEFT, 0, 0)
# Create a style
label_style = lv.style_t()
label_style.init()
label_style.set_bg_color(lv.color_hex(0xFF0000))  # Blue
label_style.set_bg_opa(lv.OPA.COVER)              # Fully visible
label_style.set_border_width(2)
label_style.set_border_color(lv.color_hex(0x000000))  # Black border
label_style.set_border_opa(lv.OPA.COVER)
label_style.set_radius(10)  # rounded corners
label_style.set_pad_all(10)
label_style.set_pad_left(5)
label_style.set_pad_top(8)
label_style.set_text_color(lv.color_hex(0xFFFFFF))  # white text
label.add_style(label_style, 0)

# 3. lv.button
# A clickable button.
# Create button on screen
btn1 = lv.button(scr)
btn1.align(lv.ALIGN.TOP_MID, 0, 0)
# Add label to button
btn1_label = lv.label(btn1)
btn1_label.set_text('This is Button1!')
btn1_label.center()  # Center label on the button
# Create style
btn1_style = lv.style_t()
btn1_style.init()
# Set style properties
btn1_style.set_bg_color(lv.color_hex(0x2ecc71))   # Green
btn1_style.set_bg_opa(lv.OPA.COVER)
btn1_style.set_radius(12)                         # Rounded corners
btn1_style.set_border_width(2)
btn1_style.set_border_color(lv.color_hex(0x1e8449))
btn1_style.set_pad_all(10)
# Apply to button
btn1.add_style(btn1_style, 0)
"""
# 4. lv.img
# Displays images (png, jpg, binary images).
img1 = lv.img(scr)
#img1.set_src("S:/my_image.bin")  # path depends on your platform
#img1.set_src(lv.SYMBOL.ADD)  # for built-in symbol
img1.set_src(lv.SYMBOL.WARNING)   # works for label-like symbols
img1.align(None, lv.ALIGN.BOTTOM_MID, 0, 0)  # center the image
"""
lbl = lv.label(scr)
lbl.set_text("+++")   # simple text works in simulator
lbl.align(lv.ALIGN.CENTER, 0, 0)

# 5. lv.line
# Draws straight lines (vector graphics).
points = [
    (0, 0),    # start point
    (50, 50),  # middle point
    (100, 0)   # end point
]
# Create the lne object
line1 = lv.line(scr)      # create line on the screen
line1.set_points(points, len(points))  # set points
line1.align(None, lv.ALIGN.BOTTOM_MID, 0, 0)  # center on screen
# Style the line
line_style = lv.style_t()
line_style.init()
line_style.set_line_width(3)           # thickness
line_style.set_line_color(lv.color_hex(0xFF0000))  # red color
line_style.set_line_rounded(True)      # rounded ends
line1.add_style(line_style, 0)         # apply style



"""
6. lv.arc

Circular arc — used for gauges, spinners, progress.

7. lv.bar

Horizontal or vertical bar (progress bar).

8. lv.slider

A bar that you can drag left/right.

9. lv.switch

Toggle switch (ON/OFF).

10. lv.checkbox

Selectable checkbox with text.

🔹 CONTAINER / LAYOUT OBJECTS
11. lv.obj (as a container)

You can place children inside and manage layout.

12. lv.table

Displays table-like data.

13. lv.tileview

A swipable multi-page view.

14. lv.tabview

Tabbed interface — like Android tabs.

15. lv.list

Scrollable list of items (like menu items).

16. lv.dropdown

Drop-down menu with items.

17. lv.roller

Picker wheel (like iOS date picker).

18. lv.canvas

Pixel-based drawing area (your own drawing).

🔹 ADVANCED / SPECIAL OBJECTS
19. lv.chart

Plotting data — similar to graphs.

20. lv.spinner

Animated loading indicator.

21. lv.calendar

Calendar widget.

22. lv.keyboard

On-screen keyboard.

23. lv.textarea

Text input box.

24. lv.msgbox

Pop-up dialog.

25. lv.scale

A gauge-like scale.

26. lv.colorwheel

Color picker.
"""