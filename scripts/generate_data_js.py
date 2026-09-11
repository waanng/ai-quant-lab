#!/usr/bin/env python3
"""
GitHub Actions 用：yfinance 拉取 5 只股票数据 → 生成 data.js
输出格式与现有 indicator-lab/data.js 完全兼容
"""
import yfinance as yf
import json, os
from datetime import datetime, timezone, timedelta

STOCKS = [
    ('688981.SH', '688981.SS', '中芯国际 A', 'SH', 'CNY'),
    ('002594.SZ', '002594.SZ', '比亚迪 A', 'SZ', 'CNY'),
    ('600900.SH', '600900.SS', '长江电力 A', 'SH', 'CNY'),
    ('0981.HK',   '0981.HK',   '中芯国际 HK', 'HK', 'HKD'),
    ('1211.HK',   '1211.HK',   '比亚迪股份 HK', 'HK', 'HKD'),
]

OUTPUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      'indicator-lab', 'data.js')

def main():
    records = []
    for ts_code, yf_code, name, market, currency in STOCKS:
        print(f"  {ts_code}...", end=' ', flush=True)
        try:
            ticker = yf.Ticker(yf_code)
            df = ticker.history(period='3y', auto_adjust=True)
            if df.empty:
                print("empty")
                continue
            df = df.reset_index()
            data = []
            for _, row in df.iterrows():
                data.append({
                    'd': str(row['Date'])[:10],
                    'o': round(float(row['Open']), 2),
                    'h': round(float(row['High']), 2),
                    'l': round(float(row['Low']), 2),
                    'c': round(float(row['Close']), 2),
                    'v': int(row['Volume']),
                })
            key = ts_code.replace('.SH', '_SH').replace('.SZ', '_SZ').replace('.HK', '_HK')
            records.append({'key': key, 'name': name, 'market': market, 'currency': currency, 'data': data})
            print(f"{len(data)} rows")
        except Exception as e:
            print(f"error: {e}")

    js = f"const STOCK_DATA = {json.dumps(records, ensure_ascii=False)};"
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(js)

    tz = timezone(timedelta(hours=8))
    print(f"[{datetime.now(tz):%Y-%m-%d %H:%M}] data.js written ({len(js)} bytes)")

if __name__ == '__main__':
    main()
