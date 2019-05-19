import os
from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for
from googleapiclient.discovery import build
from operator import itemgetter

app = Flask(__name__)

# connect with google custom search engine
def google_search(search_term):
  service = build("customsearch", "v1", developerKey="AIzaSyCyWXcPBCMrE-PVO97hWjjEkCr_L3c2GYc")
  res = service.cse().list(q=search_term, cx='008154114684342405093:uuxrxyvjqsq', num=10).execute()
  dic = {}
  dic = res['searchInformation']
  if dic['totalResults']!="0":
      return res['items']
  else:
      return 1

# / means root directory, home page
@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

# / index page root
# / call this user function when click the search button from the index page
# / reaction to "form" function that in index.html
@app.route('/search', methods=['POST'])
def user():
  # save number
  k = 0
  list = []
  # save all websites
  list2 = []
  # save website without duplicate
  list3 = []
  list4 = []
  list5 = []
  list6 = []
  list7 = []
  list8 = []
  list9=[]
  recog=[]
  info = []
  kind = []
  table_data = []
  sorted_listall = []
  time = []
  rank = []
  new = []
  new2 = []
  new3 = []

  # extract the input information from the clients
  name = request.form['name']
  method = request.form['method']
  # split the method information extracted from the clients to the mylist
  # ignore the none input and space input
  mylist = method.split(',')
  for i in range(0,len(mylist)):
      mylist[i] = mylist[i].strip()
      if mylist[i]!="":
          key=name+" "+mylist[i]
          if key not in new3:
              new3.append(key)
  for x in range(0, len(new3)):
      mysearch = new3[x]
      k += 1
      # call google custom search engine
      # print links from the search engine results
      results = google_search(mysearch)
      #pprint.pprint(results)
      if results==1:
          recog.append(mysearch)
          if k==len(new3) and len(info)==0:
              return render_template('reempty.html', recog=recog)
          #***********************************
          if k == len(new3):
              for e in range(0, len(list)):
                  if list[e] not in list2:
                      list2.append(list[e])
              # list3 calculate the appearance of each website
              for e in range(0, len(list2)):
                  temp = list.count(list2[e])
                  list3.append(temp)
              # table data save the website with its appearance
              for i in range(0, len(list)):
                  list4.append(i)
                  list5.append('1')
              table_data = [[list2[i], list3[i], list4[i], list5[i], list9[i]] for i in range(0, len(list2))]
              table_data = sorted(table_data, key=itemgetter(1), reverse=True)
              for i in range(0, len(table_data)):
                  table_data[i][2] = i
              for i in range(0, len(info)):
                  list7.append('0')
                  list8.append('0')

              listall = [[info[a], kind[a], list7[a], list8[a], rank[a]] for a in range(0, len(info))]
              for a in range(0, len(info)):
                  print(listall[a])
              for t in range(0,len(listall)):
                  print(t)
              for i in range(0, len(table_data)):
                  list6.append(table_data[i])
                  for m in range(0, len(listall)):
                      if not urlparse(listall[m][0]).scheme:
                          listall[m][0] = 'https://' + listall[m][0]
                      parsed_m = urlparse(listall[m][0])
                      judge = '{uri.netloc}/'.format(uri=parsed_m)
                      if judge.startswith('www.'):
                          judge = judge[4:]
                      if table_data[i][0] == judge:
                          listall[m][2] = table_data[i][2]
                          list6.append(listall[m])

              i = 0
              while i <= (len(list6) - table_data[list6[len(list6) - 1][2]][1]):
                  # print(i)
                  b = []
                  a = list6[i][1]
                  b.append(list6[i + 1][1])
                  c = list6[i + 1][1]
                  time = 1
                  if int(a) != 1:
                      if int(a) == 2:
                          if c != list6[i + 2][1]:
                              time += 1;
                      if int(a) >= 3:
                          for m in range(i + 2, int(a) + i + 1):
                              if list6[m][1] not in b:
                                  b.append(list6[m][1])
                                  time += 1
                  list6[i][1] = time
                  i = i + int(a) + 1


              for e in range(0, len(list6)):
                  if list6[e][3] == '1':
                      new.append(list6[e])
              new = sorted(new, key=itemgetter(1), reverse=True)
              for e in range(0, len(new)):
                  print(new[e])
              for i in range(0, len(new)):
                  new2.append(new[i])
                  for m in range(0, len(listall)):
                      if not urlparse(listall[m][0]).scheme:
                          listall[m][0] = 'https://' + listall[m][0]
                      parsed_m = urlparse(listall[m][0])
                      judge = '{uri.netloc}/'.format(uri=parsed_m)
                      if judge.startswith('www.'):
                          judge = judge[4:]
                      if new[i][0] == judge:
                          listall[m][2] = new[i][2]
                          new2.append(listall[m])
      else:
          for i in range(1, 11):
              tem=i;
              rank.append(i)
              print(rank)
          #print(list_rank)
          for result in results:
              title = result['title']
              link = result['formattedUrl']
              info.append(link)
              kind2 = new3[x]
              kind2=kind2[len(name)+1:]
              kind.append(kind2)
              #print(link)
              if not urlparse(link).scheme:
                  link = 'https://' + link
              parsed_url = urlparse(link)
              domain = '{uri.netloc}/'.format(uri=parsed_url)
              domain2 = '{uri.scheme}://'.format(uri=parsed_url)

              if domain.startswith('www.'):
                  domain = domain[4:]
              domain3 = domain2 + domain
              if domain3 not in list9:
                  list9.append(domain3)
              list.append(domain)
          # list2 have the elements in list without duplicate
          if k == len(new3):
              for e in range(0, len(list)):
                  if list[e] not in list2:
                      list2.append(list[e])
              # list3 calculate the appearance of each website
              for e in range(0, len(list2)):
                  temp = list.count(list2[e])
                  list3.append(temp)
              # table data save the website with its appearance
              for i in range(0, len(list)):
                  list4.append(i)
                  list5.append('1')
              table_data = [[list2[i], list3[i], list4[i], list5[i], list9[i]] for i in range(0, len(list2))]
              table_data = sorted(table_data, key=itemgetter(1), reverse=True)
              for i in range(0, len(table_data)):
                  table_data[i][2] = i
              for i in range(0, len(info)):
                  list7.append('0')
                  list8.append('0')

              listall = [[info[a], kind[a], list7[a], list8[a], rank[a]] for a in range(0, len(info))]
              for i in range(0,len(kind)):
                  print(kind[i])
              for a in range(0, len(info)):
                  print(listall[a])
              for t in range(0,len(listall)):
                  print(t)
              for i in range(0, len(table_data)):
                  list6.append(table_data[i])
                  for m in range(0, len(listall)):
                      if not urlparse(listall[m][0]).scheme:
                          listall[m][0] = 'https://' + listall[m][0]
                      parsed_m = urlparse(listall[m][0])
                      judge = '{uri.netloc}/'.format(uri=parsed_m)
                      if judge.startswith('www.'):
                          judge = judge[4:]
                      if table_data[i][0] == judge:
                          listall[m][2] = table_data[i][2]
                          list6.append(listall[m])

              i = 0
              while i <= (len(list6) - table_data[list6[len(list6) - 1][2]][1]):
                  # print(i)
                  b = []
                  a = list6[i][1]
                  b.append(list6[i + 1][1])
                  c = list6[i + 1][1]
                  time = 1
                  if int(a) != 1:
                      if int(a) == 2:
                          if c != list6[i + 2][1]:
                              time += 1;
                      if int(a) >= 3:
                          for m in range(i + 2, int(a) + i + 1):
                              if list6[m][1] not in b:
                                  b.append(list6[m][1])
                                  time += 1
                  list6[i][1] = time
                  i = i + int(a) + 1


              for e in range(0, len(list6)):
                  if list6[e][3] == '1':
                      new.append(list6[e])
              new = sorted(new, key=itemgetter(1), reverse=True)
              for e in range(0, len(new)):
                  print(new[e])
              for i in range(0, len(new)):
                  new2.append(new[i])
                  for m in range(0, len(listall)):
                      if not urlparse(listall[m][0]).scheme:
                          listall[m][0] = 'https://' + listall[m][0]
                      parsed_m = urlparse(listall[m][0])
                      judge = '{uri.netloc}/'.format(uri=parsed_m)
                      if judge.startswith('www.'):
                          judge = judge[4:]
                      if new[i][0] == judge:
                          listall[m][2] = new[i][2]
                          new2.append(listall[m])

  # there is no data returned from the search engine
  if len(info)==0 and len(recog) != 0:
    return render_template('reempty.html', recog=recog)
  # all the information clients required has data returned
  elif len(recog)==0:
    return render_template('result.html', new2=new2,k=k)
  # some of the information clients required has data returned
  else:
    return render_template('results2.html', new2=new2,k=k,recog=recog)

@app.route('/back', methods=['POST'])
def back():
  return render_template('index.html')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)