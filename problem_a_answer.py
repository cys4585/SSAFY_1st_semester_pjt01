import json
from pprint import pprint

# 영화 정보 중에서 필요한 정보만 추출하기

def movie_info(movie):
    # 필요한 정보만 따로 담기위한 dictionary 생성
    new_data = {}
    # 넘어온 movie 정보 중에서 필요한 정보만 저장
    new_data['id'] = movie['id']
    new_data['title'] = movie['title']
    new_data['poster_path'] = movie['poster_path']
    new_data['vote_average'] = movie['vote_average']
    new_data['overview'] = movie['overview']
    new_data['genre_ids'] = movie['genre_ids']
    return new_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    pprint(movie_info(movie_dict))