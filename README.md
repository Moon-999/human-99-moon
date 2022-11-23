# 부동산 챗봇 프로젝트
- 22.11.17 ~ 22.11.22
- 개발환경
    - 코딩환경 : vsCode / jupyterlab 
    - 웹환경 : Github / Heroku / Flask / SQLalchemy / kakao open builder 
    - 언어 : python
- 프로젝트 ppt
    - 
- 영상
    - 신청자격 - https://youtu.be/ibZtP0mG4c0
    - 부동산뉴스 - https://youtu.be/awkQyPooWlA


- 프로젝트 주요 기능
    - 부동산 뉴스(주요뉴스 / 지역별 뉴스 검색)
        - 웹크롤링을 통한 부동산 뉴스기사 수집
    - 안심전환대출관련 정보(보유 아파트 시세 조회)
        - 데이터베이스와 연동하여 검색 조건에 맞는 결과 도출하는 스킬 구현
        - 챗봇컨텍스트 기능을 활용하여 검색조건을 보다 자연스러운 대화처럼 받아올 수 있음.

- 프로젝트 기간 외 기능
    - 아파트 실거래가 공공API를 활용하여 매달 업데이트된 실거래가를 데이터베이스에 자동으로 입력해주는 배치파일을 생성함. [공공API활용파일](data.py), [배치파일](autoCreateDF.bat)