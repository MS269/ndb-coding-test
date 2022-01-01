# 개발형 코딩 테스트

**정해진 목적에 따라서 동작하는 완성된 프로그램을 개발**하는 것을 요구하는 코딩 테스트 유형이다.

| 알고리즘 코딩 테스트              | 개발형 코딩 테스트                 |
| --------------------------------- | ---------------------------------- |
| 요구 사항에 맞는 하나의 모듈 개발 | 완성도 높은 하나의 프로그램을 개발 |
| 시간 복잡도와 공간 복잡도 분석    | 모듈을 적절히 조합하는 능력 요구   |

일부 기업은 해커톤을 통해 채용을 진행한다.

- **해커톤(Hackathon)**이란 단기간에 아이디어를 제품화하는 프로젝트 이벤트이다.

개발형 코딩 테스트는 분야에 따라 상세 요구사항이 다를 수 있다.

- 예시) 웹 서버 개발: 스프링(Spring), 장고(Django) 등의 서버 개발 프레임워크 활용

하지만 분야에 상관없이 꼭 알아야 하는 개념과 도구에 대해서 학습할 필요가 있다.

- 서버, 클라이언트, JSON, REST API, ...

## 서버(Server)와 클라이언트(Client)

클라이언트가 요청(Request)을 보내면 서버가 응답(Response)을 한다.

### 클라이언트 = 고객

서버로부터 요청을 보내고 응답이 도착할 때까지 기다린다.

서버로부터 응답을 받은 뒤에는 서버의 응답을 화면에 출력한다.

- 예시) 웹 브라우저: 서버로부터 받은 HTML, CSS 코드를 화면에 적절한 형태로 출력한다.

### 서버 = 서비스 제공자

클라이언트로부터 받은 요청을 처리해 응답을 전송한다.

- 예시) 웹 서버: 로그인 요청을 받아 아이디와 비밀번호가 정확한지 검사하고 그 결과를 응답한다.

## HTTP 개요

**HTTP(HyperText Transfer Protocol)**는 **웹상에서 데이터를 주고받기 위한 프로토콜**을 의미한다.

- 보통은 웹 문서(HTML 파일)를 주고받는 데 사용된다.
- 모바일 앱 및 게임 개발 등에서 특정 형식의 데이터를 주고받는 용도로도 사용된다.

클라이언트는 **요청의 목적**에 따라서 적절한 HTTP 메서드를 이용해 통신을 진행한다.

- 대표적인 **HTTP 메서드**는 다음과 같다.

| HTTP 메서드 | 설명                             | 사용 예시                   |
| ----------- | -------------------------------- | --------------------------- |
| GET         | 특정한 데이터의 조회를 요청한다. | 특정 페이지 접속, 정보 검색 |
| POST        | 특정한 데이터의 생성을 요청한다. | 회원가입, 글쓰기            |
| PUT         | 특정한 데이터의 수정을 요청한다. | 회원 정보 수정              |
| DELETE      | 특정한 데이터의 삭제를 요청한다. | 회원 정보 삭제              |

### 파이썬 웹 요청 예제: GET 방식

```python
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)
```

## REST의 등장 배경

**HTTP**는 GET, POST, PUT, DELETE 등의 **다양한 HTTP 메서드를 지원**한다.

- 실제로는 서버가 각 메서드의 기본 설명을 따르지 않아도 프로그램을 개발할 수 있다.
- 하지만 저마다 다른 방식으로 개발하면 문제가 될 수 있어 기준이 되는 아키텍처가 필요하다.

## REST의 개요

**REST(Representational State Transfer)**는 **각 자원(Resource)에 대하여 자원의 상태에 대한 정보를 주고받는 개발 방식**을 의미한다.

REST의 **구성 요소**

- 자원(Resource): URI를 이용
- 행위(Verb): HTTP 메서드를 이용
- 표현(Representations): 페이로드(Payload)를 이용

예시) HTTP 패킷 정보

- URI: https://www.google.com/users
- HTTP Method: POST
- Payload: {"id": "ms269", "password": "991211"}

## REST API란?

**API(Application Programming Interface)**: **프로그램이 상호작용하기 위한 인터페이스**를 의미한다.

**REST API**: **REST 아키텍처를 따르는 API**를 의미한다.

**REST API 호출**: **REST 방식을 따르고 있는 서버에 특정한 요청을 전송**하는 것을 의미한다.

## JSON

**JSON(JavaScript Object Notation)**: 데이터를 주고받는 데 사용하는 경량의 데이터 형식

JSON 데이터는 **키와 값의 쌍**으로 이루어진 데이터 객체를 저장한다.

### JSON 객체 사용 예제

```python
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "ms269",
    "password": "991211"
}

# 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent=4)
print(json_data)
```

### JSON 객체 파일 저장 예제

```python
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "ms269",
    "password": "991211"
}

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent-4)
```

## REST API를 호출하여 회원 정보를 처리하는 예제

```python
import requests

# REST API 경로에 접속하여 응답 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = request.get(url=target)

# 응답 데이터가 JSON 형식이므로 파이썬 객체로 변환
data = response.json()

# 모든 사용자 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user["name"])

print(name_list)
```
