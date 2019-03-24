from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from . import googlesheet
import logging
import datetime
from datetime import date

logger = logging.getLogger(__name__)


class ActionMarcarReuniao(Action):
    def name(self):
        return "action_marcar_reuniao"

    def run(self, dispatcher, tracker, domain):        
        sheets = None
        try:
            sheets = googlesheet.GoogleSheetIntegration(sheetName='relacao_alunos_lappis')            
        except ValueError:
            dispatcher.utter_message(ValueError)
            logger.error(ValueError)
        try:
            dispatcher.utter_message("Teste")
        except ValueError:
            dispatcher.utter_message(ValueError)
            logger.error(ValueError)
