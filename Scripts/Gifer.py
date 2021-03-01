Caption = Image.open(get(Config()["Image"]["URL"], stream = True).raw)

Width = Pasted.size[0]
Percentage = (Width / float(Caption.size[0]))
Height_Size = int((float(Caption.size[1]) * float(Percentage)))
Caption = Caption.resize((Width, Height_Size), PIL.Image.LANCZOS)

Captionized = Margin(Caption, Pasted.size[1])
Captionized.paste(Pasted)