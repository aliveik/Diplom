import configuration
import requests
import data

# ручка на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

# ручка на получение заказа по номеру трека
def get_order_by_track(path):
    return requests.get(configuration.URL_SERVICE + path, headers=data.headers)  # подставляем полный url и заголовки