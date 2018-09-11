text = "X-DSPAM-Confidence:    0.8475";

atpos = text.find("    ")

result = float(text[atpos+4:])

print(result)
