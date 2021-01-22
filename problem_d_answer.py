import json
from pprint import pprint

# 가장 높은 수익을 창출한 영화의 제목을 조사

def max_revenue(movies):
    # 가장 높은 수익을 저장하기 위한 변수 생성
    max_revenue = 0
    # 가장 높은 수익인 영화의 제목을 저장하기 위한 변수 생성
    max_movie_title = ''
    # 모든 영화를 하나씩 조사
    for movie in movies:
        # 영화의 id를 통해 movies 폴더에 있는 json 파일들을 open
        movie_id = movie['id']
        detail_info_json = open(f'data/movies/{movie_id}.json', encoding='UTF-8')
        # json 파일을 python에서 사용하기 위한 load함수
        detail_info = json.load(detail_info_json)
        # 영화의 수익이 max라면
        if max_revenue < detail_info['revenue']:
            # 수익과 영화제목을 변수에 각각 저장
            max_revenue = detail_info['revenue']
            max_movie_title = detail_info['title']
    # 영화 제목을 리턴
    return max_movie_title
                
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))