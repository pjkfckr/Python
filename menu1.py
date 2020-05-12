import time  ## (초)의 시간을 두고 출력하기위해 time을 import함
import random ## 음식을 랜덤으로 고르기위해 import 함

lunch = [] ## 먼저 변수에 값을 저장하여야 하므로 빈 공간 리스트를 만들어준다.

while True: ## while문을 사용한 이유는 for문을 이용하여 주어진 횟수만큼 작동시킬수 있지만, 리스트에 몇번, 또는 몇회가 추가될지 모르기 때문에 끝이없는 무한loop인 while True:를 사용했다.
    print(lunch) ## 사용해도 되고 사용 안해도 되지만, 현재 무엇이 주어져있는지 또는 주어진 값이 제대로 변수에 들어가있는지 확인하기위해 넣었다.
    item = input("음식을 추가 해주세요 :") ## 그러고나서 lunch의 변수에 추가할 변수를 작성했다.
    if (item == "q"): ## 무한loop문은 잘못하면 과부하가 생길수있기때문에 어떠한 조건에 의해서 중단할지를 if문에 작성하였다.       
        break    
    else:        
        lunch.append(item) ## 만약 중단을 하지 않을 경우에는 작성된 item의 변수값을 lunch에 추가하는 append를 사용했다. 위에 lunch는 list() 이기 때문에 append로 추가 한것이다.
        
print(lunch)

set_lunch = set(lunch) ## 리스트의 del 등 삭제하는 명령어를 사용할수 있지만, 집합(set())을 사용하면 좀더 보기에 간편하고 쉽게 사용할 수 있기때문에 사용하였다.

while True:  ## 위에서 음식을 추가 하는 loop를 종료 한 뒤에는 삭제할 수 있는 loop를 만들어주었다.
    print(set_lunch)
    item = input("음식을 삭제 해주세요 : ")
    if (item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item]) ## 위에 set_lunch가 실질적으로 이루어지는 곳이다. 입력한item의 값을 집합으로 만들기 위해 set([item])을 사용하였다. []을 사용하여 item을 리스트로 만든뒤 set()으로 집합을 만들어준다. 위에 set_lunch는 set(lunch)의 값을 저장하였고, 이 set_lunch의 값에 set으로 만들어준 set([item])을 차집합 한 값이 저장이 된다.

print(set_lunch, "중에서 선택합니다.")
print("5")   
time.sleep(1)    ## 위에서 import time을 한 이유는 time.sleep(sec)을 쓰기 위해서 이다. 이 기능은 ()사이에 주어진 초 만큼 쉰 다음 그 다음의 값이 출력되게 하는 기능이다.
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print((random.choice(list(set_lunch)))) ## import random 을 사용한 이유가 여기 있다. 먼저 주어진 값이 set()의 형태로 저장된 set_lunch를 random.choice를 사용하여 그중 값을 하나 랜덤하게 출력한다. 하지만 random.choice는 list의 형태에서만 동작을 하기때문에 set_lunch를 list()로 묶어준뒤 출력하게 작성하였다.