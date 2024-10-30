"""
함수 정의하기

def 함수_이름():        <~ 함수 정의의 첫 줄: 헤더
	실행 코드
"""


# 함수 정의 예시
def hello():
	print("HI")


hello()


# 카페 모카 레시피
def cafe_mocha_recipe():
	print("1. 준비된 컵에 초코 소스를 넣는다.")
	print("2. 에스프레소를 추출하고 잔에 부어 준다.")
	print("3. 초코 소스와 커피를 잘 섞어 준다.")
	print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
	print("5. 생크림을 얹어준다.") 

cafe_mocha_recipe()
cafe_mocha_recipe()

# 파라미터를 받는 함수
def hello(name): # name은 파라미터(parameter)
	print("hello")
	print(name)
	print("welcome!")

hello("Emma")
