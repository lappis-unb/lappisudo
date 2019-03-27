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
        dispatcher.utter_message("Conferindo...")
        sheet = None
        try:
            sheet = googlesheet.GoogleSheetIntegration()
        except ValueError:
            dispatcher.utter_message("Não consegui me conectar ao google sheets :/")
            logger.error(ValueError)
        try:
            dispatcher.utter_message(sheet.get_now_timetable())
        except ValueError:
            dispatcher.utter_message("Não consegui ler a planilha :/")
            logger.error(ValueError)

class ActionIntegranteHorario(Action):
    def name(self):
        return "action_integrante_horario"

    def run(self, dispatcher, tracker, domain):        
        dispatcher.utter_message("Conferindo...")
        name = tracker.get_slot('nome')
        dispatcher.utter_message(name)
        x = tracker.current_slot_values()['nome']
        dispatcher.utter_message(x)
