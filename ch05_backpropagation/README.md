## 개요

- 앞 장에서 신경망의 가중치 매개변수의 기울기를 수치 미분을 사용해 구했다. 수치 미분은 단순하고 구현하기도 쉽지만 계산이 오래걸린다. 이번 장에서는 가중치 매개변수의 기울기를 효율적으로 구하는 '오차역전파법'을 배운다.

- 오차역전파법을 제대로 이해하는 방법에는 수식을 통한 방법, 계산 그래프를 통한 방법이 있다. 보통 전자 쪽이 일반적인 방법이지만 이번 장에서는 계산 그래프를 사용해서 '시각적'으로 이해하도록 설명한다.

## 5.1 계산그래프

- 계산 그래프는 계산 과정을 표현한 그래프로 복수의 노드와 에지로 표현된다.

### 5.1.1 계산 그래프로 풀다.

- 계산 그래프는 계산 과정을 노드와 화살표로 표현하는데 노드는 원으로 표기하고 원 안에 연산 내용을 적는다.
  - 곱셈만을 연산으로 생각할 수도 있기 때문에 곱하는 숫자를 원 밖에 표기할 수도 있다.

![5-1-1](images/5-1-1.png)

- 계산 그래프를 이용한 문제풀이는 다음과 같은 흐름으로 진행된다.
  - 1. 계산 그래프를 구성한다.
  - 2. 그래프에서 계산을 왼쪽에서 오른쪽으로 진행한다.

- 여기서 계산을 왼쪽에서 오른쪽으로 진행하는 것을 순전파, 오른쪽에서 왼쪽으로 진행하는 것을 역전파라고 하는데 이는 미분을 계산할 때 중요한 역할을 한다.

### 5.1.2 국소적 계산

- 계산 그래프는 '국소적 계산'을 전파함으로써 최종 결과를 얻는다.
  - 국소적이란 '자신과 직접 관계된 작은 범위'라는 뜻으로 국소적 계산은 결국 전체에서 어떤 일이 벌어지든 상관없이 자신과 관계된 정보만으로 결과를 출력한다.

![5-1-2](images/5-1-2.png)

- 위의 그래프에서는 복잡한 계산을 거쳐 여러 식품을 계산한 후 사과의 계산값을 더한다.
  - 여기서 계산은 '국소적' 계산이기 때문에 이전의 복잡한 계산이 어떻게 계산되었느냐를 상관할 필요 없이 자신과 관련한 계산만 신경쓰면 된다.
  - 이처럼 계산 그래프는 국소적 계산에 집중하기 때문에 단순하지만 그 결과를 전달함으로써 전체를 구성하는 복잡한 계산을 해낼 수 있다.

### 5.1.3 왜 계산 그래프로 푸는가?

- 계산 그래프의 이점은 '국소적 계산'이다. 또한 중간 계산 결과를 모두 보관할 수 있다는 장점이 있다.
- 또한 실제 계산 그래프를 사용하는 가장 큰 이유는 역전파를 통해 '미분'을 효율적으로 계산할 수 있다는 점에 있다.

![5-1-3](images/5-1-3.png)

- 여기서는 '사과 가격에 대한 지불 금액의 미분'같으 값을 역전파를 통해 구할 수 있다.
  - 사과가 1원 오르면 최종 금액은 2.2원 오른다는 뜻이다.

- 소비세에 대한 지불 금액의 미분이나 사과 개수에 대한 지불 금액의 미분도 같은 순서로 구할 수 있으며 중간까지 구한 미분 결과를 공유할 수 있어서 효율적이다.

## 5.2 연쇄법칙

- 역전파는 '국소적인 미분'을 순방향과는 반대로 전달하는데 이 원리는 '연쇄법칙'에 따른 것이다.

### 5.2.1 계산 그래프의 역전파

![5-2-1](images/5-2-1.png)

