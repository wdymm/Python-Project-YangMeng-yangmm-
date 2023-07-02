import pandas as pd
df = pd.read_csv(r'C:\Users\yangmm\Desktop\DoubanMovieRecommendationSystem-master\Data\douban_movies.csv',encoding='utf-8')
# df.fillna('',inplace=True)
print(df)
# df.to_excel('douban_movies.xlsx',index=False)
# df = pd.read_excel('douban_movies.xlsx')
# df.fillna('',inplace=True)
# df.to_excel('douban_movies.xlsx',index=False)
