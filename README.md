# pjt01

## problem A

- 영화 정보 중에서 필요한 정보만 추출하기

- dictionary를 만들어서 필요한 key값을 만들고, 넘어온 dictionary 데이터에서 key를 통해 value를 얻고 저장한다.

  ```{python}
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
  ```

- json 사용
  1. import json
  2. json_data = open('json파일의 경로 및 이름', encoding='UTF-8')
  3. dict_data = json.load(json_data)



## problem B

- 영화의 genre id를 통해 genre name을 추출하기
- problem A와 같이 dictionary를 만들고, value를 찾아 저장
- for문을 통해 genres List에 있는 genre id를 모두 조사
- 2중 for문을 통해 각 genre id마다  영화의 genre id와 같은지 비교
- for문의 genre id와 영화의 genre id가 같을 때, 그 dictionary에 있는 genre name을 얻고 저장

```{python
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
```

- genres도 list, movie['genre_id']도 list여서 두 개의 리스트에 있는 정보를 비교하기 위해 고민을 많이 함



## problem C

- problem B를 응용하여 여러 개의 영화들을 조사
- 영화 정보들을 담을 list만 먼저 준비하고, problem B에 있던 코드를 for문 안에 넣어서 해결

```{python}
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
```



## problem D

- 영화의 수익 정보를 조사해서, 가장 높은 수익을 기록한 영화의 제목 얻기
- 수익을 비교하기 위한 변수, 가장 높은 수익을 기록한 영화의 제목을 저장하기 위한 변수 생성
- for문을 통해 모든 영화를 하나씩 조사
- 영화의 상세정보가 id.json 형식의 파일에 저장되어 있기 때문에 id를 통해 json 파일에 접근
- f-string을 활용 (f'경로/{id}.json')

```{python}
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
```



## problem E

- 영화들의 개봉일을 조사해 12월에 개봉한 영화들을 추출하기
- 영화를 담을 list 생성
- problem D와 동일하게 f-string을 활용하여 json 파일에 접근
- 영화의 개봉일이 str타입의 yyyy-mm-dd로 되어있어 string[5:7]을 통해 mm을 추출
- mm == '12'인 경우 그 영화의 제목을 list에 추가

```{python
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
```

