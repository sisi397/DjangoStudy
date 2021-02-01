# Django 사용법

프로젝트(newproject) 생성
```
django-admin startproject newproject
```

프로젝트 안에 앱(members) 생성
```
cd newproject/
django-admin startapp members
```

opentutorials/settings.py에 모든 ip또는 본인 ip를 허용하도록 설정, 생성한 앱 등록
```
allowed_hosts=['*']
INSTALLED_APPS=[
  'members'
  ]
```

members/models.py에 모델 만들기
```
class Users(models.Model):
  username = models.CharField(max_length=30, verbose_name="name")
  password = models.CharField(max_length=30, verbose_name="pass")
```

객체를 만들어 DB에 모델 적용
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### admin 설정
```
python3 manage.py createsuperuser
```
members/admin.py에 만든 모델을 admin 사이트에 등록
```
from .models import Users
admin.site.register(Users)
```
### url 설정
newproject/newproject/urls.py 파일에서 url 설정
```
import include
path('members/', include('members.urls'))
```
-> IP주소:8000/members 입력 시 members view를 열어 준다.

newproject/members안에 urls.py 파일을 만든 후 다음을 입력해준다.
```
from django.urls import path
from . import views
urlpatterns = [
  path('register', views.register, name='register'),
]
```
-> IP주소:8000/members/register 라고 접속 했을 때 views.py의 reigster 함수를 실행시킨다.

### views.py
newproject/members/views.py에 다음을 입력한면 register.html을 실행시키게 된다.
register.html은 members에 templates 폴더에 넣는다.
```
def register(request):
  return render(request, 'register.html')
```
templates를 사용하기 위해서는 settings.py에 templates 폴더를 사용하겠다고 말해줘야 한다.
```
TEMPLATES=[
  { 'DIRS' : ['tempaltes'] }
]
```
### 정적 파일 사용
정적 파일 : js, css, image, font 등과 같이 개발자가 사전에 미리 서버에 저장해둔 파일.  
정적 파일을 사용하기 위해서는 settings.py에 어떤 폴더에 위치한 파일을 사용할지 알려줘야한다.  
정적파일을 가져오기 위해서는 html 파일 가장 상단에 {% load static %}를 추가하고 <img src="{% static 'cat.jpg'%}와 같이 사용한다.  
```
STATIC_URL = '/static/'
STATICFILES_DIRS=[
  BASE_DIR / "images"
 ]
 ```