- 위 그림과 같이 신호 E에 노드의 국소적 미분을 곱한 후 다음 노드로 전달하여 역전파를 계산한다.
  - 여기서 말하는 국소적 미분은 순전파 때의 함수의 계산의 미분을 구한다는 뜻이며 이는 x에 대한 y의 미분이다.
  - 그리고 이 국소적인 미분을 상류에서 전달된 값에 곱해 앞쪽 노드로 전달하는 것이다.

### 5.2.2 연쇄법칙이란?

- 연쇄법칙을 설명하려면 합성 함수부터 시작한다.
  - 합성 함수란 여러 함수로 구성된 함수

- 합성 함수의 미분은 합성 함수를 구성하는 각 함수의 미분의 곱으로 나타낼 수 있다.
  - 예를 들어 x에 대한 z의 미분은 t에 대한 z의 미분과 x에 대한 t의 미분의 곱으로 나타낼 수 있는 것이다.

### 5.2.3 연쇄법칙과 계산 그래프

![5-2-2](images/5-2-2.png)

- 계산 그래프에 연쇄법칙을 적용한 것이다.
  - 국소적 미분을 하면 역전파에서 각 노드에서 바로 앞뒤 관계만 미분하게 된다.
  - 역전파를 진행하면 이것들을 계속 곱하게 되는데 그 결과 최종 출력을 처음 변수에 대해 미분한 값을 얻게 되는 것이다.
  - 결국에는 여러 국소적 미분을 연쇄법칙으로 연결해서 전체 미분값을 얻을 수 있다.

## 5.3 역전파

- 이번 절에서는 '+'와 'x'등의 연산을 예로 들어 역전파의 구조를 설명한다.

### 5.3.1 덧셈 노드의 역전파

- z=x+y라는 식을 대상으로 역전파를 살펴보자. - x에 대한 z의 미분, y에 대한 z의 미분 모두 1이 된다.
  ![5-3-1](images/5-3-1.png)
- 위와 같이 역전파는 상류에서 전해진 미분에 1을 곱하여 그대로 하류로 흘린다. 즉 덧셈 노드의 역전파는 입력된 값을 그대로 다음 노드로 전달한다.
  - 여기서 최종적으로 L이라는 값을 출력하는 큰 계산 그래프를 가정하기 때문에 z에 대한 L의 미분값을 전달한 것이다.

### 5.3.2 곱셈 노드의 역전파

- z=xy라는 식을 생각해 보자. - x에 대한 z의 미분은 y, y에 대한 z의 미분은 x이다.
  ![5-3-2](images/5-3-2.png)

- 곱셈 노드 역전파는 상류의 값에 순전파 때의 입력신호들을 '서로 바꾼 값'을 곱해서 하류로 보낸다.
  - 덧셈의 역전파와는 달리 곱셈의 역전파는 순방향 입력 신호의 값이 필요하다.
  - 따라서 곱셈 노드를 구현할 때는 순전파의 입력 신호를 변수에 저장해 둔다.

### 5.3.3 사과 쇼핑의 예

![5-3-3](images/5-3-3.png)

- 이 문제에서는 사과의 가격, 사과의 개수, 소비세라는 세 변수 각각이 최종 금액에 어떻게 영향을 주느냐를 풀었다.
- 다만 이 예에서 사과 가격과 소비세의 단위가 다르므로 주의

## 5.4 단순한 계층 구현하기

- 이번 절에서는 사과 쇼핑의 예를 파이썬으로 구현하는데, 곱셈노드는 MulLayer클래스, 덧셈 노드는 AddLayer클래스이다.

### 5.4.1 곱셈 계층

- 모든 계층은 forward() 순전파, backward() 역전파 공통 메서드를 갖도록 구현한다.

```python
class MulLayer:
    def __init__(self):
        self.x=None
        self.y=None
    def forward(self,x,y):
        self.x=x
        self.y=y
        out = x*y

        return out

    def backward(self,dout):
        dx=dout*self.y
        dy=dout*self.x

        return dx,dy
```

