

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
#scr_style.set_bg_color(lv.color_hex(0x3498db))
scr.add_style(scr_style, 0)

# Create tabview
tv = lv.tabview(scr)
# tv.set_size(420, 300)
tv.set_size(lv.pct(100), lv.pct(100)) # Maximum size of display 480, 320
tv.align(lv.ALIGN.TOP_LEFT, 0, 0)
# Add tabs
tab1 = tv.add_tab("Home")
tab2 = tv.add_tab("Settings")
tab3 = tv.add_tab("About")
tab4 = tv.add_tab("other")
tab5 = tv.add_tab("Advanced")
tab6 = tv.add_tab("More")
tab7 = tv.add_tab("More2")

# 2. lv.label
# Shows text.
# Create label on screen
label = lv.label(tab1)
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
btn1 = lv.button(tab1)
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
lbl = lv.label(tab1)
lbl.set_text("+++")   # simple text works in simulator
lbl.align(lv.ALIGN.CENTER, 0, 0)

"""
# 5. lv.line
# Draws straight lines (vector graphics).
"""
# 6. lv.arc
# Create an arc object
arc = lv.arc(tab1)         # create an arc on the screen
arc.set_size(150, 100)    # width, height
arc.align(lv.ALIGN.CENTER, 50, 50)  # center it
# Set the angles
# Angles are in degrees, from 0 to 360.
# set_angles(start, end) sets where the arc starts and ends.
arc.set_angles(0, 270)  # draws a 3/4 circle
# Style the arc
arc_style = lv.style_t()
arc_style.init()
arc_style.set_line_width(10)                # thickness
arc_style.set_line_color(lv.color_hex(0xFF0000))  # red
arc_style.set_line_rounded(True)           # rounded ends
arc.add_style(arc_style, 0)                # part 0 = main line
# background arc
bg_style = lv.style_t()
bg_style.init()
bg_style.set_line_width(10)
bg_style.set_line_color(lv.color_hex(0xCCCCCC))
arc.add_style(bg_style, 1)  # part 1 = background
"""
Circular arc — used for gauges, spinners, progress.
"""

# 7. lv.bar
#Horizontal or vertical bar (progress bar).
bar = lv.bar(tab1)
bar.set_value(60, lv.ANIM.ON)
bar.align(lv.ALIGN.BOTTOM_MID, 0, 0)

# 8. lv.slider
# A bar that you can drag left/right.
slider = lv.slider(tab2)
slider.align(lv.ALIGN.TOP_RIGHT, 0, 0)

# 9. lv.switch
# Toggle switch (ON/OFF).
sw = lv.switch(tab2)
sw.align(lv.ALIGN.TOP_LEFT, 0, 20)

# 10. lv.checkbox
# Selectable checkbox with text.
cb = lv.checkbox(tab2)
cb.set_text("Accept?")
cb.align(lv.ALIGN.BOTTOM_RIGHT, 0, 0)

# 🔹 CONTAINER / LAYOUT OBJECTS
# 11. lv.obj (as a container)
# You can place children inside and manage layout.
# 12. lv.table
# Displays table-like data.
table = lv.table(tab2)
table.set_size(150, 150)
table.align(lv.ALIGN.BOTTOM_LEFT, 0, 0)
# Set content
table.set_cell_value(0, 0, "Name")
table.set_cell_value(0, 1, "Age")
table.set_cell_value(1, 0, "Sam")
table.set_cell_value(1, 1, "28")

# 13. lv.tileview
# A swipable multi-page view.
tileview = lv.tileview(tab3)
# Create 2 tiles
tile1 = lv.obj(tileview)
tile1.set_size(240, 240)
tile1.set_style_bg_color(lv.palette_main(lv.PALETTE.BLUE), 0)
tile2 = lv.obj(tileview)
tile2.set_size(240, 240)
tile2.set_style_bg_color(lv.palette_main(lv.PALETTE.RED), 0)
# Position tiles (next to each other)
tile2.set_pos(240, 0)   # swipe horizontally

# 14. lv.tabview
# Tabbed interface — like Android tabs.
# tabs = lv.tabview(scr)
# tab1 = tabs.add_tab("One")
# tab2 = tabs.add_tab("Two")
# label = lv.label(tab1)
# label.set_text("Page One")

# 15. lv.list
# Scrollable list of items (like menu items).
lst = lv.list(tab4)
lst.add_text("Menu")
lst.add_button(None, "Item 1")
lst.add_button(None, "Item 2")
lst.align(lv.ALIGN.TOP_RIGHT, 0, 0)

# 16. lv.dropdown
# Drop-down menu with items.
dd = lv.dropdown(tab4)
dd.set_options("Apple\nBanana\nCherry")
dd.align(lv.ALIGN.TOP_LEFT, 0, 30)

# 17. lv.roller
# Picker wheel (like iOS date picker).
roller = lv.roller(tab4)
roller.set_options("One\nTwo\nThree", lv.roller.MODE.NORMAL)
roller.align(lv.ALIGN.TOP_LEFT, 0, 60)

# 18. lv.canvas
#Pixel-based drawing area (your own drawing).
# canvas = lv.canvas(scr)
# canvas.set_buffer(bytearray(200*200*4), 200, 200, lv.COLOR_FORMAT.ARGB8888)
# canvas.align(lv.ALIGN.CENTER, 0, 0)

# 🔹 ADVANCED / SPECIAL OBJECTS
# 19. lv.chart
# Plotting data — similar to graphs.
chart = lv.chart(tab5)
chart.set_size(240, 150)
chart.align(lv.ALIGN.TOP_RIGHT, -10, 10)
# Set point count
chart.set_point_count(10)
# Add a line series
ser = chart.add_series(lv.palette_main(lv.PALETTE.RED), lv.chart.TYPE.LINE)
# Add data values
chart.set_next_value(ser, 10)
chart.set_next_value(ser, 30)
chart.set_next_value(ser, 20)
chart.set_next_value(ser, 40)
chart.set_next_value(ser, 15)


# 20. lv.spinner
# Animated loading indicator.
spinner = lv.spinner(tab6)
spinner.set_size(80, 80)
spinner.align(lv.ALIGN.CENTER, 0, 0)

# 21. lv.calendar
# Calendar widget.
calendar = lv.calendar(tab7)
calendar.set_size(220, 220)
calendar.align(lv.ALIGN.CENTER, 0, 0)

# 22. lv.keyboard
# On-screen keyboard.
kb = lv.keyboard(tab7)
kb.align(lv.ALIGN.BOTTOM_MID, 0, 0)

# 23. lv.textarea
# Text input box.
ta = lv.textarea(tab7)
ta.set_placeholder_text("Type here...")
ta.align(lv.ALIGN.TOP_LEFT, 0, 100)

# 24. lv.msgbox
# Pop-up dialog.
msgbox = lv.msgbox(tab7)
msgbox.set_text("Hello!\nThis is a message box.")
msgbox.add_close_button()
msgbox.align(lv.ALIGN.CENTER, 0, 0)

# 25. lv.scale
# A gauge-like scale.
scale = lv.scale(tab7)
scale.set_size(200, 200)
scale.align(lv.ALIGN.CENTER, 0, 0)
scale.set_range(0, 100)
scale.set_value(75)
 
# 26. lv.colorwheel
# Color picker.
# cw = lv.colorwheel(scr)
# cw.set_size(200, 200)
# cw.align(lv.ALIGN.CENTER, 0, 0)
