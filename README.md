# Sangchu
  > 부산 지역 상권 분석 & 매물 추천 서비스
## 📌 프로젝트 소개

### 📆 개발 기간
- 2023.11.9 ~ 2023.12.29
- 11.9 ~ 11.30: 데이터 수집, 분석, 모델링
- 12.6 ~ 12.29: 웹 구현


### ⭐️ 팀원 구성
- 김동환 [@offensivesoup](https://github.com/offensivesoup)
- 박현서 [@kyunoes](https://github.com/kyunoes)
- 정서영 [@jszxro](https://github.com/jszxro)
- 조정인 [@blueberryade](https://github.com/blueberryade)
- 최성훈 [@padari07](https://github.com/padari07)
- 하진우 [@jinuwuu12](https://github.com/jinuwuu12)

### 🛠️ 기술 스택
<img width="800" alt="기술스택_메인" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/ef5dfab4-5c65-45a6-a063-0ca772375a0e">

## 페이지별 구현 기능
### [메인 페이지]
<img width="800" height="600" alt="메인페이지" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/e46ba6bc-e111-46e3-a611-bd05a81c6036">

- 헤더에서 각 페이지로 이동하거나 로그인/로그아웃을 할 수 있습니다.
- Go There 버튼으로 부산시 분석 페이지로 이동할 수 있습니다.
- 조회수 기준으로 Top4 매물을 보여줍니다.
  
### [부산시 분석 페이지]
<img width="800" height="600" alt="부산시 분석 페이지" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/c43f604d-cbea-483a-bade-f6bd00d1610a">

- 아래의 부산시 분석 데이터들을 차트와 지도로 보여줍니다.
  - 임대료 추세 데이터
  - 집객시설 분포도
  - 인구밀도 분포도
  - 인구수 분포도
  - 구별 서비스 인구 분포도
  - 구별 점포 밀도 분포도
- 지도의 각 구를 클릭하면 구별 분석 페이지로 이동합니다.

### [구별 분석 페이지]
<img width="800" height="600" alt="구별 분석 페이지" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/93137b13-7299-414a-ae97-076eaf9cd1c8">

- 아래의 구별 분석 데이터를 차트로 보여줍니다.
  - 주요 상권 정보
  - 업종별 점포 수
  - 연령, 요일, 시간대 유동인구
  - 년도별 유동인구
  - 월세 비교
  - 지하철 승하차 인원 데이터
  - 월별/시군구별 업종평가점수
- 지도에서 구의 학교, 병원, 약국, 상권별 도시철도를 핀으로 표시해서 보여줍니다.
- 구를 클릭해서 다른 구로 이동할 수 있습니다.
   
### [매물 목록 페이지]
<img width="800" height="600" alt="매물목록 페이지" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/f2e8b0a6-5eab-401c-a162-44903f483461">

- 구별 상가 월세 매물 리스트를 제공합니다.
- 지도에서 각 매물의 위치를 핀으로 보여줍니다.

  
### [매물 상세 페이지]
<img width="800" height="600" alt="매물 상세 페이지" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/54a5074c-a55c-44c5-bd0f-888df9ffeff0">

- 선택한 매물의 상세정보를 제공합니다.
- 유사도 분석을 통해 선택한 매물과 유사한 매물을 추천해주는 모델
- 선택한 매물과 유사한 매물 5개를 추천해 줍니다.
  
### [월세 예측 페이지]
<img width="800" height="600" alt="월세 예측 페이지" src="https://github.com/offensivesoup/Sangchu_Final_PJT/assets/115989049/6f458118-328c-4878-bae9-73bb8827d0fa">

- 회귀분석을 통해 선택한 매물과 유사한 매물을 추천해주는 모델
- 평수, 보증금, 상가종류, 임대면적, 전용면적, 층, 총층을 입력하여 월세 예측을 합니다.
- 월세 예측을 통해 이미 임대된 상가와 비교하여 본인이 원하는 수준의 월세를 찾는 도움을 줍니다.