- 구현한 코드는 buy_apple.py에 있다.
- 여기서 왜 MulLayer()라는 클래스를 각각 다른 객체로 만들어서 사용할까?
  - 그 이유는 각 곱셈 노드가 본인의 입력값을 따로 기억해야 하기 때문이다.
  - forward() 순전파에서 입력값을 객체 내부에 저장하는데, 각 객체가 기억하는 값이 다르다.
  - 역전파에서는 이 저장된 값들을 이용해서 미분하는 것이다!
    - 만약 역전파가 필요 없다면 각각의 객체를 만들 필요는 없다.

### 5.4.2 덧셈 계층

```python
class AddLayer:
    def __init__(self):
        pass

    def forward(self,x,y):
        out=x+y
        return out

    def backward(self,dout):
        dx=dout*1
        dy=dout*1
        return dx,dy
```

- 구현한 코드는 buy_apple_orange.py에 있다.

## 5.5 활성화 함수 계층 구현하기

- 이제 계산 그래프를 신경망에 구현하는데, 여기에서는 신경망을 구성하는 층 각각을 클래스 하나로 구현한다.
- 우선 활성화 함수인 ReLU와 Sigmoid 계층을 구현한다.

### 5.5.1 ReLU 계층

- ReLU 수식에서 순전파 때의 입력인 x가 0보다 크면 역전파는 상류의 값을 그대로 하류로 흘리지만 순전파 때 x가 0이면 역전파 때는 하류로 신로를 보내지 않는다.(0을 보냄)

![5-5-1](images/5-5-1.png)

```python
class Relu:
  def __init__(self):
    self.mask = None

  def forward(self,x):
    self.mask = (x<=0)
    out = x.copy()
    out[self.mask]=0

    return out

  def backward(self,dout):
    dout[self.mask]=0
    dx=dout

    return dx
```

- ReLU 클래스는 mask라는 인스턴스 변수를 갖는다.
  - 이는 True/False로 구성된 넘파이 배열으로, 순전파 입력이 0이하인 인덱스는 True, 그 외는 False로 유지
    - 그러니까 이 self.mask에는 넘파이 배열이 들어간다. 그래서 out[self.mask]=0 이라는 것의 뜻은 self.mask가 True인 위치의 값을 0으로 바꾼다는 뜻.
  - 그래서 순전파 때 만들어둔 mask가 True이면 역전파때 이걸 사용해서 dout을 0으로 만드는 것
    - dout은 out과 별개의 배열이지만(그래서 완전히 값이 다르고 또 순전파때와 달리 양수 값이더라도) out으로 만들어진 self.mask를 역전파에 다시 써서 그대로 적용하는 것이다.

### 5.5.2 Sigmoid 계층

![5-5-2](images/5-5-2.png)

- 시그모이드 함수의 계산그래프는 위와 같다.
- exp노드는 y=exp(x) 계산을 수행하고, / 노드는 y=1/x 계산을 수행한다.

![5-5-3](images/5-5-3.png)

- 시그모이드 역전파의 흐름
  - /를 미분하면 -y^2 이 된다. 이를 상류에서 흘러온 값에 곱해서 하류로 전한다.
  - +는 그대로 전달
  - exp연산의 미분은 exp(x)이므로 이를 곱해서 전달한다. 여기서는 exp(-x)
  - x노드는 순전파 때의 값을 서로 바꿔서 곱하므로 여기에서는 -1을 곱한다.

- 간소화하면 다음과 같다.
  ![5-5-4](images/5-5-4.png)

- 위와 같이 사용하면 세세한 계산 없이 간단하게 입력과 출력에만 집중할 수 있다. 그리고 입력과 출력만으로 계산할 수 있다는 사실을 알 수 있다.
- 하지만 식을 더 간소화할 수 있다.
  ![5-5-5](images/5-5-5.png)
