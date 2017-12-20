import GmailApi
import Util
import Template2Pdf

def main():
    Mails = []
    # Api'ye gore mail'ler toplaniyor.
    WhichApi = "Gmail"
    if WhichApi == "Gmail":
        service = GmailApi.init()

        # Gmailden okunmamis tum mesajlari al.
        unreaded_messages = GmailApi.get_unreaded_messages(service, 'me', ['INBOX', 'UNREAD'])

        messages_list = unreaded_messages['messages']

        # Tum mesajlar daha detayli cekilir.
        Mails = Util.get_messages_with_details(service, messages_list)
    else:
        print("Outlook")

    # Mail listesi olusturulduktan, Mail icindeki ek dosyalar indirilecek ve mail okundu olarak isaretlenecek.
    # Sonra mail'ler filtrelenecek, sonrasinda pdf olusturulacak.
    StudentListForGeneratePdf = {}
    for mail in Mails:
        if WhichApi == "Gmail":
            # mark_message_readed(service, 'me', mail['MessageId'])
            GmailApi.GetAttachments(service, 'me', mail['MessageId'], mail['Directory'])
        else:
            print("Outlook")

        # Filtreleme kismi
        if StudentListForGeneratePdf.get(mail['Directory'], None) is None:
            StudentListForGeneratePdf[mail['Directory']] = []
        StudentListForGeneratePdf[mail['Directory']].append(mail)

    print(StudentListForGeneratePdf)
    Template2Pdf.create_pdfs(StudentListForGeneratePdf)

if __name__ == '__main__':
    main()
