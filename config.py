import os
from dotenv import load_dotenv

load_dotenv()

# Upbit API 설정
UPBIT_ACCESS_KEY = os.getenv('UPBIT_ACCESS_KEY')
UPBIT_SECRET_KEY = os.getenv('UPBIT_SECRET_KEY')

# 거래 설정
TRADING_PAIR = 'BTC'  # 거래할 코인
INVESTMENT_AMOUNT = 100000  # 투자 금액 (원)
STOP_LOSS_PERCENT = 2.0  # 손절 비율 (%)
TAKE_PROFIT_PERCENT = 3.0  # 익절 비율 (%)

# Flask 설정
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
DEBUG = True 