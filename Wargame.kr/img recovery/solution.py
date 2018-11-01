from PIL import Image

one = Image.open("apngframe0.png")
another = Image.open("apngframe1.png")

# turn white pixels to transparent pixels.
another = another.convert("RGBA")
datas = another.getdata()

newData = []
for item in datas:
	if item[0] == 255 and item[1] == 255 and item[2] == 255:
		newData.append((255, 255, 255, 0))
	else:
		newData.append(item)
		
another.putdata(newData)
another.save("apngframe1.png", format="png")

another = Image.open("apngframe1.png")

# overlap one with another
combined = Image.new('RGBA', (105,105), (0, 0, 0, 0))
combined.paste(one, (0, 0))
combined.paste(another, (0, 0), mask=another)
combined.save("combined.png", format="png")