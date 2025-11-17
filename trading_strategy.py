import time
from datetime import datetime
from config import INVESTMENT_AMOUNT, STOP_LOSS_PERCENT, TAKE_PROFIT_PERCENT
from upbit_api import UpbitTrader

class TradingStrategy:
    def __init__(self):
        self.trader = UpbitTrader()
        self.last_buy_price = 0
        self.position = False
        self.investment_amount = INVESTMENT_AMOUNT
        self.stop_loss_percent = STOP_LOSS_PERCENT
        self.take_profit_percent = TAKE_PROFIT_PERCENT

    def check_conditions(self):
        """매매 조건 확인"""
        current_price = self.trader.get_current_price()
        if not current_price:
            return

        # 포지션이 없는 경우 (매수 조건)
        if not self.position:
            # 여기에 매수 조건 로직 추가
            # 예: 이동평균선 돌파, RSI 과매도 등
            if self.should_buy(current_price):
                self.buy(current_price)
        
        # 포지션이 있는 경우 (매도 조건)
        else:
            # 손절 조건
            if current_price <= self.last_buy_price * (1 - self.stop_loss_percent / 100):
                self.sell(current_price, "손절")
            # 익절 조건
            elif current_price >= self.last_buy_price * (1 + self.take_profit_percent / 100):
                self.sell(current_price, "익절")

    def should_buy(self, current_price):
        """매수 조건 확인"""
        # 여기에 실제 매수 전략 구현
        # 예시: 단순히 1분마다 매수
        return True

    def buy(self, price):
        """매수 실행"""
        try:
            units = self.investment_amount / price
            order_id = self.trader.place_buy_order(price, units)
            if order_id:
                self.position = True
                self.last_buy_price = price
                print(f"[{datetime.now()}] 매수 주문 실행: {price}원, {units}개")
        except Exception as e:
            print(f"매수 실행 중 오류 발생: {e}")

    def sell(self, price, reason):
        """매도 실행"""
        try:
            balance = self.trader.get_balance()
            if balance and balance.get('total_coin', 0) > 0:  # 보유 수량이 있는 경우
                coin_amount = balance['total_coin']
                order_id = self.trader.place_sell_order(price, coin_amount)
                if order_id:
                    self.position = False
                    print(f"[{datetime.now()}] {reason} 매도 주문 실행: {price}원, {coin_amount}개")
        except Exception as e:
            print(f"매도 실행 중 오류 발생: {e}")

    def run(self):
        """전략 실행"""
        while True:
            try:
                self.check_conditions()
                time.sleep(60)  # 1분마다 체크
            except Exception as e:
                print(f"전략 실행 중 오류 발생: {e}")
                time.sleep(60) 