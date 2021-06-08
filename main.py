import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")

print('\n\n\n')
print('PROYECTO DESEOS VERSION: 0.0.1 (ALPHA)')
print('DE @xXACRVXx (Abrahán) en python 3.8')

def start(update, context):
      update.message.reply_text("""Bot de deseos de @hentai_s3 VERSION: 0.0.1 (ALPHA)""")

def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']
     
     if str(Texto).__contains__('#deseo'):
      context.bot.send_message(chat_id='1407312660',text='Grupo:' + str(Grupo).replace('None', 'privado' ) + '\n' +'Usuario: ' + str(Usuario).replace('None','Anónimo') + '\n\n ' + str(Texto) +  '\n\n')
    
if __name__ == "__main__":
  
    Hentaibot = telegram.Bot(token=TOKEN)
    
actualizador = Updater(Hentaibot.token, use_context=True)
       
despachador = actualizador.dispatcher

despachador.add_handler(CommandHandler('start', start))

despachador.add_handler(MessageHandler(filters=Filters.text, callback= mensajes_entrantes))
   
print('\nIniciando\n')
  
actualizador.start_polling()
  
actualizador.idle   