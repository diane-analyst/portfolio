# 데이터 분석 포트폴리오

A/B 테스트와 통계분석 역량을 보여주는 데이터 분석 포트폴리오입니다.

## 📊 프로젝트 개요

이 포트폴리오는 데이터 분석가로서의 역량을 보여주기 위해 다음 두 가지 주요 프로젝트를 포함합니다:

1. **A/B 테스트 분석**: 웹사이트 전환율 개선을 위한 A/B 테스트 설계 및 분석
2. **통계분석**: 다양한 통계 기법을 활용한 종합 데이터 분석

## 🎯 주요 역량

### A/B 테스트 역량
- ✅ 통계적 가설 검정 (Z-검정, 카이제곱 검정)
- ✅ 효과 크기(Effect Size) 계산 및 해석
- ✅ 검정력 분석(Power Analysis) 및 샘플 크기 최적화
- ✅ 신뢰구간 계산 및 해석
- ✅ 비즈니스 인사이트 도출 및 권장사항 제시

### 통계분석 역량
- ✅ 기술통계 및 탐색적 데이터 분석(EDA)
- ✅ 가설검정 (t-검정, ANOVA, 비모수 검정)
- ✅ 상관분석 (피어슨, 스피어만)
- ✅ 회귀분석 (단순선형회귀, 다중회귀)
- ✅ 시계열 분석 (트렌드, 계절성 분해)
- ✅ 데이터 시각화 및 인사이트 도출

## 📁 프로젝트 구조

```
portfolio/
├── README.md                    # 프로젝트 소개
├── requirements.txt             # 필요한 패키지 목록
├── ab_test_analysis.ipynb      # A/B 테스트 분석 노트북
└── statistical_analysis.ipynb  # 통계분석 노트북
```

## 🚀 시작하기

### 1. 환경 설정

```bash
# 가상환경 생성 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. Jupyter Notebook 실행

```bash
# Jupyter Notebook 실행
jupyter notebook

# 또는 JupyterLab 사용
jupyter lab
```

### 3. 노트북 실행 순서

1. **ab_test_analysis.ipynb**: A/B 테스트 분석 프로젝트
   - 웹사이트 전환율 개선을 위한 A/B 테스트 설계
   - 통계적 검정 및 효과 크기 분석
   - 비즈니스 의사결정을 위한 인사이트 도출

2. **statistical_analysis.ipynb**: 통계분석 프로젝트
   - 다양한 통계 기법을 활용한 종합 분석
   - 가설검정, 회귀분석, 시계열 분석 등

## 📦 주요 사용 라이브러리

- **데이터 처리**: pandas, numpy
- **시각화**: matplotlib, seaborn
- **통계분석**: scipy, statsmodels
- **머신러닝**: scikit-learn
- **노트북**: jupyter

## 📈 분석 내용 상세

### A/B 테스트 분석 (ab_test_analysis.ipynb)

1. **데이터 생성 및 탐색적 분석**
   - A/B 테스트 시나리오 시뮬레이션
   - 그룹별 전환율 비교 및 시각화

2. **통계적 가설 검정**
   - Z-검정 (양측/단측)
   - 카이제곱 검정
   - 유의성 해석

3. **효과 크기 및 검정력 분석**
   - Cohen's h 계산
   - 검정력 분석 및 샘플 크기 최적화

4. **신뢰구간 계산**
   - 각 그룹의 95% 신뢰구간
   - 전환율 차이의 신뢰구간

5. **비즈니스 인사이트**
   - 통계적 결론 도출
   - 롤아웃 권장사항
   - 추가 고려사항

### 통계분석 (statistical_analysis.ipynb)

1. **기술통계 및 EDA**
   - 기술통계 요약
   - 분포 시각화
   - 상관관계 분석

2. **가설검정**
   - 독립표본 t-검정
   - 일원분산분석 (ANOVA)
   - 비모수 검정 (Mann-Whitney U)

3. **상관분석**
   - 피어슨 상관계수
   - 스피어만 상관계수
   - 상관관계 시각화

4. **회귀분석**
   - 단순선형회귀
   - 다중회귀분석
   - 모델 평가 (R², RMSE)

5. **시계열 분석**
   - 시계열 분해 (트렌드, 계절성, 잔차)
   - 자기상관 검정 (Ljung-Box)

## 💡 주요 학습 포인트

### 통계적 검정
- **가설 설정**: 귀무가설과 대립가설의 명확한 정의
- **유의수준**: α = 0.05 기준으로 통계적 유의성 판단
- **p-value 해석**: p-value < 0.05일 때 귀무가설 기각

### 효과 크기
- **Cohen's h**: 비율 데이터의 효과 크기 측정
- **해석 기준**: 
  - < 0.2: 작은 효과
  - 0.2-0.5: 중간 효과
  - 0.5-0.8: 큰 효과
  - > 0.8: 매우 큰 효과

### 검정력 분석
- **검정력(Power)**: 실제로 차이가 있을 때 이를 검출할 수 있는 확률
- **권장 검정력**: 0.8 이상
- **샘플 크기**: 검정력을 확보하기 위한 최소 샘플 크기 계산

## 📝 참고사항

- 모든 분석은 재현 가능하도록 시드값을 설정했습니다 (np.random.seed(42))
- 한글 폰트 설정이 포함되어 있어 Windows 환경에서 바로 실행 가능합니다
- 실제 데이터 대신 시뮬레이션 데이터를 사용하여 분석 기법을 시연합니다

## 🔗 추가 학습 자료

- [A/B Testing Guide](https://www.optimizely.com/optimization-glossary/ab-testing/)
- [Statistical Hypothesis Testing](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
- [Effect Size](https://en.wikipedia.org/wiki/Effect_size)

## 📧 문의

프로젝트에 대한 질문이나 피드백이 있으시면 언제든지 연락주세요!

---

**작성일**: 2025년 11월 21일  
**버전**: 1.0

