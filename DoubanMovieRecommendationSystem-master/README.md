# Python-Project-YangMeng-yangmm-
Final Project for advanced python training -- login: yangmm

## Introduction
This recommender application makes movie suggestions for uses based on their history data. First, users' watch history is scraped from Douban, which is best-known rating site for books and movies in China. Then recommendation algorithm is applied, which is the core of the application. Finally. GUI is designed to allow users to easily get their movie suggestions.  

**There are mainly three modules in the application：**

1. Crawl module：request, json, MySQL 

2. Recommender module：Item-based collaborative filtering(ItemCF)

3. GUI module：PyQt5

**Develop environment：Python 3.11**

**Libraries used in Python**

pandas

numpy

sklearn

pymysql

PyQt5

requests

fake_useragent

lxml

## Instruction
Run main.py in GUI file to start app

## Information

author：Yang Meng

login：yangmm

date：06/27/2023 - 07/03/2023

## ​Features
#### 1.  Login page
User can login by input login name and password in dataset `users_info.csv`.

![Signin.png](https://github.com/wdymm/Python-Project-YangMeng-yangmm-/blob/main/DoubanMovieRecommendationSystem-master/Screenshot/Signin.PNG)

#### 2. Landing page
User will enter landing page after login. Recommendation part is in the left, and ranking list part is in the right. 

![LandingPage.png](https://github.com/wdymm/Python-Project-YangMeng-yangmm-/blob/main/DoubanMovieRecommendationSystem-master/Screenshot/Recommendation.PNG)

#### 3. Movie searching page 
By clicking movie search button in landing page, user can search movie info by entering movie's name, and fuzzy search is applied in search system. 

<img src="https://github.com/wdymm/Python-Project-YangMeng-yangmm-/blob/main/DoubanMovieRecommendationSystem-master/Screenshot/Search.PNG" alt="电影搜索界面.png" style="zoom: 50%;" />

#### 4.Movie datail page
By clicking movie datail info button in landing page, user can get movie datail info like actors, directors, screen writers and movie introductions.  

![Detail.png](https://github.com/wdymm/Python-Project-YangMeng-yangmm-/blob/main/DoubanMovieRecommendationSystem-master/Screenshot/Intro.PNG)

#### 5. User profile page
By clicking user profile button, user info will be listed.  

![用户个人界面.png](https://github.com/wdymm/Python-Project-YangMeng-yangmm-/blob/main/DoubanMovieRecommendationSystem-master/Screenshot/Userprofile.PNG)
