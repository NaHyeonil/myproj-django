# myproj-django

## `.env` 예시

```angular2html
SECRET_KEY = SECRET KEY
DEBUG=False
ALLOWED_HOSTS = api.hyeonil.com
CORS_ALLOWED_ORIGINS = www.hyeonil.com

ACCESS_TOKEN_LIFETIME_DAYS=7
ACCESS_TOKEN_LIFETIME_HOURS=0
ACCESS_TOKEN_LIFETIME_MINUTES=0

# 하나의 환경변수에서 DB 정보를 입력토록 도와줍니다.
DATABASE_URL=mysql://myuser:mypassword@127.0.0.1:3306/mydb
```