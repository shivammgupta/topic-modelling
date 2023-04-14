# This is a sample Python script.
import psycopg2
from bertopic import BERTopic


def get_db_connection():
    conn = psycopg2.connect(
        database="relay", user='postgres', password='admin', host='127.0.0.1', port='5432'
        # database="wap", user='root', password='root', host='10.109.178.43', port='5432'
    )
    return conn


def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(""" SELECT feedback_pos FROM healthcare where iscurrentjob = 0  and employer = 'Mayo Clinic' and feedback_pos is not null """)
    response = cur.fetchall()
    cur.close()
    conn.close()
    return response



def db_to_list():
    data = get_data()
    final_list = []
    for obj in data:
        l = str(obj)
        final_list.append(l)
    # print(final_list[0])
    return final_list


def bertopic():
    docs = db_to_list()
    # print(docs[0])
    model = BERTopic(verbose=True, embedding_model='paraphrase-MiniLM-L3-v2', min_topic_size=7)
    headline_topics, _ = model.fit_transform(docs)
    freq = model.get_topic_info()
    # print("Number of topics: {}".format(len(freq)))
    freq.head()
    a_topic = freq.iloc[1]["Topic"]  # Select the 1st topic
    print(model.get_topic(a_topic))


if __name__ == '__main__':
    bertopic()
