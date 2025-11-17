import pybithumb
from config import TRADING_PAIR

class BithumbTrader:
    def __init__(self):
        self.api_key = 'e90f25881b9b8e4f5ee77ec4fd161673'
        self.secret_key = '71d71086c4b929606661f47b487c1700'
        self.trading_pair = TRADING_PAIR
        self.bithumb = pybithumb.Bithumb(self.api_key, self.secret_key)

    def get_current_price(self):
        """현재가 조회"""
        try:
            return pybithumb.get_current_price(self.trading_pair)
        except Exception as e:
            print(f"가격 조회 중 오류 발생: {e}")
            return None

    def get_balance(self):
        """잔고 조회"""
        try:
            # KRW 잔고 조회
            krw_balance = self.bithumb.get_balance("BTC")
            if krw_balance is None:
                return None

            # 특정 코인 잔고 조회
            coin_balance = self.bithumb.get_balance(self.trading_pair)
            if coin_balance is None:
                return None

            return {
                'total_krw': krw_balance[0],  # 보유 KRW
                'in_use_krw': krw_balance[1],  # 사용중인 KRW
                'total_coin': coin_balance[0],  # 보유 코인
                'in_use_coin': coin_balance[1],  # 사용중인 코인
                'xcoin_last': coin_balance[2]  # 마지막 거래가
            }
        except Exception as e:
            print(f"잔고 조회 중 오류 발생: {e}")
            return None

    def place_buy_order(self, price, units):
        """매수 주문"""
        try:
            return self.bithumb.buy_limit_order(self.trading_pair, price, units)
        except Exception as e:
            print(f"매수 주문 중 오류 발생: {e}")
            return None

    def place_sell_order(self, price, units):
        """매도 주문"""
        try:
            return self.bithumb.sell_limit_order(self.trading_pair, price, units)
        except Exception as e:
            print(f"매도 주문 중 오류 발생: {e}")
            return None

    def get_order_status(self, order_id):
        """주문 상태 조회"""
        try:
            return self.bithumb.get_order_status(order_id)
        except Exception as e:
            print(f"주문 상태 조회 중 오류 발생: {e}")
            return None 