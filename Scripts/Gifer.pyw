Caption = Image.open(Frame)

Width = Pasted.size[0]
Percentage_ = (Width / float(Caption.size[0]))
Height_Size = int((float(Caption.size[1]) * float(Percentage_)))
Caption = Caption.resize((Width, Height_Size))

Captionized = Margin(Caption, Pasted.size[1])
Captionized.paste(Pasted)