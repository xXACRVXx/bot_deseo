import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")

print('DE @xXACRVXx (Abrahán) en python 3.8')

def start(update, context):
      update.message.reply_text("""Bot de deseos de @hentai_s3 VERSION: 0.1.27 (beta)
      By @xXACRVXx""")
     

def updates(update, context):
      update.message.reply_text( """Historial de cambios ver: 0.1.27(beta)\n\nSe agrego el @ del usuario en el deseo para ayudar a encontrarlo en el grupo (en caso de el usuario no contara con @ se dará el id aunque aún mo lo e probado)\n\nver: 0.1.26(beta)\n\nCorrección de errores y mejoras de seguridad, como el  toDus :v\n\nversion: 0.25(Alpha)\n\nEsta versión fue cancelada en estado de Alpha por problemas con el reenvío.\nF por ella""" )

def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']
     Usuario2= update.effective_user['username']
     
     if str(Texto).startswith('#deseo'):
      context.bot.send_message(chat_id='-1001407312660',text='Grupo:' + str(Grupo).replace('None', 'privado' ) + '\n' +'Usuario: ' + str(Usuario).replace('None','Anónimo')+' @'+str(Usuario2) + '\n\n ' + str(Texto) +  '\n\n')
      

    
if __name__ == "__main__":
  
    Hentaibot = telegram.Bot(token=TOKEN)
    
actualizador = Updater(Hentaibot.token, use_context=True)
       
despachador = actualizador.dispatcher

despachador.add_handler(CommandHandler('start', start))
despachador.add_handler(CommandHandler('updates', updates))

despachador.add_handler(MessageHandler(filters=Filters.text, callback= mensajes_entrantes))


   
print('\nIniciando\n')
  
actualizador.start_polling()
  
actualizador.idle   