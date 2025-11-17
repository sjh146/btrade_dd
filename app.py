from flask import Flask, jsonify, request
from trading_strategy import TradingStrategy
from bithumb_api import BithumbTrader
from config import FLASK_HOST, FLASK_PORT, DEBUG
import threading

app = Flask(__name__)
trader = BithumbTrader()
strategy = TradingStrategy()
strategy_thread = None

@app.route('/api/status', methods=['GET'])
def get_status():
    """현재 거래 상태 조회"""
    current_price = trader.get_current_price()
    balance = trader.get_balance()
    
    return jsonify({
        'current_price': current_price,
        'balance': balance,
        'position': strategy.position,
        'last_buy_price': strategy.last_buy_price
    })

@app.route('/api/start', methods=['POST'])
def start_trading():
    """자동 거래 시작"""
    global strategy_thread
    
    if strategy_thread and strategy_thread.is_alive():
        return jsonify({'message': '이미 실행 중입니다.'}), 400
    
    strategy_thread = threading.Thread(target=strategy.run)
    strategy_thread.daemon = True
    strategy_thread.start()
    
    return jsonify({'message': '자동 거래가 시작되었습니다.'})

@app.route('/api/stop', methods=['POST'])
def stop_trading():
    """자동 거래 중지"""
    global strategy_thread
    
    if not strategy_thread or not strategy_thread.is_alive():
        return jsonify({'message': '실행 중이 아닙니다.'}), 400
    
    # 스레드 종료 로직 추가 필요
    return jsonify({'message': '자동 거래가 중지되었습니다.'})

@app.route('/api/buy', methods=['POST'])
def manual_buy():
    """수동 매수"""
    try:
        price = float(request.json.get('price', 0))
        if price <= 0:
            return jsonify({'message': '유효하지 않은 가격입니다.'}), 400
        
        strategy.buy(price)
        return jsonify({'message': '매수 주문이 실행되었습니다.'})
    except Exception as e:
        return jsonify({'message': f'매수 주문 실패: {str(e)}'}), 500

@app.route('/api/sell', methods=['POST'])
def manual_sell():
    """수동 매도"""
    try:
        price = float(request.json.get('price', 0))
        if price <= 0:
            return jsonify({'message': '유효하지 않은 가격입니다.'}), 400
        
        strategy.sell(price, "수동 매도")
        return jsonify({'message': '매도 주문이 실행되었습니다.'})
    except Exception as e:
        return jsonify({'message': f'매도 주문 실패: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=DEBUG) 