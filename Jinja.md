# Jinja Template
Flask : 파이썬을 기반으로 한 웹 프레임워크 중 하나. 쉽고 결과물이 빨리 나옴.  
Jinja : html 문서의 한계를 뛰어넘기 위한 양식  


html의 한계1. 정적이다. ->  템플릿 파일을 열 때 뷰에서 인자를 전달하여 템플릿에서 호출하도록 하자!  
```
{{뷰에서 전달한 인자}}
{% Jinja template 작성. 여기에 if, for 사용 가능 %}

views.py에
context = {"loop":range(10)}
render(req, 'a.html', context)로 인자를 보낼 수 있다.

예시)
  {% for i in loop %}
  <div> 안녕하세요? <div>
  {% endfor %}
```
html의 한계2. 반복 코드를 계속 입력해야 하는 경우도 생긴다.
```
부모에 {% block content %} ~~ {% endblock %}을 작성해주고
자식에서 {% extends 'mother.html' %} {% block content %} ~~ {% endblock %}을 작성해주면
~~ 사이에 자식태그가 들어가서 중복된 코드를 줄일 수 있다.
```
