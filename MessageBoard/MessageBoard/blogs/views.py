from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blogs.models import blog
from django.views.decorators.csrf import csrf_exempt

def index(req):
    myblogs = blog.objects.filter()
    res = {'blogs':myblogs}
    return render_to_response("home.html",res)

@csrf_exempt
def delete(req):
    try:
        blog_id = req.POST.get('blogid', '')
        oneblog = blog.objects.get(id=int(blog_id))
        oneblog.delete()
        res = {"result":"suc"}
        json_data = json.dumps(res)
        return HttpResponse(json_data,content_type="application/json")
    
    except:
        return render_to_response("error.html")

def browse(req,blog_id=''):
    try:
        oneblog = blog.objects.get(id=int(blog_id))
        res = {'blog':oneblog}
        return render_to_response("blog.html",res)
    except:
        return render_to_response("error.html")
    
@csrf_exempt
def modify(req):
    try:
        blog_id = req.POST.get('blogid', '')
        title = req.POST.get('title', '')
        contents = req.POST.get('contents', '')
        oneblog = blog.objects.get(id=int(blog_id))
        oneblog.title = title
        oneblog.contents = contents
        oneblog.save()
        res = {"result":"suc"}
        json_data = json.dumps(res)
        return HttpResponse(json_data,content_type="application/json")
    except:
        return render_to_response("error.html")

def correctData(req,blog_id=''):
    try:
        oneblog = blog.objects.get(id=int(blog_id))
        res = {'blog':oneblog}
        return render_to_response("correct.html",res)
    except:
        return render_to_response("error.html")
    
    
def toWrite(req):
    return render_to_response("write.html")

@csrf_exempt
def publish(req):
    try:
        title = req.POST.get('title', '')
        contents = req.POST.get('contents', '')
        oneblog = blog(title=title,contents=contents)
        oneblog.save()
        return index(req)
    except:
        return render_to_response("error.html")
# Create your views here.

