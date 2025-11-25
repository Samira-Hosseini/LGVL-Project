

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
tab7 = tv.add_tab("CALKEY")
tab8 = tv.add_tab("More2")
tab9 = tv.add_tab("SCALe")
# Create style
style_tabview = lv.style_t()
style_tabview.init()
style_tabview.set_bg_color(lv.color_hex(0xecf0f1))
tv.add_style(style_tabview, 0)

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
#arc.set_value(60)
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
bar1 = lv.bar(tab1)
bar1.set_value(60, lv.ANIM.ON)
bar1.align(lv.ALIGN.BOTTOM_MID, 0, 0)
# Create Style
style_bar = lv.style_t()
style_bar.init()
style_bar.set_bg_color(lv.color_hex(0x95a5a6))
style_bar.set_bg_opa(lv.OPA._50)
style_bar.set_radius(5)
bar1.add_style(style_bar, 0)

# 8. lv.slider
# A bar that you can drag left/right.
slider1 = lv.slider(tab2)
slider1.set_size(150, 10)
slider1.align(lv.ALIGN.TOP_RIGHT, 0, 0)
slider1.set_value(50, lv.ANIM.OFF)
# Create Style
style_slider = lv.style_t()
style_slider.init()
style_slider.set_bg_color(lv.color_hex(0x34495e))
style_slider.set_radius(5)
slider1.add_style(style_slider, 0)

# 9. lv.switch
# Toggle switch (ON/OFF).
switch1 = lv.switch(tab2)
switch1.align(lv.ALIGN.TOP_LEFT, 0, 20)
# Create Style
style_switch = lv.style_t()
style_switch.init()
style_switch.set_bg_color(lv.color_hex(0x1abc9c))
switch1.add_style(style_switch, 0)

# 10. lv.checkbox
# Selectable checkbox with text.
cb1 = lv.checkbox(tab2)
cb1.set_text("Accept?")
cb1.align(lv.ALIGN.BOTTOM_RIGHT, 0, 0)
# Craete Style
style_cb = lv.style_t()
style_cb.init()
style_cb.set_text_color(lv.color_hex(0x8e44ad))
cb1.add_style(style_cb, 0)

# 🔹 CONTAINER / LAYOUT OBJECTS
# 11. lv.obj (as a container)
cont1 = lv.obj(tab2)
cont1.set_size(120, 80)
cont1.align(lv.ALIGN.RIGHT_MID, 0, 0)
# Create Style
style_cont = lv.style_t()
style_cont.init()
style_cont.set_bg_color(lv.color_hex(0xd35400))
style_cont.set_radius(10)
cont1.add_style(style_cont, 0)
# You can place children inside and manage layout.

# 12. lv.table
# Displays table-like data.
table1 = lv.table(tab2)
table1.set_size(250, 150)
table1.align(lv.ALIGN.BOTTOM_LEFT, 0, 0)
# Set content
table1.set_cell_value(0, 0, "Name")
table1.set_cell_value(0, 1, "Age")
table1.set_cell_value(1, 0, "Sam")
table1.set_cell_value(1, 1, "28")
# Create Style
style_table = lv.style_t()
style_table.init()
style_table.set_text_color(lv.color_hex(0x16a085))
table1.add_style(style_table, 0)

# 13. lv.tileview
# A swipable multi-page view.
tileview1 = lv.tileview(tab3)
# Create 2 tiles
tile1 = lv.obj(tileview1)
tile1.set_size(240, 240)
tile1.set_style_bg_color(lv.palette_main(lv.PALETTE.BLUE), 0)
tile2 = lv.obj(tileview1)
tile2.set_size(240, 240)
tile2.set_style_bg_color(lv.palette_main(lv.PALETTE.RED), 0)
# Position tiles (next to each other)
tile2.set_pos(240, 0)   # swipe horizontally
# Create Style
style_tileview = lv.style_t()
style_tileview.init()
style_tileview.set_bg_color(lv.color_hex(0x7f8c8d))
tileview1.add_style(style_tileview, 0)

# 14. lv.tabview
# Tabbed interface — like Android tabs.
# tabs = lv.tabview(scr)
# tab1 = tabs.add_tab("One")
# tab2 = tabs.add_tab("Two")
# label = lv.label(tab1)
# label.set_text("Page One")

# 15. lv.list
# Scrollable list of items (like menu items).
list1 = lv.list(tab4)
list1.set_size(150, 100)
list1.add_text("Menu")
list1.add_button(None, "Item 1")
list1.add_button(None, "Item 2")
list1.align(lv.ALIGN.TOP_RIGHT, 0, 0)
# Create Style
style_list = lv.style_t()
style_list.init()
style_list.set_bg_color(lv.color_hex(0xe74c3c))
list1.add_style(style_list, 0)

# 16. lv.dropdown
# Drop-down menu with items.
dd1 = lv.dropdown(tab4)
dd1.set_options("Apple\nBanana\nCherry")
dd1.align(lv.ALIGN.TOP_LEFT, 0, 30)
# Create Style
style_dd = lv.style_t()
style_dd.init()
style_dd.set_bg_color(lv.color_hex(0x3498db))
dd1.add_style(style_dd, 0)

