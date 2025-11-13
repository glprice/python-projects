import streamlit as st

# ----------------------------
# Data / helper functions
# ----------------------------

abc = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar_encoder(offset, code):
    msg = []
    for letter in code:
        if letter.lower() in abc:
            shifted = abc[(abc.index(letter.lower()) - offset) % 26]
            msg.append(shifted if letter.islower() else shifted.upper())
        else:
            msg.append(letter)

    return "".join(msg)


def caesar_decoder(offset, code):
    msg = []
    for letter in code:
        if letter.lower() in abc:
            shifted = abc[(abc.index(letter.lower()) + offset) % 26]
            msg.append(shifted if letter.islower() else shifted.upper())
        else:
            msg.append(letter)

    return "".join(msg)


def vignere_encoder(key, code):
    offsets = [abc.index(i) for i in key]
    msg = []
    key_index = 0
    for letter in code:
        if letter.lower() in abc:
            shift = offsets[key_index % len(offsets)]
            shifted = abc[(abc.index(letter.lower()) - shift) % 26]
            msg.append(shifted if letter.islower() else shifted.upper())
            key_index += 1
        else:
            msg.append(letter)
    return "".join(msg)


def vignere_decoder(key, code):
    offsets = [abc.index(i) for i in key]
    msg = []
    key_index = 0
    for letter in code:
        if letter.lower() in abc:
            shift = offsets[key_index % len(offsets)]
            shifted = abc[(abc.index(letter.lower()) + shift) % 26]
            msg.append(shifted if letter.islower() else shifted.upper())
            key_index += 1
        else:
            msg.append(letter)
    return "".join(msg)


# ----------------------------
# Streamlit app layout
# ----------------------------

st.set_page_config(page_title="Cipher Encoder/Decoder", page_icon="🔐")

st.title("🔐 Caesar / Vigenère Cipher Tool")
st.write("Encode or decode messages using a **Caesar** or **Vigenère** cipher.")

# Cipher choice
cipher = st.radio(
    "Choose your cipher:",
    ("Caesar", "Vigenere"),
    horizontal=True,
)

# Mode choice
mode = st.radio(
    "Mode:",
    ("Encode", "Decode"),
    horizontal=True,
)

st.write("---")

# Shared message input
message = st.text_area(
    "Enter your message:",
    height=150,
    placeholder="Type your message here...",
)

result = ""

if cipher == "Caesar":
    # Offset for Caesar
    offset_input = st.text_input(
        "Enter offset (integer):",
        value="3",
        help="Positive integer",
    )

    if st.button("Run Caesar"):
        try:
            offset = int(offset_input)
            if mode == "Encode":
                result = caesar_encoder(offset, message)
            else:
                result = caesar_decoder(offset, message)
        except ValueError:
            st.error("Offset must be an integer.")

else:  # Vigenere
    key = st.text_input(
        "Enter key (letters only):",
        value="key",
        help="Vigenère key; letters only, converted to lowercase.",
    )

    if st.button("Run Vigenère"):
        if not key:
            st.error("Key cannot be empty.")
        elif not key.isalpha():
            st.error("Key must contain letters only (a-z).")
        else:
            key_lower = key.lower()
            if mode == "Encode":
                result = vignere_encoder(key_lower, message)
            else:
                result = vignere_decoder(key_lower, message)

st.write("---")

st.subheader("Result:")
if result:
    st.code(result, language="text")
else:
    st.write("Your output will appear here after you run the cipher.")
