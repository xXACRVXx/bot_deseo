import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")

print('DE @xXACRVXx (Abrahán) en python 3.8')

def start(update, context):
      update.message.reply_text("""Bot de deseos de @hentai_s3 VERSION: 0.1.24 (beta)
      By @xXACRVXx""")
     

def updates(update, context):
      update.message.reply_text( """Historial de cambios ver: 0.1.24(beta)\nSe agrego el @ del usuario\n\nCorrección de errores y mejoras de seguridad, como el  toDus :v\n\nver old: 0.1.23 F por ella,duro 40minutos\nOptimizacion de de lineas de código, paso de 87 a 45 lineas\n\nCorrección de detección del #deseo (ahora solo funcionan si es la primera palabra)\n\nCorrección de errores en el log\n\nAñadida la base para futura versión con una lista de los últimos deseos enviados al bot\n\nCorreción/actualizacion de la versión en el /start""" )

def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']
     Usuario_mencion= update.message.effective_user['username']
     
     if str(Texto).startswith('#deseo'):
      context.bot.send_message(chat_id='-1001407312660',text='Grupo:' + str(Grupo).replace('None', 'privado' ) + '\n' +'Usuario: ' + str(Usuario).replace('None','Anónimo') + ' @' + str(Usuario_mencion) + '\n\n ' + str(Texto) +  '\n\n')
      

    
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