# Екатерина Ипатова, 8-а когорта - Финальный проект. Инженер по тестированию
import configuration
import data
import sender_stand_request

# Функция для позитивной проверки
def positive_assert():
    # выполнение запроса на создание заказа
    order_response = sender_stand_request.post_new_order(data.order_body)
    # формирование полного пути к ручке api на запрос получение заказа по треку заказа
    ord_track = configuration.ORDER_TRACK+str(order_response.json()["track"])
    # выполнение запроса на получение заказа по треку заказа
    track_response = sender_stand_request.get_order_by_track(ord_track)
    assert track_response.status_code == 200     # Проверка, что код ответа равен 200

# Тест на получение заказа по номеру трека
def test_get_order_track_success():
    positive_assert()