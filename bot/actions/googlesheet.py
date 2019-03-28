import re
import gspread
import logging
import datetime
from oauth2client.service_account import ServiceAccountCredentials

logger = logging.getLogger(__name__)


class GoogleSheetIntegration():
    def __init__(self, sheet=None, utc=-3, gap=2):
        self.colToLetter = {1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G'}
        self.timeTables = {1:'08h-10h', 2:'10h-12h', 3:'12h-14h', 4:'14h-16h',
                      5:'16h-18h', 6:'fim_dia'}
        self.utc = utc
        self.gap = gap
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
    
    def get_now_timetable(self):
        now = datetime.datetime.now().hour + self.utc
        timeTable = self.find_timetable(now=now)
        if timeTable == 0:
            return 'Não sei quem está no LAPPIS as {}h'.format(now)
        presence = self.get_presence(timeTable)
        if presence == '\n':
            presence = 'Ninguém :/'
        return presence


    def find_timetable(self, now=20):
        timeTable = 0
        for i in range(1, len(self.timeTables)):
            if (now >= int(self.timeTables[i].split('h')[0]) and 
                now < abs(int(self.timeTables[i].split('h')[1]))):
                timeTable = i
        return timeTable

    def get_lappis_timetable_presense(self, cellList = None):
        names = ''
        for cell in cellList:
            names += cell.value
            names += '\n'
        return names

    def get_presence(self, timeTable=0, now=datetime.datetime.now()):
        cellsRange = []
        presence = "Não consegui pegar presença"
        weekday = self.colToLetter[now.weekday()+1]
        try:
            cellsRange.append(self.sheet.find(self.timeTables[timeTable]))
            cellsRange.append(self.sheet.find(self.timeTables[timeTable+1]))
        except:
            logger.error(ValueError)
        try:
            query = weekday+str(cellsRange[0].row)+':'+weekday+str(cellsRange[1].row-self.gap)
            presence = self.get_lappis_timetable_presense(cellList=self.sheet.range(query))
            presence = re.sub('\n\n*','\n',presence)
        except:
            logger.error(ValueError)          
        return presence
