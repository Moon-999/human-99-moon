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

- 프로젝트 배경 및 목적
    - 뉴스기사를 살펴보면, 17년과 비교 했을때, 22년 전체 세대 모두 빚이 늘었지만 특히 20대는 3배 이상 빚이 늘었다는 것을 알 수 있습니다. 또한 30대도 1.5배 이상의 빚이 늘었기 때문에, 영끌족에는 젊은층이 많다는 것을 알 수 있습니다.
    그렇다면 이러한 문제를 가지고 있는 영끌족이 현재 가장 필요한 것이 무엇일까 고민하고 찾아보니, 최근 정부 정책으로 2030 영끌족들을 위한 안심전환대출 서비스가 있다는 것을 알게 되었습니다. 

    - 안심전환대출이란 서민_실수요자가 보유한 변동금리_준고정금리 주택담보대출을 저금리의 장기_고정금리_분할상환 상품으로 갈아탈 수 있는 상품입니다. 안심전환대출은 기존 은행의 금리보다 낮은 금리를 적용하고 있으며, 적용 대상자에게는 기존에 가지고 있는 대출 부담을 줄일 수 있도록 안심전환대출로 전환해주어 영끌족들의 이자 부담을 경감시키는 효과를 얻는 것을 목적으로 합니다.
    이러한 서비스에 접근하기 용이하고 이해하기도 쉬워서 많은 사람들이 이용할 수 있도록 정보 제공 서비스를 만들 예정입니다.

- 프로젝트 주요 기능
    - 부동산 뉴스(주요뉴스 / 지역별 뉴스 검색)
        - 웹크롤링을 통한 실시간 부동산 뉴스기사 수집

    - 안심전환대출관련 정보(보유 아파트 시세 조회)
        - 데이터베이스와 연동하여 검색 조건에 맞는 결과 도출하는 스킬 구현
        - 챗봇컨텍스트 기능을 활용하여 검색조건을 보다 자연스러운 대화처럼 받아올 수 있음.

- 프로젝트 기간 외 기능
    - 아파트 실거래가 공공API를 활용하여 매달 업데이트된 실거래가를 데이터베이스에 자동으로 입력해주는 배치파일을 생성함. [공공API활용파일](data.py), [배치파일](autoCreateDF.bat)