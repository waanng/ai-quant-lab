# AI Quant Lab — Indicator Lab Interactive

交互式技术指标分析工具。选择 A+H 股股票，拖拽参数实时重绘 RSI、MACD、布林带、ATR 四个技术指标。

## 快速开始

直接用浏览器打开 `index.html`（支持 file:// 协议离线使用，无需服务器）。

## 功能

- **5 只股票**：中芯国际 A · 比亚迪 A · 长江电力 A · 中芯国际 HK · 比亚迪 HK
- **4 个指标**：布林带 / RSI / MACD / ATR，每个参数独立可调
- **实时重绘**：拖拽滑块 200ms 防抖，Chart.js 渲染
- **状态持久化**：URL hash 记录当前参数，可复制分享

## 文件结构

```
ai-quant-lab/
├── index.html          # 主页面
├── data.js             # 5 只股票的 OHLCV 内联数据
├── vendor/
│   └── chart.umd.min.js  # Chart.js 4.4.1 本地副本
└── docs/
    └── spec_indicator_interactive.md  # 设计文档
```

## 技术栈

- 纯前端 HTML + CSS Grid + 原生 JS
- Chart.js 4.4.1 本地部署
- 指标计算引擎（JS 实现 RSI/MACD/BOLL/ATR）
- 零依赖运行，无需 npm install

## 免责声明

技术指标描述历史市场状态，不等于买卖信号。本工具仅供教学研究使用。
