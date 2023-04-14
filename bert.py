# -------------------------------------BERT Implementation------------------------------------------------
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
    model = BERTopic()
    topics, probs = model.fit_transform(docs)
    print(model.get_topic_info())


if __name__ == '__main__':
    bertopic()
