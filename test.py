import cv2
from pylab import *
# 添加中文字体支持
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"C:\Windows\winsxs\amd64_microsoft-windows-font-truetype-simsun_31bf3856ad364e35_6.1.7600"
                            r".16385_none_56fe10b1895fd80b\simsun.ttc", size=14)

# 载入图像
im = cv2.imread('hashiqi.jpg')

# 颜色空间转换
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 显示原始图像
fig = plt.figure()
subplot(121)
plt.gray()
imshow(im)
title(u'彩色图', fontproperties=font)
axis('off')
# 显示灰度化图像
plt.subplot(122)
plt.gray()
imshow(gray)
title(u'灰度图', fontproperties=font)
axis('off')

show()