# 17. lv.roller
# Picker wheel (like iOS date picker).
roller1 = lv.roller(tab4)
roller1.set_options("One\nTwo\nThree", lv.roller.MODE.NORMAL)
roller1.align(lv.ALIGN.TOP_LEFT, 0, 60)
# Create Style
style_roller = lv.style_t()
style_roller.init()
style_roller.set_text_color(lv.color_hex(0x2c3e50))
roller1.add_style(style_roller, 0)

# 18. lv.canvas
#Pixel-based drawing area (your own drawing).
# canvas1 = lv.canvas(scr)
# canvas1.set_buffer(bytearray(200*200*4), 200, 200, lv.COLOR_FORMAT.ARGB8888)
# canvas1.align(lv.ALIGN.CENTER, 0, 0)
# Create Style
# style_canvas = lv.style_t()
# style_canvas.init()
# style_canvas.set_bg_color(lv.color_hex(0x9b59b6))
# canvas1.add_style(style_canvas, 0)

# 🔹 ADVANCED / SPECIAL OBJECTS
# 19. lv.chart
# Plotting data — similar to graphs.
chart1 = lv.chart(tab5)
chart1.set_size(240, 150)
chart1.align(lv.ALIGN.TOP_RIGHT, -10, 10)
# Set point count
chart1.set_point_count(10)
# Add a line series
ser = chart1.add_series(lv.palette_main(lv.PALETTE.RED), lv.chart.TYPE.LINE)
# Add data values
chart1.set_next_value(ser, 10)
chart1.set_next_value(ser, 30)
chart1.set_next_value(ser, 20)
chart1.set_next_value(ser, 40)
chart1.set_next_value(ser, 15)
# Create Style
style_chart = lv.style_t()
style_chart.init()
style_chart.set_bg_color(lv.color_hex(0x34495e))
chart1.add_style(style_chart, 0)

# 20. lv.spinner
# Animated loading indicator.
spinner1 = lv.spinner(tab6)
spinner1.set_size(80, 80)
spinner1.align(lv.ALIGN.CENTER, 0, 0)
# Create Style
style_spinner = lv.style_t()
style_spinner.init()
style_spinner.set_line_color(lv.color_hex(0xe74c3c))
spinner1.add_style(style_spinner, 0)

# 21. lv.calendar
# Calendar widget.
calendar1 = lv.calendar(tab7)
calendar1.set_size(220, 220)
calendar1.align(lv.ALIGN.CENTER, 0, 0)
# Create Style
style_cal = lv.style_t()
style_cal.init()
style_cal.set_bg_color(lv.color_hex(0x1abc9c))
calendar1.add_style(style_cal, 0)


# 22. lv.keyboard
# On-screen keyboard.
kb1 = lv.keyboard(tab7)
kb1.align(lv.ALIGN.BOTTOM_MID, 0, 0)
# Create Style
style_kb = lv.style_t()
style_kb.init()
style_kb.set_bg_color(lv.color_hex(0x2c3e50))
kb1.add_style(style_kb, 0)

# 23. lv.textarea
# Text input box.
ta1 = lv.textarea(tab8)
ta1.set_placeholder_text("Type here...")
ta1.align(lv.ALIGN.TOP_LEFT, 0, 100)
# Create Style
style_ta = lv.style_t()
style_ta.init()
style_ta.set_bg_color(lv.color_hex(0xecf0f1))
style_ta.set_text_color(lv.color_hex(0x34495e))
ta1.add_style(style_ta, 0)

# 24. lv.msgbox
# Pop-up dialog.
# Simulated message box
mb = lv.obj(tab8)
mb.set_size(200, 100)
#mb.center()
mb.align(lv.ALIGN.TOP_MID, 0, -5)
# Style for the box
style_mb = lv.style_t()
style_mb.init()
style_mb.set_bg_color(lv.color_hex(0xe67e22))
style_mb.set_radius(8)
mb.add_style(style_mb, 0)
# Add text
lbl = lv.label(mb)
lbl.set_text("Hello!\nThis is a message box.")
lbl.center()
# Add close button
btn_close = lv.button(mb)
btn_close.set_size(60, 30)
btn_close.align(lv.ALIGN.BOTTOM_MID, 0, -5)
lbl_btn = lv.label(btn_close)
lbl_btn.set_text("Close")
lbl_btn.center()


# 25. lv.scale
# A gauge-like scale.
scale1 = lv.scale(tab9)
scale1.set_size(200, 200)
scale1.align(lv.ALIGN.TOP_RIGHT, 0, 0)
scale1.set_range(0, 100)
#scale.set_value(75)
scale1.set_value(30, lv.ANIM.OFF)
# Create Style
style_scale = lv.style_t()
style_scale.init()
style_scale.set_line_color(lv.color_hex(0x2980b9))
scale1.add_style(style_scale, 0)
 
# 26. lv.colorwheel
# Color picker.
# cw = lv.colorwheel(scr)
# cw.set_size(200, 200)
# cw.align(lv.ALIGN.CENTER, 0, 0)
# Create Style

