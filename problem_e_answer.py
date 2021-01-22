import json
from pprint import pprint

# 12월 개봉작 조사

def dec_movies(movies):
    # 영화의 제목들을 담을 list 생성
    movies_list = []
    # 모든 영화를 순차적으로 조사
    for movie in movies:
        # 영화의 id를 통해 movies 폴더에 있는 json 파일을 open
        movie_id = movie['id']
        detail_info_json = open(f'data/movies/{movie_id}.json', encoding='UTF-8')
        # json 파일을 사용하기 위한 코드
        detail_info = json.load(detail_info_json)
        # 개봉월을 저장
        release_month = detail_info['release_date'][5:7]
        # 개봉월이 12월이면 그 영화의 제목을 list에 추가
        if release_month == '12':
            movies_list.append(detail_info['title'])
    return movies_list
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))