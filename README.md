# RTZ-PreTask
텍스트를 크롤링해서 자막(srt)을 만드는 것

## 과정
1. URL get 요청으로 HTML 가져오기
2. HTML 파일에서 자막부분 Json 추출하기
3. 나눠져 있는 자막 파일을 파이썬의 리스트 형태로 정렬
4. .srt 형태에 맞게 변형 후 저장

## 필요한 함수
- get_html_from_url
    - 변수로 들어온 URL에 get 요청의 반환 된 HTML 반환
- json_data_from_html
    - HTML에서 자막부분의 Json을 추출후 반환
- make_subtitle_list
    - Json 데이터를 리스트로 변환
- make_srt
    - 변수로 들어온 자막 리스트를 srt 형식으로 변환
    - 순서, 시간 정보 (시작 시간 -> 끝 시간), 자막 텍스트
- number_to_time_format
    - 숫자를 시간 형태로 변환

## 보고서 및 실행 방법
https://chanyoung-kwon.notion.site/srt-350b6a9d52bd46b4a6154670ef085d31?pvs=4