- 위와 같이 시그모이드 계층의 역전파는 순전파의 출력만으로 계산할 수 있다.

```python
class Sigmoid:
  def __init__(self):
    self.out = None

  def forward(self,x):
    out = sigmoid(x) #순전파 때의 출력을 out에 보관한 후 역전파 계산 때 그 값을 사용
    self.out = out
    return out

    def backward(self,dout):
      dx=dout*(1.0-self.out)*self.out
      return dx

```

## 5.6 Affine/Softmax 계층 구현하기

### 5.6.1 Affine 계층

- Affine 계층의 계산 그래프에서는 스칼라 대신 행렬이 흐른다.
  ![5-5-6](images/5-5-6.png)

- Affine 계층의 역전파를 계산 그래프로 나타내면 다음과 같다.
  ![5-5-7](images/5-5-7.png)

- X와 X를 미분한것, W와 W를 미분한 것은 같은 형상임에 주의하자.

### 5.6.2 배치용 Affine 계층

![5-5-8](images/5-5-8.png)

- 데이터 N개를 묶어 순전파 하는 경우(배치용 Affine 계층)
- 기존과 다른 부분은 입력인 X의 형상이 (N,2)가 된 것이다.
  - 역전파 때는 행렬의 형상에 주의하면 이전과 같이 도출할 수 있다.

- 편향을 더할 때에도 주의해야 하는데 순전파 때의 편향 덧셈음 각 데이터(N개의 데이터에 각각) 더해진다.
  - 예를 들어 N=2일때 이런식으로 두 데이터 각각의 계산 결과에 더해진다.

  ```python
  import numpy as np

  X_dot_W = np.array([[0,0,0], [10,10,10]])
  B = np.array([1,2,3])

  print(X_dot_W)
  print(X_dot_W + B)

  >>>
  [[ 0  0  0]
   [10 10 10]]
  [[ 1  2  3]
   [11 12 13]]
  ```

  - 역전파 때는 각 데이터의 역전파 값이 편향의 원소에 모여야 한다.

  ```python
  dY = np.array([[1,2,3],[4,5,6]])
  print(dY)
  dB = np.sum(dY, axis=0)
  print(dB)

  >>>
  [[1 2 3]
   [4 5 6]]
  [5 7 9]
  ```

  - 순전파에서 편향은 각각의 데이터에 들어가게 되며 이는 '하나의 편향'을 모든 데이터가 공유하는 것이라고 할 수 있다.
  - 그래서 역전파할 때는 편향이 손실함수에 미친 전체 영향을 구하려면 데이터 개수에 해당하는 만큼의 경로에서 오는 기울기를 합쳐야 한다.
    - 그리고 axis=0은 세로로 더하는 것

```python
class Affine:
  def __init__(self,W,b):
    self.W=W
    self.b=b
    self.x=None
    #가중치 편향과 매개변수의 미분
    self.dW=None
    self.db=None

  def forward(self,x):
    self.x=x
    out=np.dot(x,self.W)+self.b
    return out

  def backward(self,dout):
    dx=np.dot(dout,self.W.T) #넘파이 배열의 전치속성 T
    self.dW=np.dot(self.x.T,dout)
    self.db=np.sum(dout,axis=0)
    return dx

```

### 5.6.3 Softmax-with-Loss 계층

- 소프트맥스 함수는 입력 값을 정규화(출력의 합이 1이 되도록 변형)하려 출력한다. 손글씨 숫자 인식에서의 Softmax 계층의 출력은 다음과 같고, 손글씨 숫자가 10개니까 입력도 10개가 된다.

![5-6-1](images/5-6-1.png)

- 신경망에서는 학습과 추론을 둘 다 하는데
  - 추론할 때는 가장 높은 점수만 알면 되기 때문에 소프트맥스 함수를 거치기 전(정규화 되지 않은 상태)의 점수만 알아도 되고,
  - 다만 신경망을 학습할 때에는 소프트맥스 함수가 필요하다.

