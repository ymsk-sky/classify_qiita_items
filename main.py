# -*- coding: utf-8 -*-

import http.client
import json
import csv

def get_token():
    token_file = open("./TOKEN_FILE", "r")
    token = token_file.readline()
    token_file.close()
    return token

def main():
    token = get_token()
    headers = {
        "Authorization": "Bearer " + token
    }

    connection = http.client.HTTPSConnection("qiita.com", 443)
    connection.request("GET", "/api/v2/items", headers=headers)

    response = connection.getresponse()

    data = response.read().decode("utf-8")
    json_data = json.loads(data)

    articles_file_name = "articles.csv"
    articles_file = open(articles_file_name, 'w')
    articles_csv = csv.writer(articles_file, lineterminator='\n')

    for num in range(len(json_data)):
        created_at = json_data[num]['created_at']
        title = json_data[num]['title']
        url = json_data[num]['url']
        user_id = json_data[num]['user']['id']
        user_name = json_data[num]['user']['name']

        article = [title, created_at, user_id, user_name, url]
        articles_csv.writerow(article)

    articles_file.close()    

if __name__ == "__main__":
    main()
