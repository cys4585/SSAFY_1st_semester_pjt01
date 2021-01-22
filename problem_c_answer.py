import json
from pprint import pprint

# 다수의 영화의 장르 id를 조사해서 장르 이름 데이터 만들기

def movie_info(movies, genres):
    # 영화들을 담을 리스트 생성
    new_list = []
    # 모든 영화를 하나씩 조사
    for movie in movies:
        # 영화 정보 중에서 필요한 정보만 추출하기 위한 dictionary 생성
        new_data = {}
        new_data['id'] = movie['id']
        new_data['title'] = movie['title']
        new_data['poster_path'] = movie['poster_path']
        new_data['vote_average'] = movie['vote_average']
        new_data['overview'] = movie['overview']
        # 장르 이름은 일단 비워두고 생성
        new_data['genre_names'] = []
        # genre id를 조사해서 해당하는 id에 맞는 genre name을 저장하기 위해
        # genre.json에서 넘어온 모든 genre id를 하나씩 조사  
        for g in genres:
            # 영화의 장르 id를 조사
            for genre_id in movie['genre_ids']:
                # 영화의 genre id가 genre.json에 있는 id와 일치하면
                if genre_id == g['id']:
                    # genre name을 영화 장르에 추가
                    new_data['genre_names'].append(g['name'])      
        
        new_list.append(new_data)
    return new_list

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))