# 🧪 AI Quant Lab — 量化策略实验平台

多策略量化作品集。浏览器内实时计算，零安装、零后端。

🔗 **访问**: https://waanng.github.io/ai-quant-lab/

## 策略工具

| 策略 | 路径 | 说明 |
|------|------|------|
| 📊 指标实验室 | [/indicator-lab/](indicator-lab/) | RSI / MACD / 布林带 / ATR 交互分析 |
| 🐢 海龟法则 | [/turtle-strategy/](turtle-strategy/) | 唐奇安通道 + ATR 止损 + 风险预算回测 |
| 📈 均线交叉 | [/ma-cross/](ma-cross/) | 双均线金叉死叉策略回测 |
| 🤖 机器学习 | 即将推出 | 随机森林 + XGBoost 趋势预测 |
| 🎯 组合优化 | 即将推出 | 风险平价 / 动态权重 |

## 共享数据

5 只 A+H 股票（中芯国际 A/H、比亚迪 A/H、长江电力 A），近 3 年日线。

数据每日由 GitHub Actions 自动更新（`scripts/generate_data_js.py`）。

## 技术栈

- 纯前端 HTML + CSS + 原生 JS
- Chart.js 4.x
- 零依赖运行，支持 `file://` 协议离线使用
- 部署：GitHub Pages

## 文件结构

```
ai-quant-lab/
├── index.html                # 🏠 首页门户
├── indicator-lab/             # 📊 指标实验室
│   ├── index.html
│   └── data.js                # 共享股票数据
├── turtle-strategy/           # 🐢 海龟法则
│   ├── index.html
│   └── js/turtle_engine.js    # JS 引擎
├── ma-cross/                  # 📈 均线交叉
│   └── index.html
├── shared/
│   ├── common.css             # 公共样式
│   └── lib/chart.umd.min.js   # Chart.js
├── scripts/
│   └── generate_data_js.py    # 数据更新脚本
├── .github/workflows/         # Actions 每日部署
└── docs/                      # 设计文档
```

## 免责声明

所有策略仅供教学研究使用，不构成投资建议。
