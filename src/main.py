import os
import time

from iqoptionapi.stable_api import IQ_Option

import binary_star
import iq
from redline import inicia

print('iniciando...')
try:
    inicia()
    os.system('cls')
except:
    print('falha ao executar a primeira função\niniciando...')
    time.sleep(1)
    os.system('cls')


class bcolors:
    HEADER = '\033[95m'
    AMARELO = '\033[33m'
    VERMELHO = '\033[31m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


investing = 'a'
while investing == 'a':
    try:
        investing = int(input('digite o valor do investimento:\n'))
    except:
        os.system('cls')
        continue
CANDLE_TIME = 60
CANDLE_NUMBER = 300

MAX_INSTRUMENTS = 5

ema_cross = 0
macd_cross = 0
adx_cross = 0

api_iq = iq.login(IQ_Option, input(
    f'{bcolors.WARNING}informe o tipo da conta! digite{bcolors.ENDC} "PRACTICE" {bcolors.WARNING}para usar conta de teste ou {bcolors.ENDC}"REAL"{bcolors.WARNING} para usar a  conta real:{bcolors.ENDC}\n'))
assets = iq.load_goals(api_iq)

while True:
    while int(time.localtime().tm_sec % 60) < 2:
        start = time.process_time()
        print(f'{bcolors.OKCYAN}obtendo indicadores{bcolors.ENDC}\n')
        for asset in assets.keys():

            goal_asset = iq.rename_data(api_iq.get_candles(
                asset, CANDLE_TIME, CANDLE_NUMBER, time.time()))

            target_df = iq.get_indicators(goal_asset)

            ema_cross = binary_star.ema_cross(target_df)
            macd_cross = binary_star.macd_cross(target_df)
            adx_cross = binary_star.adx_cross(target_df)

            # Strategy Call
            if ema_cross == 1 and macd_cross == 1 and adx_cross == 1:
                ID = api_iq.buy(1, asset, 'call', 3)
                print(f'{bcolors.OKGREEN}comprando: {bcolors.ENDC}',
                      asset, ' ID: ', ID)

            # Strategy Put
            if ema_cross == -1 and macd_cross == -1 and adx_cross == -1:
                ID = api_iq.buy(1, asset, 'put', 3)
                print(f'{bcolors.VERMELHO}Vendendo: {bcolors.ENDC}',
                      asset, ' ID: ', ID)

        print('Obtendo lucros\n')

        # Setting goals by profit
        assets = iq.load_goals(api_iq)
        timeToSleep = 60 - time.localtime().tm_sec - 1
        print('Esperando proxima a proxima vela ', timeToSleep, " segundos.\n")
        time.sleep(timeToSleep)
        print('')
