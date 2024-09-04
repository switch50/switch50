# =========================================================================
#  지역별 기온 정보를 확인하고 옷차림을 추천해주는 프로그램
# =========================================================================
# 1)날씨정보 가져오기
import requests
import datetime

# 기상청 API URL
weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

# 일반인증키 (인코딩된 값)
encoding_key = "Cvzl0n5R3aZ7Jtzmam8s6AcplvKGhMhWZxouzD12WqweqwGuLWpmczItRO8cOdT5bhHkmUdKDIb3vh79f7ulmw%3D%3D" 

# 기준이 되는 날짜 (오늘 날짜를 YYYYMMDD 형식으로)
base_date = datetime.datetime.today().strftime("%Y%m%d")  

# 기준이 되는 시간 (기본값 0800, 8시)
base_time = "0800"   

# 사용자에게 지역 선택을 위한 숫자 입력 요청. 유효한 값 입력하도록 요청
while True:
    try:
        area = int(input(
            "1  서울     2  부산     3  대구     4  인천\n"
            "5  광주     6  대전     7  울산     8  세종\n"
            "9  경기도   10 충청북도 11 충청남도 12 전라남도\n"
            "13 전라북도 14 경상북도 15 경상남도 16 제주도\n"
            "17 강원도\n"
            "\n해당하는 지역의 숫자를 입력하세요: "
        ))
        print()
        1
        # 입력된 값이 1에서 17 사이일 경우 반복문 종료
        if 1 <= area <= 17:
            break
        else:
            # 유효하지 않은 숫자가 입력된 경우 메시지 출력
            print("유효한 숫자를 입력해주세요.") 
    except ValueError:
        # 숫자가 아닌 값이 입력된 경우 메시지 출력
        print("유효한 숫자를 입력해주세요.")

# area 값이 유효한 경우 지역에 해당하는 위도와 경도 값을 설정
if area == 1:
    nx = "59"
    ny = "126" # 서울 위도 경도 좌표
    region = "서울"
elif area == 2:
    nx = "98"
    ny = "76" # 부산 위도 경도 좌표
    region = "부산"
elif area == 3:
    nx = "89"
    ny = "90" # 대구 위도 경도 좌표
    region = "대구"
elif area == 4:
    nx = "55"
    ny = "124" # 인천 위도 경도 좌표
    region = "인천"
elif area == 5:
    nx = "58"
    ny = "74" # 광주 위도 경도 좌표
    region = "광주"
elif area == 6:
    nx = "67"
    ny = "100" # 대전 위도 경도 좌표
    region = "대전"
elif area == 7:
    nx = "102"
    ny = "84" # 울산 위도 경도 좌표
    region = "울산"
elif area == 8:
    nx = "66"
    ny = "103" # 세종 위도 경도 좌표
    region = "세종"
elif area == 9:
    nx = "60"
    ny = "120" # 경기도 위도 경도 좌표
    region = "경기도"
elif area == 10:
    nx = "69"
    ny = "107" # 충청북도 위도 경도 좌표
    region = "충청북도"
elif area == 11:
    nx = "68"
    ny = "100" # 충청남도 위도 경도 좌표
    region = "충청남도"
elif area == 12:
    nx = "51"
    ny = "67" # 전라남도 위도 경도 좌표
    region = "전라남도"
elif area == 13:
    nx = "63"
    ny = "89" # 전라북도 위도 경도 좌표
    region = "전라북도"
elif area == 14:
    nx = "87"
    ny = "106" # 경상북도 위도 경도 좌표
    region = "경상북도"
elif area == 15:
    nx = "90"
    ny = "77" # 경상남도 위도 경도 좌표
    region = "경상남도"
elif area == 16:
    nx = "52"
    ny = "38" # 제주도 위도 경도 좌표
    region = "제주도"
elif area == 17:
    nx = "73"
    ny = "134" # 강원도 위도 경도 좌표
    region = "강원도"

