import source.request_url as request_url
import source.conversion_subtitle as conversion_subtitle    
import argparse

parser = argparse.ArgumentParser(description='URL를 받기 위한 argparse 입니다.')
parser.add_argument('--url', required=True, help='자막이 필요한 URL을 입력하여 주세요.')
args = parser.parse_args()

response = request_url.get_html_from_url(args.url)

if response:
    # '__NEXT_DATA__' 데이터 추출
    json_data = request_url.extract_json_data_from_html(response)
    if json_data:
        # JSON 데이터 출력
        conversion_subtitle.make_srt("output.srt", conversion_subtitle.make_subtitle_list(json_data["props"]["pageProps"]["transcriptData"]["translation"]["paragraphs"]))
    else:
        print("HTML 파일 안에 JSON 데이터가 없습니다.")
else:
    print("HTML 파일에 문제가 발생하였습니다.")