- Softmax-with-Loss 계층의 계산 그래프
  ![5-6-2](images/5-6-2.png)

- 간소화하면 다음과 같다.
  ![5-6-3](images/5-6-3.png)

- Softmax 계층
  - 입력(a1,a2,a3)을 정규화하여 (y1,y2,y3)를 출력한다.
- Cross Entropy Error 계층
  - Softmax의 출력과 정답레이블을 받고 이 데이터로 부터 손실 L을 출력(출력과 정답의 차분)
  - 역전파에서는 이 오차가 앞 계층에 전해지게 된다.

```python
class SoftmaxWithLoss:
  def __init__(self):
    self.loss=None
    self.y=None
    self.t=None

  def forward(self,x,t):
    self.t=t
    self.y=softmax(x)
    self.loss=crosss_entropy_error(self.y,self.t)

    return self.loss

  def backward(self,dout=1):
    batch_size=self.t.shape[0]
    if self.t.size==self.y.size:
      dx= (self.y-self.t)/batch_size
    else:
      dx=self.y.copy()
      dx[np.arange(batch_size),self.t]-=1
      dx=dx/batch_size

    return dx
```

- 역전파 때는 전파하는 값을 배치의 수로 나눠서 데이터 1개당 오차를 앞 계층으로 전파한다.

## 5.7 오차역전파법 구현하기

- 이번 절에서는 지금까지 구현한 계층을 조합해서 신경망을 구축한다.

### 5.7.1 신경망 학습의 전체 그림

- 신경망 학습의 순서

- 전제
  - 신경망에는 적응 가능한 가중치와 편향이 있고, 이 가중치와 편향을 훈련 데이터에 적응하도록 조정하는 과정을 '학습'이라고 한다.
- 1단계 - 미니배치
  - 훈련 데이터 중 일부를 무작위로 가져온다(미니배치) 그 미니배치의 손실함수 값을 줄이는 것이 목표이다.
- 2단계 - 기울기 산출
  - 미니배치의 손실 함수 값을 줄이기 위해 각 가중치 매개변수의 기울기를 구한다. 기울기는 손실 함수의 값을 가장 작게 하는 방향을 제시, 여기서 오차역전파법이 등장하는 것이다.
- 3단계 - 매개변수 갱신
  - 가중치 매개변수를 기울기 방향으로 아주 조금 갱신한다.
- 4단계 - 반복

### 5.7.2 오차역전파법을 적용한 신경망 구현하기

- 여기서는 2층 신경망을 TwoLayerNet 클래스로 구현한다.

```python
import sys, os
sys.path.append(os.pardir)  #부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict

class TwoLayerNet:

  def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        # 계층 생성
        self.layers = OrderedDict()
        #신경망의 계층을 OrderedDict에 보관한다. 이는 순서가 있는 딕셔너리라서 딕셔너리에 추가한 순서를 기억한다.
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()

  def predict(self,x):
    for layer in self.layers.values():
      x=layer.forward(x)
      # 순전파 때는 추가한 순서대로 각 계층의 forward() 메서드를 호출하면 처리가 완료된다.

    return x

  def loss(self,x,t):
    y=self.predict(x)

    return self.lastLayer.forward(y,t)

  def accuracy(self,x,t):
    y=self.predict(x)
    y=np.argmax(y,axis=1)
    if t.ndim != 1 : t=np.argmax(t,axis=1)

    accuracy = np.sum(y==t)/float(x.shape[0])
    return accuracy

  def numerical_gradient(self,x,t):
    loss_W = lambda W: self.loss(x,t)

    grads = {}
    grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
    grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
    grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
    grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

    return grads

  def gradient(self,x,t):
    self.loss(x,t)

    dout = 1
    dout = self.lastLayer.backward(dout)

    layers = list(self.layers.values())
    layers.reverse()
    #역전파 때는 계층을 반대로 호출하기만 하면 된다.

    for layer in layers:
      dout = layer.backward(dout)

    grads = {}
    grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
    grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

    return grads

```

