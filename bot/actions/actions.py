from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from . import googlesheet
import logging
import datetime
from datetime import date

logger = logging.getLogger(__name__)


class ActionIntegrantesAgora(Action):
    def name(self):
        return "action_integrantes_agora"

    def run(self, dispatcher, tracker, domain):        
        dispatcher.utter_message("Ta ok, vou conferir aqui..")
        sheet = None
        try:
            sheet = googlesheet.GoogleSheetIntegration()            
        except ValueError:
            dispatcher.utter_message("Não consegui me conectar ao google sheets :/")
            logger.error(ValueError)
        sheetValues = []
        try:
            sheetValues = sheet.sheet_values()
        except ValueError:
            dispatcher.utter_message("Não consegui ler a planilha :/")
            logger.error(ValueError)
        dispatcher.utter_message(sheetValues[4][1])
