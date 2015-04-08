from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Board.models import blog
from django.views.decorators.csrf import csrf_exempt

def index(req):
    blogs = blog.objects.filter()
    '''
    bloglist = []
    for item in blogs:
        tmpblog = {'id':item.id,'title':item.title,'contents':item.contents[0:(100>len(item.contents) and len(item.content) or 100)]+"..."}
        bloglist.append(tmpblog)
    '''
    res = {'blogs':blogs}
    print "............................"
    return render_to_response("home.html",res)

@csrf_exempt
def delete(req):
    try:
        blog_id = req.POST.get('blogid', '')
        print "delete....",blog_id
        oneblog = blog.objects.get(id=int(blog_id))
        oneblog.delete()
        print "delete...."
        res = {"result":"suc"}
        print res
        json_data = json.dumps(res)
        print json_data
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
        print "int to ..."
        blog_id = req.POST.get('blogid', '')
        print blog_id
        title = req.POST.get('title', '')
        print title;
        contents = req.POST.get('contents', '')
        print contents
        oneblog = blog.objects.get(id=int(blog_id))
        oneblog.title = title
        oneblog.contents = contents
        oneblog.save()
        res = {"result":"suc"}
        json_data = json.dumps(res)
        print json_data
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
        print "sha"
        oneblog = blog(title=title,contents=contents)
        print "douwo"
        oneblog.save()
        print "douwo2"
        return index(req)
    except:
        return render_to_response("error.html")
# Create your views here.

