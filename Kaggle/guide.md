# Kaggle

### 데이터 가져오기

1. train
2. test
3. submission

이후 정보확인

### 데이터 속성 확인

1. 열 정보 확인
2. 각 열의 의미 파악
3. 데이터 속성 확인 : `dtypes`

### 데이터 중복 확인

- `train_df['컬럼명'].valuse_counts()`

### 데이터 결측치 확인

- `train_df.isnull().sum()`
- `test_df.isnull().sum()`

### 데이터 결측치 제외

- `train_df[[’col1’, ‘col2’, ]].dropna()`

### 데이터를 수평으로 변환하기

- `.unstack()`

### 데이터 시각화

- `df.plot.bar(stacked = *False*)`

### 원-핫 인코딩

- 성별이 남,여로 주어진 데이터를 1,0으로 바꿔줘 머신러닝에 용이하게 사용
- `pd.get_dummies(데이터프레임명, columns=[”변수화하고 싶은 컬럼명”])`

### 상관 행렬 작성

- `데이터프레임명.corr()`

## 전처리

### 학습 데이터와 테스트 데이터의 통합

- 전체 집계와 통계 정보를 얻기 위함
- `all_df = pd.concat([train_df, test_df], sort=*False*).reset_index(drop=*True*)`
    - sort=False : 결합 후 순서가 바뀌지 않음
    - reset_index(drop=True) : 원래 행 번호를 삭제

### 결측치 메우기

예시에 Fare 값에 결측치가 있음 → 이를 제거

→ Pclass별 Fare의 평균을 구해 평균값으로 해당 결측치를 채우는 방법
