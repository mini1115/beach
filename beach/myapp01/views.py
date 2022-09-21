import json
from pydoc import render_doc
from urllib import request, response
from django.shortcuts import render,redirect
from myapp01.models import Board,Comment
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp01 import Data
from django.template.loader import render_to_string
import math
import urllib.parse
import datetime 
upload_dir ='C:/Users/DMB-GICT/desktop/djangowork/beach/upload/'
# Create your views here.
# CRUD 작업


def index(request):
  data_Management = Data.Data_Management()
  now = datetime.datetime.now()
  day = now.day
  month = now.month
  year = now.year
  time = repr(year)+'0'+repr(month)+'0'+repr(day)
  # result = data_Management.get_sea_data_day_include_rainfall(int(time))
  data=data_Management.total_value(20220831)
  print(data)
  if data==1:
    return render(request,'index.html',{'img':'bad.png'})
  elif data==2:
    return render(request,'index.html',{'img':'normal.png'})
  else :
    return render(request,'index.html',{'img':'good.png'})
def tour(request):
  return render(request,'tour.html')
def write_form(request):
  return render(request, 'board/insert.html')
#insert 글작성
@csrf_exempt
@csrf_exempt
def insert(request):
   fname=''
   fsize=0
   if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' %(upload_dir, fname),'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()    

   dto = Board(writer=request.POST['writer'],
            title=request.POST['title'],
            content=request.POST['content'],
            filename=fname,
            filesize=fsize
    )
   dto.save()
   return redirect('/list/') 


def list(request):
  page = request.GET.get('page',1)
  # 전체 게시글 수 
  boardCount = Board.objects.all().count() 
  


  # 페이징
  pageSize = 5
  blockPage = 3
  currentPage = int(page)

  start = (currentPage - 1) * pageSize

  totPage = math.ceil(boardCount/pageSize)
  startPage = math.floor((currentPage-1)/blockPage) * blockPage+1
  endPage = startPage + blockPage -1 

  if endPage> totPage:
    endPage = totPage

  boardList = Board.objects.all().order_by('-id')[start:start+pageSize]
  context = {'boardList':boardList,'startPage' : startPage,'blockPage': blockPage, 'endPage':endPage , 'currentPage':currentPage,'totPage':totPage,'range':range(startPage,endPage+1)}
  return render(request, 'board/list.html',context)

#download count
def download_count(request):
  id = request.GET['id']
  print('id:',id)
  dto = Board.objects.get(id = id)
  dto.down_up()
  dto.save()
  count = dto.down

  return JsonResponse({'id':id,'count':count})


def download(request):
  id = request.GET['id']
  print('id: ' , id)
  dto = Board.objects.get(id = id)
  path = upload_dir + dto.filename
  filename = urllib.parse.quote(dto.filename)
  print('filename:' , filename)
  with open(path, 'rb') as file:
    response = HttpResponse(file.read(),content_type='application/octet-stream')
    response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(filename)
    return response

#오늘의 상세지수
def value(request):
  data_Management = Data.Data_Management()
  now = datetime.datetime.now()
  day = now.day
  month = now.month
  year = now.year
  time = repr(year)+'0'+repr(month)+'0'+repr(day)
  #int(time)
  result = []
  
  data_Management.get_data(20220831,result)
  # result = [{ temp, wind , rainfall, digging , water_temp}]

  return render(request,'beach/value.html', {'data':result} )

@csrf_exempt
#과거 지수 조회    
def search(request):

  data_Management = Data.Data_Management()

  
  data=data_Management.total_value(int(20220831))
  result = [] 
  data_Management.get_data(20220831,result)

  if data==1:
    return render(request,'beach/search.html',{'img':'bad.png', 'datas':result})
  elif data==2:
    return render(request,'beach/search.html',{'img':'normal.png','datas':result})
  else :
    return render(request,'beach/search.html',{'img':'good.png','datas':result})

# @csrf_exempt
# def fix(request):
#   data_Management = Data.Data_Management()
#   date = request.POST.get('date')
#   print('날짜값',date)
#   new_date = int(date.replace('-',''))
#   print("새날짜",new_date)
#   data=data_Management.total_value(new_date)
#   if data==1:
#     return JsonResponse(json.load(response),{'img':'bad.png'})
#   elif data==2:
#     return JsonResponse(json.load(response),{'img':'normal.png'})
#   else :
#     return JsonResponse(json.load(response),{'img':'good.png'})

@csrf_exempt
def test(request):
  date = request.POST.get('date')
  print(date)
  new_date = int(date.replace('-',''))
  print(new_date)
  data_Management = Data.Data_Management()
  result = []
  
  data_Management.get_data(new_date,result)
  print("성공")
  response = render_to_string("beach/search.html", context={"datas": result})
  return JsonResponse(response,safe=False)