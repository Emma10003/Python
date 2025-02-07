<Overfitting 개선>
0. 오버피팅 원인
1. RandomForest 알고리즘 사용 -> 정규화 필요한지?
2. MAE 계산 방식
3. 학습시킨 모델로 예측시켰을 때 mae가 차이나는 원인
	> Overfitting
	> train data와 test data의 분포 차이: 데이터 샘플링/변환 방식
	> test data의 특성: 이상치 or 노이즈
	> 모델의 일반화 성능

그냥 시도
1. EDA
2. 데이터 전처리
3. 데이터 정규화
4. RandomForest 모델 정의
5. 최적의 하이퍼파라미터 찾기
6. 전진선택법으로 변수 선택
7. 선택된 변수로 모델 학습/평가

----------------------------------------------------------------------
[Links]
* RandomForest Hyperparameter
https://injo.tistory.com/30