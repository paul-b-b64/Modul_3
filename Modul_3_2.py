def send_email(message, recipient, *, sender='university.help@gmail.com'):
    ext_ = ('.com', '.ru', '.net')

    if not ("@" in recipient and "@" in sender and sender.endswith(ext_) and recipient.endswith(ext_)):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)

send_email('Проверка связи', 'wdlj@gmail.com')
send_email('Здравствуйте', 'help@gmail.com', sender='dump@mail.ru')
send_email('Я вас попрошу', 'uni@gmail.com', sender='delo@mail.rk')
send_email('Письмо себе', 'university.help@gmail.com')
