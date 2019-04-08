numbers_to_message = ['+2348156625870', '+2348163891244', '+2349075202194']
for number in numbers_to_message:
    client.messages.create(
        body = 'Hi ' +str(name) + ' you have sent us ' + str(amount) + ' You have ' +str(mins) + ' Your verification code is ' + smsCode,
        from_ = '+13866434696',
        to = 'number'
    )