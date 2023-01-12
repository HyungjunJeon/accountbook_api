# 가계부 API

## Users

- 회원가입, 로그인 구현
- api view 방식으로 구현
- 패스워드는 sha256 방식으로 암호화

| Users  |          URL           | Method |                   Data Params                   | Success Response | Error Response |
| :----: | :--------------------: | :----: | :---------------------------------------------: | :--------------: | :------------: |
| signup |    api/user/signup/    |  post  | {email: string, name: string, password: string} |    code: 201     |   code: 400    |
| login  | api/user/login/normal/ |  post  |        {email: string, password: string}        |    code: 200     |   code: 401    |

## Accounts

- 가계부 작성, 수정, 삭제, 리스트 조회, 세부 내역 조회 구현
- api view 방식으로 구현
- 로그인하지 않은 경우 접근 제한 처리

| Accounts |             URL              | Method |               Data Params                | Success Response |       Error Response       |
| :------: | :--------------------------: | :----: | :--------------------------------------: | :--------------: | :------------------------: |
|  create  |     api/accounts/create/     |  post  | access token,{amount: int, memo: string} |    code: 201     | code: 401(토큰 미 전달 시) |
|   list   |        api/accounts/         |  get   |               access token               |    code: 200     | code: 401(토큰 미 전달 시) |
|  detail  |    api/accounts/<int:pk>     |  get   |               access token               |    code: 200     | code: 401(토큰 미 전달 시) |
|  update  | api/accounts/update/<int:pk> |  put   | access token,{amount: int, memo: string} |    code: 200     | code: 401(토큰 미 전달 시) |
|  delete  | api/accounts/delete/<int:pk> | delete |               access token               |    code: 200     | code: 401(토큰 미 전달 시) |
