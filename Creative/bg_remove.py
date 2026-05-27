from withoutbg import WithoutBG
model = WithoutBG.opensource()

def progress(value):
    print(f"Progress: {value * 100:.1f}%")
result = model.remove_background("img.jpg", progress_callback=progress)
result.save("img.png")