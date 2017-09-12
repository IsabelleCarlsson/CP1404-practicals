"""
CP1404 Practical
Find hexadecimal equivalent of various colours
"""

HEXADECIMAL_COLOURS = {"aliceblue": "#f0f8ff", "blueviolet": "#8a2be2", "coral": "#ff7f50", "cornflowerblue": "#6495ed",
                       "darkgreen": "#006400", "greenyellow": "#adff2f", "indianred": "#cd5c5c", "khaki": "#f0e68c",
                       "lavender": "#e6e6fa", "lightslateblue": "#8470ff", "magenta": "#ff00ff"}

text_colour = input("Enter colour in text: ").lower()
while text_colour != "":
    if text_colour in HEXADECIMAL_COLOURS:
        print(text_colour, "is", HEXADECIMAL_COLOURS[text_colour])
    else:
        print("Invalid colour")
    text_colour = input("Enter colour in text: ").lower()
