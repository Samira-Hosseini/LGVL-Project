
# Initialize

import display_driver
import lvgl as lv

# 1. Create a screen
scr = lv.obj()
lv.screen_load(scr)

# 2.1 Create a label on the screen
label = lv.label(scr)
# 2.2 Create a button on the screen
btn = lv.button(scr)
# 2.3 Create a lable on the button
lable_btn = lv.label(btn)

# 3.1. Set the text to label
label.set_text("Hello LVGL!")
# 3.2. Set the text to label of button
lable_btn.set_text("This is a button!")

# 4.1. Align lable to the center
label.align(lv.ALIGN.TOP_LEFT, 5, 5)
# 4.2. Align button to the center
btn.align(lv.ALIGN.TOP_MID, 0, 5)
#print(lv.scr_act().get_width(), lv.scr_act().get_height())

# 1. Create style
btn_style = lv.style_t()
btn_style.init()

# 2. Set style properties
btn_style.set_bg_color(lv.color_hex(0x2ecc71))   # Green
btn_style.set_bg_opa(lv.OPA.COVER)
btn_style.set_radius(12)                         # Rounded corners
btn_style.set_border_width(2)
btn_style.set_border_color(lv.color_hex(0x1e8449))
btn_style.set_pad_all(10)

# 3. Apply to button
btn.add_style(btn_style, 0)


btn2 = lv.button(scr)
lable_btn2 = lv.label(btn2)
lable_btn2.set_text("This is another button!")
btn2.align(lv.ALIGN.CENTER, 0, 0)

btn2.add_style(btn_style, 0)


#5 Create a style
scr_style = lv.style_t()
scr_style.init()

#5.1 set background color to red:
scr_style.set_bg_color(lv.color_hex(0x3498db))
scr.add_style(scr_style, 0)


#5 Create a style
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










