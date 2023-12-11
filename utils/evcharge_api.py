from soloProject import settings
import requests

def get_data(metroCd, cityCd:None=""):
    """
    Open Data API - 전기차 충전소 설치 현황
    
    Args:
        * metroCd (int): 시도 코드
        * cityCd (int): 시군구 코드 
        
    Returns:
        * success -> JSON data (전기차 충전소 위치): https://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000493&pstate=ev&redirect=Y
        * failed  -> None
    """
    response = requests.get(f"https://bigdata.kepco.co.kr/openapi/v1/EVcharge.do?metroCd={metroCd}&cityCd={cityCd}&apiKey={settings.EVCHARGE_API_KEY}&returnType=json",)
    
    if response.status_code == 200:
        return response.json()
    print(response.status_code)
    return None

def get_code():
    """
    Open Data API - 시군구 코드 정보
    
    Returns:
        * success -> JSON data (시도/시군구 코드): https://bigdata.kepco.co.kr/cmsmain.do
        * failed  -> None
    """
    response = requests.get(f"https://bigdata.kepco.co.kr/openapi/v1/commonCode.do?codeTy=cityCd&apiKey={settings.EVCHARGE_API_KEY}&returnType=json")
    
    if response.status_code == 200:
        return response.json()
    print(response.status_code)
    return None
