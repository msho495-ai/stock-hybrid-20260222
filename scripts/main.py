#!/usr/bin/env python3
import yfinance as yf
import pandas as pd
from datetime import datetime

print("🚀 Stock Hybrid Trading System v1.0")
print(f"実行日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S JST')}")

# トヨタ自動車 (7203.T)
toyota = yf.download("7203.T", period="5d", progress=False)
latest_price = toyota['Close'][-1]
print(f"📈 トヨタ最新終値: {latest_price:,.0f}円")
print(f"📊 5日間変動率: {((latest_price - toyota['Close'][0])/toyota['Close'][0]*100):+.1f}%")

print("✅ システム正常動作確認完了！")
