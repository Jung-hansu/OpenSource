from soloProject import settings
import requests

def geocoding(address, coordinate:None=""):
    """
    Naver Map API - Geocoding
    
    Args:
        * address (String): 지번 주소
        
    Returns:
        * success -> JSON data (좌표): https://api.ncloud-docs.com/docs/ai-naver-mapsgeocoding-geocode 
        * failed  -> None
    """
    response = requests.get(
        f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}&coordinate={coordinate}",
        headers={
            "X-NCP-APIGW-API-KEY-ID": settings.NAVER_API_KEY_ID,
            "X-NCP-APIGW-API-KEY": settings.NAVER_API_KEY,
        })
    
    if response.status_code == 200:
        return response.json()
    print(response.status_code)
    return None

def reverse_geocoding(latitude, longitude):
    """
    Naver Map API - ReverseGeocoding
    Args:
        * latitude (float): 위도
        * longitude (float): 경도
    Returns:
        * success -> JSON data (행정 코드): https://api.ncloud-docs.com/docs/ai-naver-mapsreversegeocoding-gc
        * failed  -> None
    """
    response = requests.get(
        f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?request=coordsToaddr&coords={longitude},{latitude}&sourcecrs=epsg:4326&output=json&orders=addr,admcode",
        headers={
            "X-NCP-APIGW-API-KEY-ID": settings.NAVER_API_KEY_ID,
            "X-NCP-APIGW-API-KEY": settings.NAVER_API_KEY,
        })
    
    if response.status_code == 200:
        return response.json()
    print(response.status_code)
    return None
    