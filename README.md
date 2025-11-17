# 빗썸 자동 거래 프로그램

빗썸 거래소 API를 이용한 암호화폐 자동 거래 프로그램입니다.

## 기능

- 실시간 가격 모니터링
- 자동 매매 전략 실행
- 수동 매매 기능
- 손절/익절 자동화
- REST API 제공

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

2. 환경 변수 설정:
`.env` 파일을 생성하고 다음 내용을 추가합니다:
```
BITHUMB_API_KEY=your_api_key
BITHUMB_SECRET_KEY=your_secret_key
```

## 실행 방법

```bash
python app.py
```

## API 엔드포인트

- `GET /api/status`: 현재 거래 상태 조회
- `POST /api/start`: 자동 거래 시작
- `POST /api/stop`: 자동 거래 중지
- `POST /api/buy`: 수동 매수
- `POST /api/sell`: 수동 매도

## 설정

`config.py` 파일에서 다음 설정을 변경할 수 있습니다:

- `TRADING_PAIR`: 거래할 코인
- `INVESTMENT_AMOUNT`: 투자 금액
- `STOP_LOSS_PERCENT`: 손절 비율
- `TAKE_PROFIT_PERCENT`: 익절 비율

## 주의사항

- 실제 거래에 사용하기 전에 반드시 테스트넷에서 충분한 테스트를 진행하세요.
- 암호화폐 거래는 높은 위험을 수반하므로 신중하게 투자하세요.
- API 키는 절대 공개되지 않도록 주의하세요. 