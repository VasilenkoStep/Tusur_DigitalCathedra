print("Задача №6: Мир захватили левши")
text_list = ["left", "right", "left", "stop", "bright aright", "ok"]
for i in range((len(text_list))):
    if "right" in text_list[i]:
        text_list[i] = text_list[i].replace("right", "left")
print(text_list)



