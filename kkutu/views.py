from django.shortcuts import render

# Create your views here.
year_dic = {1:"하루종일", 2:"내일까지", 3:"할일없이",4:"배고픈데",5:"밥먹는데",6:"갑자기",7:"어디선가",8:"이제부터",9:"새벽에",0:"일어나니"}
month_dic = {1:"코딩하는",2:"놀고먹는",3:"고장난",4:"파일 날아간",5:"저장 안한",6:"잘 돌아가는",7:"키보드 고장난", 8:"에러난",9:"나타난",10:"없어진",11:"이상한",12:"찾아온"}
day_dic = {1:"개발자",2:"블루스크린",3:"컨트롤 S",4:"운영진",5:"창업자",6:"탈주닌자",7:"대학생",8:"컴퓨터",9:"파이썬",10:"장고",11:"컴파일 에러",12:"런타임 에러",13:"프로젝트 팀장",14:"프로젝트 팀원",15:"멋쟁이 사자",16:"디자이너",17:"워드 카운트",18:"블로그",19:"깃허브",20:"멋쟁이 고양이",21:"VSC",22:"웹서비스",23:"컴퓨터 고쳐주는 선배",24:"노트북 골라주는 선배",25:"비전공자",26:"신입개발자",27:"스트레스성 위염",28:"정수리탈모",29:"M자 탈모",30:"프로 술꾼",31:"아이스크림에 감자 찍어먹는 누렁이"}
def home(request):
    return render(request, 'home.html')

def result(request):
    year = int(request.GET['year'])
    month = int(request.GET['month'])
    day = int(request.GET['day'])
    year_name = year_dic[year]
    month_name = month_dic[month]
    day_name = day_dic[day]

    return render(request, 'result.html',{'year_name':year_name, 'month_name':month_name, 'day_name':day_name})