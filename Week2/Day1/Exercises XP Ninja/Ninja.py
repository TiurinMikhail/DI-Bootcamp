#Exercise 1 : Call History

class Phone:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self,other_phone):
        other_phone_number = other_phone.phone_number
        print(f'Calling phone number: {other_phone_number}')
        self.call_history.append(other_phone_number)

    def show_call_history(self):
        print('Call History:')
        print(*self.call_history, sep=', ')
        print('---------')

    def send_message(self, phone, content):
        dic_message_out = {'to': phone.phone_number, 'from': self.phone_number, 'content': content}
        self.messages.append(dic_message_out)
        phone.messages.append(dic_message_out)

    def show_outgoing_messages(self):
        print(f'Outgoing messages:\n')
        for message in self.messages:
            if message['from'] == self.phone_number:
                for key, value in message.items():
                    print(f'{key}: {value}')
                print('----------')

    def show_incoming_messages(self):
        print(f'Incoming messages:\n')
        for message in self.messages:
            if message['to'] == self.phone_number:
                for key, value in message.items():
                    print(f'{key}: {value}')
                print('----------')

    def show_messages_from(self,phone):
        for message in self.messages:
            if message['from'] == phone.phone_number:
                for key, value in message.items():
                    print(f'{key}: {value}')



megan_phone = Phone('0557707812')
avner_phone = Phone('0557777813')
michael_phone = Phone('0550999876')
kanan_phone = Phone('0520977654')

megan_phone.call(avner_phone)
megan_phone.call(michael_phone)
megan_phone.call(kanan_phone)

megan_phone.show_call_history()

megan_phone.send_message(avner_phone,'Hello')

kanan_phone.send_message(megan_phone,"Hiii!!")
avner_phone.send_message(megan_phone,'Hello there!')

megan_phone.show_incoming_messages()
megan_phone.show_outgoing_messages()

print('---------------')
megan_phone.show_messages_from(avner_phone)