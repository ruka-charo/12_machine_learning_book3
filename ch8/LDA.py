'''潜在ディリクレ配分(LDA)'''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv('/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/12_machine_learning_book3/\
ch8/movie_data.csv', encoding='utf-8')
df.head()

# トピック分析
count = CountVectorizer(stop_words='english', max_df=.1,
    max_features=5000)
X = count.fit_transform(df['review'].values)

lda = LatentDirichletAllocation(n_components=10, random_state=123,
    learning_method='batch')
X_topics = lda.fit_transform(X)

lda.components_.shape

# トピックの抽出
n_top_words = 5
feature_names = count.get_feature_names()

for topic_idx, topic in enumerate(lda.components_):
    print('Topic %d:' % (topic_idx + 1))
    print(' '.join([feature_names[i]
        for i in topic.argsort() [:-n_top_words - 1:-1]]))

# ホラー映画カテゴリの3つのレビューを表示
horror = X_topics[:, 5].argsort()[::-1]

for iter_idx, movie_idx in enumerate(horror[:3]):
    print('\nHorror movie #%d:' % (iter_idx + 1))
    print(df['review'][movie_idx][:300], '...')
