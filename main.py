import GmailApi
import Util

def main():
    AllMails = []
    # Api'ye gore mail'ler toplaniyor.
    WhichApi = "Gmail"
    if WhichApi == "Gmail":
        service = GmailApi.init()

        # Gmailden okunmamis tum mesajlari al.
        unreaded_messages = GmailApi.get_unreaded_messages(service, 'me', ['INBOX', 'UNREAD'])

        messages_list = unreaded_messages['messages']
        #messages_amount = len(messages_list)

        #print(messages_list)
        #print(messages_amount)

        # Tum mesajlar daha detayli cekilir.
        for message_obj in messages_list:
            MessageData = {}
            MessageData['MessageId'] = message_obj['id']

            message = GmailApi.get_message(service, 'me', MessageData['MessageId'])

            for header in message['payload']['headers']:
                if header['name'] == 'From':
                    MessageData['From'] = header['value']
                if header['name'] == 'Subject':
                    MessageData['Subject'] = header['value']
                if header['name'] == 'Date':
                    MessageData['Date'] = header['value']
                if header['name'] == 'Content-Type':
                    MessageData['Content-Type'] = header['value']

            MessageData['Snippet'] = message['snippet']
            print(MessageData)
            AllMails.append(MessageData)

    else:
        print("Outlook")

    # Toplandiktan sonra konu basliklarina bakiliyor. Uygun olanlar kaydediliyor.
    for mail in AllMails:
        result_mail = Util.is_valid_mail(mail)
        if result_mail:
            print(result_mail)
            dir_path = Util.create_directory(result_mail)
            # Mailler okundu olarak isaretle, ve mailden dosya cek.
            if WhichApi == "Gmail":
                # mark_message_readed(service, 'me', one_message['MessageId'])
                GmailApi.GetAttachments(service, 'me', mail['MessageId'], dir_path)
            else:
                print("Outlook")

if __name__ == '__main__':
    main()
