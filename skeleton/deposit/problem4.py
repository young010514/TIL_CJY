import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


# "fin_prdt_cd": "01030500560002",


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()['result']

    # 번역할 데이터 생성
    to_korean ={
        'fin_prdt_cd' :'금융상품코드',
        'intr_rate' : '저축 금리',
        'save_trm' : '저축 기간',
        'intr_rate_type' : '저축금리유형',
        'intr_rate_type_nm' : '저축금리유형명',
        'intr_rate2' : '최고 우대금리',
        "fin_prdt_nm": "금융상품명",
        "kor_co_nm": "금융회사명",
    }

    # option list 먼저 생성 => 필요한 데이터만 
    option_list = []
    for raw_data in response['optionList']:
        result_one_data = {}
        for k in raw_data:
            if k in to_korean.keys():
                result_one_data[to_korean[k]] = raw_data[k]
        option_list.append(result_one_data)
    
    
    # code 맞는지 검증하고, result에 추가
    result = []
    for base_list in response['baseList']:
        
        option_result = []
        for option_data in option_list:
            # 코드 동일한 option만 추가
            if option_data[to_korean['fin_prdt_cd']] == base_list['fin_prdt_cd']:
                # 금융상품코드는 결과값에 없으므로 comprehension 사용
                option_result.append(dict((k,v) for k, v in option_data.items() if k != to_korean['fin_prdt_cd']))        
        
        # data 추가
        one_data = {
            to_korean['fin_prdt_nm'] :base_list['fin_prdt_nm'],
            to_korean['kor_co_nm'] : base_list['kor_co_nm'],
            '금리정보' : option_list
        }
        
        result.append(one_data)

    return result
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)