import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))  #넘파이로 저장된 이미지 데이터를 PIL용 데이터 객체로 변환해야 한다.
    pil_img.show()
    
(x_train, t_train),(x_test,t_test)=load_mnist(flatten = True, normalize = False) #이미지는 1차원 넘파이 배열로 저장되어 있다.

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img=img.reshape(28,28) #이미지를 표시하기 위해서는 원래 형상인 28x28 크기로 다시 변형해야 한다.(형상을 바꿈)
print(img.shape)

img_show(img)