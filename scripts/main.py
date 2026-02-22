#!/usr/bin/env python3
import yfinance as yf
from datetime import datetime

print("🚀 Stock Hybrid Trading System v1.0")
print(f"実行日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S JST')}")

toyota = yf.Ticker("7203.T").history(period="5d")
latest_price = float(toyota['Close'].iloc[-1])
first_price = float(toyota['Close'].iloc[0])
change_rate = ((latest_price - first_price) / first_price) * 100

print(f"データ行数: {len(toyota)}")
print(f"📈 トヨタ最新: ¥{latest_price:,.0f}")
print(f"📉 初日価格: ¥{first_price:,.0f}")
print(f"📊 5日変動: {change_rate:+.1f}%")
print("✅ 完璧動作！Actions準備OK")
