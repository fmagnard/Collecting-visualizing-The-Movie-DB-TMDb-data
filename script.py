#!/usr/bin/python
# coding: utf-8

from urllib2 import Request, urlopen
import json
import time
import fileinput

#creation of the files in writting mode
f_movie_id_name= open("movie_ID_name.txt", "w")
f_movie_id_sim_movie_id= open("movie_ID_sim_movie_ID.txt","w")



headers = {'Accept': 'application/json'}
#id Science Fiction = 878 so genre=878 in the url request
page = 1

#we need 300 movies, There are only 20 movies per page so we need to pass through 15 pages
while page < 16:

	url1 = "http://api.themoviedb.org/3/discover/movie?api_key=d48608b6b79437317a0d1430af4a3378&include_all_movies=true&with_genres=878&release_date.gte=2000-01-01&page=%s" % page
	request = Request(url1, headers=headers)
	response_body = urlopen(request).read()
	response_body = json.loads(response_body)
	results = response_body["results"]

	for result in results :
		#we stock the id and the title of each movie in the movie_id_name file
		f_movie_id_name.write(str(result["id"])+", "+str(result["title"].encode('utf8'))+"\n")
		print "%s,%s" %(result["id"], result["title"].encode('utf8'))
		
		#For each movies id we look for the similar one
		movie_id = result["id"]
		url2 = "http://api.themoviedb.org/3/movie/%s/similar?api_key=d48608b6b79437317a0d1430af4a3378" % movie_id
		request2 = Request(url2, headers=headers)
		response_body2 = urlop%en(request2).read()
		response_body2 = json.loads(response_body2)
		results2 = response_body2["results"]		

		i=1
		for result2 in results2 :
			#we limit the request to 5 similarity per movies
			if i<6:
				f_movie_id_sim_movie_id.write(str(movie_id)+", "+str(result2["id"])+"\n")
				i=i+1
			else:
				1	
				#else do nothing
		time.sleep(1.5)	
		# we are allow to do 40 request in 10s. Every 6 requests (1 for the movie id_title + 5 for the similarity) we need a break of 1.5s 
		

		
	page= page+1



f_movie_id_name.close()
f_movie_id_sim_movie_id.close()
#we need to modify the file so firstly we will read it, modify the data and finally write the modified data
f_movie_id_sim_movie_id= open("movie_ID_sim_movie_ID.txt","r")

pairs=set()
#we create a set which will work on the unicity of each couple.
for line in f_movie_id_sim_movie_id :
	element = line.split('\n')
	element1 = element[0].split(', ')
	if (element1[1]+", "+element1[0]) in pairs:
		if element1[1]<element1[0]:
			pairs.update([(element1[1]+", "+element1[0])])
		else:
			pairs.update([(element1[0]+", "+element1[1])])
			a=set([(element1[1]+", "+element1[0])])
			pairs.difference_update(a)
	else :
		pairs.update([(element1[0]+", "+element1[1])])
			
print pairs

liste=[]
liste.extend(pairs)

f_movie_id_sim_movie_id.close()

f_movie_id_sim_movie_id=open("movie_ID_sim_movie_ID.txt","w")
for item in liste:
	f_movie_id_sim_movie_id.write(str(item)+"\n")


f_movie_id_sim_movie_id.close()

print "done"