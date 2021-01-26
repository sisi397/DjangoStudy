from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.

def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    if req.method=='POST':
        username = req.POST.get('username', None)
        useremail = req.POST.get('useremail', None)

        err = {}

        if not (useremail and usrename):
            err['err']='유효성이 잘못되었습니다.'
            return render(req, 'login.html', err)
        else:
            member = Members.objects.get(username=username)

            if useremail == member.useremail :
                req.session['user'] = member.id
                return redirect('/members')
            else:
                err['err'] = "비밀번호가 잘못되었습니다."
                return render(req, "login.html", err)

            return HttpResponse(f"<h1>{member.useremail}</h1>")
        return redirect('/')

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']

        member = Members(
                username = username,
                useremail = email
                )
        member.save()
        res_data={}
        res_data['res'] = '등록성공'
        return render(req, 'signup.html', res_data)
    return render(req, 'signup.html')

def login_after(req):
    user_id = req.session.get('user')

    if user_id:
        return HttpResponse(f"로그인 유저 {user_id}")

    return redirect("/login")

def logout(req):
    if req.session.get('user'):
        del(req.session['user'])

        return redirect("/")

def index(request):
    context = {"loop_1" : range(1, 32)}
    return render(request, "todo.html", context)

def my_novel(request, character1, character2):
    character = {"ch1":character1, "ch2":character2}
    return render(request, "novel.html", character)
