from datetime import date, timedelta, datetime
import math
import requests
import pandas as pd
import numpy as np
import re
# import json # requests에 내장 .json()이 있다
from bs4 import BeautifulSoup as bs

## 지표
class Data_Management:
    day_list = [] # 총 리스트

  # 날짜 구하는 함수
    def daterange(self, start_date, end_date):  
      for n in range(int((end_date - start_date).days)):
          yield start_date + timedelta(n)

  # 원하는 기간 배열로 생성
    def set_period_to_list(self, start_date,start_month, end_date,end_month):
      for i in range(start_date, end_date+1):  
          year_list=[] # 1년단위로 끊기 위한 리스트
          
          start_date = date(i, start_month, 1)  # 시작 날짜
          end_date = date(i, end_month+1, 1)  # 끝 날짜의 다음 날
          print(start_date,end_date)
          for single_date in self.__daterange(start_date, end_date):  
              year_list.append(single_date.strftime("%Y%m%d")) # 날짜 형식 포맷
              year_list = [int(i) for i in year_list]  # str 형태를 int로 변환

          self.day_list.append(year_list)
      print(self.day_list)

  # 수온
    def get_temp(self):
      a_list = []
      for i in range(len(self.day_list)):
          for day in self.day_list[i]:     
              req = requests.get("https://www.khoa.go.kr/api/oceangrid/tidalBuTemp/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
              data = bs(req.text, 'html.parser')
              jsonData = req.json()

              result = []
              try:
                  for i in jsonData.get("result").get("data"):
                      result.append(i['water_temp'])
              except Exception: # 중간에 비는 날이 있다면
                  pass
              result_a = [float(i) for i in result] # 실수형으로 변환
  #             for i in result_a:
  #                 print(i)
              print(day,"-------------------------------------------")
              avg = np.round(np.mean(result_a),2)
              print(avg)
              a_list.append([day,avg])
      print("수온",a_list)
      return a_list

  # 수온 하루치
  # day : 20220108
    def get_temp_oneday(self,day):
      req = requests.get("https://www.khoa.go.kr/api/oceangrid/tidalBuTemp/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
      jsonData = req.json()

      result = []
      try:
          for i in jsonData.get("result").get("data"):
              result.append(i['water_temp'])
      except Exception: # 중간에 비는 날이 있다면
          pass
      result_a = [float(i) for i in result] # 실수형으로 변환
      print(day,"-------------------------------------------")
      avg = np.round(np.mean(result_a),2)
      print(avg)
      return avg


  # 파고 
    def get_digging(self):
      b_list = []
      for i in range(len(self.day_list)):
          for day in self.day_list[i]:     
                  req = requests.get("https://www.khoa.go.kr/api/oceangrid/obsWaveHight/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
                  data = bs(req.text, 'html.parser')
                  jsonData = req.json()

                  result = []
                  try:
                      for i in jsonData.get("result").get("data"):
                          result.append(i['wave_height'])
                  except Exception: # 중간에 비는 날이 있다면
                      pass
                  result_a = [float(i) for i in result]
                  print(day,"-------------------------------------------")
                  avg = np.round(np.mean(result_a),2)
                  print(avg)
                  b_list.append([avg])

      print('파고',b_list)
      return b_list

  # 파고 하루
    def get_digging_oneday(self,day):
      req = requests.get("https://www.khoa.go.kr/api/oceangrid/obsWaveHight/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
      jsonData = req.json()

      result = []
      try:
          for i in jsonData.get("result").get("data"):
              result.append(i['wave_height'])
      except Exception: # 중간에 비는 날이 있다면
          pass
      result_a = [float(i) for i in result]
      print(day,"-------------------------------------------")
      avg = np.round(np.mean(result_a),2)
      print(avg)
      return avg


  # 풍속
    def get_wind_speed(self):
      c_list = []
      for i in range(len(self.day_list)):
          for day in self.day_list[i]:     
                  req = requests.get("http://www.khoa.go.kr/api/oceangrid/tidalBuWind/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
                  data = bs(req.text, 'html.parser')
                  jsonData = req.json()

                  result = []
                  try:
                      for i in jsonData.get("result").get("data"):
                          result.append(i['wind_speed'])
                  except Exception: # 중간에 비는 날이 있다면
                      pass
                  result_a = [float(i) for i in result]
                  print(day,"-------------------------------------------")
                  avg = np.round(np.mean(result_a),2)
                  print(avg)
                  c_list.append([avg])

      print('풍속',c_list)
      return c_list

  # 풍속 하루
    def get_wind_speed_onday(self, day):
      req = requests.get("http://www.khoa.go.kr/api/oceangrid/tidalBuWind/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
      jsonData = req.json()

      result = []
      try:
          for i in jsonData.get("result").get("data"):
              result.append(i['wind_speed'])
      except Exception: # 중간에 비는 날이 있다면
          pass
      result_a = [float(i) for i in result]
      print(day,"-------------------------------------------")
      avg = np.round(np.mean(result_a),2)
      print(avg)
      return avg

  # 기온
    def get_AirTemp(self):
      airTemp_list = []
      for i in range(len(self.day_list)):
          for day in self.day_list[i]:     
                  req = requests.get("http://www.khoa.go.kr/api/oceangrid/tidalBuAirTemp/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
                  data = bs(req.text, 'html.parser')
                  jsonData = req.json()

                  result = []
                  try:
                      for i in jsonData.get("result").get("data"):
                          result.append(i['air_temp'])
                  except Exception: # 중간에 비는 날이 있다면
                      pass
                  result_a = [float(i) for i in result]
                  print(day,"-------------------------------------------")
                  avg = np.round(np.mean(result_a),2)
                  print(avg)
                  airTemp_list.append([avg])

      print('기온',airTemp_list)
      return airTemp_list


  # 기온 하루
    def get_AirTemp_oneday(self, day):
      req = requests.get("http://www.khoa.go.kr/api/oceangrid/tidalBuAirTemp/search.do?ServiceKey=6tMtfhu2UhiktZk16RGGgA==&ObsCode=TW_0062&Date=%d&ResultType=json" %day)
      jsonData = req.json()

      result = []
      try:
          for i in jsonData.get("result").get("data"):
              result.append(i['air_temp'])
      except Exception: # 중간에 비는 날이 있다면
          pass
      result_a = [float(i) for i in result]
      print(day,"-------------------------------------------")
      avg = np.round(np.mean(result_a),2)
      print(avg)
      return avg

  # 강수량 과거 관측 데이터 하루 지정
    def get_rainfall_oneday(self,day):
      year = int(day/10000)
      month = int(day/100)%10
      today = int(day%100)
      req = requests.get("https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-element.do?stn=159&yy=%d&obs=21"%year)
      soup = bs(req.text, 'html.parser')
      table_tbody = soup.select_one('#weather_table>tbody')
      data_td = table_tbody.select('tr')[today-1].select('td>span')
      if data_td[month].text == u'\xa0': result =-1
      else: result= float(data_td[month].text)
      return result

  # 강수량 지정일
  # 당일 = 0, 내일 = 1, 모레 =2
    def get_rainfall_from_weather(self,idx_day):
      url = 'https://www.weatheri.co.kr/forecast/forecast01.php?rid=1101010100&k=9&a_name=%EB%B6%80%EC%82%B0'
      req = requests.get(url)
      soup = bs(req.text, 'html.parser')
      table_elem= soup.findAll('tr', attrs={'bgcolor':'#FFFFFF','align':'center'})[0]

      rainfall_elem= table_elem.findAll('td',{'style':'cursor:pointer'})
      rainfall=rainfall_elem[idx_day].findAll('font')[3].get_text().split(' ')[0]
      if rainfall == '-': return -1
      
      return float(rainfall)

 
  # (지정) 범위일  DB에 넣기 -> truncate 이후 삽입
  # start_date, end_date 지정
  # -> 결과 여러개 리스트
    def save_sea_data_range_to_db(self, start_date=2022,start_month=1, end_date=2023,end_month=12):
      if start_date <= end_date and 12>= start_month >= 1 and 12 >= end_month >= 1:
          self.__set_period_to_list(start_date,start_month, end_date, end_month)
          df1 = pd.DataFrame(self.get_temp(), columns=['날짜','수온'])
          df2 = pd.DataFrame(self.get_digging(), columns=['파고'])
          df3 = pd.DataFrame(self.get_wind_speed(), columns=['풍속'])
          df4 = pd.DataFrame(self.get_AirTemp(), columns=['기온'])

          # dataframe 병합
          df_all = pd.concat([df1,df2,df3,df4],axis=1)
          df_all.to_csv('sea_data.csv', header='False', encoding='utf-8-sig')
      else: 
          print('기간 맞지 않음')

  # 지정일자 지표들(강수량 제외) 가져오기
  # ex) day = 20220824
    def get_sea_data_day_except_rainfall(self, day): # -> 결과 1개 리스트
      date_day = datetime.strptime(day, '%Y%m%d').date()
      date_today = datetime.now().date()

      if date_day < date_today+timedelta(days=2):

          temp= self.get_temp_oneday(day)
          digging= self.get_digging_oneday(day)
          wind_speed= self.get_wind_speed_onday(day)
          air_temp= self.get_AirTemp_oneday(day)

          print(day,temp,digging,wind_speed,air_temp)
          return [day,temp,digging,wind_speed,air_temp]


  # 지정일자 지표들(강수량 포함) 가져오기
  # ex) day = 20220824
    def get_sea_data_day_include_rainfall(self, day): # -> 결과 1개 리스트
        date_day = datetime.strptime(str(day), '%Y%m%d').date()
        date_today = datetime.now().date()

        if date_day < date_today+timedelta(days=2):
            
            if date_day < date_today: # 20220801 < 20220831(오늘)
                rainfall = self.get_rainfall_oneday(day)
            else:
                idx_day = (date_day - date_today).days
                rainfall =self.get_rainfall_from_weather(idx_day)

            temp= self.get_temp_oneday(day)
            digging= self.get_digging_oneday(day)
            wind_speed= self.get_wind_speed_onday(day)
            air_temp= self.get_AirTemp_oneday(day)

        if rainfall >=1 :
            return '나쁨'    
        elif rainfall > 0:
            return '보통'
        else:
            return (temp *0.7 + digging*2 + wind_speed*1 + air_temp*0.3)
            
            #return [day,temp,digging,wind_speed,air_temp,rainfall]

    def get_data(self, day, datas): # -> 결과 1개 리스트
        date_day = datetime.strptime(str(day), '%Y%m%d').date()
        date_today = datetime.now().date()
        value = dict()
        if date_day < date_today+timedelta(days=2):
            
            if date_day < date_today: # 20220801 < 20220831(오늘)
                value['rainfall'] = self.get_rainfall_oneday(day)
            else:
                idx_day = (date_day - date_today).days
                value['rainfall']=self.get_rainfall_from_weather(idx_day)

            value['water_temp'] = self.get_temp_oneday(day)            
            value['digging'] =self.get_digging_oneday(day)
            value['wind'] =self.get_wind_speed_onday(day)
            value['temp'] =self.get_AirTemp_oneday(day)
            datas.append(value)
            return datas

    # 지표 가중치 계산 
    def cal_temp(self,day):
        weight = (float)(0.3)
        n=self.get_AirTemp_oneday(day)
        
        if n >= 30 : return weight * 1
        elif n >= 27 : return weight * 0.8
        elif n >= 25 : return weight * 0.6
        elif n >= 22 : return weight * 0.4
        else : return weight * 0.2

    def cal_water_temp(self,day):
        weight = (float)(0.7)
        n= round(self.get_temp_oneday(day),0)

        if n >= 24 : return weight * 1
        elif 24 > n >= 22 : return weight * 0.8
        elif 22 > n >= 21 : return weight * 0.6
        elif 21 > n >= 20: return weight * 0.4
        elif 20 > n : return weight * 0.2

    def cal_digging(self,day):
        weight = 2
        n=self.get_digging_oneday(day)

        if 0.5 > n : return weight * 5/5
        elif 1.0 > n >= 0.5 : return weight * 4/5
        elif 1.3 > n >= 1.0 : return weight * 3/5
        elif 1.7 > n >= 1.3 : return weight * 2/5
        elif n >= 1.7 : return weight * 1/5
    
    def cal_wind(self,day):
        weight = 1
        n =self.get_wind_speed_onday(day)
        if 2 > n : return weight * 5/5
        elif 5 > n >= 2 : return weight * 4/5
        elif 8 > n >= 5 : return weight * 3/5
        elif 10 > n >= 8 : return weight * 2/5
        elif n >= 10 : return weight * 1/5
    
    def rainfall(self,day):
        date_day = datetime.strptime(str(day), '%Y%m%d').date()
        date_today = datetime.now().date()
        if date_day < date_today+timedelta(days=2):
            
            if date_day < date_today: # 20220801 < 20220831(오늘)
                rainfall = self.get_rainfall_oneday(day)
            else:
                idx_day = (date_day - date_today).days
                rainfall =self.get_rainfall_from_weather(idx_day)
        return rainfall

    #해수욕 지수 
    def total_value(self,day):
        
        rain_value = self.rainfall(day)
        if rain_value>=1:
            total = 1
        elif rain_value >=0:
            total = 2
        else:
            total = math.trunc(self.cal_temp(day)+self.cal_water_temp(day)+self.cal_digging(day)+self.cal_wind(day))
        return total

