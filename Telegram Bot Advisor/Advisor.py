import telebot
from extensions import ConvertionException, CurrencyConverter
from config import all_keys, TOKEN

bot = telebot.TeleBot(TOKEN)


# Выводим Инструкцию как пользоваться ботом
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, "Инструкция как пользоваться ботом! "
                                      "Отправьте пожалуйста сообщение в виде <имя валюты цену которой хотите получить> "
                                      "<имя валюты в которой надо узнать цену первой валюты> <количество первой валюты> Для получения о валютах введите команду values")


# При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
@bot.message_handler(commands=['values'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Все доступные валюты: {', '.join(all_keys)}")


# При ошибке пользователя (например, введена неправильная или несуществующая валюта
# или неправильно введено число)
# вызывать собственно написанное исключение APIException с текстом пояснения ошибки.

# Для взятия курса валют необходимо использовать API и отправлять к нему запросы с помощью библиотеки Requests.
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    try:
        if len(values) != 3:
            raise ConvertionException('Количество символов не соответствует параметрам ввода данных')

        quote, base, amount = values
        result = CurrencyConverter.get_price(base, quote, amount)
        text = f'Цена {amount} {quote} в {base} - {result}'
        bot.send_message(message.chat.id, text)

    except ConvertionException as e:
        bot.send_message(message.chat.id, str(e))


if __name__ == "__main__":
    bot.polling(none_stop=True)