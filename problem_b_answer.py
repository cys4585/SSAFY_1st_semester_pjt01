import json
from pprint import pprint

# 한 영화의 장르 id를 조사해서 장르 이름 데이터 만들기

def movie_info(movie, genres):
    # 필요한 정보만 담기위한 dictionary 생성
    new_data = {}
    new_data['id'] = movie['id']
    new_data['title'] = movie['title']
    new_data['poster_path'] = movie['poster_path']
    new_data['vote_average'] = movie['vote_average']
    new_data['overview'] = movie['overview']
    # 장르이름은 일단 비워두기
    new_data['genre_names'] = []
    # genres에는 (genre id와 genre name)들이 묶여서 저장되어있음
    # genre id를 조사해서 그 dictionary의 genre name을 new_data['genre_names']에 저장하면 됨
    for g in genres:
        # 영화의 genre id를 조사
        for genre_id in movie['genre_ids']:
            # 영화의 genre id와 genres의 genre id가 같을 때
            if genre_id == g['id']:
                # 그 장르 이름을 new_data['genre_names'] 리스트에 추가
                new_data['genre_names'] += [g['name']] 

    return new_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))