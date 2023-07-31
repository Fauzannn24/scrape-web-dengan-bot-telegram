import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler

# Perintah untuk melakukan scrape web "https://plniconplus.co.id/e-proc/"
def scrape_eproc(update, context):
    url = "https://plniconplus.co.id/e-proc/" 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Sesuaikan dengan struktur HTML dari situs yang ingin di scrape
    eproc_items = soup.find_all('div',class_="post__detail")  
    for item in eproc_items:
        title = item.find('h3',class_="post__title").text.strip()
        date = item.find('div',class_="post__date").text.strip()
        description = item.find("p").text.strip()
        link = item.find("a")["href"]
        pembuka = 'Automated Message...'
        penutup = 'Pesan ini dikirim oleh sistem secara otomatis dari website https://plniconplus.co.id/e-proc/,\nDemikian informasi ini disampaikan semoga bermanfaat.\nTerimakasih'

        # Perintah kirim hasil scraping sebagai pesan ke Bot Telegram
        message = f"{pembuka}\n\nRelease On : {date}\n\n{title}\n\nDescription : {description}\n\nRead More : {link}\n\n{penutup}"
        update.message.reply_text(message)

# Perintah untuk menampilkan pesan saat /start diberikan 
def start(update, context):
    update.message.reply_text("Hallo Dekk...!!!\nKetik /update untuk mengetahui tender terbaru ICON+.")

def main():
    # "6594995717:AAGiMrwKQXGxlo2KVPKq1ocs3RsQx6VhwPs" adalah Token Bot untuk menghubungkan hasil scraping ke Bot Telegram 
    updater = Updater("6594995717:AAGiMrwKQXGxlo2KVPKq1ocs3RsQx6VhwPs", use_context=True)
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah /start dan /update
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("update", scrape_eproc))

    # Jalankan Bot
    print('Bot Berjalan')
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()