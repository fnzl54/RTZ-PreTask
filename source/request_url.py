import requests
from bs4 import BeautifulSoup
import json

def get_html_from_url(url):
    try:
        response = requests.get(url)
        # 요청이 성공적으로 처리되었는지 확인
        response.raise_for_status()

        # HTML 데이터 반환
        html_data = response.text
        return html_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
def extract_json_data_from_html(html_data):
    try:
        soup = BeautifulSoup(html_data, 'html.parser')

        # id가 '__NEXT_DATA__'인 스크립트 태그 가져오기
        script_tag = soup.find('script', id='__NEXT_DATA__')

        # JSON 데이터 추출
        if script_tag:
            json_data = json.loads(script_tag.string)
            return json_data
        else:
            print("'__NEXT_DATA__' tag가 존재하지 않습니다.")
            return None
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        return None