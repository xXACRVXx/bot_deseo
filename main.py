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


def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']