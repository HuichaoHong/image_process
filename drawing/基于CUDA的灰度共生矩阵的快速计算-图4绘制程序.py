#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
x = np.linspace(0, 2 * np.pi, 6)
y1, y2,y3,y4= [1.8,5.2,9.3,8.3,9.0,9.0], [2.8,7.2,9.1,10.6,10.9,12.1],[2.5,5.7,8.0,8.8,8.8,9.0],[2.8,7.5,9.2,10.1,11.1,13.9]

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

#plt.title('CPU与GPU计算灰度共生矩阵运行加速比',fontproperties=zhfont1)
plt.ylabel('加速比',fontproperties=zhfont1)
plt.xlabel('图像尺寸（单位：像素）',fontproperties=zhfont1)
plt.plot(x, y1, marker='s',label='θ=0°,  d=1',)
plt.plot(x, y2,marker='o', label='θ=45°,d=1')
plt.plot(x, y3,marker='+', label='θ=0°,  d=4')
plt.plot(x, y4,marker='x', label='θ=45°,d=4')
plt.annotate(str(1.8),xy=(0,1.8-0.2))
#plt.annotate(str(2.8),xy=(0,2.8))
plt.annotate(str(2.5),xy=(0,2.5-0.3))
plt.annotate(str(2.8),xy=(0,2.8+0.2))


plt.annotate(str(5.2),xy=(1+0.2,5.2))
plt.annotate(str(7.2),xy=(1+0.2,7.2-0.5))
plt.annotate(str(2.5),xy=(1+0.2,5.7))
plt.annotate(str(7.5),xy=(1+0.2,7.5))

plt.annotate(str(9.3),xy=(2+0.4,9.3+0.2))
plt.annotate(str(9.1),xy=(2+0.4,9.1-0.4))
plt.annotate(str(8.0),xy=(2+0.4,8.0-0.2))
plt.annotate(str(9.2),xy=(2+0.4,9.2-0.1))


plt.annotate(str(8.3),xy=(3+0.6,8.3-0.1))
plt.annotate(str(10.6),xy=(3+0.6,10.6+0.1))
plt.annotate(str(8.8),xy=(3+0.6,8.8))
plt.annotate(str(10.1),xy=(3+0.6,10.1-0.4))

plt.annotate(str(9.0),xy=(4+0.9,9.0+0.2))
plt.annotate(str(12.1),xy=(4+0.9,10.9-0.4))
plt.annotate(str(8.8),xy=(4+0.9,8.8-0.3))
plt.annotate(str(11.1),xy=(4+0.9,11.1+0.1))

plt.annotate(str(9.0),xy=(5+1,9.0+0.2))
plt.annotate(str(12.1),xy=(5+1,11.5))
#plt.annotate(str(9.0),xy=(5+1,8.8-0.3))
plt.annotate(str(13.9),xy=(5+1,13.1+0.3))

group_labels = ['128×128', '256×256','512×512','1024×1024','2048×2048','4096×4096']
plt.xticks(x, group_labels, rotation=0)



plt.legend()
plt.show()