- Affine 계층과 ReLU 계층이 각자 내부에서 순전파와 역전파를 제대로 처리하고 있으니 여기서는 그냥 계층을 올바른 순서대로 연결한다음 순서대로 호출해 주기만 하면 된다.
- 이처럼 계층을 모듈화해서 구현한다면 단순히 필요한 만큼 계층을 더 추가하면 되기 때문에 편리하다.

### 5.7.3 오차역전파법으로 구현 기울기 검증하기

- 앞서 말했듯이 기울기를 구하는 방법은 두가지이다.
  - 수치 미분
  - 해석적으로 수식을 풀어 구하는 방법(오차역전파법), 이는 매개변수가 많아도 효율적으로 계산 가능

- 이제부터는 비교적 빠른 오차역전파법을 사용한다.
  - 수치 미분은 오차역전파법을 제대로 구현해두면 필요없지만
  - 오차역전파법을 정확히 구현했는지 확인하기 위해 필요하다.

- 수치 미분은 구현하기 쉽다는 이점이 있으며 그렇기 때문에 버그가 숨어있기 어렵다.
- 하지만 오차역전파법은 구현하기 복잡하기 때문에 종종 실수를 하곤 한다.
  - 그래서 수치 미분의 결과와 오차역전파법의 결과를 비교하여 오차역전파법을 제대로 구현했는지 검증한다.
  - 이를 기울기 확인이라고 한다.

```python
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

(x_train, t_train),(x_test,t_test) = load_mnist(normaliz=True,one_hot_label=True)

network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

for key in grad_numerical.keys():
    diff = np.average(np.abs(grad_backprop[key]-grad_numerical[key]))
    print(key+":"+str(diff))

```

- 가장 먼저 mnist 데이터셋을 읽고 훈련 데이터 일부를 수치 미분으로 구한 기울기와 오차역전파법으로 구한 기울기의 오차를 확인한다.
  - 여기에서는 각 가중치 매개변수의 차이의 절대값을 구하고, 이를 평균한 값이 오차가 된다.

- 결과가 다음과 같이 나온다.

```python
W1:4.776667786377981e-10
b1:2.878415981464981e-09
W2:5.33318360614366e-09
b2:1.402352762733261e-07
```

- 이 결과는 수치 미분과 오차역전파법으로 구한 기울기의 차이가 매우 작다는 것을 말해준다.
  - 이로써 오차역전파법으로 구한 기울기가 올바름이 드러나는 것이다.

### 5.7.4 오차역전파법을 사용한 학습 구현하기

- 기울기를 오차역전파법으로 구현한 신경망 학습을 구현한 코드이다.

```python
import sys, os
sys.path.append(os.pardir)

import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 기울기 계산
    #grad = network.numerical_gradient(x_batch, t_batch) # 수치 미분 방식
    grad = network.gradient(x_batch, t_batch) # 오차역전파법 방식(훨씬 빠르다)

    # 갱신
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)
```

## 5.8 정리

- 이번 장에서는 계산그래프부터 시작해서
  - 이를 이용하여 신경망의 동작과 오차역전파법을 설명했다.
  - 그 처리 과정을 계층이라는 단위로 구현하였다.
    - ReLU 계층, Softmax-with-Loss 계층, Affine 계층, Softmax 계층 등
    - 모든 계층에서는 forward 순전파, backward 역전파 메서드를 구현한다.
    - 이를 통해 가중치 매개변수의 기울기를 효율적으로 구할 수 있다.
  - 이처럼 동작을 계층으로 '모듈화'한 덕분에 신경망에서 계층을 자유롭게 재조합하여 원하는 신경망을 쉽게 만들 수 있다.
