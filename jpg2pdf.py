import glob
from PIL import Image

# 读取图片文件
images = []
for file_name in glob.glob("input/*.jpg"):
    images.append(Image.open(file_name))

# 创建 PDF 文件
pdf_file_name = "images.pdf"
images[0].save(pdf_file_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

print("PDF created successfully!")