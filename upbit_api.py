import pyupbit
from config import TRADING_PAIR, UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY

class UpbitTrader:
    def __init__(self):
        # 환경 변수에서 가져오거나 하드코딩된 키 사용
        self.access_key = UPBIT_ACCESS_KEY or 'e90f25881b9b8e4f5ee77ec4fd161673'
        self.secret_key = UPBIT_SECRET_KEY or '71d71086c4b929606661f47b487c1700'
        # 업비트 티커 형식: KRW-BTC, KRW-ETH 등
        self.trading_pair = f"KRW-{TRADING_PAIR}"
        self.upbit = pyupbit.Upbit(self.access_key, self.secret_key)

    def get_current_price(self):
        """현재가 조회"""
        try:
            return pyupbit.get_current_price(self.trading_pair)
        except Exception as e:
            print(f"가격 조회 중 오류 발생: {e}")
            return None

    def get_balance(self):
        """잔고 조회"""
        try:
            # 전체 잔고 조회
            balances = self.upbit.get_balances()
            if balances is None:
                return None

            # KRW 잔고 찾기
            krw_balance = 0.0
            coin_balance = 0.0
            coin_locked = 0.0
            
            for balance in balances:
                currency = balance['currency']
                if currency == 'KRW':
                    krw_balance = float(balance['balance'])
                elif currency == TRADING_PAIR:
                    coin_balance = float(balance['balance'])
                    coin_locked = float(balance['locked'])

            # 현재가 조회
            current_price = self.get_current_price()
            
            return {
                'total_krw': krw_balance,  # 보유 KRW
                'in_use_krw': 0.0,  # 사용중인 KRW (업비트는 별도로 제공하지 않음)
                'total_coin': coin_balance,  # 보유 코인
                'in_use_coin': coin_locked,  # 사용중인 코인 (주문 중인 수량)
                'xcoin_last': current_price  # 마지막 거래가
            }
        except Exception as e:
            print(f"잔고 조회 중 오류 발생: {e}")
            return None

    def place_buy_order(self, price, units):
        """매수 주문"""
        try:
            # 업비트는 지정가 매수 주문
            result = self.upbit.buy_limit_order(self.trading_pair, price, units)
            if result:
                return result.get('uuid')  # 주문 UUID 반환
            return None
        except Exception as e:
            print(f"매수 주문 중 오류 발생: {e}")
            return None

    def place_sell_order(self, price, units):
        """매도 주문"""
        try:
            # 업비트는 지정가 매도 주문
            result = self.upbit.sell_limit_order(self.trading_pair, price, units)
            if result:
                return result.get('uuid')  # 주문 UUID 반환
            return None
        except Exception as e:
            print(f"매도 주문 중 오류 발생: {e}")
            return None

    def get_order_status(self, order_id):
        """주문 상태 조회"""
        try:
            return self.upbit.get_order(order_id)
        except Exception as e:
            print(f"주문 상태 조회 중 오류 발생: {e}")
            return None

