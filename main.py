import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = os.getenv("TOKEN")

lista = []

print('DE @xXACRVXx (Abrahán) en python 3.8')

def start(update, context):
          
   Usuario2 =update.effective_user['username']
   
   print(Usuario2)

   if Usuario2 == 'xXACRVXx' or Usuario2 == 'RathHunt' or Usuario2 == 'Adam000000001' or Usuario2 == 'Leonardo2004' or Usuario2 == 'Noran_PG':  
      
      update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido activado ")
      
      if lista.__contains__('1'):
         lista.remove('1')
         return lista
         print(lista)
      
         
   else:   
     
      update.message.reply_text("""Bot hentai_s3 VERSION: 1.0.0
      By @xXACRVXx""")
     
def stop(update, context):
      
   Usuario2 =update.effective_user['username']
   
   print(Usuario2)

   if Usuario2 == 'xXACRVXx' or Usuario2 == 'RathHunt' or Usuario2 == 'Adam000000001' or Usuario2 == 'Leonardo2004' or Usuario2 == 'Noran_PG':
      update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido desactivado ")
      lista.append('1')
      print(lista)
      return lista


def updates(update, context):
      update.message.reply_text( """Historial de cambios ver: 1.0.0\n\nInformacion clasificada hasta que me entren ganas de escribir """ )

def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']
     Usuario2= update.effective_user['username']
     
     Id_grupo = update.message.chat.id
     
     Subtitulos = update.message.caption
     
     if Usuario2 == 'xXACRVXx' or Usuario2 == 'RathHunt' or Usuario2 == 'Adam000000001' or Usuario2 == 'Leonardo2004' or Usuario2 == 'Noran_PG':
       if str(Texto).startswith('-off'):
          update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido desactivado ")
          lista.append('1')
          print(lista)
          return lista
          
          update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido activado ")
      
       if str(Texto).startswith('-on'):
         if lista.__contains__('1'):
          lista.remove('1')
          return lista
          print(lista)
       
       if str(Texto).startswith('-lista'):
         
          update.message.reply_text(str(lista))
        
     
     
     if not lista.__contains__('1') :
       
         if not str(Usuario) == 'Telegram':
           
           if str(Subtitulos).__contains__('#hentai'):
            Id_mensage = update.message.message_id
            context.bot.forward_message(chat_id='@solo_hentai_s3',from_chat_id = Id_grupo , message_id= Id_mensage )
           
           if str(Texto).startswith('#hentai'):
            Id_mensage_re = update.message.reply_to_message.message_id
            
            context.bot.forward_message(chat_id='@solo_hentai_s3',from_chat_id = Id_grupo , message_id= Id_mensage_re )
            update.message.reply_text("Tu mensaje fue enviado")
     
     if str(Texto).startswith('#deseo'):
      context.bot.send_message(chat_id='-1001407312660',text=f"Grupo:{str(Grupo).replace('None', 'privado' )}\nUsuario: {str(Usuario).replace('None','Anónimo')} @{str(Usuario2)}\n\nt.me/{update.message.chat.username}/{update.message.message_id}\n\n{str(Texto)}")
      
      update.message.reply_text("Tu deseo fue enviado")
      

    
if __name__ == "__main__":
  
    Hentaibot = telegram.Bot(token=TOKEN)
    
actualizador = Updater(Hentaibot.token, use_context=True)
       
despachador = actualizador.dispatcher

despachador.add_handler(CommandHandler('start', start))

despachador.add_handler(CommandHandler('stop', stop))

despachador.add_handler(CommandHandler('updates', updates))

despachador.add_handler(MessageHandler(filters=Filters.all, callback= mensajes_entrantes))


   
print('\nIniciando\n')
  
actualizador.start_polling()
  
actualizador.idle   
