import decoders
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(columnspan=20, rowspan=20)

my_data = tk.StringVar()

# tk.Label()
read_text_box = tk.Entry(root, textvariable=my_data)
read_text_box.grid(column=0, row=1,ipadx=200,ipady=10)


def decode_me():
    # Encoders
    data = my_data.get()
    url_data = decoders.decode_Url(data)
    base64_data = decoders.base64_Decode(data)
    base32_data = decoders.base32_Decode(data)
    base16_data = decoders.base16_Decode(data)

    # URL Decoder
    title = tk.Label(root, text="Url Decoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=3)
    text_url_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_url_de.insert(1.0, url_data)
    text_url_de.grid(column=1, row=3)

    # Base64
    title = tk.Label(root, text="Base64 Decoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=4)
    text_base64_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_base64_de.insert(1.0, base64_data)
    text_base64_de.grid(column=1, row=4)

    # Base32
    title = tk.Label(root, text="Base32 Decoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=5)
    text_base32_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_base32_de.insert(1.0,base32_data)
    text_base32_de.grid(column=1, row=5)

    # Base16
    title = tk.Label(root, text="Base16 Decoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=6)
    text_base16_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_base16_de.insert(1.0, base16_data)
    text_base16_de.grid(column=1, row=6)


def encode_me():
    data = my_data.get()
    url_data = decoders.encode_Url(data)
    base64_data = decoders.base64_Encode(data)
    base32_data = decoders.base32_Encode(data)
    base16_data = decoders.base16_Encode(data)

    title = tk.Label(root, text="Url Encoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=3)
    text_url_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_url_de.insert(1.0, url_data)
    text_url_de.grid(column=1, row=3)

    # Base64
    title = tk.Label(root, text="Base64 Encoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=4)
    text_base64_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_base64_de.insert(1.0, base64_data)
    text_base64_de.grid(column=1, row=4)

    # Base32
    title = tk.Label(root, text="Base32 Encoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=5)
    text_base32_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_base32_de.insert(1.0, base32_data)
    text_base32_de.grid(column=1, row=5)

    # Base16
    title = tk.Label(root, text="Base16 Encoded data", font="Raleway")
    title.grid(columnspan=1, column=0, row=6)
    text_base16_de = tk.Text(root, height=2, width=70, padx=5, pady=5)
    text_base16_de.insert(1.0, base16_data)
    text_base16_de.grid(column=1, row=6)


# Button for Decode
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:decode_me(), font="Raleway", bg="#20bebe", fg="white", height=0, width=10)
browse_text.set("Decode")
browse_btn.grid(column=1, row=1)


# Button for Encode
browse_text_2 = tk.StringVar()
browse_btn_2 = tk.Button(root, textvariable=browse_text_2,command=lambda:encode_me(), font="Raleway", bg="#20bebe", fg="white", height=0, width=10)
browse_text_2.set("Encode")
browse_btn_2.grid(column=2, row=1)


canvas = tk.Canvas(root, width=600, height=200)
canvas.grid(columnspan=3)

root.mainloop()

