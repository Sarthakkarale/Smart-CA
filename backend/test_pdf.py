from pdf2image import convert_from_path

images = convert_from_path("new sid resume.pdf")

print(f"Pages: {len(images)}")

for i, image in enumerate(images):
    image.save(f"page_{i+1}.png")

print("PDF converted successfully!")