# API 요청에 필요한 데이터 구성
load_data = "serviceKey=" + encoding_key + "&" + \
          "dataType=json" + "&" + \
          "base_date=" + base_date + "&" + \
          "base_time=" + base_time + "&" + \
          "nx=" + nx + "&" + \
          "ny=" + ny

# 응답 데이터를 저장할 딕셔너리 생성
data = dict()
data['date'] = base_date
weather = dict()

# 날씨 정보 요청
res = requests.get(weather_url + load_data)
# API 응답에서 필요한 데이터 추출
items = res.json().get('response').get('body').get('items')
for item in items['item']:
    # 온도(TMP) 정보 가져오기
    if item['category'] == 'TMP':
        weather['tmp'] = item['fcstValue']

data['weather'] = weather

# 현재 기온 정보 추출
items1 = res.json().get('response').get('body').get('items')
items1['item']
for item in items1['item']:
    if item['category'] == 'TMP':
        current_temperature = int(item['fcstValue'])

# ============================================================================================================================================
# 네이버 쇼핑 검색 OpenAPI 사용하기
# ============================================================================================================================================

# 네이버 쇼핑 검색을 위한 함수 정의
def naver_shop_search(query, display):
    # 네이버 애플리케이션의 인증 헤더 설정
    headers = {
        "X-Naver-Client-Id": "3JKKhUYF8FQCQxm0owkD",    # 네이버 애플리케이션의 client_id
        "X-Naver-Client-Secret": "TPonc2ZJLB"           # 네이버 애플리케이션의 client_secret 키 설정
    }
    # 네이버 쇼핑 검색 요청 파라미터 설정
    params = {
        "query": query,                                 
        "display": display,         
        "sort": "date"
    }
    # 네이버 쇼핑 검색 API URL
    naver_shop_url = "https://openapi.naver.com/v1/search/shop.json" 
    # 네이버 쇼핑 검색 요청   
    res = requests.get(naver_shop_url, headers=headers, params=params)   
    if res.status_code == 200:
        # 네이버 쇼핑 검색 결과 확인
        items = res.json().get('items')                     
        # 각 항목에서 'link' 필드만 추출하여 리스트로 반환
        links = [item['link'] for item in items]
        return links
    return []

# 기온에 따른 옷차림 추천 및 검색어 설정
if current_temperature >= 23:
    temperature = "민소매, 반바지, 반팔, 스커트"
elif 20 <= current_temperature < 23:
    temperature = "반팔, 얇은 셔츠, 반바지, 면바지"
elif 17 <= current_temperature < 20:
    temperature = "얇은 가디건, 긴팔티, 면바지, 청바지"
elif 12 <= current_temperature < 17:
    temperature = "얇은 니트, 가디건, 맨투맨, 얇은 자켓, 면바지, 청바지"    
elif 9 <= current_temperature < 12:
    temperature = "자켓, 가디건, 야상, 맨투맨, 니트스타킹, 청바지, 면바지"
elif 5 <= current_temperature < 9:
    temperature = "코트, 히트텍, 니트, 청바지, 레깅스"
else:
    temperature = "패딩, 두꺼운 코트, 기모제품, 목도리"

# 추천 옷차림들을 쉼표로 분리해서 검색어 리스트를 생성
search_terms = temperature.split(", ")

# 출력: 지역, 현재 기온, 추천 옷차림, 구매처 링크
print(f"지역: {region}\n")
print(f"현재 기온: {current_temperature}도\n")
print(f"추천 옷차림: {temperature}\n")
print("해당 옷들의 구매처 링크는 다음과 같습니다")
print("----------------------------------------")

# 각 검색어에 대해 네이버 쇼핑 검색 수행
for term in search_terms:
    # 각 검색어에 대해 2개의 결과 링크 가져오기
    result_links = naver_shop_search(term, 2)  
    print(f"{term} 검색 결과")
    for link in result_links:
        print(link)
    print()
print("----------------------------------------")