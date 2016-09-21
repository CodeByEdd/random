from flask import Flask
from flask import request
import pymysql.cursors

app = Flask(__name__)


@app.route('/api/v1.0/send_location', methods=['POST'])
def send_location():

    connection = pymysql.connect(host='localhost',
                                 user='test',
                                 password='test',
                                 db='localisation_app')

    if not request.json or 'mac' not in request.json:
        return "Nope"
    
    mac = request.json['mac']
    timestamp = request.json['timestamp']
    rss_mean = request.json['rss_mean']
    count = request.json['count']
    rss_variance = request.json['rss_variance']

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `test` (`id`, `mac`, `timestamp`, `rss_mean`, `count`, `rss_variance`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, ('0', mac, timestamp, rss_mean, count, rss_variance))

        connection.commit()
    finally:
        connection.close()

        return "Your API call was successful. Please let me (Edd) know! \n"


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
