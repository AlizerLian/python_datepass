import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('1.jpg')  # 替换为你的图像路径
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV默认使用BGR格式，转换为RGB

# 获取原始图像的尺寸
height, width = image.shape[:2]

# 设置目标分辨率
new_width = width * 8  # 放大2倍
new_height = height * 8

# 使用双线性插值放大图像
bilinear_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# 使用双三次插值放大图像
bicubic_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

# 显示结果
plt.figure(figsize=(12, 8))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Bilinear Interpolation")
plt.imshow(bilinear_image)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Bicubic Interpolation")
plt.imshow(bicubic_image)
plt.axis('off')

plt.show()