from fastdtw import fastdtw
import matplotlib.pyplot as plt
# グラフを横長固定（お好みで）
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 10, 6
# データ作成
from numpy.random import *


seed(100)
rand()

a = list(randint(0, 20, 30))
# bはaを少しだけずらしたデータにする
b = [0, 1, 10, 4] + a
print (type(a))

plt.plot(a, label="a")
plt.plot(b, label="b")
plt.legend()
plt.show()
distance, path = fastdtw(a, b)
distance

