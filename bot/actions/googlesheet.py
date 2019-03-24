import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials

logger = logging.getLogger(__name__)


class GoogleSheetIntegration():
    def __init__(self, sheet=None):
        try:
            self.sheet = self.connect_to_google_sheets()
        except ValueError:
            logger.error(ValueError)

    def connect_to_google_sheets(self, sheetName='relacao_alunos_lappis',
                                 secretFile='actions/client_secret.json'):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = None
        client = None
        sheet = None
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                                                                 secretFile,
                                                                 scope)
            client = gspread.authorize(creds)
        except ValueError:
            logger.error(ValueError)
        try:
            sheet = client.open(sheetName).sheet1
        except ValueError:
            logger.error(ValueError)
        return sheet

    def sheet_values(self):
        data = None
        try:
            data = self.sheet.get_all_values()
        except ValueError:
            logger.error(ValueError)
        return data

    def update_sheet(self, value=['', ''], row=3):
        try:
            self.sheet.insert_row(value, row)
        except ValueError:
            logger.error(ValueError)
