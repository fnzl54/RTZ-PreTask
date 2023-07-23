import requests

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