import os
import telegram
import sys
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")



print('\n\n')



print('                #################')
print('              ###   ###############')
print('              ###   ###############')
print('              #####################')
print('                        ###########')
print('       ############################ ,,,,,,')
print('     ############################## ,,,,,,,,.')
print('    ############################### ,,,,,,,,,.')
print('   ################################ ,,,,,,,,,,')
print('   ###############################  ,,,,,,,,,,')
print('   ##############                 ,,,,,,,,,,,,')
print('   ###########  .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
print('   ##########  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
print('   ########## ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
print('    ######### ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
print('      ####### ,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
print('              ,,,,,,,,,,,')
print('              ,,,,,,,,,,,,,,,,,,,,,')
print('              ,,,,,,,,,,,,,,,   ,,,')
print('              .,,,,,,,,,,,,,,   ,,,')
print('                ,,,,,,,,,,,,,,,,,,')

#print('\nEl que me robe el logo lo demando, me llevo 40m -_-')


print('\n\n\n')
print('PROYECTO SHIROMI VERSION: 0.0.1 (ALPHA)')
print('DE @xXACRVXx (Abrahán) en python 3.8')

def start(update, context):
      update.message.reply_text('Hola, humano\n\nSoy Xx_A_xX ver: 0.08.12(beta)')


def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']
     
     
     
     if str(Texto).__contains__('-say'):
      context.bot.send_message(chat_id='@Xx_A_xX_soporte',text=str(Texto).replace('-say', ''))
     
     
     
     
     
if __name__ == "__main__":
  
    elbot = telegram.Bot(token=TOKEN)
    
actualizador = Updater(elbot.token, use_context=True)
       
  
despachador = actualizador.dispatcher

despachador.add_handler(MessageHandler(filters=Filters.text, callback= mensajes_entrantes))
   
   
print('\nIniciando\n')
  
actualizador.start_polling()
  
actualizador.idle   
   