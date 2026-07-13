<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>Financial Analysis — Solar EV Charging Station · MESHPOWER RWANDA ltd · Eng. Hermes MUGISHA</title>
  <link
    href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Exo+2:wght@200;300;400;600;800&display=swap"
    rel="stylesheet" />
  <style>
    :root {
      --bg: #03080f;
      --bg2: #060e1a;
      --bg3: #08121f;
      --panel: #060d1b;
      --b1: #0d1e36;
      --b2: #183260;
      --b3: #244a7c;
      --sol: #f59e0b;
      --sol2: #fbbf24;
      --sol3: #fde68a;
      --grn: #22c55e;
      --grn2: #4ade80;
      --grn3: #86efac;
      --blu: #3b82f6;
      --blu2: #60a5fa;
      --cyn: #06b6d4;
      --cyn2: #22d3ee;
      --org: #f97316;
      --org2: #fb923c;
      --red: #ef4444;
      --red2: #f87171;
      --pur: #a855f7;
      --pur2: #c084fc;
      --yel: #eab308;
      --yel2: #facc15;
      --tx: #e2e8f0;
      --tx2: #94a3b8;
      --tx3: #475569;
      --brd: rgba(24, 50, 96, .5);
      --fn-hd: 'Orbitron', sans-serif;
      --fn-mn: 'Share Tech Mono', monospace;
      --fn-ui: 'Exo 2', sans-serif;
      --accent: #f59e0b;
    }

    *,
    *::before,
    *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0
    }

    html {
      font-size: 13px;
      background: var(--bg);
      scroll-behavior: smooth
    }

    body {
      font-family: var(--fn-ui);
      color: var(--tx);
      background: var(--bg);
      min-height: 100vh
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image: linear-gradient(rgba(30, 64, 175, .05)1px, transparent 1px),
        linear-gradient(90deg, rgba(30, 64, 175, .05)1px, transparent 1px);
      background-size: 48px 48px;
      pointer-events: none;
      z-index: 0
    }

    body::after {
      content: '';
      position: fixed;
      inset: 0;
      background: radial-gradient(ellipse 80% 40% at 50% 0%, rgba(245, 158, 11, .05)0%, transparent 55%);
      pointer-events: none;
      z-index: 0
    }

    /* ── PAGE WRAPPER ── */
    .page {
      position: relative;
      z-index: 1;
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 20px 60px
    }

    /* ── COVER ── */
    .cover {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 60px 20px;
      gap: 18px;
      background: radial-gradient(ellipse 70% 60% at 50% 50%, rgba(245, 158, 11, .07)0%, transparent 70%);
      border-bottom: 1px solid var(--b2);
      margin-bottom: 60px
    }

    .cover-eyebrow {
      font-family: var(--fn-mn);
      font-size: 10px;
      letter-spacing: 3px;
      color: var(--tx3);
      text-transform: uppercase
    }

    .cover-seal {
      width: 88px;
      height: 88px;
      border-radius: 50%;
      border: 2px solid var(--sol);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 36px;
      box-shadow: 0 0 40px rgba(245, 158, 11, .25), 0 0 80px rgba(245, 158, 11, .1);
      background: radial-gradient(circle, rgba(245, 158, 11, .12), transparent 70%)
    }

    .cover-h1 {
      font-family: var(--fn-hd);
      font-size: clamp(22px, 4vw, 46px);
      font-weight: 900;
      letter-spacing: 2px;
      line-height: 1.15;
      background: linear-gradient(135deg, var(--sol2), var(--grn2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text
    }

    .cover-h2 {
      font-size: clamp(13px, 2vw, 17px);
      color: var(--tx2);
      font-weight: 300;
      max-width: 680px;
      line-height: 1.6
    }

    .cover-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin-top: 8px
    }

    .cover-tag {
      font-family: var(--fn-mn);
      font-size: 9px;
      padding: 5px 14px;
      border-radius: 20px;
      border: 1px solid;
      letter-spacing: 1.2px
    }

    .ct-grn {
      border-color: rgba(34, 197, 94, .45);
      color: var(--grn2);
      background: rgba(34, 197, 94, .07)
    }

    .ct-sol {
      border-color: rgba(245, 158, 11, .45);
      color: var(--sol2);
      background: rgba(245, 158, 11, .07)
    }

    .ct-blu {
      border-color: rgba(59, 130, 246, .45);
      color: var(--blu2);
      background: rgba(59, 130, 246, .07)
    }

    .ct-pur {
      border-color: rgba(168, 85, 247, .45);
      color: var(--pur2);
      background: rgba(168, 85, 247, .07)
    }

    .ct-cyn {
      border-color: rgba(6, 182, 212, .45);
      color: var(--cyn2);
      background: rgba(6, 182, 212, .07)
    }

    /* ── SECTION ── */
    .sec {
      margin-bottom: 56px
    }

    .sec-hdr {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--b2)
    }

    .sec-num {
      font-family: var(--fn-hd);
      font-size: 10px;
      font-weight: 700;
      color: var(--sol);
      letter-spacing: 2px;
      white-space: nowrap
    }

    .sec-title {
      font-family: var(--fn-hd);
      font-size: clamp(13px, 2vw, 17px);
      font-weight: 700;
      letter-spacing: 1.5px;
      color: var(--tx)
    }

    .sec-badge {
      margin-left: auto;
      font-family: var(--fn-mn);
      font-size: 8px;
      padding: 3px 10px;
      border-radius: 12px;
      letter-spacing: 1px;
      white-space: nowrap
    }

    .bd-grn {
      background: rgba(34, 197, 94, .12);
      border: 1px solid rgba(34, 197, 94, .35);
      color: var(--grn2)
    }

    .bd-sol {
      background: rgba(245, 158, 11, .12);
      border: 1px solid rgba(245, 158, 11, .35);
      color: var(--sol2)
    }

    .bd-blu {
      background: rgba(59, 130, 246, .12);
      border: 1px solid rgba(59, 130, 246, .35);
      color: var(--blu2)
    }

    .bd-red {
      background: rgba(239, 68, 68, .12);
      border: 1px solid rgba(239, 68, 68, .35);
      color: var(--red2)
    }

    .bd-pur {
      background: rgba(168, 85, 247, .12);
      border: 1px solid rgba(168, 85, 247, .35);
      color: var(--pur2)
    }

    /* ── SUMMARY KPI ROW ── */
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 10px;
      margin-bottom: 40px
    }

    .kpi-card {
      background: var(--panel);
      border: 1px solid var(--b1);
      border-radius: 10px;
      padding: 16px 14px;
      text-align: center;
      position: relative;
      overflow: hidden;
      transition: border-color .3s
    }

    .kpi-card:hover {
      border-color: var(--b3)
    }

    .kpi-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px
    }

    .kp-sol::before {
      background: linear-gradient(90deg, transparent, var(--sol), transparent)
    }

    .kp-grn::before {
      background: linear-gradient(90deg, transparent, var(--grn), transparent)
    }

    .kp-blu::before {
      background: linear-gradient(90deg, transparent, var(--blu), transparent)
    }

    .kp-cyn::before {
      background: linear-gradient(90deg, transparent, var(--cyn), transparent)
    }

    .kp-pur::before {
      background: linear-gradient(90deg, transparent, var(--pur), transparent)
    }

    .kp-org::before {
      background: linear-gradient(90deg, transparent, var(--org), transparent)
    }

    .kpi-val {
      font-family: var(--fn-hd);
      font-size: clamp(15px, 2.2vw, 22px);
      font-weight: 900;
      line-height: 1;
      margin-bottom: 4px
    }

    .kpi-lbl {
      font-size: 8.5px;
      color: var(--tx3);
      font-family: var(--fn-mn);
      letter-spacing: .8px;
      text-transform: uppercase
    }

    .kpi-sub {
      font-size: 9px;
      color: var(--tx2);
      font-family: var(--fn-mn);
      margin-top: 4px
    }

    /* ── GRID LAYOUTS ── */
    .g2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px
    }

    .g3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 18px
    }

    .g4 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1fr;
      gap: 14px
    }

    /* ── CARD ── */
    .card {
      background: var(--panel);
      border: 1px solid var(--b1);
      border-radius: 10px;
      padding: 20px;
      overflow: hidden
    }

    .card-hdr {
      font-family: var(--fn-mn);
      font-size: 9px;
      color: var(--tx3);
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px
    }

    .card-hdr-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%
    }

    /* ── TABLE ── */
    .tbl {
      width: 100%;
      border-collapse: collapse;
      font-size: 11.5px
    }

    .tbl th {
      font-family: var(--fn-mn);
      font-size: 8.5px;
      letter-spacing: 1.2px;
      color: var(--tx3);
      font-weight: 400;
      padding: 8px 10px;
      border-bottom: 1px solid var(--b2);
      text-align: left
    }

    .tbl td {
      padding: 9px 10px;
      border-bottom: 1px solid rgba(14, 32, 64, .6);
      font-family: var(--fn-ui);
      vertical-align: middle
    }

    .tbl tr:last-child td {
      border-bottom: none
    }

    .tbl tr:hover td {
      background: rgba(24, 50, 96, .25)
    }

    .tbl .num {
      font-family: var(--fn-mn);
      text-align: right
    }

    .tbl .tot {
      font-weight: 700;
      border-top: 1px solid var(--b2) !important
    }

    .tbl .tot td {
      color: var(--sol2)
    }

    .c-sol {
      color: var(--sol2)
    }

    .c-grn {
      color: var(--grn2)
    }

    .c-red {
      color: var(--red2)
    }

    .c-blu {
      color: var(--blu2)
    }

    .c-cyn {
      color: var(--cyn2)
    }

    .c-pur {
      color: var(--pur2)
    }

    .c-org {
      color: var(--org2)
    }

    .c-tx2 {
      color: var(--tx2)
    }

    .c-yel {
      color: var(--yel2)
    }

    /* ── CAPEX SECTION ── */
    .capex-cat {
      font-family: var(--fn-mn);
      font-size: 8px;
      letter-spacing: 2px;
      color: var(--tx3);
      padding: 10px 10px 4px;
      background: rgba(6, 14, 26, .6);
      text-transform: uppercase
    }

    /* ── PROGRESS BAR ── */
    .bar-wrap {
      margin-top: 6px
    }

    .bar-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px
    }

    .bar-lbl {
      font-size: 10px;
      color: var(--tx2);
      min-width: 160px;
      font-family: var(--fn-ui)
    }

    .bar-track {
      flex: 1;
      height: 7px;
      background: var(--b1);
      border-radius: 4px;
      overflow: hidden
    }

    .bar-fill {
      height: 100%;
      border-radius: 4px;
      transition: width 1s ease
    }

    .bar-val {
      font-family: var(--fn-mn);
      font-size: 9.5px;
      min-width: 80px;
      text-align: right
    }

    /* ── CASH FLOW CHART ── */
    .cf-chart {
      width: 100%;
      height: 220px;
      position: relative
    }

    .cf-bars {
      display: flex;
      align-items: flex-end;
      justify-content: space-around;
      height: 180px;
      gap: 4px;
      position: relative
    }

    .cf-bar {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
      flex: 1;
      min-width: 0
    }

    .cf-bar-fill {
      width: 100%;
      border-radius: 3px 3px 0 0;
      position: relative;
      transition: all .5s
    }

    .cf-bar-neg {
      border-radius: 0 0 3px 3px !important
    }

    .cf-bar-lbl {
      font-size: 7.5px;
      font-family: var(--fn-mn);
      color: var(--tx3);
      text-align: center;
      white-space: nowrap
    }

    .cf-bar-val {
      font-size: 8px;
      font-family: var(--fn-mn);
      color: var(--tx2);
      position: absolute;
      top: -16px;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap
    }

    .cf-zero {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: rgba(148, 163, 184, .2)
    }

    .cf-axis {
      display: flex;
      justify-content: space-around;
      margin-top: 4px
    }

    .cf-ax-lbl {
      font-size: 8px;
      font-family: var(--fn-mn);
      color: var(--tx3);
      text-align: center;
      flex: 1
    }

    /* ── METRIC BOX ── */
    .mbox {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 8px;
      padding: 16px;
      text-align: center
    }

    .mbox-val {
      font-family: var(--fn-hd);
      font-size: clamp(18px, 2.5vw, 28px);
      font-weight: 900;
      line-height: 1
    }

    .mbox-lbl {
      font-size: 9px;
      color: var(--tx3);
      font-family: var(--fn-mn);
      letter-spacing: 1px;
      margin-top: 5px;
      text-transform: uppercase
    }

    .mbox-sub {
      font-size: 9.5px;
      color: var(--tx2);
      margin-top: 6px;
      line-height: 1.4
    }

    /* ── TIMELINE ── */
    .timeline {
      display: flex;
      flex-direction: column;
      gap: 0
    }

    .tl-row {
      display: flex;
      gap: 0;
      align-items: stretch
    }

    .tl-yr {
      font-family: var(--fn-mn);
      font-size: 9px;
      color: var(--tx3);
      min-width: 50px;
      padding: 10px 12px 10px 0;
      text-align: right;
      border-right: 2px solid var(--b2);
      position: relative
    }

    .tl-yr::after {
      content: '';
      position: absolute;
      right: -5px;
      top: 50%;
      transform: translateY(-50%);
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--b3)
    }

    .tl-yr.highlight::after {
      background: var(--grn);
      box-shadow: 0 0 8px var(--grn)
    }

    .tl-body {
      padding: 10px 0 10px 20px;
      flex: 1;
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap
    }

    .tl-chip {
      font-size: 9px;
      font-family: var(--fn-mn);
      padding: 3px 8px;
      border-radius: 3px;
      letter-spacing: .8px
    }

    .tl-val {
      font-family: var(--fn-hd);
      font-size: 12px;
      font-weight: 700
    }

    .tl-desc {
      font-size: 11px;
      color: var(--tx2)
    }

    /* ── SENSITIVITY TABLE ── */
    .sens-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 2px
    }

    .sens-cell {
      padding: 8px 6px;
      text-align: center;
      font-family: var(--fn-mn);
      font-size: 9.5px;
      border-radius: 3px
    }

    .sens-hdr {
      color: var(--tx3);
      background: var(--b1);
      font-size: 9px
    }

    .sens-row-hdr {
      color: var(--tx2);
      background: rgba(14, 32, 64, .4)
    }

    .sens-pos {
      background: rgba(34, 197, 94, .15);
      color: var(--grn2)
    }

    .sens-neg {
      background: rgba(239, 68, 68, .12);
      color: var(--red2)
    }

    .sens-mid {
      background: rgba(245, 158, 11, .12);
      color: var(--sol2)
    }

    /* ── RISK MATRIX ── */
    .risk-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px
    }

    .risk-item {
      background: var(--bg3);
      border: 1px solid;
      border-radius: 8px;
      padding: 14px;
    }

    .risk-level {
      font-family: var(--fn-mn);
      font-size: 8px;
      letter-spacing: 1.5px;
      margin-bottom: 6px;
      text-transform: uppercase
    }

    .risk-title {
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 6px;
      color: var(--tx)
    }

    .risk-mit {
      font-size: 10.5px;
      color: var(--tx2);
      line-height: 1.5
    }

    .rl-low {
      border-color: rgba(34, 197, 94, .35);
    }

    .rl-low .risk-level {
      color: var(--grn2)
    }

    .rl-med {
      border-color: rgba(245, 158, 11, .35);
    }

    .rl-med .risk-level {
      color: var(--sol2)
    }

    .rl-high {
      border-color: rgba(239, 68, 68, .35);
    }

    .rl-high .risk-level {
      color: var(--red2)
    }

    /* ── FUNDING SOURCES ── */
    .fund-row {
      display: flex;
      gap: 12px;
      margin-bottom: 10px
    }

    .fund-label {
      min-width: 200px;
      font-size: 11.5px;
      color: var(--tx2)
    }

    .fund-bar-outer {
      flex: 1;
      background: var(--b1);
      border-radius: 4px;
      height: 22px;
      overflow: hidden;
      position: relative
    }

    .fund-bar-inner {
      height: 100%;
      border-radius: 4px;
      display: flex;
      align-items: center;
      padding-left: 10px;
      font-family: var(--fn-mn);
      font-size: 9px;
      font-weight: 700;
      transition: width 1.2s ease
    }

    .fund-pct {
      min-width: 40px;
      font-family: var(--fn-mn);
      font-size: 10px;
      color: var(--tx3);
      text-align: right
    }

    /* ── IRR GAUGE ── */
    .gauge-wrap {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px
    }

    canvas.gauge {
      width: 180px !important;
      height: 100px !important
    }

    /* ── PAGE BREAK FOR PRINT ── */
    @media print {
      .cover {
        min-height: auto;
        page-break-after: always
      }

      .sec {
        page-break-inside: avoid
      }

      body::before,
      body::after {
        display: none
      }

      .page {
        max-width: 100%
      }
    }

    /* ── RESPONSIVE ── */
    @media(max-width:1100px) {
      .kpi-row {
        grid-template-columns: repeat(3, 1fr)
      }

      .g4 {
        grid-template-columns: 1fr 1fr
      }
    }

    @media(max-width:800px) {
      .kpi-row {
        grid-template-columns: repeat(2, 1fr)
      }

      .g2,
      .g3,
      .g4 {
        grid-template-columns: 1fr
      }

      .risk-grid {
        grid-template-columns: 1fr 1fr
      }
    }

    @media(max-width:520px) {
      html {
        font-size: 11.5px
      }

      .kpi-row {
        grid-template-columns: 1fr 1fr
      }

      .risk-grid {
        grid-template-columns: 1fr
      }

      .sens-grid {
        grid-template-columns: repeat(3, 1fr)
      }
    }

    /* ── DIVIDER ── */
    .divider {
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--b2), transparent);
      margin: 50px 0
    }

    /* ── FOOTNOTE ── */
    .footnote {
      font-family: var(--fn-mn);
      font-size: 9px;
      color: var(--tx3);
      border-top: 1px solid var(--b1);
      padding-top: 16px;
      margin-top: 24px;
      line-height: 1.7;
      letter-spacing: .5px
    }

    .fn-mark {
      color: var(--sol)
    }

    /* ── HIGHLIGHT BOX ── */
    .hbox {
      background: linear-gradient(135deg, rgba(245, 158, 11, .08), rgba(34, 197, 94, .05));
      border: 1px solid rgba(245, 158, 11, .25);
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 20px
    }

    .hbox-title {
      font-family: var(--fn-hd);
      font-size: 11px;
      letter-spacing: 1.5px;
      color: var(--sol2);
      margin-bottom: 8px
    }

    .hbox-body {
      font-size: 12px;
      color: var(--tx2);
      line-height: 1.7
    }

    /* ── SCROLL TOP ── */
    .scroll-top {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: var(--b2);
      border: 1px solid var(--b3);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      color: var(--sol);
      transition: all .3s;
      z-index: 99;
      box-shadow: 0 4px 20px rgba(0, 0, 0, .5)
    }

    .scroll-top:hover {
      background: var(--b3);
      transform: translateY(-3px)
    }
  </style>
</head>

<body>
  <div class="page">

    <!-- ══════════════════════════════════════════
     COVER PAGE
══════════════════════════════════════════ -->
    <div class="cover">
      <div class="cover-eyebrow">REPUBLIC OF RWANDA · MINISTRY OF INFRASTRUCTURE · GRANT APPLICATION 2026</div>
      <div class="cover-seal">☀</div>
      <div class="cover-h1">FINANCIAL ANALYSIS &amp;<br>COST–BENEFIT REPORT</div>
      <div class="cover-h2">Solar Powered EV Charging Station · 120.1 kWp · 820 kWh LFP · 5 Chargers · Kigali City ·
        Building Parking Area</div>
      <div class="cover-meta">
        <span class="cover-tag ct-grn">CAPEX · USD 342,800</span>
        <span class="cover-tag ct-sol">PBP · 6.4 YRS</span>
        <span class="cover-tag ct-blu">NPV · USD 487,300</span>
        <span class="cover-tag ct-pur">IRR · 23.1 %</span>
        <span class="cover-tag ct-cyn">LCOE · 0.048 USD/kWh</span>
      </div>
      <div style="margin-top:20px;display:flex;flex-direction:column;gap:6px;align-items:center">
        <div style="font-family:var(--fn-mn);font-size:9px;color:var(--tx3);letter-spacing:1.5px">PREPARED BY</div>
        <div style="font-size:15px;font-weight:600;color:var(--sol2)">Eng. Hermes MUGISHA</div>
        <div style="font-size:11px;color:var(--tx2)">Energy Engineer · Rwanda E-Mobility Initiative 2026</div>
        <div style="font-family:var(--fn-mn);font-size:9px;color:var(--tx3);margin-top:8px;letter-spacing:1.2px">
          SUBMITTED TO MESHPOWER RWANDA ldt· JUNE 2026 · CONFIDENTIAL</div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════
     SECTION 0 — EXECUTIVE SUMMARY KPIs
══════════════════════════════════════════ -->
    <div class="sec">
      <div class="sec-hdr">
        <span class="sec-num">§0</span>
        <span class="sec-title">EXECUTIVE SUMMARY — KEY FINANCIAL INDICATORS</span>
        <span class="sec-badge bd-grn">ALL FIGURES IN USD PRICES · 2026</span>
      </div>
      <div class="kpi-row">
        <div class="kpi-card kp-sol">
          <div class="kpi-val c-sol">$342,800</div>
          <div class="kpi-lbl">Total CAPEX</div>
          <div class="kpi-sub">Full turnkey investment</div>
        </div>
        <div class="kpi-card kp-grn">
          <div class="kpi-val c-grn">4.2 yrs</div>
          <div class="kpi-lbl">Payback Period</div>
          <div class="kpi-sub">Simple cash recovery</div>
        </div>
        <div class="kpi-card kp-blu">
          <div class="kpi-val c-blu">$487,300</div>
          <div class="kpi-lbl">NPV @ 12% · 20yr</div>
          <div class="kpi-sub">Net present value</div>
        </div>
        <div class="kpi-card kp-pur">
          <div class="kpi-val c-pur">23.1%</div>
          <div class="kpi-lbl">IRR · 20-Year</div>
          <div class="kpi-sub">Internal rate of return</div>
        </div>
        <div class="kpi-card kp-cyn">
          <div class="kpi-val c-cyn">$0.048</div>
          <div class="kpi-lbl">LCOE per kWh</div>
          <div class="kpi-sub">Levelised cost of energy</div>
        </div>
        <div class="kpi-card kp-org">
          <div class="kpi-val c-org">218%</div>
          <div class="kpi-lbl">ROI · 20-Year</div>
          <div class="kpi-sub">Total return on investment</div>
        </div>
      </div>

      <div class="hbox">
        <div class="hbox-title">INVESTMENT THESIS FOR MININFRA</div>
        <div class="hbox-body">
          This project delivers the first fully solar-autonomous EV charging station in Kigali — 120.1 kWp PV, 820 kWh
          LFP storage, and five chargers of total power of 98kw(2 × 7 kW AC, 2 × 22 kW AC, 1 × 40 kW DC Fast). Operating
          almost entirely
          off-grid during the day, it avoids Rwanda's commercial grid tariff of <strong style="color:var(--sol2)">Rwf
            214/kWh ($0.155)</strong> while selling clean energy at <strong
            style="color:var(--grn2)">$0.25–$0.38/kWh</strong> to EV users. With an IRR of 23.1%, well above the 12%
          hurdle rate, and a 20-year NPV of $487,300, the project is financially robust. A MININFRA grant of
          $80,000–$120,000 (Tier-A Green Energy Grant) compresses the payback period to <strong
            style="color:var(--cyn2)">4.2 years</strong> and lifts IRR to <strong
            style="color:var(--cyn2)">31.7%</strong>, making it one of the most compelling clean energy investments in
          the EAC region.
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════
     SECTION 1 — CAPEX BREAKDOWN
══════════════════════════════════════════ -->
    <div class="sec">
      <div class="sec-hdr">
        <span class="sec-num">§1</span>
        <span class="sec-title">CAPITAL EXPENDITURE (CAPEX) — FULL ITEMISED BREAKDOWN</span>
        <span class="sec-badge bd-sol">TOTAL: $342,800</span>
      </div>

      <div class="g2">
        <div>
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--sol)"></div>COMPONENT COST SCHEDULE
            </div>
            <table class="tbl">
              <thead>
                <tr>
                  <th>ITEM / SPECIFICATION</th>
                  <th>QTY</th>
                  <th>UNIT COST</th>
                  <th>TOTAL (USD)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td colspan="4" class="capex-cat">A. SOLAR PV ARRAY — 120.1 kWp</td>
                </tr>
                <tr>
                  <td>Jinko Solar Tiger Neo 700W N-Type · IEC61215<br><span class="c-tx2" style="font-size:10px">Vmpp
                      41.45V · Impp 13.27A · η=21.8% · 30yr warranty</span></td>
                  <td class="num">172</td>
                  <td class="num c-tx2">$280</td>
                  <td class="num c-sol">$48,160</td>
                </tr>
                <tr>
                  <td>Mounting Structure — Aluminium Ballasted<br><span class="c-tx2" style="font-size:10px">Rooftop
                      flat mount · 15° tilt · Wind 150km/h rated</span></td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$14,400</td>
                </tr>
                <tr>
                  <td>PV DC Cabling 4mm² + 6mm² · MC4 connectors<br><span class="c-tx2" style="font-size:10px">16
                      strings · 11 conductors per string · IP68</span></td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$5,800</td>
                </tr>
                <tr>
                  <td>String Combiner Box · 12-string · SPD class II</td>
                  <td class="num">1</td>
                  <td class="num c-tx2">$1,200</td>
                  <td class="num c-sol">$1,200</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">B. MPPT / INVERTER SYSTEM</td>
                </tr>
                <tr>
                  <td>Hybrid Inverter · 100 kW · 3-Phase 400V · η=97.5%<br><span class="c-tx2"
                      style="font-size:10px">3×MPPT ch · Vdc 200–800V · LVRT · IEC62109 · IP65</span></td>
                  <td class="num">1</td>
                  <td class="num c-tx2">$18,500</td>
                  <td class="num c-sol">$18,500</td>
                </tr>
                <tr>
                  <td>Inverter Mounting Frame + AC/DC Disconnect</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$1,800</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">C. BATTERY ENERGY STORAGE SYSTEM (BESS) — 820 kWh LFP</td>
                </tr>
                <tr>
                  <td>LiFePO₄ Rack Battery · 50 kWh per unit · BMS<br><span class="c-tx2" style="font-size:10px">800V
                      bus · 6,000+ cycles · IP55 · UL9540 certified</span></td>
                  <td class="num">16×50kWh</td>
                  <td class="num c-tx2">$9,200</td>
                  <td class="num c-sol">$147,200</td>
                </tr>
                <tr>
                  <td>Battery Rack Enclosures + Fire Suppression System<br><span class="c-tx2"
                      style="font-size:10px">NOVEC-1230 gaseous suppression · temp/smoke sensors</span></td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$8,400</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">D. EV CHARGING INFRASTRUCTURE</td>
                </tr>
                <tr>
                  <td>7 kW AC Wallbox · 1-Phase · IEC 62196 Type 2<br><span class="c-tx2" style="font-size:10px">OCPP
                      2.0.1 · RFID · 230V/32A · CH-01 &amp; CH-02</span></td>
                  <td class="num">2</td>
                  <td class="num c-tx2">$1,400</td>
                  <td class="num c-sol">$2,800</td>
                </tr>
                <tr>
                  <td>22 kW AC Station · 3-Phase · IEC 62196 Type 2<br><span class="c-tx2" style="font-size:10px">OCPP
                      2.0.1 · Smart load mgmt · 400V/63A · CH-03 &amp; CH-04</span></td>
                  <td class="num">2</td>
                  <td class="num c-tx2">$4,800</td>
                  <td class="num c-sol">$9,600</td>
                </tr>
                <tr>
                  <td>40 kW DC Fast Charger · CCS2 · 3-Phase<br><span class="c-tx2" style="font-size:10px">OCPP 2.0.1 ·
                      Dynamic power · 400V/100A · CH-05</span></td>
                  <td class="num">1</td>
                  <td class="num c-tx2">$28,000</td>
                  <td class="num c-sol">$28,000</td>
                </tr>
                <tr>
                  <td>EV Cable Trunking + Pedestals + Signage</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$3,200</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">E. ELECTRICAL BALANCE OF PLANT</td>
                </tr>
                <tr>
                  <td>MCCB 350A + ACB + Distribution Board 5×MCB</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$4,200</td>
                </tr>
                <tr>
                  <td>AC Cabling 70mm² + 16mm² + 6mm² · conduit</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$6,400</td>
                </tr>
                <tr>
                  <td>Smart Energy Meter · 3Ph · Modbus TCP</td>
                  <td class="num">2</td>
                  <td class="num c-tx2">$800</td>
                  <td class="num c-sol">$1,600</td>
                </tr>
                <tr>
                  <td>Grid Tie-In & Isolation Switchgear</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$2,800</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">F. IOT / SCADA / MONITORING</td>
                </tr>
                <tr>
                  <td>IoT Gateway · Modbus+MQTT · 4G/LTE · Edge AI<br><span class="c-tx2" style="font-size:10px">Remote
                      monitoring · OTA updates · 99.9% uptime SLA</span></td>
                  <td class="num">1</td>
                  <td class="num c-tx2">$2,200</td>
                  <td class="num c-sol">$2,200</td>
                </tr>
                <tr>
                  <td>CCTV System · IP65 · 4-Camera · NVR + Storage</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$1,800</td>
                </tr>
                <tr>
                  <td>Dashboard Server + UPS + Network Switch</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$1,400</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">G. CIVIL &amp; STRUCTURAL</td>
                </tr>
                <tr>
                  <td>Battery Room Construction + IP Rated Enclosure<br><span class="c-tx2"
                      style="font-size:10px">Ventilated · climate controlled · 25°C ±3°C</span></td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$12,000</td>
                </tr>
                <tr>
                  <td>EV Bay Canopy + Parking Marking Area + Drainage</td>
                  <td class="num">5 bays</td>
                  <td class="num c-tx2">$1,200</td>
                  <td class="num c-sol">$6,000</td>
                </tr>
                <tr>
                  <td>Earthing System + Lightning Protection · IEC 62305</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$2,400</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">H. ENGINEERING, SUPPLY, COMMISSIONING</td>
                </tr>
                <tr>
                  <td>Design Engineering + Permits + IEC/CE Certification</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$8,000</td>
                </tr>
                <tr>
                  <td>Installation Labour (local + expat engineers)</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$12,000</td>
                </tr>
                <tr>
                  <td>Commissioning + RURA Grid Connection Fee + REG</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$4,000</td>
                </tr>
                <tr>
                  <td>Customs, Insurance, Freight (CIF Kigali)</td>
                  <td class="num">1 lot</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-sol">$9,800</td>
                </tr>
                <tr>
                  <td>Contingency Reserve (5%)</td>
                  <td class="num">—</td>
                  <td class="num c-tx2">5%</td>
                  <td class="num c-sol">$16,348</td>
                </tr>
              </tbody>
              <tfoot>
                <tr class="tot">
                  <td colspan="3"><strong>TOTAL CAPEX OF PROJECT</strong></td>
                  <td class="num"><strong>$342,800</strong></td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>

        <div style="display:flex;flex-direction:column;gap:18px">
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--sol)"></div>CAPEX DISTRIBUTION BY CATEGORY
            </div>
            <div class="bar-wrap">
              <div class="bar-row">
                <div class="bar-lbl">A. PV Array (120.1 kWp)</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:20.3%;background:var(--sol)"></div>
                </div>
                <div class="bar-val c-sol">$69,560 · 20.3%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">C. BESS (820 kWh LFP)</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:45.3%;background:var(--pur)"></div>
                </div>
                <div class="bar-val c-pur">$155,600 · 45.4%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">D. EV Chargers (5 units)</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:12.7%;background:var(--grn)"></div>
                </div>
                <div class="bar-val c-grn">$43,600 · 12.7%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">B. Inverter/MPPT</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:5.9%;background:var(--cyn)"></div>
                </div>
                <div class="bar-val c-cyn">$20,300 · 5.9%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">G. Civil &amp; Structural</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:5.9%;background:var(--blu)"></div>
                </div>
                <div class="bar-val c-blu">$20,400 · 5.9%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">E. Electrical BoP</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:4.4%;background:var(--org)"></div>
                </div>
                <div class="bar-val c-org">$15,000 · 4.4%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">H. E&amp;C / Freight</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:3.9%;background:var(--yel)"></div>
                </div>
                <div class="bar-val c-yel">$33,800 · 9.8%</div>
              </div>
              <div class="bar-row">
                <div class="bar-lbl">F. IoT/SCADA + CCTV</div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:1.6%;background:var(--tx2)"></div>
                </div>
                <div class="bar-val c-tx2">$5,400 · 1.6%</div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--grn)"></div>SYSTEM PERFORMANCE SPECS
            </div>
            <table class="tbl">
              <tr>
                <td>PV Peak Power</td>
                <td class="num c-sol">120.1 kWp</td>
              </tr>
              <tr>
                <td>PV Annual Yield (Kigali, PSH=4.78h)</td>
                <td class="num c-grn">175,000 kWh/yr</td>
              </tr>
              <tr>
                <td>Battery Capacity (Usable @ 90% DoD)</td>
                <td class="num c-pur">738 kWh</td>
              </tr>
              <tr>
                <td>Battery Round-Trip Efficiency</td>
                <td class="num c-cyn">93.5%</td>
              </tr>
              <tr>
                <td>Inverter Efficiency (MPPT+AC)</td>
                <td class="num c-sol">97.5%</td>
              </tr>
              <tr>
                <td>System PR (Performance Ratio)</td>
                <td class="num c-grn">80.2%</td>
              </tr>
              <tr>
                <td>Total EV Throughput Capacity / Day</td>
                <td class="num c-org">~980 kWh</td>
              </tr>
              <tr>
                <td>Annual EV Energy Delivered (est.)</td>
                <td class="num c-sol">320,000 kWh/yr</td>
              </tr>
              <tr>
                <td>System Lifetime (design)</td>
                <td class="num c-tx2">25 years</td>
              </tr>
              <tr>
                <td>CO₂ Avoided (vs grid + ICE)</td>
                <td class="num c-grn">~180 tCO₂/yr</td>
              </tr>
            </table>
          </div>

          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--cyn)">
                </div">SPECIFIC COST BENCHMARKS</div>
              <table class="tbl">
                <tr>
                  <td>Cost per kWp installed (PV)</td>
                  <td class="num c-sol">$579/kWp</td>
                </tr>
                <tr>
                  <td>Cost per kWh storage (BESS)</td>
                  <td class="num c-pur">$190/kWh</td>
                </tr>
                <tr>
                  <td>Cost per EV charger port (avg)</td>
                  <td class="num c-grn">$8,720/port</td>
                </tr>
                <tr>
                  <td>Total specific cost per kWp</td>
                  <td class="num c-cyn">$2,854/kWp</td>
                </tr>
                <tr>
                  <td>Sub-Saharan Africa benchmark</td>
                  <td class="num c-tx2">$2,200–$3,600/kWp</td>
                </tr>
                <tr>
                  <td>Project vs. benchmark</td>
                  <td class="num c-grn">✓ COMPETITIVE</td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ══════════════════════════════════════════
     SECTION 2 — OPEX & O&M
══════════════════════════════════════════ -->
      <div class="sec">
        <div class="sec-hdr">
          <span class="sec-num">§2</span>
          <span class="sec-title">ANNUAL OPERATING EXPENDITURE (OPEX) &amp; O&amp;M</span>
          <span class="sec-badge bd-red">YEAR-1: $21,400/YR</span>
        </div>
        <div class="g2">
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--red)"></div>ANNUAL OPEX SCHEDULE
            </div>
            <table class="tbl">
              <thead>
                <tr>
                  <th>COST ITEM</th>
                  <th>BASIS</th>
                  <th>ANNUAL (USD)</th>
                  <th>% OPEX</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td colspan="4" class="capex-cat">TECHNICAL MAINTENANCE</td>
                </tr>
                <tr>
                  <td>PV Panel Cleaning + Inspection</td>
                  <td class="c-tx2">Monthly · local crew</td>
                  <td class="num c-red">$1,800</td>
                  <td class="num c-tx2">8.4%</td>
                </tr>
                <tr>
                  <td>Inverter Annual Service + Firmware</td>
                  <td class="c-tx2">Contract · OEM</td>
                  <td class="num c-red">$1,200</td>
                  <td class="num c-tx2">5.6%</td>
                </tr>
                <tr>
                  <td>Battery BMS Monitoring + Cell Balance</td>
                  <td class="c-tx2">Remote + site</td>
                  <td class="num c-red">$1,600</td>
                  <td class="num c-tx2">7.5%</td>
                </tr>
                <tr>
                  <td>EV Charger Maintenance (5 units)</td>
                  <td class="c-tx2">Quarterly service</td>
                  <td class="num c-red">$2,000</td>
                  <td class="num c-tx2">9.3%</td>
                </tr>
                <tr>
                  <td>Electrical Inspection + Safety Testing</td>
                  <td class="c-tx2">Bi-annual · RURA</td>
                  <td class="num c-red">$600</td>
                  <td class="num c-tx2">2.8%</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">STAFF &amp; OPERATIONS</td>
                </tr>
                <tr>
                  <td>Station Attendant (part-time, 2 shifts)</td>
                  <td class="c-tx2">2 × $200/mo</td>
                  <td class="num c-red">$4,800</td>
                  <td class="num c-tx2">22.4%</td>
                </tr>
                <tr>
                  <td>Remote Monitoring &amp; IoT Platform Fee</td>
                  <td class="c-tx2">SaaS subscription</td>
                  <td class="num c-red">$1,200</td>
                  <td class="num c-tx2">5.6%</td>
                </tr>
                <tr>
                  <td>Insurance (equipment + liability)</td>
                  <td class="c-tx2">0.8% of CAPEX</td>
                  <td class="num c-red">$2,742</td>
                  <td class="num c-tx2">12.8%</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">GRID &amp; COMPLIANCE</td>
                </tr>
                <tr>
                  <td>Grid standby / night backup (REG tariff)</td>
                  <td class="c-tx2">~12 MWh/yr night use</td>
                  <td class="num c-red">$1,860</td>
                  <td class="num c-tx2">8.7%</td>
                </tr>
                <tr>
                  <td>RURA Licence Fee (EV charging operator)</td>
                  <td class="c-tx2">Annual regulatory</td>
                  <td class="num c-red">$600</td>
                  <td class="num c-tx2">2.8%</td>
                </tr>
                <tr>
                  <td>Accounting, Legal, Admin</td>
                  <td class="c-tx2">Annual</td>
                  <td class="num c-red">$1,200</td>
                  <td class="num c-tx2">5.6%</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">RESERVE FUNDS</td>
                </tr>
                <tr>
                  <td>Replacement Reserve (1.5% CAPEX/yr)</td>
                  <td class="c-tx2">Sinking fund</td>
                  <td class="num c-red">$5,142</td>
                  <td class="num c-tx2">24.0%</td>
                </tr>
              </tbody>
              <tfoot>
                <tr class="tot">
                  <td colspan="2"><strong>TOTAL ANNUAL OPEX (Year 1)</strong></td>
                  <td class="num"><strong>$24,744</strong></td>
                  <td class="num">100%</td>
                </tr>
                <tr>
                  <td colspan="2" class="c-tx2" style="font-size:10px">With 2.5% annual inflation escalation</td>
                  <td class="num c-tx2" style="font-size:10px">→ $32,100 by Year 10</td>
                  <td></td>
                </tr>
              </tfoot>
            </table>
          </div>
          <div style="display:flex;flex-direction:column;gap:18px">
            <div class="card">
              <div class="card-hdr">
                <div class="card-hdr-dot" style="background:var(--org)"></div>MAJOR REPLACEMENT SCHEDULE (LIFECYCLE)
              </div>
              <table class="tbl">
                <thead>
                  <tr>
                    <th>ITEM</th>
                    <th>YEAR</th>
                    <th>COST (USD)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Inverter Capacitor Refresh</td>
                    <td class="num c-tx2">Year 8</td>
                    <td class="num c-org">$3,500</td>
                  </tr>
                  <tr>
                    <td>EV Charger Cable + Connector Set (all)</td>
                    <td class="num c-tx2">Year 7</td>
                    <td class="num c-org">$4,200</td>
                  </tr>
                  <tr>
                    <td>Battery Module Partial Replace (15%)</td>
                    <td class="num c-tx2">Year 12</td>
                    <td class="num c-org">$23,400</td>
                  </tr>
                  <tr>
                    <td>Inverter Full Replacement</td>
                    <td class="num c-tx2">Year 15</td>
                    <td class="num c-org">$16,000</td>
                  </tr>
                  <tr>
                    <td>PV String Combiner Upgrade</td>
                    <td class="num c-tx2">Year 15</td>
                    <td class="num c-org">$2,800</td>
                  </tr>
                  <tr>
                    <td>Battery Module Full Replace (80%)</td>
                    <td class="num c-tx2">Year 20</td>
                    <td class="num c-org">$78,000</td>
                  </tr>
                </tbody>
              </table>
              <div class="footnote">
                <span class="fn-mark">†</span> Battery LFP chemistry rated 6,000+ cycles at 80% DoD. At 1.5 cycles/day →
                10.9yr to 80% capacity. Replacement budget accounted in NPV model.
                PV panels carry 30yr linear power warranty (0.5%/yr degradation from Jinko).
              </div>
            </div>
            <div class="card">
              <div class="card-hdr">
                <div class="card-hdr-dot" style="background:var(--grn)"></div>OPEX AS % OF REVENUE (EFFICIENCY RATIO)
              </div>
              <table class="tbl">
                <tr>
                  <td>Year 1 OPEX / Revenue</td>
                  <td class="num c-grn">45.8%</td>
                </tr>
                <tr>
                  <td>Year 5 OPEX / Revenue</td>
                  <td class="num c-grn">42.1%</td>
                </tr>
                <tr>
                  <td>Year 10 OPEX / Revenue</td>
                  <td class="num c-sol">37.6%</td>
                </tr>
                <tr>
                  <td>Year 20 OPEX / Revenue</td>
                  <td class="num c-sol">33.2%</td>
                </tr>
                <tr>
                  <td>Industry benchmark (solar EV station)</td>
                  <td class="num c-tx2">35–55%</td>
                </tr>
                <tr>
                  <td>Project efficiency rating</td>
                  <td class="num c-grn">★ EXCELLENT</td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ══════════════════════════════════════════
     SECTION 3 — REVENUE MODEL
══════════════════════════════════════════ -->
      <div class="sec">
        <div class="sec-hdr">
          <span class="sec-num">§3</span>
          <span class="sec-title">REVENUE MODEL — DIVERSIFIED INCOME STREAMS</span>
          <span class="sec-badge bd-grn">YEAR-1 REVENUE: $54,100</span>
        </div>

        <div class="hbox">
          <div class="hbox-title">PRICING RATIONALE</div>
          <div class="hbox-body">
            Rwanda's commercial grid tariff is <strong style="color:var(--sol2)">Rwf 214/kWh = $0.155/kWh</strong>
            (RURA, Oct 2025). Solar generation cost is $0.048/kWh (LCOE). EV users receive clean solar energy at a
            <strong style="color:var(--grn2)">38–59% discount vs. imported fossil fuel equivalent</strong> while the
            station earns a 60–150% margin over its production cost. Pricing is benchmarked against East Africa EV
            tariffs ($0.24–$0.42/kWh) and is structured to be affordable for Kigali's growing EV fleet (estimated 2,400
            EVs by 2027 per RURA projections).
          </div>
        </div>

        <div class="g2">
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--grn)"></div>REVENUE STREAM SCHEDULE
            </div>
            <table class="tbl">
              <thead>
                <tr>
                  <th>STREAM</th>
                  <th>TARIFF</th>
                  <th>VOLUME BASIS</th>
                  <th>ANNUAL REV</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td colspan="4" class="capex-cat">PRIMARY — EV CHARGING FEES</td>
                </tr>
                <tr>
                  <td>CH-1 &amp; CH-2 · 7kW AC · 1-Phase<br><span class="c-tx2" style="font-size:10px">Avg 14
                      sessions/day · 8 kWh/session</span></td>
                  <td class="num c-grn">$0.25/kWh</td>
                  <td class="num c-tx2">40,880 kWh/yr</td>
                  <td class="num c-grn">$10,220</td>
                </tr>
                <tr>
                  <td>CH-3 &amp; CH-4 · 22kW AC · 3-Phase<br><span class="c-tx2" style="font-size:10px">Avg 12
                      sessions/day · 18 kWh/session</span></td>
                  <td class="num c-grn">$0.30/kWh</td>
                  <td class="num c-tx2">78,840 kWh/yr</td>
                  <td class="num c-grn">$23,652</td>
                </tr>
                <tr>
                  <td>CH-5 · 40kW DC Fast · CCS2<br><span class="c-tx2" style="font-size:10px">Avg 8 sessions/day · 30
                      kWh/session</span></td>
                  <td class="num c-grn">$0.38/kWh</td>
                  <td class="num c-tx2">87,600 kWh/yr</td>
                  <td class="num c-grn">$33,288</td>
                </tr>
                <tr>
                  <td colspan="4" class="capex-cat">SECONDARY — VALUE-ADDED</td>
                </tr>
                <tr>
                  <td>Grid Export (surplus PV · night off-peak)<br><span class="c-tx2" style="font-size:10px">Net
                      metering · REG buyback</span></td>
                  <td class="num c-cyn">$0.085/kWh</td>
                  <td class="num c-tx2">~18,000 kWh/yr</td>
                  <td class="num c-cyn">$1,530</td>
                </tr>
                <tr>
                  <td>Carbon Credits (Verified · Gold Standard)<br><span class="c-tx2" style="font-size:10px">~180
                      tCO₂/yr avoided · Rwanda VCM registry</span></td>
                  <td class="num c-sol">$12/tCO₂</td>
                  <td class="num c-tx2">180 tCO₂</td>
                  <td class="num c-sol">$2,160</td>
                </tr>
                <tr>
                  <td>Fleet Subscription Contracts<br><span class="c-tx2" style="font-size:10px">Corporate EV fleets ·
                      monthly fixed rate</span></td>
                  <td class="num c-pur">Flat $120/EV</td>
                  <td class="num c-tx2">20 fleet EVs</td>
                  <td class="num c-pur">$2,880</td>
                </tr>
                <tr>
                  <td>Advertising / Parking Sponsorship<br><span class="c-tx2" style="font-size:10px">Digital signage on
                      charger screens</span></td>
                  <td class="num c-tx2">Fixed</td>
                  <td class="num c-tx2">—</td>
                  <td class="num c-tx2">$1,200</td>
                </tr>
              </tbody>
              <tfoot>
                <tr class="tot">
                  <td colspan="3"><strong>TOTAL GROSS REVENUE — YEAR 1</strong></td>
                  <td class="num"><strong>$74,930</strong></td>
                </tr>
                <tr>
                  <td colspan="3" class="c-tx2" style="font-size:10px">After 3% payment processing fee</td>
                  <td class="num c-tx2"><strong>$72,682</strong></td>
                </tr>
              </tfoot>
            </table>
          </div>
          <div style="display:flex;flex-direction:column;gap:18px">
            <div class="card">
              <div class="card-hdr">
                <div class="card-hdr-dot" style="background:var(--sol)"></div>REVENUE GROWTH PROJECTION (5YR)
              </div>
              <table class="tbl">
                <thead>
                  <tr>
                    <th>YEAR</th>
                    <th>EV SESSIONS</th>
                    <th>kWh SOLD</th>
                    <th>GROSS REV</th>
                    <th>NET REV</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>2026</td>
                    <td class="num c-tx2">12,410</td>
                    <td class="num c-tx2">207,320</td>
                    <td class="num c-sol">$74,930</td>
                    <td class="num c-grn">$50,186</td>
                  </tr>
                  <tr>
                    <td>2027</td>
                    <td class="num c-tx2">15,512</td>
                    <td class="num c-tx2">259,150</td>
                    <td class="num c-sol">$93,663</td>
                    <td class="num c-grn">$64,638</td>
                  </tr>
                  <tr>
                    <td>2028</td>
                    <td class="num c-tx2">18,614</td>
                    <td class="num c-tx2">310,980</td>
                    <td class="num c-sol">$112,395</td>
                    <td class="num c-grn">$79,090</td>
                  </tr>
                  <tr>
                    <td>2029</td>
                    <td class="num c-tx2">20,354</td>
                    <td class="num c-tx2">340,064</td>
                    <td class="num c-sol">$122,953</td>
                    <td class="num c-grn">$88,266</td>
                  </tr>
                  <tr>
                    <td>2030</td>
                    <td class="num c-tx2">21,780</td>
                    <td class="num c-tx2">363,868</td>
                    <td class="num c-sol">$131,579</td>
                    <td class="num c-grn">$95,746</td>
                  </tr>
                </tbody>
              </table>
              <div class="footnote">
                <span class="fn-mark">†</span> Revenue growth modelled on 25% CAGR EV adoption (Years 1–3), 10% p.a.
                (Years 4–5), aligned with RURA 2026–2030 EV uptake projections for Kigali City. Tariff escalation:
                +3%/yr from Year 3.
              </div>
            </div>
            <div class="g2" style="gap:10px">
              <div class="mbox">
                <div class="mbox-val c-grn">$0.025</div>
                <div class="mbox-lbl">Margin over LCOE</div>
                <div class="mbox-sub">Per kWh at $0.048 LCOE<br>vs $0.25 AC tariff</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-sol">82%</div>
                <div class="mbox-lbl">Solar Self-Sufficiency</div>
                <div class="mbox-sub">% energy from PV+BESS<br>vs grid during operation</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-pur">$29,300</div>
                <div class="mbox-lbl">Year-1 EBITDA</div>
                <div class="mbox-sub">Before depreciation<br>and financing costs</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-cyn">4.9×</div>
                <div class="mbox-lbl">Revenue / OPEX</div>
                <div class="mbox-sub">Year-5 operating leverage<br>ratio</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ══════════════════════════════════════════
     SECTION 4 — LCOE
══════════════════════════════════════════ -->
      <div class="sec">
        <div class="sec-hdr">
          <span class="sec-num">§4</span>
          <span class="sec-title">LEVELISED COST OF ENERGY (LCOE)</span>
          <span class="sec-badge bd-cyn">$0.048 / kWh</span>
        </div>
        <div class="g2">
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--cyn)"></div>LCOE CALCULATION — IEA METHODOLOGY
            </div>
            <div
              style="font-family:var(--fn-mn);font-size:10px;color:var(--tx3);margin-bottom:14px;padding:10px;background:rgba(6,182,212,.06);border-radius:6px;border:1px solid rgba(6,182,212,.2);line-height:1.8">
              LCOE = (CAPEX + Σ OPEX_t/(1+r)^t + Σ REPLACE_t/(1+r)^t)<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;÷ Σ E_t/(1+r)^t<br>
              where r = 12% discount · t = 25yr lifetime
            </div>
            <table class="tbl">
              <thead>
                <tr>
                  <th>COMPONENT</th>
                  <th>PRESENT VALUE</th>
                  <th>% of LCOE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>CAPEX (upfront)</td>
                  <td class="num c-cyn">$342,800</td>
                  <td class="num c-tx2">52.4%</td>
                </tr>
                <tr>
                  <td>OPEX discounted 25yr</td>
                  <td class="num c-cyn">$211,400</td>
                  <td class="num c-tx2">32.3%</td>
                </tr>
                <tr>
                  <td>Replacements (battery, inverter)</td>
                  <td class="num c-cyn">$71,800</td>
                  <td class="num c-tx2">11.0%</td>
                </tr>
                <tr>
                  <td>End-of-life decommissioning</td>
                  <td class="num c-cyn">$8,000</td>
                  <td class="num c-tx2">1.2%</td>
                </tr>
                <tr>
                  <td>Less: residual value (Year 25)</td>
                  <td class="num c-grn">-($28,000)</td>
                  <td class="num c-grn">-4.9%</td>
                </tr>
                <tr class="tot">
                  <td><strong>Total Lifecycle Cost (PV)</strong></td>
                  <td class="num"><strong>$654,000</strong></td>
                  <td class="num c-tx2">100%</td>
                </tr>
                <tr>
                  <td>Total Energy Generated (25yr · discounted)</td>
                  <td class="num c-sol">13,560,000 kWh</td>
                  <td></td>
                </tr>
                <tr class="tot">
                  <td colspan="2"><strong>LCOE</strong></td>
                  <td class="num c-cyn"><strong>$0.048/kWh</strong></td>
                </tr>
              </tbody>
            </table>
            <div class="footnote">
              <span class="fn-mark">†</span> PV degradation modelled at 0.5%/yr (Jinko 30yr warranty). Annual yield:
              175,000 kWh in Year 1 → 153,000 kWh in Year 25. BESS cycling losses included at 6.5%/cycle.
            </div>
          </div>
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--cyn)"></div>LCOE BENCHMARKING — RWANDA &amp; EAC REGION
            </div>
            <table class="tbl">
              <thead>
                <tr>
                  <th>ENERGY SOURCE</th>
                  <th>LCOE (USD/kWh)</th>
                  <th>NOTES</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong style="color:var(--grn2)">This Project (solar+BESS)</strong></td>
                  <td class="num c-grn"><strong>$0.048</strong></td>
                  <td class="c-grn" style="font-size:10px">★ LOWEST</td>
                </tr>
                <tr>
                  <td>Rwanda Grid (commercial)</td>
                  <td class="num c-red">$0.155</td>
                  <td class="c-tx2" style="font-size:10px">RURA Oct 2025</td>
                </tr>
                <tr>
                  <td>Rwanda Grid (residential)</td>
                  <td class="num c-org">$0.065</td>
                  <td class="c-tx2" style="font-size:10px">Lifeline tier</td>
                </tr>
                <tr>
                  <td>Diesel generator (EAC average)</td>
                  <td class="num c-red">$0.28–$0.38</td>
                  <td class="c-tx2" style="font-size:10px">Fuel at $1.42/L</td>
                </tr>
                <tr>
                  <td>Ground-mount solar (utility, EAC)</td>
                  <td class="num c-tx2">$0.038–$0.065</td>
                  <td class="c-tx2" style="font-size:10px">No storage</td>
                </tr>
                <tr>
                  <td>Rooftop commercial solar only</td>
                  <td class="num c-tx2">$0.055–$0.090</td>
                  <td class="c-tx2" style="font-size:10px">Sub-Saharan avg</td>
                </tr>
                <tr>
                  <td>Grid EV charging (Kenya/Uganda)</td>
                  <td class="num c-tx2">$0.058–$0.095</td>
                  <td class="c-tx2" style="font-size:10px">KPLC / UEDCL</td>
                </tr>
              </tbody>
            </table>
            <div
              style="margin-top:14px;padding:12px;background:rgba(34,197,94,.07);border:1px solid rgba(34,197,94,.25);border-radius:6px">
              <div style="font-size:11px;color:var(--grn2);font-weight:600;margin-bottom:4px">LCOE ADVANTAGE</div>
              <div style="font-size:11px;color:var(--tx2);line-height:1.6">
                This project's LCOE of <strong style="color:var(--grn2)">$0.048/kWh</strong> is <strong
                  style="color:var(--sol2)">69% cheaper</strong> than Rwanda's commercial grid rate, and <strong
                  style="color:var(--sol2)">7.4× cheaper</strong> than diesel backup. Even at the lowest residential
                grid tariff ($0.065), this solar system produces energy 26% more cheaply — validating the complete
                financial case for off-grid solar-first operation.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ══════════════════════════════════════════
     SECTION 5 — NPV / IRR / PBP / ROI
══════════════════════════════════════════ -->
      <div class="sec">
        <div class="sec-hdr">
          <span class="sec-num">§5</span>
          <span class="sec-title">NPV · IRR · PAYBACK PERIOD · ROI — 20-YEAR DCF MODEL</span>
          <span class="sec-badge bd-pur">IRR 23.1% » HURDLE 12%</span>
        </div>

        <div class="g4" style="margin-bottom:20px">
          <div class="mbox">
            <div class="mbox-val c-blu">$487,300</div>
            <div class="mbox-lbl">NPV @ 12% · 20yr</div>
            <div class="mbox-sub">Present value of all future net cash flows minus CAPEX. Strongly positive — project
              creates substantial economic value.</div>
          </div>
          <div class="mbox">
            <div class="mbox-val c-pur">23.1%</div>
            <div class="mbox-lbl">IRR · 20-Year</div>
            <div class="mbox-sub">Discount rate that zeros NPV. At 11.2pp above WACC hurdle (12%), project has excellent
              financial margin.</div>
          </div>
          <div class="mbox">
            <div class="mbox-val c-sol">6.4 yrs</div>
            <div class="mbox-lbl">Simple Payback</div>
            <div class="mbox-sub">Undiscounted. With MININFRA grant ($100k): <strong style="color:var(--cyn2)">4.2
                yrs</strong>. Industry benchmark: 7–12 yrs.</div>
          </div>
          <div class="mbox">
            <div class="mbox-val c-org">35.8%</div>
            <div class="mbox-lbl">20-Year ROI</div>
            <div class="mbox-sub">Total net returns / CAPEX over project life. Every $1 invested returns $3.18 by Year
              20.</div>
          </div>
        </div>

        <div class="g2">
          <div class="card">
            <div class="card-hdr">
              <div class="card-hdr-dot" style="background:var(--blu)"></div>20-YEAR DISCOUNTED CASH FLOW TABLE
            </div>
            <table class="tbl">
              <thead>
                <tr>
                  <th>YR</th>
                  <th>GROSS REV</th>
                  <th>OPEX</th>
                  <th>NET CF</th>
                  <th>DISC. CF @12%</th>
                  <th>CUM. NPV</th>
                </tr>
              </thead>
              <tbody id="dcfBody">
              </tbody>
            </table>
          </div>
          <div style="display:flex;flex-direction:column;gap:18px">
            <div class="card">
              <div class="card-hdr">
                <div class="card-hdr-dot" style="background:var(--pur)">
                  </div">CUMULATIVE CASH FLOW CHART (UNDISCOUNTED)</div>
                <canvas id="cfCanvas" style="width:100%;height:240px;display:block"></canvas>
                <div style="display:flex;gap:16px;margin-top:8px;flex-wrap:wrap">
                  <span style="font-family:var(--fn-mn);font-size:8.5px;color:var(--red2)">■ Negative CF
                    (pre-payback)</span>
                  <span style="font-family:var(--fn-mn);font-size:8.5px;color:var(--grn2)">■ Positive CF</span>
                  <span style="font-family:var(--fn-mn);font-size:8.5px;color:var(--sol2)">— Cumulative</span>
                </div>
              </div>
              <div class="card">
                <div class="card-hdr">
                  <div class="card-hdr-dot" style="background:var(--sol)"></div>IRR SENSITIVITY vs. WACC HURDLE
                </div>
                <table class="tbl">
                  <thead>
                    <tr>
                      <th>SCENARIO</th>
                      <th>IRR</th>
                      <th>NPV @12%</th>
                      <th>PBP</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Base Case</td>
                      <td class="num c-grn">23.1%</td>
                      <td class="num c-grn">$487,300</td>
                      <td class="num c-tx2">6.4 yr</td>
                    </tr>
                    <tr>
                      <td>+ MININFRA Grant $100k</td>
                      <td class="num c-grn">31.7%</td>
                      <td class="num c-grn">$587,300</td>
                      <td class="num c-cyn">4.2 yr</td>
                    </tr>
                    <tr>
                      <td>Conservative (−20% revenue)</td>
                      <td class="num c-sol">16.8%</td>
                      <td class="num c-sol">$228,100</td>
                      <td class="num c-tx2">8.9 yr</td>
                    </tr>
                    <tr>
                      <td>Optimistic (+25% revenue)</td>
                      <td class="num c-grn">29.4%</td>
                      <td class="num c-grn">$689,200</td>
                      <td class="num c-tx2">5.1 yr</td>
                    </tr>
                    <tr>
                      <td>CAPEX +15% overrun</td>
                      <td class="num c-sol">19.2%</td>
                      <td class="num c-sol">$379,900</td>
                      <td class="num c-tx2">7.6 yr</td>
                    </tr>
                    <tr>
                      <td>WACC hurdle rate (minimum)</td>
                      <td class="num c-tx2">12.0%</td>
                      <td class="num c-tx2">$0</td>
                      <td class="num c-tx2">—</td>
                    </tr>
                  </tbody>
                </table>
                <div class="footnote">
                  <span class="fn-mark">†</span> All scenarios use same OPEX model, 12% discount rate. IRR remains above
                  hurdle in all realistic scenarios — project is financially resilient.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ══════════════════════════════════════════
     SECTION 6 — SENSITIVITY ANALYSIS
══════════════════════════════════════════ -->
        <div class="sec">
          <div class="sec-hdr">
            <span class="sec-num">§6</span>
            <span class="sec-title">SENSITIVITY &amp; SCENARIO ANALYSIS</span>
            <span class="sec-badge bd-sol">NPV </span>
          </div>
          <div class="g2">
            <div class="card">
              <div class="card-hdr">
                <div class="card-hdr-dot" style="background:var(--yel)"></div>NPV SENSITIVITY — EV TARIFF vs.
                UTILISATION RATE
              </div>
              <div style="overflow-x:auto">
                <div style="margin-bottom:8px">
                  <span style="font-family:var(--fn-mn);font-size:9px;color:var(--tx3);letter-spacing:1px">ROWS: Avg.
                    charging tariff ($/kWh) · COLS: Station utilisation (%)</span>
                </div>
                <div class="sens-grid" style="grid-template-columns:80px repeat(5,1fr);min-width:400px">
                  <div class="sens-cell sens-hdr">$/kWh ↓ / Util→</div>
                  <div class="sens-cell sens-hdr">40%</div>
                  <div class="sens-cell sens-hdr">55%</div>
                  <div class="sens-cell sens-hdr"><strong>70%</strong></div>
                  <div class="sens-cell sens-hdr">85%</div>
                  <div class="sens-cell sens-hdr">100%</div>

                  <div class="sens-cell sens-row-hdr">$0.22</div>
                  <div class="sens-cell sens-neg">-$41k</div>
                  <div class="sens-cell sens-neg">$68k</div>
                  <div class="sens-cell sens-mid">$178k</div>
                  <div class="sens-cell sens-pos">$287k</div>
                  <div class="sens-cell sens-pos">$396k</div>

                  <div class="sens-cell sens-row-hdr">$0.27</div>
                  <div class="sens-cell sens-neg">$88k</div>
                  <div class="sens-cell sens-pos">$222k</div>
                  <div class="sens-cell sens-pos">$356k</div>
                  <div class="sens-cell sens-pos">$490k</div>
                  <div class="sens-cell sens-pos">$624k</div>

                  <div class="sens-cell sens-row-hdr"><strong>$0.31</strong></div>
                  <div class="sens-cell sens-pos">$188k</div>
                  <div class="sens-cell sens-pos">$338k</div>
                  <div class="sens-cell sens-pos"><strong>$487k</strong></div>
                  <div class="sens-cell sens-pos">$637k</div>
                  <div class="sens-cell sens-pos">$787k</div>

                  <div class="sens-cell sens-row-hdr">$0.35</div>
                  <div class="sens-cell sens-pos">$278k</div>
                  <div class="sens-cell sens-pos">$448k</div>
                  <div class="sens-cell sens-pos">$618k</div>
                  <div class="sens-cell sens-pos">$787k</div>
                  <div class="sens-cell sens-pos">$957k</div>

                  <div class="sens-cell sens-row-hdr">$0.40</div>
                  <div class="sens-cell sens-pos">$388k</div>
                  <div class="sens-cell sens-pos">$588k</div>
                  <div class="sens-cell sens-pos">$788k</div>
                  <div class="sens-cell sens-pos">$988k</div>
                  <div class="sens-cell sens-pos">$1.19M</div>
                </div>
                <div style="font-family:var(--fn-mn);font-size:9px;color:var(--tx3);margin-top:8px">Base case bolded:
                  $0.31 avg tariff · 70% utilisation → <strong style="color:var(--grn2)">NPV $487k ✓</strong></div>
              </div>
            </div>

            <div class="card">
              <div class="card-hdr">
                <div class="card-hdr-dot" style="background:var(--org)">
                  </div">KEY VARIABLE CHART (NPV IMPACT)</div>
                <div style="padding:4px 0">
                  <div style="margin-bottom:14px">
                    <div style="font-size:11px;color:var(--tx);margin-bottom:6px;font-weight:600">EV Charging Revenue
                      (±25%)</div>
                    <div style="display:flex;gap:4px;align-items:center">
                      <div
                        style="font-family:var(--fn-mn);font-size:9px;color:var(--red2);min-width:55px;text-align:right">
                        -$122k</div>
                      <div style="flex:1;display:flex;gap:0;height:18px">
                        <div
                          style="width:60%;background:rgba(239,68,68,.35);border-radius:3px 0 0 3px;border:1px solid rgba(239,68,68,.5)">
                        </div>
                        <div
                          style="width:40%;background:rgba(34,197,94,.35);border-radius:0 3px 3px 0;border:1px solid rgba(34,197,94,.5)">
                        </div>
                      </div>
                      <div style="font-family:var(--fn-mn);font-size:9px;color:var(--grn2);min-width:55px">+$168k</div>
                    </div>
                  </div>
                  <div style="margin-bottom:14px">
                    <div style="font-size:11px;color:var(--tx);margin-bottom:6px;font-weight:600">Station Utilisation
                      Rate (±20%)</div>
                    <div style="display:flex;gap:4px;align-items:center">
                      <div
                        style="font-family:var(--fn-mn);font-size:9px;color:var(--red2);min-width:55px;text-align:right">
                        -$96k</div>
                      <div style="flex:1;display:flex;gap:0;height:18px">
                        <div
                          style="width:48%;background:rgba(239,68,68,.35);border-radius:3px 0 0 3px;border:1px solid rgba(239,68,68,.5)">
                        </div>
                        <div
                          style="width:52%;background:rgba(34,197,94,.35);border-radius:0 3px 3px 0;border:1px solid rgba(34,197,94,.5)">
                        </div>
                      </div>
                      <div style="font-family:var(--fn-mn);font-size:9px;color:var(--grn2);min-width:55px">+$130k</div>
                    </div>
                  </div>
                  <div style="margin-bottom:14px">
                    <div style="font-size:11px;color:var(--tx);margin-bottom:6px;font-weight:600">CAPEX Overrun / Saving
                      (±15%)</div>
                    <div style="display:flex;gap:4px;align-items:center">
                      <div
                        style="font-family:var(--fn-mn);font-size:9px;color:var(--red2);min-width:55px;text-align:right">
                        -$51k</div>
                      <div style="flex:1;display:flex;gap:0;height:18px">
                        <div
                          style="width:30%;background:rgba(239,68,68,.35);border-radius:3px 0 0 3px;border:1px solid rgba(239,68,68,.5)">
                        </div>
                        <div
                          style="width:70%;background:rgba(34,197,94,.35);border-radius:0 3px 3px 0;border:1px solid rgba(34,197,94,.5)">
                        </div>
                      </div>
                      <div style="font-family:var(--fn-mn);font-size:9px;color:var(--grn2);min-width:55px">+$51k</div>
                    </div>
                  </div>
                  <div style="margin-bottom:14px">
                    <div style="font-size:11px;color:var(--tx);margin-bottom:6px;font-weight:600">OPEX Escalation (±20%)
                    </div>
                    <div style="display:flex;gap:4px;align-items:center">
                      <div
                        style="font-family:var(--fn-mn);font-size:9px;color:var(--red2);min-width:55px;text-align:right">
                        -$42k</div>
                      <div style="flex:1;display:flex;gap:0;height:18px">
                        <div
                          style="width:26%;background:rgba(239,68,68,.35);border-radius:3px 0 0 3px;border:1px solid rgba(239,68,68,.5)">
                        </div>
                        <div
                          style="width:74%;background:rgba(34,197,94,.35);border-radius:0 3px 3px 0;border:1px solid rgba(34,197,94,.5)">
                        </div>
                      </div>
                      <div style="font-family:var(--fn-mn);font-size:9px;color:var(--grn2);min-width:55px">+$42k</div>
                    </div>
                  </div>
                  <div style="margin-bottom:14px">
                    <div style="font-size:11px;color:var(--tx);margin-bottom:6px;font-weight:600">Solar Yield Variation
                      (±15%)</div>
                    <div style="display:flex;gap:4px;align-items:center">
                      <div
                        style="font-family:var(--fn-mn);font-size:9px;color:var(--red2);min-width:55px;text-align:right">
                        -$31k</div>
                      <div style="flex:1;display:flex;gap:0;height:18px">
                        <div
                          style="width:22%;background:rgba(239,68,68,.35);border-radius:3px 0 0 3px;border:1px solid rgba(239,68,68,.5)">
                        </div>
                        <div
                          style="width:78%;background:rgba(34,197,94,.35);border-radius:0 3px 3px 0;border:1px solid rgba(34,197,94,.5)">
                        </div>
                      </div>
                      <div style="font-family:var(--fn-mn);font-size:9px;color:var(--grn2);min-width:55px">+$31k</div>
                    </div>
                  </div>
                  <div style="margin-bottom:4px">
                    <div style="font-size:11px;color:var(--tx);margin-bottom:6px;font-weight:600">Discount Rate Change
                      (±3%)</div>
                    <div style="display:flex;gap:4px;align-items:center">
                      <div
                        style="font-family:var(--fn-mn);font-size:9px;color:var(--red2);min-width:55px;text-align:right">
                        -$78k</div>
                      <div style="flex:1;display:flex;gap:0;height:18px">
                        <div
                          style="width:40%;background:rgba(239,68,68,.35);border-radius:3px 0 0 3px;border:1px solid rgba(239,68,68,.5)">
                        </div>
                        <div
                          style="width:60%;background:rgba(34,197,94,.35);border-radius:0 3px 3px 0;border:1px solid rgba(34,197,94,.5)">
                        </div>
                      </div>
                      <div style="font-family:var(--fn-mn);font-size:9px;color:var(--grn2);min-width:55px">+$98k</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ══════════════════════════════════════════
     SECTION 7 — FUNDING & GRANT STRUCTURE
══════════════════════════════════════════ -->
          <div class="sec">
            <div class="sec-hdr">
              <span class="sec-num">§7</span>
              <span class="sec-title">FUNDING STRUCTURE &amp; GRANT APPLICATION — MININFRA</span>
              <span class="sec-badge bd-blu">GRANT REQUEST: $100,000</span>
            </div>
            <div class="g2">
              <div class="card">
                <div class="card-hdr">
                  <div class="card-hdr-dot" style="background:var(--blu)"></div>PROPOSED FUNDING STRUCTURE
                </div>
                <div class="fund-row">
                  <div class="fund-label">MININFRA Green Energy Grant</div>
                  <div class="fund-bar-outer">
                    <div class="fund-bar-inner"
                      style="width:29.2%;background:linear-gradient(90deg,var(--blu),var(--cyn));color:#fff">$100,000
                    </div>
                  </div>
                  <div class="fund-pct">29.2%</div>
                </div>
                <div class="fund-row">
                  <div class="fund-label">Promoter Equity (own capital)</div>
                  <div class="fund-bar-outer">
                    <div class="fund-bar-inner"
                      style="width:37.3%;background:linear-gradient(90deg,var(--grn),var(--grn2));color:#000">$127,800
                    </div>
                  </div>
                  <div class="fund-pct">37.3%</div>
                </div>
                <div class="fund-row">
                  <div class="fund-label">Development Finance (BRD / IFC)</div>
                  <div class="fund-bar-outer">
                    <div class="fund-bar-inner"
                      style="width:29.2%;background:linear-gradient(90deg,var(--pur),var(--pur2));color:#fff">$100,000
                    </div>
                  </div>
                  <div class="fund-pct">29.2%</div>
                </div>
                <div class="fund-row">
                  <div class="fund-label">Carbon Finance (Gold Standard VCM)</div>
                  <div class="fund-bar-outer">
                    <div class="fund-bar-inner"
                      style="width:4.4%;background:linear-gradient(90deg,var(--sol),var(--sol2));color:#000">$15,000
                    </div>
                  </div>
                  <div class="fund-pct">4.4%</div>
                </div>
                <table class="tbl" style="margin-top:16px">
                  <thead>
                    <tr>
                      <th>METRIC</th>
                      <th>WITHOUT GRANT</th>
                      <th>WITH $100k GRANT</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Effective CAPEX</td>
                      <td class="num c-tx2">$342,800</td>
                      <td class="num c-grn">$242,800</td>
                    </tr>
                    <tr>
                      <td>IRR</td>
                      <td class="num c-sol">23.1%</td>
                      <td class="num c-grn">31.7%</td>
                    </tr>
                    <tr>
                      <td>NPV @ 12%</td>
                      <td class="num c-sol">$487,300</td>
                      <td class="num c-grn">$587,300</td>
                    </tr>
                    <tr>
                      <td>Payback Period</td>
                      <td class="num c-sol">6.4 yrs</td>
                      <td class="num c-grn">4.2 yrs</td>
                    </tr>
                    <tr>
                      <td>Year-1 Equity Cash Yield</td>
                      <td class="num c-sol">14.6%</td>
                      <td class="num c-grn">20.7%</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card">
                <div class="card-hdr">
                  <div class="card-hdr-dot" style="background:var(--grn)"></div>GRANT JUSTIFICATION — MININFRA
                  E-MOBILITY CRITERIA
                </div>
                <table class="tbl">
                  <thead>
                    <tr>
                      <th>CRITERION</th>
                      <th>PROJECT RESPONSE</th>
                      <th>STATUS</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Clean energy generation &gt;50 kWp</td>
                      <td class="c-tx2">120.1 kWp solar PV</td>
                      <td class="c-grn">✓ MEETS</td>
                    </tr>
                    <tr>
                      <td>Battery storage ≥ 200 kWh</td>
                      <td class="c-tx2">820 kWh LFP</td>
                      <td class="c-grn">✓ EXCEEDS</td>
                    </tr>
                    <tr>
                      <td>EV chargers ≥ 3 units</td>
                      <td class="c-tx2">5 chargers (2+2+1 DC)</td>
                      <td class="c-grn">✓ EXCEEDS</td>
                    </tr>
                    <tr>
                      <td>IEC/CE certified components</td>
                      <td class="c-tx2">All IEC 62196, 62109, 61215</td>
                      <td class="c-grn">✓ CERTIFIED</td>
                    </tr>
                    <tr>
                      <td>RURA / REG grid compliance</td>
                      <td class="c-tx2">Grid tie-in + smart metering</td>
                      <td class="c-grn">✓ COMPLIANT</td>
                    </tr>
                    <tr>
                      <td>EWSA / Water authority permit</td>
                      <td class="c-tx2">No water discharge impact</td>
                      <td class="c-grn">✓ APPROVED</td>
                    </tr>
                    <tr>
                      <td>Local employment creation</td>
                      <td class="c-tx2">8 direct + 15 indirect jobs</td>
                      <td class="c-grn">✓ POSITIVE</td>
                    </tr>
                    <tr>
                      <td>CO₂ emissions reduction target</td>
                      <td class="c-tx2">~180 tCO₂/yr · 20yr life = 3,600t</td>
                      <td class="c-grn">✓ SIGNIFICANT</td>
                    </tr>
                    <tr>
                      <td>NST2 / Vision 2050 alignment</td>
                      <td class="c-tx2">EV mobility + green energy node</td>
                      <td class="c-grn">✓ ALIGNED</td>
                    </tr>
                  </tbody>
                </table>
                <div
                  style="margin-top:14px;padding:12px;background:rgba(59,130,246,.07);border:1px solid rgba(59,130,246,.25);border-radius:6px">
                  <div style="font-size:11px;font-weight:600;color:var(--blu2);margin-bottom:6px">ELIGIBLE GRANT
                    PROGRAMMES</div>
                  <div style="font-size:11px;color:var(--tx2);line-height:1.7">
                    • <strong style="color:var(--sol2)">MININFRA Green Energy Facility</strong> — Tier A capital grant
                    (up to $150k)<br>
                    • <strong style="color:var(--sol2)">GCF/FONERWA Rwanda Climate Fund</strong> — Clean mobility
                    co-financing<br>
                    • <strong style="color:var(--sol2)">AfDB CDSF Sustainable Energy Fund</strong> — EAC regional clean
                    energy<br>
                    • <strong style="color:var(--sol2)">World Bank RURA Grid Modernisation</strong> — Smart grid
                    integration support<br>
                    • <strong style="color:var(--sol2)">BRD Green Finance Product</strong> — Concessional debt @ 9% p.a.
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ══════════════════════════════════════════
     SECTION 8 — RISK ANALYSIS
══════════════════════════════════════════ -->
          <div class="sec">
            <div class="sec-hdr">
              <span class="sec-num">§8</span>
              <span class="sec-title">FINANCIAL RISK ANALYSIS &amp; MITIGATION</span>
              <span class="sec-badge bd-red">6 KEY RISKS IDENTIFIED</span>
            </div>
            <div class="risk-grid">
              <div class="risk-item rl-low">
                <div class="risk-level">■ LOW RISK</div>
                <div class="risk-title">Solar Resource Variability</div>
                <div class="risk-mit">Kigali's GHI is 1,752 kWh/m²/yr — one of the most stable solar resources in
                  Sub-Saharan Africa (Coefficient of Variation &lt;8%). NASA POWER P90 yield used in financial model.
                  Oversized PV array (+22% vs load) provides buffer. Impact on NPV: ±$31k.</div>
              </div>
              <div class="risk-item rl-low">
                <div class="risk-level">■ LOW RISK</div>
                <div class="risk-title">Equipment Degradation</div>
                <div class="risk-mit">Jinko 30yr linear power warranty (0.5%/yr). LFP batteries rated 6,000+ cycles
                  (Gotion/CATL). Replacement reserves built into cash flow model. All equipment IEC/UL certified.
                  Modular replacement architecture reduces single-point failure cost.</div>
              </div>
              <div class="risk-item rl-med">
                <div class="risk-level">▲ MEDIUM RISK</div>
                <div class="risk-title">EV Adoption Rate / Demand</div>
                <div class="risk-mit">Conservative case uses 40% utilisation (vs 70% base). Even at 40%, project remains
                  NPV-positive ($188k). Rwanda EV imports growing 45%/yr (RURA 2024). Kigali parking location ensures
                  captive demand. Mitigation: fleet subscription contracts lock in 20% baseline revenue.</div>
              </div>
              <div class="risk-item rl-med">
                <div class="risk-level">▲ MEDIUM RISK</div>
                <div class="risk-title">Foreign Exchange / Import Costs</div>
                <div class="risk-mit">Equipment purchased in USD; revenues in RWF. RWF depreciated ~6%/yr vs USD (5yr
                  avg). Tariff indexed to USD CPI from Year 3 in operator agreement. BRD financing in RWF partially
                  natural hedge. USD revenue streams (carbon credits, fleet contracts) provide partial cover.</div>
              </div>
              <div class="risk-item rl-med">
                <div class="risk-level">▲ MEDIUM RISK</div>
                <div class="risk-title">Regulatory / Tariff Change</div>
                <div class="risk-mit">RURA tariff revised every 3–4 months from 2025 (stated policy). Grid export
                  buyback rate risk mitigated by solar-first operation (only 10% revenue). Full IEC/CE certification
                  ensures no compliance barrier. REG grid licence secured for 15yr term. Project aligns with NST2 Vision
                  2050.</div>
              </div>
              <div class="risk-item rl-high">
                <div class="risk-level">▲ HIGH RISK (mitigated)</div>
                <div class="risk-title">CAPEX Overrun / Supply Chain</div>
                <div class="risk-mit">5% contingency ($16,348) included in CAPEX. Fixed-price EPC contract with
                  performance bond. CIF Kigali pricing locked 90 days. Battery prices have fallen 18%/yr — risk is to
                  the downside. Freight insurance included. CAPEX +15% scenario still delivers IRR 19.2% → project
                  remains fundable.</div>
              </div>
            </div>
          </div>

          <!-- ══════════════════════════════════════════
     SECTION 9 — IMPLEMENTATION TIMELINE
══════════════════════════════════════════ -->
          <div class="sec">
            <div class="sec-hdr">
              <span class="sec-num">§9</span>
              <span class="sec-title">IMPLEMENTATION TIMELINE &amp; FINANCIAL MILESTONES</span>
              <span class="sec-badge bd-grn">18-MONTH DELIVERY</span>
            </div>
            <div class="card">
              <div class="timeline">
                <div class="tl-row">
                  <div class="tl-yr">08/2026</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(59,130,246,.15);color:var(--blu2);border:1px solid rgba(59,130,246,.3)">GRANT
                      DECISION</span>
                    <span class="tl-chip"
                      style="background:rgba(245,158,11,.12);color:var(--sol2);border:1px solid rgba(245,158,11,.3)">EPC
                      CONTRACT</span>
                    <span class="tl-val c-blu">Month 0</span>
                    <span class="tl-desc">MININFRA grant award. EPC tender awarded. BRD loan disbursement. Engineering
                      design finalised. RURA / REG licence submitted.</span>
                  </div>
                </div>
                <div class="tl-row">
                  <div class="tl-yr">09/2026</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(168,85,247,.15);color:var(--pur2);border:1px solid rgba(168,85,247,.3)">PROCUREMENT</span>
                    <span class="tl-chip"
                      style="background:rgba(249,115,22,.15);color:var(--org2);border:1px solid rgba(249,115,22,.3)">CIVIL
                      WORKS</span>
                    <span class="tl-val c-pur">Months 1–3</span>
                    <span class="tl-desc">Equipment ordered CIF Kigali. Battery room + EV bay canopy construction.
                      Earthing and civil drainage complete. CAPEX drawdown: $120,000.</span>
                  </div>
                </div>
                <div class="tl-row">
                  <div class="tl-yr">01/2027</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(6,182,212,.15);color:var(--cyn2);border:1px solid rgba(6,182,212,.3)">INSTALLATION</span>
                    <span class="tl-val c-cyn">Months 4–7</span>
                    <span class="tl-desc">PV array mounting + stringing. Inverter and BESS rack installation.
                      Distribution board, MCCB, MCB5 wiring. CAPEX drawdown: $150,000.</span>
                  </div>
                </div>
                <div class="tl-row">
                  <div class="tl-yr">02/2027</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(34,197,94,.15);color:var(--grn2);border:1px solid rgba(34,197,94,.3)">EV
                      CHARGERS</span>
                    <span class="tl-chip"
                      style="background:rgba(245,158,11,.12);color:var(--sol2);border:1px solid rgba(245,158,11,.3)">IoT
                      / SCADA</span>
                    <span class="tl-val c-grn">Months 8–10</span>
                    <span class="tl-desc">All 5 EV charger units installed + OCPP configured. IoT gateway + MQTT broker
                      live. Dashboard monitoring operational. CAPEX drawdown: $72,800.</span>
                  </div>
                </div>
                <div class="tl-row">
                  <div class="tl-yr">03/2027</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(245,158,11,.15);color:var(--sol2);border:1px solid rgba(245,158,11,.3)">COMMISSIONING</span>
                    <span class="tl-val c-sol">Months 11–13</span>
                    <span class="tl-desc">Full system energisation. RURA inspection + grid connection approved. IEC/CE
                      certification confirmed. Staff training (2 operators). Soft launch with pilot fleet
                      customers.</span>
                  </div>
                </div>
                <div class="tl-row">
                  <div class="tl-yr highlight">04/2027</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(34,197,94,.2);color:var(--grn);border:1px solid rgba(34,197,94,.5)">★
                      COMMERCIAL OPERATIONS</span>
                    <span class="tl-val c-grn">Month 14+</span>
                    <span class="tl-desc">Full commercial operations begin. Revenue Month 1: est. $6,200. Year-1 full
                      revenue target: $72,682 net. Grant reporting to MININFRA quarterly.</span>
                  </div>
                </div>
                <div class="tl-row">
                  <div class="tl-yr highlight">2033/34</div>
                  <div class="tl-body">
                    <span class="tl-chip"
                      style="background:rgba(168,85,247,.2);color:var(--pur);border:1px solid rgba(168,85,247,.5)">★
                      FULL PAYBACK</span>
                    <span class="tl-val c-pur">Year 6.4</span>
                    <span class="tl-desc">Complete CAPEX recovery achieved. All subsequent cash flows are pure returns.
                      Cumulative NPV turns firmly positive. With grant: payback achieved Year 4.2 (2031/32).</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ══════════════════════════════════════════
     SECTION 10 — SOCIAL / ENVIRONMENTAL
══════════════════════════════════════════ -->
          <div class="sec">
            <div class="sec-hdr">
              <span class="sec-num">§10</span>
              <span class="sec-title">SOCIAL &amp; ENVIRONMENTAL CO-BENEFITS — NON-FINANCIAL VALUE</span>
              <span class="sec-badge bd-grn">~180 tCO₂/yr AVOIDED</span>
            </div>
            <div class="g4">
              <div class="mbox">
                <div class="mbox-val c-grn">180 t</div>
                <div class="mbox-lbl">CO₂ / year avoided</div>
                <div class="mbox-sub">vs. grid + ICE baseline. 3,600 tCO₂ over 20 years. Equivalent to planting 165,000
                  trees.</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-sol">30</div>
                <div class="mbox-lbl">Jobs created</div>
                <div class="mbox-sub">8 direct operations staff + 22 construction / installation local jobs in Kigali.
                </div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-blu">~40</div>
                <div class="mbox-lbl">EVs served daily</div>
                <div class="mbox-sub">At 70% utilisation. Supporting Kigali's EV fleet growth per RURA 2030 projections.
                </div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-pur">78%</div>
                <div class="mbox-lbl">User cost saving</div>
                <div class="mbox-sub">vs. petrol-equivalent cost for the same km traveled. $0.062/km vs $0.105/km ICE.
                </div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-cyn">62%</div>
                <div class="mbox-lbl">Grid independent</div>
                <div class="mbox-sub">Operating hours powered by solar + BESS. Reduces pressure on Kigali city grid
                  during peak hours.</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-org">$2,160</div>
                <div class="mbox-lbl">Carbon revenue/yr</div>
                <div class="mbox-sub">Gold Standard VCM credits at $12/tCO₂. Revenue stream grows as carbon markets
                  deepen in EAC.</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-sol">175 MWh</div>
                <div class="mbox-lbl">Clean energy/yr (Yr1)</div>
                <div class="mbox-sub">Generated by 120.1 kWp array. NASA-validated yield for Kigali (−2.48°S, 29.48°E ·
                  PSH 4.78h&GHI 1765KWM/Yr).</div>
              </div>
              <div class="mbox">
                <div class="mbox-val c-grn">NST2 ✓</div>
                <div class="mbox-lbl">Policy alignment</div>
                <div class="mbox-sub">Directly supports Rwanda NST2, Vision 2050, and RURA EV Infrastructure Masterplan
                  2024–2030.</div>
              </div>
            </div>
          </div>

          <div class="divider"></div>

          <!-- FINAL SUMMARY -->
          <div class="sec">
            <div class="sec-hdr">
              <span class="sec-num">§11</span>
              <span class="sec-title">INVESTMENT SUMMARY &amp; RECOMMENDATION</span>
            </div>
            <div class="hbox"
              style="background:linear-gradient(135deg,rgba(34,197,94,.1),rgba(59,130,246,.06));border-color:rgba(34,197,94,.35)">
              <div class="hbox-title" style="color:var(--grn2)">CONCLUSION — STRONG BUY RECOMMENDATION</div>
              <div class="hbox-body">
                The Solar EV Charging Station presents a <strong style="color:var(--sol2)">financially robust,
                  environmentally impactful, and strategically aligned</strong> investment for Rwanda's e-mobility
                transition. With an IRR of <strong style="color:var(--grn2)">23.1%</strong> — 11.2 percentage points
                above the 12% hurdle rate — and a 20-year NPV of <strong style="color:var(--grn2)">$487,300</strong>,
                the project is bankable on commercial terms alone. A MININFRA grant of $100,000 transforms it into an
                <strong style="color:var(--cyn2)">exceptional 31.7% IRR, 4.2-year payback</strong> proposition. The LCOE
                of $0.048/kWh is 69% below Rwanda's commercial grid tariff, ensuring competitive and sustainable pricing
                for EV users. The project directly delivers on NST2, Vision 2050, and RURA's EV Infrastructure
                Masterplan. <strong style="color:var(--sol2)">MININFRA investment is strongly recommended.</strong>
              </div>
            </div>
            <div class="footnote">
              <span class="fn-mark">†</span> All financial projections prepared by Eng. Hermes MUGISHA (Energy Engineer)
              based on: RURA electricity tariffs effective 1 October 2025 (Rwf 214/kWh = $0.155 at 1,380 RWF/USD); NASA
              POWER GHI data for Kigali (−2.48°S, 29.48°E); IEA LCOE methodology (2024 edition); EAC EV charging tariff
              benchmarks (EV24.africa, VUKA Group, April 2025); component pricing from verified supplier quotations (CIF
              Kigali, Q1 2026); BRD development finance rates. All figures in USD unless stated. Projections are
              estimates subject to market conditions. Prepared for submission to MININFRA under Rwanda E-Mobility Grant
              Programme 2026. Date: June 2026. CONFIDENTIAL.
            </div>
          </div>

        </div><!-- /page -->

        <div class="scroll-top" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</div>

        <script>
          // ══════════════════════════════════════════
          //  DCF TABLE (20 years)
          // ══════════════════════════════════════════
          const CAPEX = 342800;
          const DISC = 0.12;
          const OPEX_1 = 24744;
          const OPEX_ESCALATION = 0.025;
          const REV_1 = 72682;
          // Revenue growth: 25% yr1-3, 12% yr4-6, 7% yr7-10, 4% yr11-20
          const revGrowth = (yr) => yr <= 3 ? 0.25 : yr <= 6 ? 0.12 : yr <= 10 ? 0.07 : 0.04;
          // Major replacements by year
          const replacements = { 7: 4200, 8: 3500, 12: 23400, 15: 18800 };

          let rows = '', cumNPV = -CAPEX, rev = REV_1, opex = OPEX_1;
          const cumData = [-CAPEX];
          let cumulativeCF = -CAPEX;

          for (let y = 1; y <= 20; y++) {
            if (y > 1) { rev *= (1 + revGrowth(y - 1)); opex *= (1 + OPEX_ESCALATION); }
            const rep = replacements[y] || 0;
            const netCF = rev - opex - rep;
            const df = Math.pow(1 + DISC, y);
            const dcf = netCF / df;
            cumNPV += dcf;
            cumulativeCF += netCF;
            cumData.push(cumulativeCF);
            const pbRow = (y >= 6 && y <= 8) ? 'style="background:rgba(34,197,94,.06)"' : '';
            rows += `<tr ${pbRow}>
    <td class="num" style="color:var(--tx3);font-family:var(--fn-mn)">${y}</td>
    <td class="num c-grn">$${Math.round(rev / 1000)}k</td>
    <td class="num c-red">$${Math.round((opex + rep) / 1000)}k${rep ? '<span style="font-size:8px;color:var(--org2)"> +R</span>' : ''}</td>
    <td class="num ${netCF >= 0 ? 'c-sol' : 'c-red'}">$${Math.round(netCF / 1000)}k</td>
    <td class="num ${dcf >= 0 ? 'c-cyn' : 'c-red'}">$${Math.round(dcf / 1000)}k</td>
    <td class="num ${cumNPV >= 0 ? 'c-grn' : 'c-red'}">${cumNPV >= 0 ? '+' : ''}$${Math.round(cumNPV / 1000)}k</td>
  </tr>`;
          }
          document.getElementById('dcfBody').innerHTML = rows;

          // ══════════════════════════════════════════
          //  CASH FLOW CANVAS CHART
          // ══════════════════════════════════════════
          const canvas = document.getElementById('cfCanvas');
          const ctx = canvas.getContext('2d');

          function drawChart() {
            const W = canvas.offsetWidth * (window.devicePixelRatio || 1);
            const H = canvas.offsetHeight * (window.devicePixelRatio || 1);
            canvas.width = W; canvas.height = H;
            const dpr = window.devicePixelRatio || 1;
            ctx.scale(dpr, dpr);
            const w = canvas.offsetWidth, h = canvas.offsetHeight;

            // Background
            ctx.fillStyle = 'transparent';
            ctx.clearRect(0, 0, w, h);

            const pad = { t: 28, b: 40, l: 14, r: 14 };
            const cw = w - pad.l - pad.r;
            const ch = h - pad.t - pad.b;

            // Data: year 0 = -CAPEX, then annual net CFs
            const rev2 = [REV_1];
            const opex2 = [OPEX_1];
            let rv = REV_1, op = OPEX_1;
            for (let y = 2; y <= 20; y++) {
              rv *= (1 + revGrowth(y - 1)); op *= (1 + OPEX_ESCALATION);
              rev2.push(rv); opex2.push(op);
            }
            const annualCFs = rev2.map((r, i) => r - opex2[i] - (replacements[i + 1] || 0));
            const allVals = [-CAPEX, ...annualCFs];
            const cumCFs = []; let cc = -CAPEX;
            allVals.forEach(v => { cc += v; cumCFs.push(cc); });
            // Merge — we show annual bars + cumulative line
            const nBars = annualCFs.length; // 20 bars
            const minV = Math.min(...annualCFs, -CAPEX);
            const maxV = Math.max(...annualCFs, ...cumCFs);
            const range = maxV - minV;
            const toY = v => pad.t + ch - ((v - minV) / range) * ch;
            const zeroY = toY(0);
            const barW = cw / nBars - 2;

            // Zero line
            ctx.strokeStyle = 'rgba(148,163,184,.18)';
            ctx.lineWidth = 1;
            ctx.setLineDash([4, 4]);
            ctx.beginPath(); ctx.moveTo(pad.l, zeroY); ctx.lineTo(pad.l + cw, zeroY); ctx.stroke();
            ctx.setLineDash([]);

            // Bars
            annualCFs.forEach((v, i) => {
              const x = pad.l + i * (barW + 2);
              const isPos = v >= 0;
              const barH = Math.abs(toY(v) - zeroY);
              const barY = isPos ? toY(v) : zeroY;
              const grad = ctx.createLinearGradient(0, barY, 0, barY + barH);
              if (isPos) { grad.addColorStop(0, 'rgba(74,222,128,.9)'); grad.addColorStop(1, 'rgba(34,197,94,.4)'); }
              else { grad.addColorStop(0, 'rgba(239,68,68,.4)'); grad.addColorStop(1, 'rgba(239,68,68,.85)'); }
              ctx.fillStyle = grad;
              ctx.beginPath();
              ctx.roundRect ? ctx.roundRect(x, barY, barW, Math.max(barH, 2), isPos ? [3, 3, 0, 0] : [0, 0, 3, 3])
                : ctx.rect(x, barY, barW, Math.max(barH, 2));
              ctx.fill();
              // Year label
              if (i % 2 === 0) {
                ctx.fillStyle = 'rgba(71,85,105,.8)';
                ctx.font = `${8 * (1 / window.devicePixelRatio || 1)}px "Share Tech Mono"`;
                ctx.textAlign = 'center';
                ctx.fillText(`Y${i + 1}`, x + barW / 2, h - pad.b + 14);
              }
            });

            // Cumulative line
            ctx.strokeStyle = 'rgba(251,191,36,.85)';
            ctx.lineWidth = 2.2;
            ctx.lineJoin = 'round';
            ctx.beginPath();
            cumCFs.forEach((v, i) => {
              const x = pad.l + i * (barW + 2) + barW / 2;
              const y2 = toY(v);
              i === 0 ? ctx.moveTo(x, y2) : ctx.lineTo(x, y2);
            });
            ctx.stroke();

            // Payback annotation
            const pbYear = 6;
            const pbX = pad.l + (pbYear - 1) * (barW + 2) + barW / 2;
            ctx.strokeStyle = 'rgba(34,197,94,.6)';
            ctx.lineWidth = 1.5;
            ctx.setLineDash([3, 3]);
            ctx.beginPath(); ctx.moveTo(pbX, pad.t); ctx.lineTo(pbX, h - pad.b); ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = 'rgba(34,197,94,.9)';
            ctx.font = `bold 9px "Share Tech Mono"`;
            ctx.textAlign = 'center';
            ctx.fillText('PBP Y6.4', pbX, pad.t + 10);

            // Y-axis label
            ctx.fillStyle = 'rgba(148,163,184,.5)';
            ctx.font = `8px "Share Tech Mono"`;
            ctx.textAlign = 'left';
            ctx.fillText(`${Math.round(maxV / 1000)}k`, pad.l, pad.t + 8);
            ctx.fillText(`0`, pad.l, zeroY - 4);
            ctx.fillText(`-${Math.round(Math.abs(minV) / 1000)}k`, pad.l, h - pad.b - 4);
          }

          drawChart();
          window.addEventListener('resize', drawChart);
        </script>
</body>

</html>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>Solar EV Station · Rwanda E-Mobility 2026 · Eng. Hermes MUGISHA</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link
    href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Share+Tech+Mono&family=Exo+2:wght@200;300;400;600;800&display=swap"
    rel="stylesheet">
  <style>
    /* ═══════════════════════════════════════════════════════════
   SOLAR EV PRO DASHBOARD  ·  Rwanda E-Mobility 2026
   Engineer: Hermes MUGISHA  ·  Energy Engineer
   HOW TO RUN: Open in VS Code → Right-click → Open with Live Server
               OR: double-click the .html file in your browser
═══════════════════════════════════════════════════════════ */
    :root {
      --bg: #020810;
      --bg2: #050e1c;
      --bg3: #081428;
      --panel: #070f1f;
      --b1: #0e2040;
      --b2: #1a3560;
      --b3: #2a4a70;
      --sol: #f59e0b;
      --sol2: #fbbf24;
      --sol3: #fde68a;
      --grn: #22c55e;
      --grn2: #4ade80;
      --grn3: #86efac;
      --blu: #3b82f6;
      --blu2: #60a5fa;
      --pur: #a855f7;
      --pur2: #c084fc;
      --cyn: #06b6d4;
      --cyn2: #22d3ee;
      --org: #f97316;
      --org2: #fb923c;
      --red: #ef4444;
      --red2: #f87171;
      --yel: #eab308;
      --tx: #e2e8f0;
      --tx2: #94a3b8;
      --tx3: #475569;
      --brd: rgba(30, 58, 95, .6);
      --fn-hd: 'Orbitron', sans-serif;
      --fn-mn: 'Share Tech Mono', monospace;
      --fn-ui: 'Exo 2', sans-serif;
    }

    *,
    *::before,
    *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0
    }

    html {
      font-size: 12.5px;
      background: var(--bg)
    }

    body {
      font-family: var(--fn-ui);
      color: var(--tx);
      min-height: 100vh;
      background: var(--bg);
      overflow: hidden
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image: linear-gradient(rgba(30, 64, 175, .06)1px, transparent 1px),
        linear-gradient(90deg, rgba(30, 64, 175, .06)1px, transparent 1px);
      background-size: 44px 44px;
      pointer-events: none;
      z-index: 0
    }

    body::after {
      content: '';
      position: fixed;
      inset: 0;
      background: radial-gradient(ellipse 70% 45% at 50% 0%, rgba(245, 158, 11, .04) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0
    }

    #root {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden
    }

    /* ── HEADER ─────────────────────────────────────────────── */
    #hdr {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 58px;
      padding: 0 16px;
      flex-shrink: 0;
      background: linear-gradient(180deg, rgba(7, 15, 31, .98), rgba(5, 10, 22, .95));
      border-bottom: 1px solid var(--b2);
      box-shadow: 0 4px 30px rgba(0, 0, 0, .7)
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 11px
    }

    .brand-sun {
      width: 42px;
      height: 42px;
      position: relative;
      flex-shrink: 0
    }

    .brand-sun svg {
      filter: drop-shadow(0 0 10px rgba(245, 158, 11, .6))
    }

    .spin-d {
      animation: spinD 8s linear infinite;
      transform-origin: 21px 21px
    }

    @keyframes spinD {
      to {
        stroke-dashoffset: -60
      }
    }

    .b-title {
      font-family: var(--fn-hd);
      font-size: 17px;
      font-weight: 900;
      letter-spacing: 2.5px;
      color: var(--tx);
      line-height: 1
    }

    .b-title .ac {
      color: var(--sol)
    }

    .b-sub {
      font-size: 8.5px;
      color: var(--tx3);
      letter-spacing: 1.5px;
      font-family: var(--fn-mn);
      margin-top: 2px
    }

    .hdr-mid {
      text-align: center;
      min-width: 240px
    }

    .live-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: rgba(34, 197, 94, .1);
      border: 1px solid rgba(34, 197, 94, .3);
      padding: 2px 11px;
      border-radius: 99px;
      font-size: 8.5px;
      font-weight: 700;
      letter-spacing: 2px;
      color: var(--grn);
      font-family: var(--fn-mn)
    }

    .live-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--grn);
      box-shadow: 0 0 7px var(--grn);
      animation: blink 1.2s ease-in-out infinite
    }

    @keyframes blink {

      0%,
      100% {
        opacity: 1
      }

      50% {
        opacity: .2
      }
    }

    #clock {
      font-family: var(--fn-hd);
      font-size: 24px;
      color: var(--sol);
      letter-spacing: 3px;
      text-shadow: 0 0 18px rgba(245, 158, 11, .5);
      margin-top: 2px;
      line-height: 1
    }

    #dateTxt {
      font-size: 8px;
      color: var(--tx3);
      letter-spacing: 2px;
      font-family: var(--fn-mn)
    }

    #modeBadge {
      display: inline-block;
      margin-top: 2px;
      padding: 2px 9px;
      border-radius: 3px;
      font-size: 8.5px;
      font-weight: 700;
      letter-spacing: 1.5px;
      font-family: var(--fn-mn);
      transition: all .5s;
      background: rgba(34, 197, 94, .15);
      border: 1px solid rgba(34, 197, 94, .4);
      color: var(--grn)
    }

    .hdr-right {
      display: flex;
      gap: 16px
    }

    .hstat {
      text-align: center
    }

    .hsl {
      display: block;
      font-size: 7.5px;
      color: var(--tx3);
      letter-spacing: 1.5px;
      font-family: var(--fn-mn)
    }

    .hsv {
      display: block;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
      font-family: var(--fn-mn);
      margin-top: 2px
    }

    .on {
      color: var(--grn);
      text-shadow: 0 0 7px rgba(34, 197, 94, .5)
    }

    .off {
      color: var(--red)
    }

    /* ── MAIN DASHBOARD GRID ─────────────────────────────────── */
    #dash {
      display: grid;
      grid-template-columns: 1.15fr 1.05fr 1.05fr 0.95fr;
      gap: 7px;
      padding: 7px;
      flex: 1;
      overflow: hidden;
      min-height: 0
    }

    .col {
      display: flex;
      flex-direction: column;
      gap: 7px;
      overflow-y: auto;
      min-height: 0;
      scrollbar-width: thin;
      scrollbar-color: var(--b2) transparent
    }

    .col::-webkit-scrollbar {
      width: 3px
    }

    .col::-webkit-scrollbar-thumb {
      background: var(--b2);
      border-radius: 2px
    }

    /* ── CARDS ────────────────────────────────────────────────── */
    .card {
      background: var(--panel);
      border: 1px solid var(--brd);
      border-radius: 9px;
      padding: 11px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0
    }

    .card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--sol), transparent);
      opacity: .3
    }

    .ch {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 9px;
      font-size: 9px;
      font-weight: 600;
      letter-spacing: 1.8px;
      color: var(--tx2);
      font-family: var(--fn-mn)
    }

    .chi {
      font-size: 13px;
      color: var(--sol)
    }

    .cbadge {
      margin-left: auto;
      font-size: 7.5px;
      padding: 1px 7px;
      border-radius: 3px;
      background: rgba(245, 158, 11, .1);
      border: 1px solid rgba(245, 158, 11, .3);
      color: var(--sol);
      letter-spacing: 1px
    }

    .cbadge.grn {
      background: rgba(34, 197, 94, .1);
      border-color: rgba(34, 197, 94, .3);
      color: var(--grn)
    }

    .cbadge.pur {
      background: rgba(168, 85, 247, .1);
      border-color: rgba(168, 85, 247, .3);
      color: var(--pur2)
    }

    .cbadge.cyn {
      background: rgba(6, 182, 212, .1);
      border-color: rgba(6, 182, 212, .3);
      color: var(--cyn2)
    }

    .cbadge.yel {
      background: rgba(234, 179, 8, .1);
      border-color: rgba(234, 179, 8, .3);
      color: var(--yel)
    }

    .cbadge.blu {
      background: rgba(59, 130, 246, .1);
      border-color: rgba(59, 130, 246, .3);
      color: var(--blu2)
    }

    /* ═══════════════════════════════════════════════════════════
   COLUMN 1 — SUN + PV ARRAY
═══════════════════════════════════════════════════════════ */
    /* Sun card */
    .sun-body {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 9px
    }

    .sun-orb {
      position: relative;
      width: 96px;
      height: 96px;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center
    }

    .sr {
      position: absolute;
      border-radius: 50%;
      border: 1.5px solid;
      animation: rotr 6s linear infinite
    }

    .sr1 {
      width: 88px;
      height: 88px;
      border-color: rgba(245, 158, 11, .2);
      border-style: dashed;
      animation-duration: 9s
    }

    .sr2 {
      width: 72px;
      height: 72px;
      border-color: rgba(245, 158, 11, .12);
      animation-direction: reverse;
      animation-duration: 13s
    }

    .sc {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #fde68a, #f59e0b 55%, #d97706);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 22px rgba(245, 158, 11, .7), 0 0 45px rgba(245, 158, 11, .18);
      z-index: 2
    }

    @keyframes rotr {
      to {
        transform: rotate(360deg)
      }
    }

    .sc-irr {
      font-family: var(--fn-hd);
      font-size: 13px;
      font-weight: 700;
      color: #1a0800;
      line-height: 1
    }

    .sc-u {
      font-size: 6.5px;
      color: #5a3000;
      letter-spacing: .8px
    }

    .sun-stats {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4px;
      flex: 1
    }

    .ss {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 4px;
      padding: 4px 6px
    }

    .ss span:first-child {
      display: block;
      font-size: 7.5px;
      color: var(--tx3);
      letter-spacing: .8px;
      font-family: var(--fn-mn)
    }

    .ss span:last-child {
      display: block;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--sol);
      font-family: var(--fn-mn);
      margin-top: 1px
    }

    /* Operational schedule */
    .sched {
      margin-top: 2px
    }

    .sched-ttl {
      font-size: 7.5px;
      color: var(--tx3);
      letter-spacing: 1.5px;
      font-family: var(--fn-mn);
      margin-bottom: 4px
    }

    .sched-bar {
      display: flex;
      height: 26px;
      border-radius: 4px;
      overflow: visible;
      position: relative;
      gap: 1px
    }

    .seg {
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 8.5px;
      font-weight: 700;
      font-family: var(--fn-mn);
      border-radius: 3px
    }

    .seg-b1 {
      width: 16.67%;
      background: rgba(59, 130, 246, .22);
      border: 1px solid rgba(59, 130, 246, .45);
      color: var(--blu2)
    }

    .seg-pv {
      width: 58.33%;
      background: rgba(34, 197, 94, .18);
      border: 1px solid rgba(34, 197, 94, .35);
      color: var(--grn);
    }

    .seg-b2 {
      width: 12.5%;
      background: rgba(37, 99, 235, .22);
      border: 1px solid rgba(37, 99, 235, .45);
      color: var(--blu2);
    }

    .needle {
      position: absolute;
      top: -5px;
      bottom: -5px;
      width: 2.5px;
      background: white;
      border-radius: 1px;
      z-index: 5;
      box-shadow: 0 0 10px rgba(255, 255, 255, .8);
      transition: lseft .3s ease;
    }

    .needle-label {
      position: absolute;
      top: -18px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 7px;
      color: #ffffff;
      white-space: nowrap;
      letter-spacing: .8px;
      font-family: var(--fn-mn);
      z-index: 6;
    }

    .sched-tks {
      position: relative;
      height: 16px;
      font-size: 7px;
      color: var(--yel);
      font-family: var(--fn-mn);
      margin-top: 3px;
    }

    .sched-tks span {
      position: absolute;
      top: 0;
      white-space: nowrap;
      transform: translateX(-50%);
    }

    .sched-tks span:first-child {
      left: 0%;
      transform: translateX(0);
    }

    .sched-tks span:nth-child(2) {
      left: 8.33%;
    }

    .sched-tks span:nth-child(3) {
      left: 37.5%;
    }

    .sched-tks span:nth-child(4) {
      left: 50%;
    }

    .sched-tks span:nth-child(5) {
      left: 62.5%;
    }

    .sched-tks span:nth-child(6) {
      left: 83.33%;
    }

    .sched-tks span:nth-child(7) {
      left: 100%;
      transform: translateX(-100%);
    }

    #schedStatus {
      font-size: 8px;
      color: var(--grn);
      font-family: var(--fn-mn);
      font-weight: 700;
      margin-top: 4px;
      transition: color .5s;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis
    }

    /* PV array */
    #pvGrid {
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      gap: 2px;
      margin-bottom: 7px
    }

    .pvm {
      aspect-ratio: 3/4;
      background: #1a237e;
      border: 1px solid #3949ab;
      border-radius: 2px;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      transition: border-color .3s, box-shadow .3s
    }

    .pvm.act {
      border-color: var(--sol);
      box-shadow: 0 0 5px rgba(245, 158, 11, .4)
    }

    .pvm.act::before {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(245, 158, 11, .09);
      animation: pvp 2.5s ease-in-out infinite
    }

    @keyframes pvp {

      0%,
      100% {
        opacity: .3
      }

      50% {
        opacity: 1
      }
    }

    .pvm::after {
      content: '';
      position: absolute;
      inset: 0;
      background: repeating-linear-gradient(45deg, transparent, transparent 3px,
          rgba(92, 107, 192, .1)3px, rgba(92, 107, 192, .1)4px)
    }

    .str-lbl {
      font-size: 6.5px;
      color: var(--org);
      font-weight: 700;
      font-family: var(--fn-mn);
      text-align: left;
      margin-bottom: 1px;
      padding-left: 1px
    }

    /* String diagram */
    #strDiag {
      margin-bottom: 7px
    }

    .str-row {
      display: flex;
      align-items: center;
      gap: 3px;
      margin-bottom: 2.5px;
      height: 14px
    }

    .srid {
      font-size: 6.5px;
      color: var(--org);
      font-family: var(--fn-mn);
      width: 16px;
      flex-shrink: 0
    }

    .srwire {
      height: 2.5px;
      flex: 1;
      border-radius: 1px;
      position: relative;
      transition: background .5s, opacity .5s
    }

    .srwire::after {
      content: '▶';
      position: absolute;
      right: -1px;
      top: -4px;
      font-size: 7px;
      color: inherit;
      opacity: .8
    }

    .srfuse {
      width: 11px;
      height: 12px;
      background: #1b5e20;
      border: 1px solid #4caf50;
      border-radius: 1px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0
    }

    .srfuse-dot {
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #00e676
    }

    .srval {
      font-size: 6.5px;
      color: var(--tx3);
      font-family: var(--fn-mn);
      width: 58px;
      text-align: right;
      flex-shrink: 0
    }

    .pv-stats {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 5px
    }

    .pvs {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 4px;
      padding: 5px 4px;
      text-align: center
    }

    .pvs-v {
      font-family: var(--fn-mn);
      font-size: 12px;
      font-weight: 600;
      color: var(--tx)
    }

    .pvs-v.hi {
      color: var(--sol);
      text-shadow: 0 0 8px rgba(245, 158, 11, .35)
    }

    .pvs-l {
      font-size: 7px;
      color: var(--tx3);
      letter-spacing: .8px;
      margin-top: 1px;
      font-family: var(--fn-mn)
    }

    /* ═══════════════════════════════════════════════════════════
   COLUMN 2 — BMS + INVERTER/MPPT
═══════════════════════════════════════════════════════════ */
    /* BMS */
    .bms-body {
      display: grid;
      grid-template-columns: 60px 1fr 1fr;
      gap: 9px;
      margin-bottom: 8px
    }

    .batt-tower {
      display: flex;
      flex-direction: column;
      align-items: center
    }

    .batt-cap {
      width: 22px;
      height: 6px;
      background: var(--grn);
      border-radius: 2px 2px 0 0;
      margin-bottom: -1px
    }

    .batt-shell {
      width: 46px;
      height: 100px;
      background: var(--bg);
      border: 2px solid var(--grn);
      border-radius: 3px;
      position: relative;
      overflow: hidden
    }

    .batt-fill {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(to top, #15803d, #22c55e 55%, #4ade80);
      transition: height 1.5s ease;
      border-radius: 0 0 1px 1px
    }

    .batt-pct {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--fn-hd);
      font-size: 13px;
      font-weight: 700;
      color: white;
      text-shadow: 0 1px 4px rgba(0, 0, 0, .9);
      z-index: 2
    }

    .batt-segs {
      position: absolute;
      inset: 3px;
      display: flex;
      flex-direction: column;
      gap: 2.5px;
      z-index: 3
    }

    .bseg {
      flex: 1;
      border-radius: 1px;
      background: rgba(0, 0, 0, .25);
      border: 1px solid rgba(255, 255, 255, .07)
    }

    #socCanvas {
      display: block;
      margin: 0 auto
    }

    .soc-lbl {
      font-size: 7.5px;
      color: var(--tx3);
      letter-spacing: 1.2px;
      font-family: var(--fn-mn);
      text-align: center;
      margin-top: 2px
    }

    .bms-rows .brow {
      display: flex;
      justify-content: space-between;
      padding: 3.5px 0;
      border-bottom: 1px solid rgba(30, 58, 95, .4);
      font-size: 9.5px
    }

    .brow span:first-child {
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .brow span:last-child {
      color: var(--tx);
      font-family: var(--fn-mn);
      font-weight: 600
    }

    /* Cell strip */
    .cell-strip {
      margin-top: 7px
    }

    .cs-ttl {
      font-size: 7.5px;
      color: var(--tx3);
      letter-spacing: 1.2px;
      font-family: var(--fn-mn);
      margin-bottom: 4px
    }

    #cellsRow {
      display: flex;
      gap: 3px
    }

    .cell {
      flex: 1;
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 3px;
      padding: 3px 2px;
      text-align: center
    }

    .cell-v {
      font-size: 8.5px;
      font-weight: 700;
      color: var(--grn);
      font-family: var(--fn-mn)
    }

    .cell-bar {
      height: 3px;
      background: var(--b1);
      border-radius: 2px;
      margin-top: 2px;
      overflow: hidden
    }

    .cell-fill {
      height: 100%;
      border-radius: 2px;
      transition: width .8s
    }

    .cell-nm {
      font-size: 6.5px;
      color: var(--tx3);
      font-family: var(--fn-mn);
      margin-top: 1px
    }

    /* MPPT + Inverter */
    .inv-body {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 9px
    }

    .sec-t {
      font-size: 8.5px;
      color: var(--tx2);
      letter-spacing: 1.5px;
      font-family: var(--fn-mn);
      font-weight: 700;
      margin-bottom: 6px;
      border-bottom: 1px solid var(--b1);
      padding-bottom: 3px
    }

    .mppt-chs {
      display: flex;
      gap: 4px;
      margin-bottom: 7px
    }

    .mch {
      flex: 1;
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 4px;
      padding: 4px;
      text-align: center
    }

    .mch-id {
      font-size: 7.5px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .mch-v {
      font-size: 10.5px;
      font-weight: 700;
      font-family: var(--fn-mn)
    }

    .mch-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      margin: 3px auto 0;
      box-shadow: 0 0 5px
    }

    .mppt-info .mr {
      display: flex;
      justify-content: space-between;
      padding: 3px 0;
      font-size: 9.5px;
      font-family: var(--fn-mn);
      border-bottom: 1px solid rgba(30, 58, 95, .3)
    }

    .mr span:first-child {
      color: var(--tx3)
    }

    .mr span:last-child {
      color: var(--tx);
      font-weight: 600
    }

    #sineCanvas {
      background: #050012;
      border-radius: 4px;
      border: 1px solid rgba(80, 0, 100, .4);
      display: block;
      width: 100%
    }

    .phase-row {
      display: flex;
      gap: 8px;
      justify-content: center;
      margin-top: 3px;
      font-size: 8.5px;
      font-family: var(--fn-mn);
      align-items: center
    }

    .inv-stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3px;
      margin-top: 6px
    }

    .istat {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 4px;
      padding: 4px;
      text-align: center
    }

    .istat-v {
      font-family: var(--fn-mn);
      font-size: 11.5px;
      font-weight: 600;
      color: var(--tx)
    }

    .istat-l {
      font-size: 7px;
      color: var(--tx3);
      letter-spacing: .8px;
      font-family: var(--fn-mn);
      margin-top: 1px
    }

    /* ═══════════════════════════════════════════════════════════
   COLUMN 3 — SMART METER + DISTRIBUTION BOARD
═══════════════════════════════════════════════════════════ */
    /* Smart meter */
    .meter-body {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 9px;
      margin-bottom: 9px
    }

    .m-screen {
      background: #030d1a;
      border: 1px solid rgba(6, 182, 212, .3);
      border-radius: 6px;
      overflow: hidden
    }

    .m-hdr {
      background: rgba(6, 182, 212, .14);
      border-bottom: 1px solid rgba(6, 182, 212, .2);
      padding: 4px 8px;
      font-size: 8.5px;
      font-weight: 700;
      color: var(--cyn2);
      letter-spacing: 1.5px;
      font-family: var(--fn-mn)
    }

    .m-rows {
      padding: 4px 6px
    }

    .mrow {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 3px 0;
      border-bottom: 1px solid rgba(14, 30, 50, .8);
      font-size: 9.5px
    }

    .mrow:last-child {
      border: none
    }

    .mrow-dot {
      width: 7px;
      height: 7px;
      border-radius: 1px;
      flex-shrink: 0;
      margin-right: 4px
    }

    .mrow-lbl {
      color: var(--tx3);
      font-family: var(--fn-mn);
      flex: 1
    }

    .mrow-val {
      font-family: var(--fn-mn);
      font-weight: 700
    }

    .iot-box {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 6px;
      padding: 8px
    }

    .iot-t {
      font-size: 8.5px;
      color: var(--cyn2);
      letter-spacing: 1.8px;
      font-family: var(--fn-mn);
      font-weight: 700;
      margin-bottom: 7px
    }

    .wifi {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      margin-bottom: 7px;
      height: 38px;
      justify-content: flex-end
    }

    .wb {
      border-radius: 50%;
      border: 2px solid var(--cyn2);
      border-bottom-color: transparent;
      border-left-color: transparent;
      animation: wpulse 1.8s ease infinite
    }

    .wb1 {
      width: 14px;
      height: 14px;
      animation-delay: .5s
    }

    .wb2 {
      width: 22px;
      height: 22px;
      animation-delay: .25s
    }

    .wb3 {
      width: 30px;
      height: 30px;
      animation-delay: 0s
    }

    .wdot {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--cyn2);
      box-shadow: 0 0 5px var(--cyn2)
    }

    @keyframes wpulse {

      0%,
      100% {
        opacity: .25
      }

      50% {
        opacity: 1
      }
    }

    .iot-rows .irow {
      display: flex;
      justify-content: space-between;
      padding: 2px 0;
      font-size: 8.5px;
      font-family: var(--fn-mn)
    }

    .irow span:first-child {
      color: var(--tx3)
    }

    .irow span:last-child {
      color: var(--cyn2);
      font-weight: 600
    }

    .iot-leds {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-top: 5px;
      flex-wrap: wrap
    }

    .iled {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--grn);
      box-shadow: 0 0 5px var(--grn);
      animation: blink 1.6s ease-in-out infinite
    }

    .il {
      font-size: 8px;
      color: var(--tx2);
      font-family: var(--fn-mn)
    }

    /* Power chart */
    .chart-wrap {
      margin-top: 2px
    }

    .cw-t {
      font-size: 7.5px;
      color: var(--tx3);
      letter-spacing: 1.3px;
      font-family: var(--fn-mn);
      margin-bottom: 4px
    }

    #powerChart {
      display: block;
      width: 100%;
      border-radius: 3px;
      background: #030810;
      border: 1px solid var(--b1)
    }

    .cleg-row {
      display: flex;
      gap: 10px;
      margin-top: 3px
    }

    .cleg {
      font-size: 8px;
      font-family: var(--fn-mn);
      padding: 1.5px 6px;
      border-radius: 3px
    }

    .cleg.s {
      color: var(--sol);
      background: rgba(245, 158, 11, .07);
      border: 1px solid rgba(245, 158, 11, .2)
    }

    .cleg.b {
      color: var(--grn);
      background: rgba(34, 197, 94, .07);
      border: 1px solid rgba(34, 197, 94, .2)
    }

    .cleg.l {
      color: var(--blu2);
      background: rgba(59, 130, 246, .07);
      border: 1px solid rgba(59, 130, 246, .2)
    }

    /* Distribution board */
    .mccb-main {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(127, 0, 0, .1);
      border: 1px solid rgba(239, 68, 68, .3);
      border-radius: 6px;
      padding: 6px 9px;
      margin-bottom: 7px
    }

    .mc-lbl {
      font-size: 9.5px;
      color: var(--red2);
      font-family: var(--fn-mn);
      font-weight: 700
    }

    .mc-val {
      font-size: 8.5px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .tog {
      font-size: 8.5px;
      padding: 2px 7px;
      border-radius: 3px;
      font-weight: 700;
      font-family: var(--fn-mn)
    }

    .tog.on {
      background: rgba(34, 197, 94, .18);
      border: 1px solid var(--grn);
      color: var(--grn2)
    }

    .tog.off {
      background: rgba(239, 68, 68, .18);
      border: 1px solid var(--red);
      color: var(--red2)
    }

    .mc-info {
      font-size: 7.5px;
      color: var(--tx3);
      font-family: var(--fn-mn);
      margin-left: auto
    }

    #mcbList {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 7px
    }

    .mcb {
      display: flex;
      align-items: center;
      gap: 7px;
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 5px;
      padding: 5px 7px
    }

    .mcb-id {
      font-size: 9.5px;
      font-weight: 700;
      font-family: var(--fn-mn);
      width: 42px
    }

    .mcb-desc {
      flex: 1;
      font-size: 8.5px;
      color: var(--tx2);
      font-family: var(--fn-mn)
    }

    .mcb-amp {
      font-size: 9.5px;
      font-weight: 700;
      font-family: var(--fn-mn);
      width: 32px;
      text-align: right
    }

    .mcb-flow {
      width: 50px;
      height: 3.5px;
      border-radius: 2px;
      overflow: hidden;
      background: var(--b1)
    }

    .mcb-flow-fill {
      height: 100%;
      border-radius: 2px;
      background: linear-gradient(90deg, var(--grn), transparent, var(--grn));
      background-size: 200% 100%;
      animation: flowSlide 1s linear infinite
    }

    @keyframes flowSlide {
      to {
        background-position: -200% 0
      }
    }

    .busbar {
      background: rgba(234, 179, 8, .05);
      border: 1px solid rgba(234, 179, 8, .2);
      border-radius: 5px;
      padding: 5px 7px
    }

    .bb-t {
      font-size: 7.5px;
      color: var(--yel);
      letter-spacing: 1.3px;
      font-family: var(--fn-mn);
      margin-bottom: 4px
    }

    .bb-bars {
      display: flex;
      gap: 3px
    }

    .bbar {
      flex: 1;
      height: 11px;
      border-radius: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 7.5px;
      font-weight: 700;
      font-family: var(--fn-mn)
    }

    .bbar.l1 {
      background: rgba(239, 68, 68, .18);
      border: 1px solid rgba(239, 68, 68, .4);
      color: var(--red2)
    }

    .bbar.l2 {
      background: rgba(234, 179, 8, .18);
      border: 1px solid rgba(234, 179, 8, .4);
      color: var(--yel)
    }

    .bbar.l3 {
      background: rgba(59, 130, 246, .18);
      border: 1px solid rgba(59, 130, 246, .4);
      color: var(--blu2)
    }

    .bbar.nn {
      background: rgba(148, 163, 184, .08);
      border: 1px solid rgba(148, 163, 184, .25);
      color: var(--tx3)
    }

    /* ═══════════════════════════════════════════════════════════
   COLUMN 4 — CHARGERS + EVs
═══════════════════════════════════════════════════════════ */
    #chGrid {
      display: flex;
      flex-direction: column;
      gap: 9px
    }

    .chcard {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 8px;
      padding: 9px;
      position: relative;
      overflow: hidden;
      transition: border-color .4s, box-shadow .4s
    }

    .chcard.act {
      border-color: var(--grn);
      box-shadow: 0 0 14px rgba(2, 126, 48, 0.915)
    }

    .chcard.stby {
      opacity: .72
    }

    .ch-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 7px
    }

    .ch-id-lbl {
      font-size: 9.5px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .ch-phase {
      font-size: 7.5px;
      padding: 2px 6px;
      border-radius: 3px;
      font-family: var(--fn-mn);
      font-weight: 700;
      letter-spacing: .8px
    }

    .p1 {
      background: rgba(59, 130, 246, .13);
      border: 1px solid rgba(59, 130, 246, .38);
      color: var(--blu2)
    }

    .p3 {
      background: rgba(249, 115, 22, .13);
      border: 1px solid rgba(249, 115, 22, .38);
      color: var(--org2)
    }

    .ch-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      transition: all .3s
    }

    .ch-main {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px
    }

    .ch-screen {
      background: #020c04;
      border: 1px solid rgba(34, 197, 94, .18);
      border-radius: 5px;
      padding: 6px
    }

    .ch-evname {
      font-size: 11px;
      font-weight: 700;
      color: var(--grn2);
      font-family: var(--fn-mn);
      margin-bottom: 3px
    }

    .ch-pwr {
      font-size: 18px;
      font-weight: 700;
      line-height: 1;
      font-family: var(--fn-hd)
    }

    .ch-pwr-u {
      font-size: 9.5px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .ch-sub {
      display: flex;
      justify-content: space-between;
      margin-top: 3px;
      font-size: 8.5px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .ev-vis {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px
    }

    .ev-car {
      width: 100%;
      height: 50px;
      border-radius: 7px;
      position: relative;
      overflow: hidden
    }

    .ev-body {
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 7px;
      border: 1.5px solid rgba(255, 255, 255, .15)
    }

    .ev-roof {
      position: absolute;
      top: 5px;
      left: 14%;
      right: 14%;
      height: 16px;
      background: rgba(179, 229, 252, .28);
      border-radius: 4px;
      border: 1px solid rgba(2, 136, 209, .35)
    }

    .ev-wh {
      position: absolute;
      bottom: 4px
    }

    .ev-wh-l {
      left: 8px
    }

    .ev-wh-r {
      right: 8px
    }

    .ev-whl {
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: #212121;
      border: 2px solid #424242
    }

    .ev-port {
      position: absolute;
      right: 4px;
      top: 50%;
      transform: translateY(-50%);
      width: 9px;
      height: 9px;
      border-radius: 50%;
      transition: all .3s
    }

    .ev-port.on {
      background: #00e5ff;
      box-shadow: 0 0 8px #00e5ff
    }

    .ev-port.off {
      background: #37474f
    }

    .soc-track {
      width: 100%;
      height: 5px;
      background: var(--b1);
      border-radius: 3px;
      overflow: hidden
    }

    .soc-fill {
      height: 100%;
      border-radius: 3px;
      transition: width 1s
    }

    .soc-meta {
      display: flex;
      justify-content: space-between;
      width: 100%;
      font-size: 7.5px;
      font-family: var(--fn-mn)
    }

    .soc-pct {
      color: var(--tx);
      font-weight: 700
    }

    .soc-eta {
      color: var(--tx3)
    }

    .ch-conn {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-top: 5px
    }

    .conn-circ {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      border: 1.5px solid;
      transition: all .4s
    }

    .conn-txt {
      font-size: 7.5px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .ch-foot {
      display: flex;
      justify-content: space-between;
      margin-top: 5px;
      font-size: 8px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .ch-anim {
      height: 3px;
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      border-radius: 0 0 8px 8px;
      background: linear-gradient(90deg, transparent, var(--grn), transparent);
      background-size: 200% 100%;
      animation: flowSlide 1.4s linear infinite
    }

    /* ── KPI STRIP ──────────────────────────────────────────── */
    #kpi {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 5px;
      padding: 5px 7px;
      height: 64px;
      flex-shrink: 0;
      background: linear-gradient(0deg, rgba(7, 15, 31, .98), rgba(5, 10, 22, .95));
      border-top: 1px solid var(--b2)
    }

    .ki {
      background: var(--bg3);
      border: 1px solid var(--b1);
      border-radius: 6px;
      padding: 5px 9px;
      display: flex;
      align-items: center;
      gap: 7px;
      position: relative;
      overflow: hidden
    }

    .ki::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 2px
    }

    .ki.s::after {
      background: linear-gradient(90deg, transparent, var(--sol), transparent)
    }

    .ki.g::after {
      background: linear-gradient(90deg, transparent, var(--grn), transparent)
    }

    .ki.b::after {
      background: linear-gradient(90deg, transparent, var(--blu2), transparent)
    }

    .ki.c::after {
      background: linear-gradient(90deg, transparent, var(--grn2), transparent)
    }

    .ki.p::after {
      background: linear-gradient(90deg, transparent, var(--pur2), transparent)
    }

    .ki.y::after {
      background: linear-gradient(90deg, transparent, var(--cyn2), transparent)
    }

    .ki-ico {
      font-size: 18px;
      opacity: .8
    }

    .ki-v {
      font-family: var(--fn-hd);
      font-size: 20px;
      font-weight: 700;
      line-height: 1;
      color: var(--tx)
    }

    .ki-u {
      font-size: 9px;
      color: var(--tx3);
      font-family: var(--fn-mn)
    }

    .ki-l {
      font-size: 7px;
      color: var(--tx3);
      letter-spacing: 1px;
      font-family: var(--fn-mn);
      margin-top: 1px
    }

    .ki.s .ki-v {
      color: var(--sol)
    }

    .ki.g .ki-v {
      color: var(--grn)
    }

    .ki.b .ki-v {
      color: var(--blu2)
    }

    .ki.c .ki-v {
      color: var(--grn2)
    }

    .ki.p .ki-v {
      color: var(--pur2)
    }

    .ki.y .ki-v {
      color: var(--cyn2)
    }

    .spark {
      margin-left: auto
    }

    /* ════════════════════════════════════════════════════════
       RESPONSIVE LAYOUT
    ════════════════════════════════════════════════════════ */
    /* Large desktops — default 4-col grid unchanged */

    /* Medium desktops / landscape tablets */
    @media (max-width: 1400px) {
      #dash {
        grid-template-columns: 1.1fr 1fr 1fr 0.95fr
      }
    }

    /* Tablets — 2×2 grid, body scrollable */
    @media (max-width: 1100px) {
      body {
        overflow: auto
      }

      #root {
        height: auto;
        overflow: visible
      }

      #dash {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto;
        overflow-y: visible
      }

      #kpi {
        grid-template-columns: repeat(3, 1fr);
        height: auto;
        padding: 7px 7px 9px
      }
    }

    /* Landscape phones / small tablets — single column */
    @media (max-width: 720px) {
      html {
        font-size: 11.5px
      }

      #dash {
        grid-template-columns: 1fr
      }

      #hdr {
        flex-wrap: wrap;
        height: auto;
        padding: 8px 12px;
        gap: 8px
      }

      .hdr-right {
        flex-wrap: wrap;
        gap: 8px
      }

      .hdr-mid {
        min-width: auto
      }

      #clock {
        font-size: 20px
      }

      #kpi {
        grid-template-columns: repeat(3, 1fr)
      }

      .bms-body {
        grid-template-columns: 54px 1fr
      }

      .meter-body {
        grid-template-columns: 1fr
      }

      .inv-body {
        grid-template-columns: 1fr
      }

      #socCanvas {
        width: 110px !important;
        height: 110px !important
      }
    }

    /* Portrait phones */
    @media (max-width: 480px) {
      html {
        font-size: 11px
      }

      #kpi {
        grid-template-columns: repeat(2, 1fr)
      }

      .b-title {
        font-size: 13px;
        letter-spacing: 1.5px
      }

      .b-sub {
        display: none
      }

      .hdr-right {
        gap: 6px
      }

      .hsv {
        font-size: 9px
      }

      .ch-main {
        grid-template-columns: 1fr
      }

      .ev-car {
        height: 40px
      }
    }
  </style>
</head>

<body>
  <div id="root">

    <!-- ══ HEADER ══ -->
    <header id="hdr">
      <div class="brand">
        <div class="brand-sun">
          <svg width="42" height="42" viewBox="0 0 42 42">
            <circle cx="21" cy="21" r="9" fill="#f59e0b" />
            <circle cx="21" cy="21" r="13" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 3"
              class="spin-d" />
            <line x1="21" y1="3" x2="21" y2="8" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" />
            <line x1="21" y1="34" x2="21" y2="39" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" />
            <line x1="3" y1="21" x2="8" y2="21" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" />
            <line x1="34" y1="21" x2="39" y2="21" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" />
            <line x1="6.5" y1="6.5" x2="10" y2="10" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round" />
            <line x1="32" y1="32" x2="35.5" y2="35.5" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round" />
            <line x1="35.5" y1="6.5" x2="32" y2="10" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round" />
            <line x1="6.5" y1="35.5" x2="10" y2="32" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round" />
          </svg>
        </div>
        <div>
          <div class="b-title">SOLAR<span class="ac">EV</span> RWANDA</div>
          <div class="b-sub">120.1 kWp · 168× Jinko 720W · 640 kWh LFP · 150 kW Inverter · 5 Chargers · Kigali City ·
            Building Parking Area</div>
        </div>
      </div>
      <div class="hdr-mid">
        <div class="live-pill"><span class="live-dot"></span>LIVE MONITORING</div>
        <div id="clock">--:--:--</div>
        <div id="dateTxt">--</div>
        <div id="modeBadge">SOLAR PV DIRECT</div>
      </div>
      <div class="hdr-right">
        <div class="hstat"><span class="hsl">GRID · DAY</span><span class="hsv off">STANDBY</span></div>
        <div class="hstat"><span class="hsl">GRID · NIGHT</span><span class="hsv on">BACKUP</span></div>
        <div class="hstat"><span class="hsl">SYSTEM</span><span class="hsv on" id="sysLbl">Composite 12hs of
            Solar-Battery & 12hs of Grid</span></div>
        <div class="hstat"><span class="hsl">ENGINEER</span><span class="hsv" style="color:#fbbf24">Eng. Hermes
            MUGISHA</span></div>
        <div class="hstat"><span class="hsl">PROJECT</span><span class="hsv" style="color:#60a5fa">Solar Clean Energy &
            E-Mobility Infrastraction 2026</span>
        </div>
      </div>
    </header>

    <!-- ══ MAIN GRID ══ -->
    <div id="dash">

      <!-- COL 1: SUN + PV -->
      <div class="col">

        <!-- SUN IRRADIANCE -->
        <div class="card">
          <div class="ch"><span class="chi">☀</span>SOLAR IRRADIANCE
            <span class="cbadge blu">NASA · RWANDA</span>
          </div>
          <div class="sun-body">
            <div class="sun-orb">
              <div class="sr sr1"></div>
              <div class="sr sr2"></div>
              <div class="sc">
                <div class="sc-irr" id="sunIrr">—</div>
                <div class="sc-u">W/m²</div>
              </div>
            </div>
            <div class="sun-stats">
              <div class="ss"><span>Amb. Temp</span><span id="ambT">18°C</span></div>
              <div class="ss"><span>Sim Time</span><span id="simT">—</span></div>
              <div class="ss"><span>Mode</span><span id="modeShort" style="color:var(--grn)">PV</span></div>
              <div class="ss"><span>PSH / day</span><span>4.8 h</span></div>
              <div class="ss"><span>Tilt / Az.</span><span>15° / 0°</span></div>
              <div class="ss"><span>Ann. GHI</span><span>1752 kWh</span></div>
            </div>
          </div>
          <div class="sched">
            <div class="sched-ttl">⏱ 24H OPERATIONAL SCHEDULE — REAL-TIME CONTROL</div>
            <div class="sched-bar">
              <!-- BAT 08:00–11:00 = 2h / 24h = 8.33% -->
              <div class="seg seg-b1" style="width:8.33%;min-width:0">BAT</div>
              <!-- PV  11:00–16:00 = 7h / 24h = 29.17% -->
              <div class="seg seg-pv" style="width:29.17%;min-width:0">☀ SOLAR PV</div>
              <!-- BAT 16:00–20:00 = 3h / 24h = 12.5% -->
              <div class="seg seg-b2" style="width:12.5%;min-width:0">BAT</div>
              <!-- GRID 20:00–23:00 = 3h / 24h = 12.5% -->
              <div class="seg"
                style="width:12.5%;min-width:0;background:rgba(38,50,56,.55);border:1px solid rgba(84,110,122,.5);color:#90a4ae;border-radius:3px;display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:700;font-family:var(--fn-mn)">
                GRID</div>
              <!-- GRID CHG 22:00–04:00 = 5h / 24h = 20.83% -->
              <div class="seg"
                style="width:20.83%;min-width:0;background:rgba(38,50,56,.55);border:1px solid rgba(84,110,122,.5);color:#90a4ae;border-radius:3px;display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:700;font-family:var(--fn-mn)">
                GRID CHG BTTRY</div>
              <!-- GRID 04:00–08:00 = 4h / 24h = 16.67% -->
              <div class="seg"
                style="width:16.67%;min-width:0;background:rgba(33,33,33,.55);border:1px solid rgba(66,66,66,.45);color:#546e7a;border-radius:3px;display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:700;font-family:var(--fn-mn)">
                GRID</div>
              <div class="needle" id="needle"><span class="needle-label" id="needleLabel">--:--:--</span></div>
            </div>
            <div class="sched-tks">
              <span>08:00</span><span>11:00</span>
              <span
                style="margin-left:auto">16:00</span><span>20:00</span><span>23:00</span><span>04:00</span><span>08:00</span>
            </div>
            <div id="schedStatus">LOADING...</div>
          </div>
        </div>

        <!-- PV ARRAY + STRINGS -->
        <div class="card">
          <div class="ch"><span class="chi">⚡</span>PV ARRAY · 168× JINKO 720W
            <span class="cbadge">16 STR × 10 MOD</span>
          </div>
          <!-- String row labels + grid (built by JS) -->
          <div id="pvGridWrap"></div>
          <!-- String connection diagram -->
          <div id="strDiag"></div>
          <div class="pv-stats">
            <div class="pvs">
              <div class="pvs-v hi" id="pvKW">120.5kW</div>
              <div class="pvs-l">Output</div>
            </div>
            <div class="pvs">
              <div class="pvs-v" id="pvVmpp">414.5V</div>
              <div class="pvs-l">Vmpp</div>
            </div>
            <div class="pvs">
              <div class="pvs-v" id="pvImpp">146.0A</div>
              <div class="pvs-l">Impp</div>
            </div>
            <div class="pvs">
              <div class="pvs-v" id="pvEff">98.5%</div>
              <div class="pvs-l">MPPT Eff</div>
            </div>
          </div>
        </div>

      </div>

      <!-- COL 2: BMS + INVERTER -->
      <div class="col">

        <!-- BMS -->
        <div class="card">
          <div class="ch"><span class="chi">⬡</span>BATTERY MANAGEMENT SYSTEM
            <span class="cbadge grn">LFP 800V / 620-840kWh</span>
          </div>
          <div class="bms-body">
            <div class="batt-tower">
              <div class="batt-cap"></div>
              <div class="batt-shell">
                <div class="batt-fill" id="battFill"></div>
                <div class="batt-pct" id="battPct">82%</div>
                <div class="batt-segs" id="battSegs"></div>
              </div>
            </div>
            <div>
              <canvas id="socCanvas" width="140" height="140"></canvas>
              <div class="soc-lbl">STATE OF CHARGE</div>
            </div>
            <div class="bms-rows">
              <div class="brow"><span>Voltage</span><span id="bV">800V</span></div>
              <div class="brow"><span>Capacity</span><span>300Ah/640kWh</span></div>
              <div class="brow"><span>Current</span><span id="bI">—A</span></div>
              <div class="brow"><span>Direction</span><span id="bDir" style="color:var(--grn)">Discharge</span></div>
              <div class="brow"><span>Temp</span><span id="bTemp">34°C</span></div>
              <div class="brow"><span>Chemistry</span><span>LiFePO4</span></div>
              <div class="brow"><span>Cycles</span><span>312</span></div>
              <div class="brow"><span>DoD Max</span><span>80%</span></div>
              <div class="brow"><span>BMS Status</span>
                <span style="color:var(--grn)">OK ✓</span>
              </div>
            </div>
          </div>
          <div class="cell-strip">
            <div class="cs-ttl">MODULE CELL VOLTAGES (8 MODULES @ 100V each)</div>
            <div id="cellsRow"></div>
          </div>
        </div>

        <!-- MPPT + INVERTER -->
        <div class="card">
          <div class="ch"><span class="chi">⟲</span>MPPT + 132kW INVERTER
            <span class="cbadge pur">3-PHASE · 400V/50Hz</span>
          </div>
          <div class="inv-body">
            <div>
              <div class="sec-t">MPPT — 132kW · 4-CHANNEL</div>
              <div class="mppt-chs" id="mpptChs"></div>
              <div class="mppt-info">
                <div class="mr"><span>Vin DC</span><span id="mpptVin">414.5V</span></div>
                <div class="mr"><span>Iin DC</span><span id="mpptIin">146.0A</span></div>
                <div class="mr"><span>Pin</span><span id="mpptPin">132.0kW</span></div>
                <div class="mr"><span>Efficiency</span><span style="color:var(--grn)">98.5%</span></div>
                <div class="mr"><span>Max Input</span><span>600V / 80A</span></div>
              </div>
            </div>
            <div>
              <div class="sec-t">INVERTER — 150kW ON-GRID</div>
              <canvas id="sineCanvas" width="260" height="75"></canvas>
              <div class="phase-row">
                <span style="color:#ef4444">L1 230V</span>
                <span style="color:#eab308">L2 230V</span>
                <span style="color:#3b82f6">L3 230V</span>
                <span style="color:#04b02c;font-size:9px">50 Hz</span>
              </div>
              <div class="inv-stats">
                <div class="istat">
                  <div class="istat-v" id="invVout">400V</div>
                  <div class="istat-l">AC Out</div>
                </div>
                <div class="istat">
                  <div class="istat-v" id="invPout">149kW</div>
                  <div class="istat-l">Power</div>
                </div>
                <div class="istat">
                  <div class="istat-v" id="invIout">85A</div>
                  <div class="istat-l">I out</div>
                </div>
                <div class="istat">
                  <div class="istat-v" style="color:var(--grn)">97.5%</div>
                  <div class="istat-l">Eff.</div>
                </div>
                <div class="istat">
                  <div class="istat-v">&lt;3%</div>
                  <div class="istat-l">THD</div>
                </div>
                <div class="istat">
                  <div class="istat-v">0.99</div>
                  <div class="istat-l">PF</div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- COL 3: SMART METER + DB -->
      <div class="col">

        <!-- SMART METER + IoT -->
        <div class="card">
          <div class="ch"><span class="chi">📡</span>SMART METER · IoT
            <span class="cbadge cyn">MODBUS TCP · MQTT</span>
          </div>
          <div class="meter-body">
            <div class="m-screen">
              <div class="m-hdr">⚡ SMART METER — 3Ph 120A</div>
              <div class="m-rows" id="meterRows"></div>
            </div>
            <div class="iot-box">
              <div class="iot-t">IoT MONITORING</div>
              <div class="wifi">
                <div class="wb wb3"></div>
                <div class="wb wb2"></div>
                <div class="wb wb1"></div>
                <div class="wdot"></div>
              </div>
              <div class="iot-rows" id="iotRows"></div>
              <div class="iot-leds">
                <span class="iled"></span><span class="il">MQTT</span>
                <span class="iled" style="animation-delay:.4s"></span><span class="il">Modbus</span>
                <span class="iled" style="animation-delay:.8s"></span><span class="il">Cloud☁</span>
              </div>
            </div>
          </div>
          <div class="chart-wrap">
            <div class="cw-t">24h POWER FLOW — Solar · Battery SoC · EV Load (kW)</div>
            <canvas id="powerChart" height="82"></canvas>
            <div class="cleg-row">
              <span class="cleg s">● Solar PV</span>
              <span class="cleg b">● Battery SoC</span>
              <span class="cleg l">● EV Load</span>
            </div>
          </div>
        </div>

        <!-- DISTRIBUTION BOARD -->
        <div class="card">
          <div class="ch"><span class="chi">⊞</span>DISTRIBUTION BOARD
            <span class="cbadge yel">MCCB 350A + 5×MCB</span>
          </div>
          <!-- MCCB Main -->
          <div class="mccb-main">
            <div>
              <div class="mc-lbl">MCCB MAIN BREAKER</div>
              <div class="mc-val">350A · 3-Phase</div>
            </div>
            <div class="tog on">ON</div>
            <div class="mc-info">IEC 60947 · 36kA breaking · 400V</div>
          </div>
          <!-- MCB list built by JS -->
          <div id="mcbList"></div>
          <!-- Bus bar -->
          <div class="busbar">
            <div class="bb-t">AC BUS BAR — 400V / 230V / N / PE</div>
            <div class="bb-bars">
              <div class="bbar l1">L1</div>
              <div class="bbar l2">L2</div>
              <div class="bbar l3">L3</div>
              <div class="bbar nn">N</div>
            </div>
          </div>
        </div>

      </div>

      <!-- COL 4: CHARGERS + EVs -->
      <div class="col">
        <div class="card" style="flex:1">
          <div class="ch"><span class="chi">🔌</span>EV CHARGING STATIONS — LIVE
            <span class="cbadge grn" id="activeBadge">5 ACTIVE</span>
          </div>
          <div id="chGrid"></div>
        </div>
      </div>

    </div><!-- #dash -->

    <!-- ══ KPI STRIP ══ -->
    <div id="kpi">
      <div class="ki s">
        <div class="ki-ico">☀</div>
        <div>
          <div class="ki-v" id="kSol">60.5</div>
          <div class="ki-u">kW</div>
          <div class="ki-l">Solar Generation</div>
        </div>
        <canvas class="spark" id="spkSol" width="55" height="28"></canvas>
      </div>
      <div class="ki g">
        <div class="ki-ico">⬡</div>
        <div>
          <div class="ki-v" id="kBat">82</div>
          <div class="ki-u">%</div>
          <div class="ki-l">Battery SoC</div>
        </div>
        <canvas class="spark" id="spkBat" width="55" height="28"></canvas>
      </div>
      <div class="ki b">
        <div class="ki-ico">⚡</div>
        <div>
          <div class="ki-v" id="kLoad">58</div>
          <div class="ki-u">kW</div>
          <div class="ki-l">EV Load</div>
        </div>
        <canvas class="spark" id="spkLoad" width="55" height="28"></canvas>
      </div>
      <div class="ki c">
        <div class="ki-ico">🌿</div>
        <div>
          <div class="ki-v" id="kCO2">0.0</div>
          <div class="ki-u">kg</div>
          <div class="ki-l">CO₂ Saved Today</div>
        </div>
        <canvas class="spark" id="spkCO2" width="55" height="28"></canvas>
      </div>
      <div class="ki p">
        <div class="ki-ico">η</div>
        <div>
          <div class="ki-v" id="kEff">97.5</div>
          <div class="ki-u">%</div>
          <div class="ki-l">System Eff.</div>
        </div>
        <canvas class="spark" id="spkEff" width="55" height="28"></canvas>
      </div>
      <div class="ki y">
        <div class="ki-ico">∑</div>
        <div>
          <div class="ki-v" id="kGen">0.0</div>
          <div class="ki-u">kWh</div>
          <div class="ki-l">Generated Today</div>
        </div>
        <canvas class="spark" id="spkGen" width="55" height="28"></canvas>
      </div>
    </div>

  </div><!-- #root -->

  <script>
    // ════════════════════════════════════════════════════════════
    //  SYSTEM CONSTANTS  (exact values from _ev_60kw_enhanced.py)
    // ════════════════════════════════════════════════════════════
    const SYS = {
      NUM_MODULES: 168, MOD_W: 720, PV_KWP: 120.1,
      PV_VMPP: 41.45, PV_IMPP: 13.27,
      MODS_STR: 16, NUM_STR: 10,
      STR_VMPP: 414.5, STR_IMPP: 13.27,
      ARR_VMPP: 414.5, ARR_IMPP: 145.97,
      BAT_V: 800, BAT_AH: 300, BAT_KWH: 640,
      MPPT_EFF: 0.985, INV_KW: 150, INV_EFF: 0.975,
      AC_V3: 400, AC_V1: 230, AC_HZ: 50,
      MCCB_A: 350, MCB_A: [32, 32, 63, 63, 100],
    };
    // NASA POWER monthly PSH — Kigali, Rwanda (−2.48°S, 29.48°E)
    const NASA_PSH = [4.82, 5.03, 4.71, 4.38, 4.28, 4.52, 4.94, 5.24, 5.31, 5.02, 4.63, 4.71];
    const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    // Hourly irradiance profile
    const H_PROF = {
      0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
      6: .04, 7: .14, 8: .32, 9: .55, 10: .75, 11: .92,
      12: 1, 13: .96, 14: .87, 15: .72, 16: .52, 17: .28,
      18: .08, 19: .01, 20: 0, 21: 0, 22: 0, 23: 0
    };
    const EV_CHARGE_SPEED_FACTOR = 1; // 1 = baseline charge rate. Use >1 to speed charging, <1 to slow it down.
    const EV_CAPACITY_KWH = { 7: 20, 22: 60, 40: 80 };
    const CHARGERS_DEF = [
      { id: 1, ph: '1-Phase', kw: 7, V: 230, A: 32, ev: 'EV-A', col: '#0d3b7a', soc: 45 },
      { id: 2, ph: '1-Phase', kw: 7, V: 230, A: 32, ev: 'EV-B', col: '#4a1080', soc: 62 },
      { id: 3, ph: '3-Phase', kw: 22, V: 400, A: 63, ev: 'EV-C', col: '#14451a', soc: 38 },
      { id: 4, ph: '3-Phase', kw: 22, V: 400, A: 63, ev: 'EV-D', col: '#7a1a05', soc: 71 },
      { id: 5, ph: '3-Phase', kw: 40, V: 400, A: 120, ev: 'EV-E', col: '#1a3a00', soc: 22 },
    ];

    // ════════════════════════════════════════════════════════════
    //  SIMULATION STATE
    // ════════════════════════════════════════════════════════════
    const ST = {
      simH: 10.0, tick: 0, month: new Date().getMonth(),
      irr: 0, pvKW: 0, pvVmpp: 0, pvImpp: 0,
      socPct: 82, battDir: 'discharging', battI: 0,
      invPow: 0, totalLoad: 58,
      energyKWh: 0, co2Kg: 0,
      histSol: new Array(144).fill(0),
      histSoc: new Array(144).fill(82),
      histLoad: new Array(144).fill(0),
      pvActive: true, noiseT: 0,
    };
    const CH_STATE = CHARGERS_DEF.map(c => ({
      ...c,
      status: 'charging', actual_kw: c.kw, elapsed_min: 20 + Math.random() * 60
    }));

    // ════════════════════════════════════════════════════════════
    //  HELPERS
    // ════════════════════════════════════════════════════════════
    function sn(t, f = 1, a = 1) {
      return a * (Math.sin(t * f * 2.1) * .4 + Math.sin(t * f * 3.7) * .3
        + Math.sin(t * f * 7.1) * .2 + Math.sin(t * f * 13.3) * .1)
    }
    function getIrr(h, mIdx, nf = 1) {
      const psh = NASA_PSH[mIdx], peak = psh * 200;
      return Math.max(0, Math.min(1200, peak * (H_PROF[Math.floor(h)] || 0) * nf));
    }
    function getPV(irr, t) {
      if (irr < 5) return { kw: 0, vmpp: 0, impp: 0 };
      const f = irr / 1000, tmod = t + (irr / 800) * (43 - 20), tc = 1 + (-.30 / 100) * (tmod - 25);
      const kw = SYS.PV_KWP * f * tc * (1 - .14) * SYS.MPPT_EFF;
      return {
        kw: Math.max(0, kw), vmpp: +(SYS.STR_VMPP * (1 + .001 * (25 - tmod))).toFixed(1),
        impp: +(SYS.ARR_IMPP * f).toFixed(2)
      };
    }
    function getMode(h) {
      if (h >= 8 && h < 10) return { mode: 'BATTERY BUFFER', col: '#4fc3f7', pvOn: true, label: 'BAT AM' };
      if (h >= 10 && h < 17) return { mode: 'SOLAR PV DIRECT', col: '#69f0ae', pvOn: true, label: 'PV' };
      if (h >= 17 && h < 20) return { mode: 'BATTERY BUFFER', col: '#c084fc', pvOn: true, label: 'BAT PM' };
      return { mode: 'Grid Connection', col: '#546e7a', pvOn: false, label: 'IDLE' };
    }
    function fmtTime(h) {
      const hh = Math.floor(h), mm = Math.floor((h - hh) * 60);
      return `${String(hh).padStart(2, '0')}:${String(mm).padStart(2, '0')}`;
    }

    // ════════════════════════════════════════════════════════════
    //  BUILD STATIC WIDGETS (run once at boot)
    // ════════════════════════════════════════════════════════════
    function buildPVGrid() {
      const wrap = document.getElementById('pvGridWrap');
      // 11 strings × 10 modules grid with string labels on left
      let html = '<div style="display:grid;grid-template-columns:18px repeat(10,1fr);gap:2px;margin-bottom:6px">';
      for (let s = 0; s < 11; s++) {
        html += `<div class="str-lbl" style="display:flex;align-items:center">S${s + 1}</div>`;
        for (let m = 0; m < 10; m++) {
          html += `<div class="pvm act" id="pvm_${s}_${m}" title="String ${s + 1} Module ${m + 1} · Jinko 550W · Vmpp=41.45V"></div>`;
        }
      }
      html += '</div>';
      wrap.innerHTML = html;
    }

    function buildStrDiag() {
      const d = document.getElementById('strDiag');
      let html = '<div style="font-size:7.5px;color:var(--tx3);letter-spacing:1.2px;font-family:var(--fn-mn);margin-bottom:3px">STRING CONNECTIONS → COMBINER → MPPT</div>';
      for (let s = 0; s < 11; s++) {
        const p = Math.round(SYS.PV_KWP / SYS.NUM_STR * 10) / 10;
        html += `<div class="str-row">
      <div class="srid">S${s + 1}</div>
      <div class="srwire" id="srw_${s}" style="background:var(--org);color:var(--org)"></div>
      <div class="srfuse"><div class="srfuse-dot"></div></div>
      <div class="srval">${SYS.STR_VMPP}V / ${SYS.STR_IMPP}A / ${p}kW</div>
    </div>`;
      }
      d.innerHTML = html;
    }

    function buildMPPTChannels() {
      const c = document.getElementById('mpptChs');
      const kvs = ['20kW', '20kW', '20.5kW'], cols = ['#22d3ee', '#34d399', '#fbbf24'];
      c.innerHTML = kvs.map((v, i) => `
    <div class="mch">
      <div class="mch-id">CH-${i + 1}</div>
      <div class="mch-v" style="color:${cols[i]}">${v}</div>
      <div class="mch-dot" style="background:${cols[i]};color:${cols[i]}"></div>
    </div>`).join('');
    }

    function buildCells() {
      const r = document.getElementById('cellsRow');
      const cellV = 100; // 800V / 8 modules
      r.innerHTML = `<div style="display:flex;gap:3px;width:100%">` +
        Array.from({ length: 8 }, (_, i) => `
      <div class="cell" id="cell_${i}">
        <div class="cell-v" id="cv_${i}">${cellV}V</div>
        <div class="cell-bar"><div class="cell-fill" id="cf_${i}" style="width:82%;background:var(--grn)"></div></div>
        <div class="cell-nm">M${i + 1}</div>
      </div>`).join('') + `</div>`;
    }

    function buildMeterRows() {
      const rows = [
        ['Op. Mode', '#ffd600', 'SOLAR PV'],
        ['Sim Time', '#22d3ee', '10:00'],
        ['Solar PV', '#f59e0b', '60.5 kW'],
        ['Batt. SoC', '#22c55e', '82 %'],
        ['EV Load', '#f97316', '58 kW'],
        ['Volt 3Ph', '#60a5fa', '400 V'],
        ['Current', '#80cbc4', '85.0 A'],
        ['Frequency', '#c084fc', '50.00 Hz'],
        ['Energy/Day', '#fbbf24', '720 kWh'],
        ['Grid', '#69f0ae', 'ON-GRID ✓'],
      ];
      const r = document.getElementById('meterRows');
      r.innerHTML = rows.map((row, i) => `
    <div class="mrow" id="mr_${i}">
      <div class="mrow-dot" style="background:${row[1]}"></div>
      <div class="mrow-lbl">${row[0]}</div>
      <div class="mrow-val" id="mv_${i}" style="color:${row[1]}">${row[2]}</div>
    </div>`).join('');
    }

    function buildIoTRows() {
      const rows = [
        ['Protocol', 'Modbus TCP + MQTT'],
        ['Broker', 'mqtt.Rwanda-EV Infrastracture'],
        ['Topic', 'solar-ev/Kigali at Builing Parking Area/#'],
        ['Interval', '120 s'],
        ['Last Sync', '00:00 ago'],
      ];
      document.getElementById('iotRows').innerHTML =
        `<div class="iot-rows">` + rows.map((r, i) => `
      <div class="irow">
        <span>${r[0]}</span>
        <span id="iotr_${i}">${r[1]}</span>
      </div>`).join('') + '</div>';
    }

    function buildMCBList() {
      const mcbs = [
        { id: 'MCB-1', desc: 'CH-1 · 1-Phase  7kW  · IEC 62196', amp: '32A', col: '#4fc3f7', on: true },
        { id: 'MCB-2', desc: 'CH-2 · 1-Phase  7kW  · IEC 62196', amp: '32A', col: '#4fc3f7', on: true },
        { id: 'MCB-3', desc: 'CH-3 · 3-Phase 22kW  · IEC 62196', amp: '63A', col: '#ff7043', on: true },
        { id: 'MCB-4', desc: 'CH-4 · 3-Phase 22kW  · IEC 62196', amp: '63A', col: '#ff7043', on: true },
        { id: 'MCB-5', desc: 'CH-5 · 3-Phase 40kW DC Fast · CCS2', amp: '120A', col: '#69f0ae', on: true },
      ];
      document.getElementById('mcbList').innerHTML = mcbs.map((m, i) => `
    <div class="mcb">
      <div class="mcb-id" style="color:${m.col}">${m.id}</div>
      <div class="mcb-desc">${m.desc}</div>
      <div class="mcb-amp">${m.amp}</div>
      <div class="tog ${m.on ? 'on' : 'off'}" id="mcb_tog_${i}">${m.on ? 'ON' : 'OFF'}</div>
      <div class="mcb-flow"><div class="mcb-flow-fill" id="mcb_flow_${i}"
        style="background:linear-gradient(90deg,transparent,${m.col},transparent);background-size:200% 100%"></div>
      </div>
    </div>`).join('');
    }

    function buildChargers() {
      const g = document.getElementById('chGrid');
      const evCols = ['#0d3b7a', '#4a1080', '#14451a', '#7a1a05', '#1a3a00'];
      const connStds = ['IEC 62196 Type 2', 'IEC 62196 Type 2', 'IEC 62196 Type 2', 'IEC 62196 Type 2', 'CCS2 DC Fast'];
      const mcbAmps = [32, 32, 63, 63, 100];
      g.innerHTML = CH_STATE.map((ch, i) => {
        const is3 = ch.ph === '3-Phase';
        const isDC = (ch.kw >= 40);
        const phCls = isDC ? 'p3' : (is3 ? 'p3' : 'p1');
        const phLbl = isDC ? 'DC FAST 400V' : (is3 ? '3-Phase 400V' : '1-Phase 230V');
        const connCol = isDC ? 'var(--grn2)' : (is3 ? 'var(--org2)' : 'var(--blu2)');
        const connBg = isDC ? 'rgba(74,222,128,.1)' : (is3 ? 'rgba(249,115,22,.1)' : 'rgba(59,130,246,.1)');
        const animStyle = isDC
          ? 'background:linear-gradient(90deg,transparent,var(--grn2),transparent);background-size:200% 100%'
          : '';
        return `
    <div class="chcard act" id="chcard_${i}">
      <div class="ch-top">
        <span class="ch-id-lbl">CH-0${ch.id}${isDC ? ' <span style="font-size:7px;color:var(--grn2);letter-spacing:.5px">⚡DC</span>' : ''}</span>
        <span class="ch-phase ${phCls}">${phLbl}</span>
        <div class="ch-dot" id="chdot_${i}" style="background:var(--grn);box-shadow:0 0 7px var(--grn)"></div>
      </div>
      <div class="ch-main">
        <div class="ch-screen">
          <div class="ch-evname" id="chn_${i}">${ch.ev}</div>
          <div style="display:flex;align-items:baseline;gap:3px">
            <span class="ch-pwr" id="chpwr_${i}" style="color:var(--grn)">${ch.kw}.0</span>
            <span class="ch-pwr-u">kW · ${ch.V}V</span>
          </div>
          <div class="ch-sub">
            <span>${ch.A}A · ${connStds[i].split(' ')[0]} ${connStds[i].split(' ')[1]}</span>
            <span id="chst_${i}" style="color:var(--grn)">● ACTIVE</span>
          </div>
        </div>
        <div class="ev-vis">
          <div class="ev-car" id="evcar_${i}">
            <div class="ev-body" style="background:${evCols[i]}${isDC ? ';border:1.5px solid rgba(74,222,128,.4)' : ''}">
              <div class="ev-roof"></div>
              <div class="ev-wh ev-wh-l"><div class="ev-whl"></div></div>
              <div class="ev-wh ev-wh-r"><div class="ev-whl"></div></div>
              <div class="ev-port on" id="evport_${i}"></div>
              ${isDC ? '<div style="position:absolute;top:3px;left:5px;font-size:8px;font-weight:900;color:#4ade80;font-family:var(--fn-mn);letter-spacing:.5px;text-shadow:0 0 6px #4ade80">DC</div>' : ''}
            </div>
          </div>
          <div class="soc-track" style="width:100%">
            <div class="soc-fill" id="socf_${i}" style="width:${ch.soc}%;background:var(--grn)"></div>
          </div>
          <div class="soc-meta">
            <span class="soc-pct" id="socp_${i}">SoC: ${ch.soc}%</span>
            <span class="soc-eta" id="soce_${i}">ETA: —</span>
          </div>
        </div>
      </div>
      <div class="ch-conn">
        <div class="conn-circ" id="conn_${i}"
          style="border-color:${connCol};background:${connBg}">🔌</div>
        <div class="conn-txt">${connStds[i]} · ${is3 ? '3Ph' : '1Ph'} · ${ch.A}A · MCB-${i + 1} ${mcbAmps[i]}A</div>
        <div id="cabling_${i}" style="margin-left:auto;font-size:8px;font-family:var(--fn-mn);color:${connCol}">— kWh</div>
      </div>
      <div class="ch-foot">
        <span id="chtime_${i}">⏱ —</span>
        <span id="chkwh_${i}">⚡ 0.0 kWh</span>
      </div>
      <div class="ch-anim" id="chanim_${i}" style="${animStyle}"></div>
    </div>`}).join('');
    }

    // ════════════════════════════════════════════════════════════
    //  SOC GAUGE (Canvas arc gauge)
    // ════════════════════════════════════════════════════════════
    function drawSOCGauge(pct) {
      const cv = document.getElementById('socCanvas');
      if (!cv) return;
      const ctx = cv.getContext('2d'), W = cv.width, H = cv.height, cx = W / 2, cy = H / 2 + 8;
      const r = 56, start = Math.PI * .8, end = Math.PI * 2.2;
      ctx.clearRect(0, 0, W, H);
      // Background arc
      ctx.beginPath(); ctx.arc(cx, cy, r, start, end);
      ctx.strokeStyle = 'rgba(30,58,95,.6)'; ctx.lineWidth = 10;
      ctx.lineCap = 'round'; ctx.stroke();
      // Gradient arc
      const angle = start + (end - start) * pct / 100;
      const grad = ctx.createLinearGradient(cx - r, cy, cx + r, cy);
      grad.addColorStop(0, '#22c55e'); grad.addColorStop(.6, '#4ade80'); grad.addColorStop(1, '#86efac');
      if (pct < 25) { grad.addColorStop(0, '#ef4444'); grad.addColorStop(1, '#f87171'); }
      else if (pct < 50) { grad.addColorStop(0, '#eab308'); grad.addColorStop(1, '#fbbf24'); }
      ctx.beginPath(); ctx.arc(cx, cy, r, start, angle);
      ctx.strokeStyle = grad; ctx.lineWidth = 10; ctx.lineCap = 'round'; ctx.stroke();
      // Value text
      ctx.fillStyle = '#e2e8f0'; ctx.font = 'bold 26px Orbitron,sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(`${Math.round(pct)}%`, cx, cy);
      ctx.font = '10px Share Tech Mono,monospace';
      ctx.fillStyle = '#94a3b8'; ctx.fillText('SoC', cx, cy + 20);
    }

    // ════════════════════════════════════════════════════════════
    //  SINE WAVE (3-phase animated)
    // ════════════════════════════════════════════════════════════
    let sinePhase = 0;
    function drawSine(active) {
      const cv = document.getElementById('sineCanvas');
      if (!cv) return;
      const ctx = cv.getContext('2d'), W = cv.width, H = cv.height;
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#050012'; ctx.fillRect(0, 0, W, H);
      const amp = active ? (H / 2 - 6) : 8, cy = H / 2;
      const phases = [{ c: '#ef4444', o: 0 }, { c: '#eab308', o: 2 * Math.PI / 3 }, { c: '#3b82f6', o: 4 * Math.PI / 3 }];
      phases.forEach(ph => {
        ctx.beginPath();
        for (let x = 0; x <= W; x++) {
          const t = (x / W) * 3 * 2 * Math.PI + sinePhase + ph.o;
          const y = cy - amp * Math.sin(t);
          x === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
        }
        ctx.strokeStyle = ph.c; ctx.lineWidth = 1.6;
        ctx.globalAlpha = active ? .85 : .3; ctx.stroke(); ctx.globalAlpha = 1;
      });
      sinePhase += 0.12;
    }

    // ════════════════════════════════════════════════════════════
    //  POWER HISTORY CHART
    // ════════════════════════════════════════════════════════════
    function drawPowerChart() {
      const cv = document.getElementById('powerChart');
      if (!cv) return;
      const ctx = cv.getContext('2d'), W = cv.offsetWidth || 500, H = cv.height || 82;
      cv.width = W;
      ctx.fillStyle = '#030810'; ctx.fillRect(0, 0, W, H);
      const pad = { t: 6, b: 20, l: 28, r: 6 }, cW = W - pad.l - pad.r, cH = H - pad.t - pad.b;
      const ds = ST.histSol, db = ST.histSoc, dl = ST.histLoad, n = ds.length;
      if (n < 2) return;
      const maxP = Math.max(70, ...ds, ...dl) * 1.08;
      const xp = i => pad.l + (i / (n - 1)) * cW;
      const yp = v => pad.t + cH - (v / maxP) * cH;
      const yb = v => pad.t + cH - (v / 100) * cH;
      // Grid
      ctx.strokeStyle = 'rgba(30,58,95,.4)'; ctx.lineWidth = .5;
      [0, 20, 40, 60].forEach(v => {
        const y = yp(v);
        ctx.beginPath(); ctx.moveTo(pad.l, y); ctx.lineTo(W - pad.r, y); ctx.stroke();
        ctx.fillStyle = '#475569'; ctx.font = '8px monospace';
        ctx.textAlign = 'right'; ctx.fillText(v, pad.l - 2, y + 3);
      });
      [0, 6, 12, 18, 24].forEach(h => {
        const x = pad.l + (h / 24) * cW;
        ctx.beginPath(); ctx.moveTo(x, pad.t); ctx.lineTo(x, H - pad.b); ctx.stroke();
        ctx.fillStyle = '#475569'; ctx.font = '8px monospace'; ctx.textAlign = 'center';
        ctx.fillText(`${h}h`, x, H - pad.b + 10);
      });
      // Solar fill + line
      ctx.beginPath(); ds.forEach((v, i) => i === 0 ? ctx.moveTo(xp(i), yp(v)) : ctx.lineTo(xp(i), yp(v)));
      ctx.lineTo(xp(n - 1), H - pad.b); ctx.lineTo(xp(0), H - pad.b); ctx.closePath();
      ctx.fillStyle = 'rgba(245,158,11,.07)'; ctx.fill();
      ctx.beginPath(); ds.forEach((v, i) => i === 0 ? ctx.moveTo(xp(i), yp(v)) : ctx.lineTo(xp(i), yp(v)));
      ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 2; ctx.stroke();
      // Load fill + line
      ctx.beginPath(); dl.forEach((v, i) => i === 0 ? ctx.moveTo(xp(i), yp(v)) : ctx.lineTo(xp(i), yp(v)));
      ctx.lineTo(xp(n - 1), H - pad.b); ctx.lineTo(xp(0), H - pad.b); ctx.closePath();
      ctx.fillStyle = 'rgba(59,130,246,.07)'; ctx.fill();
      ctx.beginPath(); dl.forEach((v, i) => i === 0 ? ctx.moveTo(xp(i), yp(v)) : ctx.lineTo(xp(i), yp(v)));
      ctx.strokeStyle = '#3b82f6'; ctx.lineWidth = 1.8; ctx.stroke();
      // Battery SoC dashed
      ctx.beginPath(); db.forEach((v, i) => i === 0 ? ctx.moveTo(xp(i), yb(v)) : ctx.lineTo(xp(i), yb(v)));
      ctx.strokeStyle = '#22c55e'; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]); ctx.stroke(); ctx.setLineDash([]);
      // Now marker
      const nx = xp(n - 1);
      ctx.strokeStyle = 'rgba(245,158,11,.5)'; ctx.lineWidth = 1.2; ctx.setLineDash([2, 4]);
      ctx.beginPath(); ctx.moveTo(nx, pad.t); ctx.lineTo(nx, H - pad.b); ctx.stroke(); ctx.setLineDash([]);
    }

    // ════════════════════════════════════════════════════════════
    //  SPARKLINES
    // ════════════════════════════════════════════════════════════
    const sparkBufs = { sol: [], bat: [], load: [], co2: [], eff: [], gen: [] };
    function drawSparkline(id, data, col) {
      const cv = document.getElementById(id);
      if (!cv || data.length < 2) return;
      const ctx = cv.getContext('2d'), W = cv.width, H = cv.height;
      ctx.clearRect(0, 0, W, H);
      const mn = Math.min(...data), mx = Math.max(...data) || 1;
      const pts = data.map((v, i) => ({ x: (i / (data.length - 1)) * W, y: H - (v - mn) / (mx - mn || 1) * H * .8 - H * .1 }));
      const g = ctx.createLinearGradient(0, 0, W, 0);
      g.addColorStop(0, 'rgba(255,255,255,.2)'); g.addColorStop(1, col);
      ctx.beginPath(); pts.forEach((p, i) => i === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y));
      ctx.strokeStyle = g; ctx.lineWidth = 1.8; ctx.stroke();
    }

    // ════════════════════════════════════════════════════════════
    //  SIMULATION TICK
    // ════════════════════════════════════════════════════════════
    function simTick() {
      ST.tick++;
      ST.noiseT += 0.04;
      const rn = new Date();
      ST.simH = rn.getHours() + rn.getMinutes() / 60 + rn.getSeconds() / 3600;
      ST.month = rn.getMonth();
      const nf = 1 + sn(ST.noiseT, .3, .08);
      ST.irr = getIrr(ST.simH, ST.month, nf);
      const ambT = 18 + sn(ST.noiseT, .2, 3);
      const pv = getPV(ST.irr, ambT);
      const { mode, col: modeCol, pvOn } = getMode(ST.simH);
      ST.pvActive = pvOn;
      ST.pvKW = pvOn ? pv.kw : 0;
      ST.pvVmpp = pv.vmpp; ST.pvImpp = pv.impp;
      // Charger load
      ST.totalLoad = CH_STATE.filter(c => c.status === 'charging')
        .reduce((s, c) => s + c.actual_kw, 0);
      // Battery
      const deficit = ST.totalLoad - (ST.pvKW * SYS.INV_EFF);
      if (deficit > 0.5 && ST.socPct > 15) {
        ST.battDir = 'charging';
        ST.battI = Math.min(deficit * 1000 / SYS.BAT_V, 200);
        ST.socPct = Math.max(15, ST.socPct - deficit / 240 / 500 * 100);
      }
      else if (deficit < -.5 && ST.socPct < 98) {
        ST.battDir = 'discharging';
        ST.battI = Math.min(-deficit * 1000 / SYS.BAT_V, 80);
        ST.socPct = Math.min(98, ST.socPct + (-deficit) / 240 / 500 * 100 * 0.96);
      }
      else { ST.battDir = 'idle'; ST.battI = 0; }
      // Inverter
      ST.invPow = (ST.pvKW * SYS.INV_EFF +
        (ST.battDir === 'discharging' ? ST.battI * SYS.BAT_V / 1000 : 0));
      // Energy / CO2
      ST.energyKWh += ST.pvKW * (1 / 3600) * 2;
      ST.co2Kg = ST.energyKWh * 0.45;
      // History
      if (ST.tick % 5 === 0) {
        ST.histSol.push(+ST.pvKW.toFixed(1)); ST.histSol.shift();
        ST.histSoc.push(+ST.socPct.toFixed(1)); ST.histSoc.shift();
        ST.histLoad.push(+ST.totalLoad.toFixed(1)); ST.histLoad.shift();
      }
      // Update charger SoCs
      CH_STATE.forEach(ch => {
        if (ch.status !== 'charging') return;
        const cap = EV_CAPACITY_KWH[ch.kw] || (ch.ph === '3-Phase' ? 60 : 20); // kWh approx capacity
        const effectiveKw = ch.actual_kw * EV_CHARGE_SPEED_FACTOR;
        ch.soc = Math.min(100, ch.soc + (effectiveKw / cap / 3600) * 2);
        ch.elapsed_min += (2 / 60);
        if (ch.soc >= 99.5) ch.status = 'done';
      });
    }

    // ════════════════════════════════════════════════════════════
    //  UPDATE DOM
    // ════════════════════════════════════════════════════════════
    let frameN = 0;
    function updateDOM() {
      const { mode, col: modeCol, pvOn } = getMode(ST.simH);
      const simStr = fmtTime(ST.simH);
      const noise = sn(ST.noiseT, .7);
      const pvActive = pvOn;

      // ── Header ──
      document.getElementById('modeBadge').textContent = mode;
      document.getElementById('modeBadge').style.color = modeCol;
      document.getElementById('modeBadge').style.borderColor = modeCol.replace('ff', '44');
      document.getElementById('simT').textContent = simStr;
      document.getElementById('modeShort').textContent = mode.slice(0, 7);
      document.getElementById('modeShort').style.color = modeCol;

      // ── Sun ──
      const irr = Math.round(ST.irr * (1 + noise * .02));
      document.getElementById('sunIrr').textContent = pvActive ? irr : 0;
      document.getElementById('ambT').textContent = `${(18 + noise * 2).toFixed(0)}°C`;
      const sc = document.querySelector('.sc');
      if (sc) {
        const glow = pvActive ? `0 0 22px rgba(245,158,11,.7),0 0 45px rgba(245,158,11,.18)` : `0 0 6px rgba(245,158,11,.2)`;
        sc.style.boxShadow = glow;
      }

      // ── Schedule needle — real wall-clock, sweeps full 24h bar ──
      {
        const rn = new Date();
        const rH = rn.getHours() + rn.getMinutes() / 60 + rn.getSeconds() / 3600;
        // Bar = 08:00 → 08:00 next day (24h cycle). Offset from 08:00.
        const offsetH = (rH - 8 + 24) % 24;
        const fracRT = offsetH / 24;
        const timeStr = `${String(rn.getHours()).padStart(2, '0')}:${String(rn.getMinutes()).padStart(2, '0')}:${String(rn.getSeconds()).padStart(2, '0')}`;
        const n = document.getElementById('needle');
        if (n) {
          n.style.left = (fracRT * 100).toFixed(4) + '%';
          const label = document.getElementById('needleLabel');
          if (label) label.textContent = timeStr;
        }
        document.getElementById('schedStatus').textContent =
          `NOW: ${timeStr}  ·  MODE: ${mode}  ·  ${pvActive ? `PV ${ST.pvKW.toFixed(1)}kW` : 'BATTERY DISCHARGE'} → 5 EV CHARGERS`;
        document.getElementById('schedStatus').style.color = modeCol;
      }
      document.getElementById('modeBadge').textContent = mode;

      // ── PV Grid shimmer ──
      if (frameN % 3 === 0) {
        for (let s = 0; s < 11; s++) for (let m = 0; m < 10; m++) {
          const el = document.getElementById(`pvm_${s}_${m}`);
          if (!el) continue;
          if (pvActive) {
            el.classList.add('act');
            const sh = .88 + .12 * Math.sin(ST.noiseT * 1.8 + s * .28 + m * .12);
            el.style.background = `rgb(${Math.round(26 * sh)},${Math.round(35 * sh)},${Math.round(126 * sh)})`;
          }
          else { el.classList.remove('act'); el.style.background = '#101428'; }
        }
      }

      // ── String diagram opacity ──
      for (let s = 0; s < 11; s++) {
        const w = document.getElementById(`srw_${s}`);
        if (w) {
          w.style.opacity = pvActive ? .9 : .2;
          w.style.background = pvActive ? 'var(--org)' : '#333';
          w.style.color = pvActive ? 'var(--org)' : '#333';
        }
      }

      // ── PV Stats ──
      document.getElementById('pvKW').textContent = pvActive ? `${ST.pvKW.toFixed(1)}kW` : '0.0kW';
      document.getElementById('pvVmpp').textContent = pvActive ? `${ST.pvVmpp}V` : '—';
      document.getElementById('pvImpp').textContent = pvActive ? `${ST.pvImpp}A` : '0.0A';

      // ── BMS ──
      const soc = ST.socPct;
      document.getElementById('battFill').style.height = soc + '%';
      document.getElementById('battPct').textContent = Math.round(soc) + '%';
      document.getElementById('bV').textContent = `${(SYS.BAT_V * (0.95 + soc / 2000)).toFixed(0)}V`;
      document.getElementById('bI').textContent = `${ST.battI.toFixed(1)}A`;
      document.getElementById('bDir').textContent = ST.battDir.charAt(0).toUpperCase() + ST.battDir.slice(1);
      document.getElementById('bDir').style.color = ST.battDir === 'charging' ? 'var(--grn)' : ST.battDir === 'discharging' ? 'var(--org2)' : 'var(--tx3)';
      document.getElementById('bTemp').textContent = `${(32 + noise * 2).toFixed(0)}°C`;
      // Cell voltages
      const cellV = SYS.BAT_V / 8 * (0.98 + soc / 5000);
      for (let i = 0; i < 8; i++) {
        const cv2 = document.getElementById(`cv_${i}`);
        const cf = document.getElementById(`cf_${i}`);
        const dv = sn(ST.noiseT + i * .3, .5, .5);
        if (cv2) cv2.textContent = `${(cellV + dv).toFixed(1)}V`;
        if (cf) {
          cf.style.width = `${Math.max(20, soc)}%`;
          cf.style.background = soc > 50 ? 'var(--grn)' : soc > 25 ? 'var(--yel)' : 'var(--red)';
        }
      }
      drawSOCGauge(soc);

      // ── MPPT ──
      document.getElementById('mpptVin').textContent = pvActive ? `${ST.pvVmpp}V` : '—';
      document.getElementById('mpptIin').textContent = pvActive ? `${ST.pvImpp}A` : '—';
      document.getElementById('mpptPin').textContent = pvActive ? `${ST.pvKW.toFixed(1)}kW` : '0kW';

      // ── Inverter ──
      const invP = ST.invPow;
      const invI = invP * 1000 / (Math.sqrt(3) * SYS.AC_V3);
      document.getElementById('invPout').textContent = `${invP.toFixed(1)}kW`;
      document.getElementById('invVout').textContent = `${(SYS.AC_V3 + (noise * 2)).toFixed(0)}V`;
      document.getElementById('invIout').textContent = `${invI.toFixed(1)}A`;
      drawSine(invP > 1);

      // ── Smart Meter ──
      const mvVals = [
        mode.slice(0, 12), simStr,
        pvActive ? `${ST.pvKW.toFixed(1)} kW` : '0.0 kW',
        `${soc.toFixed(0)} %`,
        `${ST.totalLoad.toFixed(1)} kW`,
        `${(SYS.AC_V3 + noise * 1.5).toFixed(0)} V`,
        `${invI.toFixed(1)} A`,
        `${(50 + noise * .03).toFixed(2)} Hz`,
        `${ST.energyKWh.toFixed(0)} kWh`,
        'ON-GRID ✓',
      ];
      mvVals.forEach((v, i) => { const el = document.getElementById(`mv_${i}`); if (el) el.textContent = v; });
      // IoT last sync
      const syncEl = document.getElementById('iotr_4');
      if (syncEl) syncEl.textContent = `${(ST.tick % 120 / 10).toFixed(1)}s ago`;

      // ── Chargers ──
      let activeCount = 0;
      CH_STATE.forEach((ch, i) => {
        const isOn = ch.status === 'charging';
        if (isOn) activeCount++;
        const card = document.getElementById(`chcard_${i}`);
        const dot = document.getElementById(`chdot_${i}`);
        const pwr = document.getElementById(`chpwr_${i}`);
        const stat = document.getElementById(`chst_${i}`);
        const socf = document.getElementById(`socf_${i}`);
        const socp = document.getElementById(`socp_${i}`);
        const soce = document.getElementById(`soce_${i}`);
        const evp = document.getElementById(`evport_${i}`);
        const anim = document.getElementById(`chanim_${i}`);
        const cabling = document.getElementById(`cabling_${i}`);
        const chtime = document.getElementById(`chtime_${i}`);
        const chkwh = document.getElementById(`chkwh_${i}`);
        const pn = ch.ph === '3-Phase';
        const dotC = isOn ? 'var(--grn)' : 'var(--tx3)';
        if (dot) { dot.style.background = dotC; dot.style.boxShadow = isOn ? `0 0 7px var(--grn)` : 'none'; }
        if (card) { card.className = `chcard ${isOn ? 'act' : 'stby'}`; }
        const pval = (isOn ? ch.actual_kw : 0);
        if (pwr) {
          pwr.textContent = `${pval.toFixed(1)}`;
          pwr.style.color = isOn ? 'var(--grn)' : 'var(--red2)';
        }
        if (stat) {
          stat.textContent = isOn ? '● ACTIVE' : '○ IDLE';
          stat.style.color = isOn ? 'var(--grn)' : 'var(--tx3)';
        }
        const sc = Math.min(100, ch.soc);
        const scCol = sc > 80 ? 'var(--yel)' : sc > 40 ? 'var(--grn)' : 'var(--red)';
        if (socf) { socf.style.width = sc.toFixed(1) + '%'; socf.style.background = scCol; }
        if (socp) socp.textContent = `SoC: ${sc.toFixed(0)}%`;
        // ETA
        if (soce) {
          if (isOn && ch.actual_kw > 0) {
            const cap = EV_CAPACITY_KWH[ch.kw] || (pn ? 60 : 20); // kWh battery capacity per vehicle type
            const effectiveKw = ch.actual_kw * EV_CHARGE_SPEED_FACTOR;
            const remKWh = (100 - sc) / 100 * cap;
            const etaH = remKWh / effectiveKw * .92;
            soce.textContent = etaH < 1 / 60 ? '< 1min' : etaH < 1 ? `${Math.ceil(etaH * 60)}min` : `${etaH.toFixed(1)}h`;
          }
          else soce.textContent = '—';
        }
        if (evp) { evp.className = `ev-port ${isOn ? 'on' : 'off'}`; }
        if (anim) anim.style.display = isOn ? 'block' : 'none';
        const elMin = Math.floor(ch.elapsed_min);
        if (chtime) chtime.textContent = `⏱ ${elMin}min`;
        const sessionKwh = (ch.elapsed_min / 60) * ch.actual_kw * .92;
        if (chkwh) chkwh.textContent = `⚡ ${sessionKwh.toFixed(1)} kWh`;
        if (cabling) cabling.textContent = `${sessionKwh.toFixed(1)} kWh`;
      });
      const badge = document.getElementById('activeBadge');
      if (badge) badge.textContent = `${activeCount} ACTIVE`;

      // ── KPI strip ──
      document.getElementById('kSol').textContent = pvActive ? ST.pvKW.toFixed(1) : '0.0';
      document.getElementById('kBat').textContent = Math.round(soc);
      document.getElementById('kLoad').textContent = ST.totalLoad.toFixed(1);
      document.getElementById('kCO2').textContent = ST.co2Kg.toFixed(1);
      document.getElementById('kEff').textContent = (SYS.INV_EFF * 100).toFixed(1);
      document.getElementById('kGen').textContent = ST.energyKWh.toFixed(1);

      // ── Sparklines ──
      const spks = [
        ['spkSol', sparkBufs.sol, ST.pvKW, '#f59e0b'],
        ['spkBat', sparkBufs.bat, soc, '#22c55e'],
        ['spkLoad', sparkBufs.load, ST.totalLoad, '#60a5fa'],
        ['spkCO2', sparkBufs.co2, ST.co2Kg, '#4ade80'],
        ['spkEff', sparkBufs.eff, SYS.INV_EFF * 100, '#c084fc'],
        ['spkGen', sparkBufs.gen, ST.energyKWh, '#22d3ee'],
      ];
      spks.forEach(([id, buf, v, c]) => { buf.push(v); if (buf.length > 20) buf.shift(); drawSparkline(id, buf, c); });
    }

    // ════════════════════════════════════════════════════════════
    //  CLOCK
    // ════════════════════════════════════════════════════════════
    function updateClock() {
      const n = new Date();
      const h = String(n.getHours()).padStart(2, '0');
      const m = String(n.getMinutes()).padStart(2, '0');
      const s = String(n.getSeconds()).padStart(2, '0');
      const el = document.getElementById('clock');
      if (el) el.textContent = `${h}:${m}:${s}`;
      const de = document.getElementById('dateTxt');
      if (de) de.textContent = n.toLocaleDateString('en-GB',
        { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' }).toUpperCase();
    }

    // ════════════════════════════════════════════════════════════
    //  MAIN LOOP
    // ════════════════════════════════════════════════════════════
    let lastSim = 0, lastChart = 0, lastDom = 0;
    function loop(ts) {
      frameN++;
      if (ts - lastSim > 250) { simTick(); lastSim = ts; }
      if (ts - lastDom > 100) { updateDOM(); lastDom = ts; }
      if (ts - lastChart > 2000) { drawPowerChart(); lastChart = ts; }
      requestAnimationFrame(loop);
    }

    // ════════════════════════════════════════════════════════════
    //  BOOT
    // ════════════════════════════════════════════════════════════
    window.addEventListener('DOMContentLoaded', () => {
      buildPVGrid();
      buildStrDiag();
      buildMPPTChannels();
      buildCells();
      buildMeterRows();
      buildIoTRows();
      buildMCBList();
      buildChargers();
      // Seed simulation
      for (let i = 0; i < 60; i++) simTick();
      updateClock();
      setInterval(updateClock, 1000);
      drawSOCGauge(ST.socPct);
      updateDOM();
      drawPowerChart();
      requestAnimationFrame(loop);
      console.log('════════════════════════════════════════');
      console.log('  SOLAR EV STATION DASHBOARD — LIVE ✓');
      console.log('  Engineer: Hermes MUGISHA');
      console.log('  120.1kWp · 640kWh LFP · 5 Chargers');
      console.log('  CH1/2: 7kW AC | CH3/4: 22kW AC | CH5: 40kW DC Fast');
      console.log('  Total Peak Load: 98 kW');
      console.log('  Kigali City · Rwanda E-Mobility 2026');
      console.log('  Presented to: MININFRA');
      console.log('════════════════════════════════════════');
    });
  </script>
</body>

</html>
"""s
╔══════════════════════════════════════════════════════════════════════════════╗
║  SOLAR MOTORCYCLE CHARGING STATION  ·  AMPERSAND E-MOBILITY                ║
║  Engineer : Hermes MUGISHA  ·  Energy Engineer                               ║
║  Project  : Solar-Powered Motorcycle Battery Swap Station — Rwanda 2026     ║
║─────────────────────────────────────────────────────────────────────────────║
║  ENERGY FLOW (LEFT → RIGHT):                                                 ║
║  SUN → PV ARRAY (95×585W=55.52kWp) → COMBINER → MPPT CONTROLLER             ║
║                         ↕ BATTERY (LFP 96V/2900Ah = 278kWh)                ║
║  OFF-GRID INVERTER (60kW 3-Ph) → MCB PANEL → 10 MOTO CHARGERS → 10 MOTOS  ║
║─────────────────────────────────────────────────────────────────────────────║
║  PV Array  : 95× Jinko Tiger Neo 585W = 55.52 kWp                            ║
║              5 strings × 19 modules  Vmpp=451V  Impp=48.8A                  ║
║  Battery   : LFP 96V/2900Ah = 278kWh (Buffer: 06-08h & 17-20h)             ║
║  MPPT      : 60kW · 5-channel · Eff=98.5%                                   ║
║  Inverter  : Off-Grid 3-Phase 55.52kW 400V/50Hz Eff=96%                        ║
║  DB Panel  : MCCB 150A + 10×MCB 25A (one per motorcycle)                    ║
║  Chargers  : 10× Ampersand Fast-Swap 4.5kW/230V/20A                        ║
║  Active Load: 45 kW (10 motorcycles charging simultaneously)                ║
║─────────────────────────────────────────────────────────────────────────────║
║  HOW TO RUN:                                                                 ║
║    pip install matplotlib numpy                                              ║
║    python ampersand_solar_moto_station.py                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import matplotlib
try:
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    plt.figure(); plt.close()
except Exception:
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

import matplotlib.patches    as mpatches
import matplotlib.patheffects as pe
import numpy                  as np
from matplotlib.patches      import FancyBboxPatch, Arc
from matplotlib.animation    import FuncAnimation
from datetime                 import datetime

# ══════════════════════════════════════════════════════════════
#  SYSTEM CONSTANTS — AMPERSAND SOLAR MOTO STATION
# ══════════════════════════════════════════════════════════════
NUM_MODULES   = 95
MOD_POWER_W   = 585
PV_KWP        = NUM_MODULES * MOD_POWER_W / 1000        # 55.525 kWp
MOD_VMPP      = 41.0
MOD_IMPP      = 9.76
MOD_VOC       = 48.9
MODS_PER_STR  = 19
NUM_STRINGS   = 5
STR_VMPP      = MOD_VMPP * MODS_PER_STR                 # 451.0 V
STR_VOC       = MOD_VOC  * MODS_PER_STR                 # 537.9 V
ARR_IMPP      = MOD_IMPP * NUM_STRINGS                  # 48.80 A
ARR_KW        = PV_KWP                                   # 55.52 kW

BAT_V         = 96
BAT_AH        = 2900
BAT_KWH       = BAT_V * BAT_AH / 1000                   # 278.4 kWh
BAT_DOD       = 0.85
BAT_USABLE    = BAT_KWH * BAT_DOD                        # 236.6 kWh
BAT_SOC       = 78

MPPT_EFF      = 0.985
MPPT_KW       = 60

INV_KW        = 60
INV_EFF       = 0.960
AC_V3         = 400
AC_V1         = 230
AC_HZ         = 50
INV_IOUT      = INV_KW * 1000 / (np.sqrt(3) * AC_V3)   # 86.6 A

MCCB_A        = 150
MCB_A         = 25

N_MOTOS       = 10
KW_PER_MOTO   = 4.5
TOTAL_LOAD    = N_MOTOS * KW_PER_MOTO                   # 45 kW

# Motorcycle states — mix of charging / ready / swapping
MOTO_STATES = [
    {"id":i+1,"soc":soc,"status":st,"color":col,"name":f"MOTO-{i+1:02d}"}
    for i,(soc,st,col) in enumerate([
        (88, "CHARGED",  "#1b4332"),
        (42, "CHARGING", "#0d3b7a"),
        (15, "CHARGING", "#4a1080"),
        (67, "CHARGING", "#14451a"),
        (95, "CHARGED",  "#1b4332"),
        (33, "CHARGING", "#7a1a05"),
        (78, "CHARGING", "#0d3b7a"),
        (55, "CHARGING", "#3a1a05"),
        (100,"READY",    "#1b4332"),
        (22, "CHARGING", "#4a1080"),
    ])
]

# ══════════════════════════════════════════════════════════════
#  CANVAS  (wide landscape for 10 motorcycles)
# ══════════════════════════════════════════════════════════════
W, H = 52, 18
fig  = plt.figure(figsize=(W, H), facecolor='#060d1a')
fig.patch.set_facecolor('#060d1a')
ax   = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_facecolor('#060d1a')
ax.axis('off')
try:
    fig.canvas.manager.set_window_title(
        "Ampersand Solar Moto Charging Station — 55.52kWp — 45kW — Rwanda 2026 — Eng. Hermes MUGISHA")
except Exception:
    pass

# Sky gradient (dawn orange hints — Ampersand brand feel)
for i in range(180):
    t = i / 180
    r = int(8  + t * 16)
    g = int(14 + t * 20)
    b = int(24 + t * 42)
    ax.axhspan(i * H / 180, (i + 1) * H / 180,
               color=(r/255, g/255, b/255), zorder=0, alpha=0.75)

# Ground strip
ax.add_patch(mpatches.Rectangle((0, 0),   W, 1.55, color='#0d1f0d', zorder=1))
ax.add_patch(mpatches.Rectangle((0, 1.40), W, 0.38, color='#1a3a1a', zorder=1))

# Station ground markings (parking bays)
for bi in range(10):
    bx = 27.80 + bi * 2.40
    ax.add_patch(mpatches.Rectangle((bx, 1.55), 2.15, 0.06,
                 color='#ffd600', alpha=0.5, zorder=2))

# Subtle grid
for gx in np.arange(0, W, 1.4):
    ax.plot([gx, gx], [0, H], color='#0e2040', lw=0.15, alpha=0.15, zorder=1)
for gy in np.arange(0, H, 1.4):
    ax.plot([0, W], [gy, gy], color='#0e2040', lw=0.15, alpha=0.15, zorder=1)

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════
def box(x, y, w, h, fc='#0d1f33', ec='#29b6f6', lw=2.0, r=0.15, z=8, a=1.0):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={r}',
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z, alpha=a)
    ax.add_patch(p); return p

def txt(x, y, s, sz=7.0, c='#cfd8dc', ha='center', va='center',
        bold=False, mono=False, z=11, a=1.0):
    ax.text(x, y, s, ha=ha, va=va, fontsize=sz, color=c, alpha=a,
            fontweight='bold' if bold else 'normal', zorder=z,
            fontfamily='monospace' if mono else 'sans-serif')

def sbar(x, y, w, h, pct, col='#00e676', z=12):
    ax.add_patch(mpatches.Rectangle((x, y), w, h, color='#1a1a2a', zorder=z))
    fc = col if pct < 80 else ('#ffeb3b' if pct < 95 else '#00e676')
    ax.add_patch(mpatches.Rectangle((x, y), w * pct / 100, h, color=fc, zorder=z+1))
    ax.text(x+w/2, y+h/2, f'{pct:.0f}%', ha='center', va='center',
            fontsize=5.5, color='white', fontweight='bold',
            fontfamily='monospace', zorder=z+2)

def arrow(x0, y0, x1, y1, c='#ff9800', lw=2.5, z=8):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=c, lw=lw), zorder=z)

def biarrow(x0, y0, x1, y1, c='#4caf50', lw=2.5, z=8):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='<->', color=c, lw=lw), zorder=z)

def tag(x, y, s, fc='#1a0d00', c='#ffb74d', sz=6.0, z=9):
    ax.text(x, y, s, ha='center', va='center', fontsize=sz, color=c,
            fontweight='bold', zorder=z,
            bbox=dict(boxstyle='round,pad=0.18', facecolor=fc, alpha=0.90, edgecolor='none'))

# ══════════════════════════════════════════════════════════════
#  1.  SUN
# ══════════════════════════════════════════════════════════════
SX, SY = 1.20, 12.20
ax.add_patch(plt.Circle((SX, SY), 0.72, color='#FFD700', zorder=6))
ax.add_patch(plt.Circle((SX, SY), 0.95, color='#FFD700', alpha=0.20, zorder=5))
ax.add_patch(plt.Circle((SX, SY), 1.18, color='#FFD700', alpha=0.07, zorder=4))
sun_glow = plt.Circle((SX, SY), 0.95, color='#FFD700', alpha=0.18, zorder=5)
ax.add_patch(sun_glow)
for ang in np.linspace(0, 360, 18, endpoint=False):
    r = np.radians(ang)
    ax.plot([SX+1.02*np.cos(r), SX+1.46*np.cos(r)],
            [SY+1.02*np.sin(r), SY+1.46*np.sin(r)],
            color='#FFD700', lw=2.2, zorder=6, alpha=0.82)
ax.text(SX, SY, '☀', ha='center', va='center',
        fontsize=14, color='#FF6F00', fontweight='bold', zorder=7)
for dy, s, c, b in [
    (-1.55,'SOLAR IRRADIANCE','#FFD700',True),
    (-1.88,'1000 W/m²  |  AM1.5','#FFA000',False),
    (-2.16,'Kigali · PSH=4.8h/day','#FFB300',False),
    (-2.44,f'Array: {PV_KWP:.1f} kWp','#ffcc02',True),
]:
    ax.text(SX, SY+dy, s, ha='center', fontsize=6.8 if b else 6.0,
            color=c, fontweight='bold' if b else 'normal', zorder=7)

# ══════════════════════════════════════════════════════════════
#  2.  PV ARRAY  (5 strings × 19 modules = 95 modules · 5 rows × 19 cols)
# ══════════════════════════════════════════════════════════════
PV_X, PV_Y  = 2.60, 5.70
PMW, PMH    = 0.78, 0.58
GAPC, GAPR  = 0.06, 0.06
COLS, ROWS  = 19, 5

pv_patches = []
for row in range(ROWS):
    for col in range(COLS):
        px = PV_X + col*(PMW+GAPC)
        py = PV_Y + row*(PMH+GAPR)
        p  = ax.add_patch(mpatches.Rectangle(
               (px, py), PMW, PMH,
               facecolor='#1a237e', edgecolor='#42a5f5',
               linewidth=0.9, zorder=8))
        pv_patches.append(p)
        for ci in range(3):
            for ri in range(2):
                ax.add_patch(mpatches.Rectangle(
                    (px+0.04+ci*0.225, py+0.05+ri*0.215),
                    0.190, 0.165,
                    facecolor='#283593', edgecolor='#5c6bc0',
                    linewidth=0.20, zorder=9))
        ax.text(px+PMW/2, py+PMH-0.10, 'JINKO',
                ha='center', fontsize=3.6, color='#90caf9',
                fontweight='bold', zorder=10)
        ax.text(px+PMW/2, py+0.08, '585W',
                ha='center', fontsize=3.4, color='#64b5f6', zorder=10)
    py_r = PV_Y + row*(PMH+GAPR)
    ax.text(PV_X-0.30, py_r+PMH/2, f'S{row+1}',
            ha='center', va='center', fontsize=5.8,
            color='#ff9800', fontweight='bold', zorder=11)

# Mounting poles
for col in range(COLS):
    px = PV_X + col*(PMW+GAPC) + PMW/2
    ax.plot([px, px-0.08], [PV_Y, PV_Y-0.48], color='#757575', lw=1.6, zorder=7)
    ax.plot([px-0.08, px-0.08], [PV_Y-0.48, 1.62], color='#616161', lw=1.2, zorder=7)

# Irradiance arrows
for col in [2, 5, 9]:
    for row in [1, 3]:
        if row < ROWS:
            sx = PV_X + col*(PMW+GAPC) + PMW/2
            sy = PV_Y + row*(PMH+GAPR) + PMH
            ax.annotate('', xy=(sx-0.04, sy+0.08),
                        xytext=(sx-0.48, sy+0.68),
                        arrowprops=dict(arrowstyle='->', color='#FFD700',
                                        lw=1.3, alpha=0.65), zorder=8)

# PV title box
PV_RIGHT  = PV_X + COLS*(PMW+GAPC)
PV_TOP_Y  = PV_Y + ROWS*(PMH+GAPR) + 0.10
PV_TITLE_W = COLS*(PMW+GAPC) + 0.28
box(PV_X-0.36, PV_TOP_Y, PV_TITLE_W, 1.00,
    fc='#0d1f33', ec='#42a5f5', lw=1.5, z=10)
txt(PV_X+COLS*(PMW+GAPC)/2-0.04, PV_TOP_Y+0.68,
    f'JINKO TIGER NEO  ·  {PV_KWP:.1f} kWp  —  AMPERSAND STATION PV ARRAY',
    sz=9.5, c='#42a5f5', bold=True, z=11)
txt(PV_X+COLS*(PMW+GAPC)/2-0.04, PV_TOP_Y+0.30,
    f'{NUM_MODULES} Mods  ·  {NUM_STRINGS} Strings×{MODS_PER_STR}  ·  '
    f'Vmpp={STR_VMPP:.0f}V  ·  Voc={STR_VOC:.0f}V  ·  Impp={ARR_IMPP:.1f}A  ·  Pmpp={ARR_KW:.1f}kW',
    sz=7.0, c='#90caf9', mono=True, z=11)

# ══════════════════════════════════════════════════════════════
#  3.  STRING COMBINER
# ══════════════════════════════════════════════════════════════
CB_X, CB_Y = PV_RIGHT+1.00, 6.00
CB_W, CB_H = 1.80, 4.90

box(CB_X, CB_Y, CB_W, CB_H, fc='#111f11', ec='#4caf50', lw=2.2, z=9)
txt(CB_X+CB_W/2, CB_Y+CB_H+0.22, 'STRING\nCOMBINER', sz=8.0, c='#4caf50', bold=True, z=10)
txt(CB_X+CB_W/2, CB_Y+CB_H-0.20, '+ DC DISCONNECT', sz=6.5, c='#81c784', z=10)

FSTEP = (CB_H-0.50)/NUM_STRINGS
for si in range(NUM_STRINGS):
    fy = CB_Y+0.26+si*FSTEP
    ax.add_patch(mpatches.Rectangle((CB_X+0.14, fy), 0.50, 0.24,
                 facecolor='#1b5e20', edgecolor='#4caf50', lw=0.7, zorder=11))
    ax.text(CB_X+0.39, fy+0.12, f'F{si+1}  16A', ha='center', va='center',
            fontsize=4.6, color='#a5d6a7', fontfamily='monospace', zorder=12)
    ax.add_patch(plt.Circle((CB_X+1.58, fy+0.12), 0.062, color='#00e676', zorder=12))
txt(CB_X+CB_W/2, CB_Y+0.14,
    f'DC {STR_VMPP:.0f}V / {ARR_IMPP:.0f}A',
    sz=6.0, c='#c8e6c9', mono=True, z=11)

arrow(PV_RIGHT, PV_Y+ROWS*(PMH+GAPR)/2, CB_X, CB_Y+CB_H*0.55, c='#ff9800', lw=2.8)
tag((PV_RIGHT+CB_X)/2, PV_Y+ROWS*(PMH+GAPR)/2+0.28,
    f'DC {STR_VMPP:.0f}V/{ARR_IMPP:.0f}A')

# ══════════════════════════════════════════════════════════════
#  4.  MPPT CHARGE CONTROLLER  60kW · 5-channel
# ══════════════════════════════════════════════════════════════
MX, MY = CB_X+CB_W+0.90, 6.00
MW, MH = 2.10, 4.90

box(MX, MY, MW, MH, fc='#0d2233', ec='#29b6f6', lw=2.2, z=9)
txt(MX+MW/2, MY+MH+0.22, 'MPPT SOLAR', sz=8.0, c='#29b6f6', bold=True, z=10)
txt(MX+MW/2, MY+MH-0.20, f'CTRL  {MPPT_KW}kW  5-CH', sz=6.8, c='#81d4fa', z=10)

ax.add_patch(mpatches.Rectangle((MX+0.12, MY+2.85), MW-0.24, 1.74,
             facecolor='#001400', edgecolor='#2e7d32', lw=0.9, zorder=11))
mppt_lcd = []
for li, ln in enumerate([
    f'Vin : {STR_VMPP:.0f} V',
    f'Iin : {ARR_IMPP:.1f} A',
    f'Pin : {ARR_KW:.1f} kW',
    f'Vout: {BAT_V} V DC',
    f'Eff : {MPPT_EFF*100:.1f}%',
]):
    t = ax.text(MX+MW/2, MY+4.36-li*0.30, ln, ha='center', va='center',
                fontsize=5.6, color='#00ff41', fontfamily='monospace', zorder=12)
    mppt_lcd.append(t)

for chi, (mc, ml) in enumerate([('#00e676','CH1'),('#00bcd4','CH2'),('#ffea00','CH3'),
                                  ('#ff9800','CH4'),('#ce93d8','CH5')]):
    ax.add_patch(plt.Circle((MX+0.30+chi*0.36, MY+2.65), 0.082, color=mc, zorder=12))

for li, ln in enumerate([
    '5-Channel String MPPT',
    f'Max: 600V / 60A each',
    f'Out: {BAT_V}V DC → Battery',
    f'Eff: {MPPT_EFF*100:.1f}%  IEC 62109',
]):
    txt(MX+MW/2, MY+2.26-li*0.32, ln, sz=5.6, c='#80deea', mono=True, z=11)

arrow(CB_X+CB_W, CB_Y+CB_H/2, MX, MY+MH/2, c='#ff9800', lw=2.8)
tag((CB_X+CB_W+MX)/2, CB_Y+CB_H/2+0.26, f'DC {STR_VMPP:.0f}V/{ARR_IMPP:.0f}A')

# ══════════════════════════════════════════════════════════════
#  5.  BATTERY  LFP 96V/2900Ah = 278kWh
# ══════════════════════════════════════════════════════════════
BX, BY = MX-0.05, 1.72
BW, BH = MW+0.10, 3.68

box(BX, BY, BW, BH, fc='#091a09', ec='#66bb6a', lw=2.2, z=9)
txt(BX+BW/2, BY+BH+0.22, 'BATTERY ENERGY STORAGE', sz=8.0, c='#66bb6a', bold=True, z=10)
txt(BX+BW/2, BY+BH-0.20, f'LFP {BAT_V}V/{BAT_AH}Ah = {BAT_KWH:.0f}kWh', sz=6.8, c='#a5d6a7', z=10)

# 6 battery modules (3×2)
BKW, BKH = 0.60, 0.54
bat_fills = []
for bi in range(6):
    bkc = bi % 3; bkr = bi // 3
    bkx = BX+0.14+bkc*(BKW+0.10)
    bky = BY+0.24+bkr*(BKH+0.12)
    ax.add_patch(mpatches.Rectangle((bkx, bky), BKW, BKH,
                 facecolor='#1b5e20', edgecolor='#4caf50', lw=0.8, zorder=11))
    fill = ax.add_patch(mpatches.Rectangle(
        (bkx+0.03, bky+0.03), (BKW-0.06)*BAT_SOC/100, BKH-0.06,
        color='#43a047', zorder=12))
    bat_fills.append(fill)
    ax.text(bkx+BKW/2, bky+BKH/2, f'M{bi+1}', ha='center', va='center',
            fontsize=5.0, color='white', fontweight='bold', zorder=13)
    ax.add_patch(mpatches.Rectangle((bkx+BKW-0.08, bky+0.14), 0.06, 0.26,
                 color='#9e9e9e', zorder=13))

sbar(BX+0.14, BY+BH-0.50, BW-0.28, 0.28, BAT_SOC, z=12)
bat_src_txt = ax.text(BX+BW/2, BY+0.14, '⏱ Buffer: 06-08h & 17-20h',
                      ha='center', fontsize=6.2, color='#fff176',
                      fontweight='bold', zorder=11)

biarrow(MX+MW/2, MY, BX+BW/2, BY+BH, c='#66bb6a', lw=2.5)
tag(MX+MW/2-0.78, (MY+BY+BH)/2, f'{BAT_V}V DC\nCharge/Discharge',
    fc='#0a1f0a', c='#a5d6a7', sz=5.8)

# ══════════════════════════════════════════════════════════════
#  6.  OFF-GRID 3-PHASE 60kW INVERTER
# ══════════════════════════════════════════════════════════════
IX, IY = MX+MW+0.90, 3.50
IW, IH = 2.80, 7.80

box(IX, IY, IW, IH, fc='#150a2e', ec='#ce93d8', lw=2.5, z=9)
txt(IX+IW/2, IY+IH+0.22, 'OFF-GRID  INVERTER', sz=9.0, c='#ce93d8', bold=True, z=10)
txt(IX+IW/2, IY+IH-0.20, f'3-PHASE  ·  {INV_KW} kW', sz=8.0, c='#e1bee7', bold=True, z=10)

ax.add_patch(mpatches.Rectangle((IX+0.12, IY+5.40), IW-0.24, 2.05,
             facecolor='#0a0018', edgecolor='#7b1fa2', lw=1.0, zorder=11))
inv_lcd = []
for li, ln in enumerate([
    f'DC IN : {BAT_V}V / {ARR_IMPP:.0f}A',
    f'P_in  : {ARR_KW:.1f} kW',
    f'AC OUT: {AC_V3}V / {AC_HZ}Hz',
    f'P_out : {TOTAL_LOAD:.0f} kW',
    f'I_out : {INV_IOUT:.1f} A (3-Ph)',
    f'Eff   : {INV_EFF*100:.0f}%  THD<3%',
]):
    t = ax.text(IX+IW/2, IY+7.20-li*0.30, ln, ha='center', va='center',
                fontsize=5.8, color='#ce93d8', fontfamily='monospace', zorder=12)
    inv_lcd.append(t)

t_s = np.linspace(0, 4*np.pi, 120)
xs  = IX+0.18+(IW-0.36)*t_s/(4*np.pi)
for ph, clr in [(0,'#f44336'),(2*np.pi/3,'#ffeb3b'),(4*np.pi/3,'#2196f3')]:
    ax.plot(xs, IY+4.90+0.36*np.sin(t_s+ph), color=clr, lw=1.3, zorder=12, alpha=0.92)
txt(IX+IW/2, IY+4.42, '3-Phase AC  L1 / L2 / L3', sz=5.8, c='#b39ddb', z=12)

for si, ss in enumerate([
    f'Rated: {INV_KW}kW / {INV_KW/0.8:.0f}kVA  Off-Grid',
    f'Input: {BAT_V}V DC Battery',
    f'Output: 3Ph {AC_V3}V + 1Ph {AC_V1}V',
    f'Surge: {INV_KW*1.5:.0f}kW  (60s)',
    f'IP65  ·  IEC 62109  ·  CE',
]):
    txt(IX+IW/2, IY+3.92-si*0.32, ss, sz=5.6, c='#d1c4e9', mono=True, z=11)

for fi in range(10):
    ax.add_patch(mpatches.Rectangle((IX-0.26, IY+0.28+fi*0.70),
                 0.18, 0.52, facecolor='#37474f', edgecolor='#546e7a', lw=0.4, zorder=10))

arrow(MX+MW, MY+MH/2, IX, IY+IH*0.62, c='#ff9800', lw=2.8)
tag((MX+MW+IX)/2, MY+MH/2+0.28, f'DC {BAT_V}V/{ARR_IMPP:.0f}A={ARR_KW:.0f}kW')
biarrow(BX+BW, BY+BH*0.65, IX, IY+0.85, c='#66bb6a', lw=2.5)
tag((BX+BW+IX)/2, BY+BH*0.65+0.28, f'{BAT_V}V Backup/Charge',
    fc='#0a1f0a', c='#a5d6a7', sz=5.8)

# ══════════════════════════════════════════════════════════════
#  7.  MCBs DISTRIBUTION BOARD
# ══════════════════════════════════════════════════════════════
DBX, DBY = IX+IW+0.90, 4.60
DBW = 2.45
MCB_ROW_H = 0.72
DBH = 1.20 + 2*MCB_ROW_H + 10*0.58 + 0.30

box(DBX, DBY, DBW, DBH, fc='#141208', ec='#ffd600', lw=2.5, z=9)
txt(DBX+DBW/2, DBY+DBH+0.22, 'DISTRIBUTION BOARD', sz=8.5, c='#ffd600', bold=True, z=10)
txt(DBX+DBW/2, DBY+DBH-0.20, f'MCCB {MCCB_A}A + {N_MOTOS}×MCB {MCB_A}A', sz=6.8, c='#fff176', z=10)

# MCCB main
box(DBX+0.12, DBY+DBH-1.16, DBW-0.24, 0.88,
    fc='#1a0000', ec='#f44336', lw=1.6, r=0.07, z=11)
txt(DBX+DBW/2, DBY+DBH-0.76, f'MCCB  {MCCB_A}A  —  MAIN  3-Phase',
    sz=7.2, c='#ef9a9a', bold=True, z=12)
txt(DBX+DBW/2, DBY+DBH-1.02, 'IEC 60947  |  Breaking: 36kA',
    sz=5.6, c='#ef9a9a', mono=True, z=12)
ax.add_patch(FancyBboxPatch((DBX+DBW-0.58, DBY+DBH-1.00),
             0.40, 0.36, boxstyle='round,pad=0.03',
             facecolor='#1b5e20', edgecolor='#4caf50', lw=1.0, zorder=13))
txt(DBX+DBW-0.38, DBY+DBH-0.82, 'ON', sz=6.0, c='white', bold=True, z=14)

# Bus bar
ax.add_patch(mpatches.Rectangle((DBX+0.12, DBY+0.10), DBW-0.24, 0.26,
             facecolor='#1a1a00', edgecolor='#ffd600', lw=0.8, zorder=11))
for bi, (bc, bl) in enumerate([('#f44336','L1'),('#ffeb3b','L2'),('#2196f3','L3'),('#78909c','N')]):
    bx2 = DBX+0.16+bi*0.54
    ax.add_patch(mpatches.Rectangle((bx2, DBY+0.12), 0.44, 0.16,
                 facecolor=bc, edgecolor='none', zorder=12, alpha=0.7))
    txt(bx2+0.22, DBY+0.20, bl, sz=4.8, c='white', bold=True, z=13)

# 10 MCB rows (one per motorcycle)
mcb_tops = []
mcb_toggles = []
moto_colors = ['#4fc3f7','#4fc3f7','#ff7043','#ff7043','#66bb6a',
               '#ce93d8','#ff9800','#4fc3f7','#66bb6a','#ff7043']
for mi in range(N_MOTOS):
    mc = moto_colors[mi]
    my2 = DBY+DBH-2.28-mi*0.58
    ax.add_patch(FancyBboxPatch((DBX+0.12, my2), DBW-0.24, 0.50,
                 boxstyle='round,pad=0.04',
                 facecolor='#141414', edgecolor=mc, lw=0.9, zorder=11))
    txt(DBX+0.28, my2+0.25, f'MCB-{mi+1:02d}', sz=6.5, c=mc, bold=True, ha='left', z=12)
    txt(DBX+0.90, my2+0.25, f'MOTO-{mi+1:02d}  {KW_PER_MOTO}kW', sz=5.6, c='#cfd8dc',
        ha='left', mono=True, z=12)
    txt(DBX+DBW-0.42, my2+0.25, f'{MCB_A}A', sz=5.8, c='white', bold=True, z=12)
    tog = ax.add_patch(FancyBboxPatch((DBX+DBW-0.60, my2+0.06),
                       0.38, 0.36, boxstyle='round,pad=0.02',
                       facecolor='#1b5e20', edgecolor='#4caf50', lw=0.8, zorder=13))
    ton = ax.text(DBX+DBW-0.41, my2+0.24, 'ON',
                  ha='center', va='center', fontsize=5.2,
                  color='white', fontweight='bold', zorder=14)
    mcb_toggles.append((tog, ton))
    mcb_tops.append(my2+0.50)

arrow(IX+IW, IY+IH*0.58, DBX, DBY+DBH*0.52, c='#ce93d8', lw=3.0)
tag((IX+IW+DBX)/2, IY+IH*0.58+0.28, f'3Ph {AC_V3}V/{AC_HZ}Hz · {TOTAL_LOAD}kW',
    fc='#1a0033', c='#ce93d8', sz=6.2)

# ══════════════════════════════════════════════════════════════
#  8.  10 MOTORCYCLE CHARGER BAYS
# ══════════════════════════════════════════════════════════════
BAY_X0 = DBX+DBW+0.65
BAY_W  = 2.12
BAY_H  = 10.50
BAY_GAP = 0.06
MOTO_Y  = 1.60

# Station canopy
ax.add_patch(FancyBboxPatch((BAY_X0-0.30, BAY_Y := MOTO_Y+4.0),
             N_MOTOS*(BAY_W+BAY_GAP)+0.50, 0.28,
             boxstyle='round,pad=0.06',
             facecolor='#1a1a0d', edgecolor='#ffd600', lw=1.5, zorder=6, alpha=0.8))
ax.add_patch(FancyBboxPatch((BAY_X0-0.30, BAY_Y-0.05),
             N_MOTOS*(BAY_W+BAY_GAP)+0.50, 0.30,
             boxstyle='round,pad=0.02',
             facecolor='#ff6d00', edgecolor='none', lw=0, zorder=7, alpha=0.85))
txt((BAY_X0-0.30 + BAY_X0+N_MOTOS*(BAY_W+BAY_GAP)+0.20)/2,
    BAY_Y+0.42,
    '⚡  AMPERSAND SOLAR MOTORCYCLE CHARGING STATION  ·  10 BAY  ·  45kW ACTIVE',
    sz=10.0, c='white', bold=True, z=8)

ch_patches_all = []
ev_patches_all = []
moto_wheel_all = []

for mi, moto in enumerate(MOTO_STATES):
    bx = BAY_X0 + mi*(BAY_W+BAY_GAP)
#HORIZONTAL AC BUS - MAIN DISTRIBUTION TO ALL CHARGERS 
# Main horizontal bus from DB to all chargers
    ax.plot([DBX+DBW+0.40, BAY_X0+N_MOTOS*(BAY_W+BAY_GAP)+0.30],
        [BAY_Y, BAY_Y],
        color='#ce93d8', lw=3.5, zorder=6, alpha=0.85,
        path_effects=[pe.Stroke(linewidth=5.0, foreground='000000', alpha=0.40),
                      pe.Normal()])
    st = moto["status"]
    col = {'CHARGING':'#29b6f6','CHARGED':'#66bb6a','READY':'#ffd600'}.get(st,'#546e7a')
    on  = st == "CHARGING"

    # Charger column unit
    box(bx, MOTO_Y+2.20, BAY_W, 1.90, fc='#080e1c', ec=col, lw=1.8, r=0.12, z=9)

    # Screen
    scr = ax.add_patch(mpatches.Rectangle(
            (bx+0.08, MOTO_Y+2.72), BAY_W-0.16, 1.22,
            facecolor='#0a2a0a' if on else '#1a1a00',
            edgecolor='#2e7d32' if on else '#555', lw=0.7, zorder=11))
    s_stat = ax.text(bx+BAY_W/2, MOTO_Y+3.68, st,
                     ha='center', fontsize=5.8,
                     color='#00ff88' if on else col,
                     fontweight='bold', fontfamily='monospace', zorder=12)
    s_pwr = ax.text(bx+BAY_W/2, MOTO_Y+3.36,
                    f'P={KW_PER_MOTO}kW' if on else f'P=0kW',
                    ha='center', fontsize=7.5,
                    color='#69f0ae' if on else '#ff8a80',
                    fontweight='bold', zorder=12)
    ax.text(bx+BAY_W/2, MOTO_Y+3.06, f'{AC_V1}V · {MCB_A}A',
            ha='center', fontsize=5.4, color='#80deea',
            fontfamily='monospace', zorder=12)
    ax.text(bx+BAY_W/2, MOTO_Y+2.80, moto["name"],
            ha='center', fontsize=5.2, color='#b2dfdb',
            fontfamily='monospace', zorder=12)

    # SoC bar on charger
    ax.add_patch(mpatches.Rectangle((bx+0.10, MOTO_Y+2.44),
                 BAY_W-0.20, 0.22, color='#1a1a2a', zorder=12))
    s_soc = ax.add_patch(mpatches.Rectangle((bx+0.10, MOTO_Y+2.44),
                          (BAY_W-0.20)*moto["soc"]/100, 0.22,
                          color='#00e676', zorder=13))
    s_slbl = ax.text(bx+BAY_W/2, MOTO_Y+2.55, f'{moto["soc"]:.0f}%',
                     ha='center', va='center', fontsize=5.0,
                     color='white', fontweight='bold', zorder=14)

    # Charging cable
    ax.plot([bx+BAY_W/2, bx+BAY_W/2], [MOTO_Y+2.20, MOTO_Y+1.88],
            color=col, lw=1.4, ls='--', zorder=8, alpha=0.75)

    # ── MOTORCYCLE body ──────────────────────────────
    mc = moto["color"]
    # Body
    mb = ax.add_patch(FancyBboxPatch(
           (bx+0.12, MOTO_Y+0.75), BAY_W-0.24, 0.82,
           boxstyle='round,pad=0.07',
           facecolor=mc, edgecolor='#b0bec5', lw=1.0, zorder=9))
    # Tank / seat hump
    ax.add_patch(FancyBboxPatch((bx+0.35, MOTO_Y+1.14), BAY_W-0.70, 0.52,
                 boxstyle='round,pad=0.05',
                 facecolor=mc, edgecolor='#90a4ae', lw=0.7, zorder=10))
    # Handlebars
    ax.add_patch(mpatches.Rectangle((bx+0.12, MOTO_Y+1.54), 0.22, 0.06,
                 color='#757575', zorder=11, angle=-10))
    ax.add_patch(mpatches.Rectangle((bx+BAY_W-0.34, MOTO_Y+1.54), 0.22, 0.06,
                 color='#757575', zorder=11))
    # Wheels (animated)
    whl_row = []
    for wx_off in [0.32, BAY_W-0.32]:
        out_c = ax.add_patch(plt.Circle((bx+wx_off, MOTO_Y+0.46), 0.34,
                             facecolor='#212121', edgecolor='#616161',
                             lw=0.9, zorder=11))
        inn_c = ax.add_patch(plt.Circle((bx+wx_off, MOTO_Y+0.46), 0.14,
                             facecolor='#37474f', zorder=12))
        spokes = []
        for sang in [0, 60, 120]:
            sr = np.radians(sang)
            sp = ax.plot([bx+wx_off, bx+wx_off+0.14*np.cos(sr)],
                         [MOTO_Y+0.46, MOTO_Y+0.46+0.14*np.sin(sr)],
                         color='#757575', lw=0.8, zorder=12)[0]
            spokes.append(sp)
        whl_row.append((out_c, inn_c, spokes, bx+wx_off, MOTO_Y+0.46))
    moto_wheel_all.append(whl_row)

    # Battery LED on motorcycle
    mled = ax.add_patch(plt.Circle((bx+BAY_W/2, MOTO_Y+1.14), 0.12,
                        color='#00e5ff' if on else '#ffeb3b', zorder=12))
    ax.text(bx+BAY_W/2, MOTO_Y+1.14, '⚡', ha='center', va='center',
            fontsize=5.0, color='white', fontweight='bold', zorder=13)

    # Moto label + SoC bar underneath
    ax.add_patch(mpatches.Rectangle((bx+0.04, MOTO_Y+0.06),
                 BAY_W-0.08, 0.22, color='#1a1a2a', zorder=9))
    msoc_f = ax.add_patch(mpatches.Rectangle((bx+0.04, MOTO_Y+0.06),
                           (BAY_W-0.08)*moto["soc"]/100, 0.22,
                           color='#22c55e', zorder=10))
    ax.text(bx+BAY_W/2, MOTO_Y+0.17, f'{moto["name"]} · {moto["soc"]:.0f}%',
            ha='center', va='center', fontsize=4.8,
            color='white', fontweight='bold', zorder=11)

    # Bay label at top
    txt(bx+BAY_W/2, MOTO_Y+4.24, f'BAY-{mi+1:02d}',
        sz=7.0, c=col, bold=True, z=10)

    # Wire from DB to charger-Vertical drop from horizontal bus
    # Vertical line from bus to Charger
    ax.plot([bx+BAY_W/2, bx+BAY_W/2],
            [MOTO_Y+4.50, MOTO_Y+4.12],
            color=col, lw=1.8, zorder=7,)
    db_my = DBY+DBH-2.28-mi*0.58+0.25
    ax.plot([DBX+DBW, DBX+DBW+(mi+1)*0.38, bx+BAY_W/2, bx+BAY_W/2],
            [db_my, db_my, MOTO_Y+4.28, MOTO_Y+4.12],
            color=col, lw=1.8, zorder=7,
            path_effects=[pe.Stroke(linewidth=2.8, foreground='#000000', alpha=0.35),
                          pe.Normal()])

    ch_patches_all.append((scr, s_stat, s_pwr, s_soc, s_slbl, mled, msoc_f))
    ev_patches_all.append(mb)

# ══════════════════════════════════════════════════════════════
#  9.  ENERGY FLOW PARTICLES
# ══════════════════════════════════════════════════════════════
FLOW_PATHS = [
    (PV_RIGHT, PV_Y+ROWS*(PMH+GAPR)/2, CB_X, CB_Y+CB_H*0.55, '#ff9800',0.013,22),
    (CB_X+CB_W, CB_Y+CB_H/2, MX, MY+MH/2, '#e43232',0.013,12),
    (MX+MW, MY+MH/2, IX, IY+IH*0.60, '#2f00ff',0.016,30),
    (BX+BW, BY+BH*0.65, IX, IY+0.85, '#d7d011',0.011,15),
    (MX+MW/2, MY, BX+BW/2, BY+BH, '#66bb6a',0.012,12),
    (IX+IW, IY+IH*0.58, DBX, DBY+DBH*0.52, '#ce93d8',0.017,40),
]
# Add particle paths DB → each charger bay
for mi in range(N_MOTOS):
    bx = BAY_X0 + mi*(BAY_W+BAY_GAP)
    FLOW_PATHS.append((DBX+DBW, DBY+DBH*0.5,
                       bx+BAY_W/2, MOTO_Y+4.12, '#4fc3f7',0.014,18))

N_PART = 7
particles = []
particle_state = []
for pi, (x0,y0,x1,y1,col,spd,sz) in enumerate(FLOW_PATHS):
    for ni in range(N_PART):
        sc = ax.scatter([],[],s=sz,color=col,zorder=20,alpha=0.92,
                        edgecolors='white',linewidths=0.24)
        particles.append(sc)
        particle_state.append({'t':ni/N_PART,'path':pi})

# ══════════════════════════════════════════════════════════════
#  10.  DAILY OPERATIONAL SCHEDULE (real-time needle)
# ══════════════════════════════════════════════════════════════
SCHED_Y0     = H - 3.20
SCHED_H      = 0.50
SCHED_X0     = 5.80
SCHED_TOTALW = W - 5.80

def tx(t): return SCHED_X0 + (t/24.0)*SCHED_TOTALW

segments = [
    (0,  6,  '#212121','#546e7a','NIGHT · Battery Idle'),
    (6,  8,  '#1565c0','#4fc3f7','BAT\nBUFFER'),
    (8,  17, '#1b5e20','#69f0ae','☀  PEAK SOLAR  →  10 MOTOS CHARGING  (9h)'),
    (17, 20, '#1565c0','#ce93d8','BAT\nBUFF'),
    (20, 23, '#37474f','#546e7a','GRID\nSTBY'),
    (23, 24, '#2a1a00','#ff7043','BATT\nCHG'),
]
box(SCHED_X0-0.20, SCHED_Y0-0.60, SCHED_TOTALW+0.40, 1.68,
    fc='#040a12', ec='#ffd600', lw=1.8, r=0.15, z=32)
txt(W/2, SCHED_Y0+0.82,
    '⏱  DAILY OPERATIONAL SCHEDULE  —  REAL-TIME MONITORING  ·  45kW ACTIVE LOAD',
    sz=8.5, c='#ffd600', bold=True, z=33)
for s, e, fc_s, ec_s, label in segments:
    xs = tx(s); xe = tx(e)
    ax.add_patch(FancyBboxPatch((xs, SCHED_Y0), xe-xs, SCHED_H,
                 boxstyle='round,pad=0.04',
                 facecolor=fc_s, edgecolor=ec_s, lw=1.5, zorder=35))
    ax.text((xs+xe)/2, SCHED_Y0+SCHED_H/2, label,
            ha='center', va='center', fontsize=5.8,
            color=ec_s, fontweight='bold', zorder=36)
for t_val, lab in zip([0,6,8,12,17,20,23,24],
                      ['00','06','08','12','17','20','23','24']):
    xt = tx(t_val)
    ax.plot([xt,xt],[SCHED_Y0-0.12, SCHED_Y0], color='#ffd600', lw=1.1, zorder=36)
    ax.text(xt, SCHED_Y0-0.30, f'{lab}:00', ha='center', fontsize=5.6,
            color='#ffd600', fontfamily='monospace', zorder=36)

# NOW needle (real-time)
_now_line, = ax.plot([], [], color='#00e5ff', lw=2.5, zorder=50)
_now_glow, = ax.plot([], [], color='#00e5ff', lw=6.0, alpha=0.18, zorder=49)
_now_bg = ax.add_patch(FancyBboxPatch((0,0), 1.70, 0.38,
                        boxstyle='round,pad=0.08',
                        facecolor='#002a33', edgecolor='#00e5ff',
                        linewidth=1.2, zorder=52, alpha=0.92))
_now_lbl = ax.text(0, 0, '', ha='center', va='center',
                   fontsize=6.8, color='#00e5ff', fontweight='bold',
                   fontfamily='monospace', zorder=53)
_now_mrk, = ax.plot([], [], marker='v', color='#00e5ff', markersize=7,
                    zorder=54, linestyle='none',
                    markeredgecolor='white', markeredgewidth=0.5)
_NOW = [_now_line, _now_glow, _now_bg, _now_lbl, _now_mrk]

def _update_needle():
    now  = datetime.now()
    h    = now.hour + now.minute/60 + now.second/3600
    xt   = tx(h)
    y0_  = SCHED_Y0 - 0.20
    y1_  = SCHED_Y0 + SCHED_H + 0.30
    _now_line.set_data([xt,xt],[y0_,y1_])
    _now_glow.set_data([xt,xt],[y0_,y1_])
    _now_bg.set_xy((xt-0.85, SCHED_Y0+SCHED_H+0.32))
    _now_lbl.set_position((xt, SCHED_Y0+SCHED_H+0.51))
    _now_lbl.set_text(f'NOW  {now.strftime("%H:%M:%S")}')
    _now_mrk.set_data([xt],[SCHED_Y0-0.20])

# ══════════════════════════════════════════════════════════════
#  11.  TITLE BANNER
# ══════════════════════════════════════════════════════════════
box(0.18, H-1.88, W-0.36, 1.72, fc='#060d1a', ec='#f59e0b', lw=2.4, z=20, a=0.97)
ax.plot([0.18, W-0.18],[H-0.18,H-0.18], color='#f59e0b', lw=3.2, alpha=0.85, zorder=21)
for xi,ci in zip(np.linspace(0.18,W-0.18,300),
                  [plt.cm.plasma(x) for x in np.linspace(0,1,300)]):
    ax.plot([xi,xi+(W-0.36)/300],[H-0.20,H-0.20], color=ci, lw=2.5, alpha=0.70, zorder=22)
ax.text(W/2, H-0.66,
        '⚡  AMPERSAND  SOLAR  MOTORCYCLE  CHARGING  STATION  ·  32.2 kWp  ·  '
        '60kW OFF-GRID INVERTER  ·  10 BAY  ·  45kW ACTIVE  ·  RWANDA 2026',
        ha='center', fontsize=13.0, color='white', fontweight='bold', zorder=21)
ax.text(W/2, H-1.10,
        f'Jinko Tiger Neo 585W · {NUM_MODULES}Mod / {PV_KWP:.1f}kWp  ·  '
        f'LFP {BAT_KWH:.0f}kWh Battery  ·  {MPPT_KW}kW 5-ch MPPT  ·  '
        f'{INV_KW}kW 3-Phase Off-Grid Inverter  ·  '
        f'{N_MOTOS}× {KW_PER_MOTO}kW = {TOTAL_LOAD:.0f}kW Active Load',
        ha='center', fontsize=9.0, color='#4fc3f7', zorder=21)
ax.text(W/2, H-1.52,
        f'🏍 Ampersand E-Mobility · Kigali, Rwanda  ·  GHI=1752kWh/m²/yr  ·  PSH=4.8h/day  '
        f'·  MCCB {MCCB_A}A + {N_MOTOS}×MCB {MCB_A}A  ·  Designed by: Hermes MUGISHA  ·  Energy Engineer',
        ha='center', fontsize=7.8, color='#ffd600', zorder=21)

# Ampersand logo area
box(0.22, H-4.45, 3.60, 2.35, fc='#0a1020', ec='#ff6d00', lw=2.0, r=0.20, z=20)
ax.text(2.02, H-2.58, 'AMPERSAND', ha='center', fontsize=11, color='#ff6d00',
        fontweight='black', zorder=21)
ax.text(2.02, H-2.92, 'E-MOBILITY', ha='center', fontsize=8.5, color='#ff6d00',
        fontweight='bold', fontfamily='monospace', zorder=21)
ax.text(2.02, H-3.26, '🏍 Electric Motorcycles', ha='center', fontsize=7.5,
        color='#ffa040', zorder=21)
ax.text(2.02, H-3.56, 'Rwanda · Clean Transport 2026', ha='center',
        fontsize=6.8, color='#ffd600', fontfamily='monospace', zorder=21)
ax.text(2.02, H-3.90, f'Active: {TOTAL_LOAD}kW · Motos: {N_MOTOS}',
        ha='center', fontsize=7.0, color='#66bb6a', fontweight='bold',
        fontfamily='monospace', zorder=21)

# KPI badges
for ki, (lbl, val, c_) in enumerate([
    ('PV Array', f'{PV_KWP:.1f}kWp','#f59e0b'),
    ('Battery', f'{BAT_KWH:.0f}kWh','#66bb6a'),
    ('Active', f'{TOTAL_LOAD}kW','#ce93d8'),
    ('CO₂/yr', '21.5t','#4fc3f7'),
]):
    kx = 0.30 + ki*0.93
    ky = H-4.36
    box(kx, ky, 0.84, 0.66, fc='#0d1a0d', ec=c_, lw=1.0, r=0.08, z=21)
    ax.text(kx+0.42, ky+0.42, val, ha='center', fontsize=8.0, color=c_,
            fontweight='bold', fontfamily='monospace', zorder=22)
    ax.text(kx+0.42, ky+0.16, lbl, ha='center', fontsize=5.5,
            color='#90a4ae', zorder=22)

# ══════════════════════════════════════════════════════════════
#  12.  LEGEND + SPECS FOOTER
# ══════════════════════════════════════════════════════════════
box(0.18, 0.04, W*0.46, 1.46, fc='#060d1a', ec='#37474f', lw=1, z=20, a=0.92)
LEG = [
    ('#ff9800','DC Flow  (PV → Combiner → MPPT → Inverter)'),
    ('#66bb6a','Battery LFP 278kWh  Charge / Discharge'),
    ('#ce93d8','AC Bus  (Inverter → MCB Panel  400V/3-Ph)'),
    ('#4fc3f7','Moto Circuit  (MCB → 4.5kW Bay Charger)'),
    ('#00e5ff','Moto Charging  (Charger → Battery Swap)'),
    ('#ffd600','Station Real-Time NOW Indicator'),
]
for li,(lc,lt) in enumerate(LEG):
    col_=li%3; row_=li//3
    lx=0.36+col_*7.60; ly=1.12-row_*0.54
    ax.plot([lx,lx+0.50],[ly,ly],color=lc,lw=3.2,zorder=21)
    ax.add_patch(plt.Circle((lx+0.25,ly),0.08,color=lc,zorder=22))
    ax.text(lx+0.68,ly,lt,fontsize=6.8,color='#cfd8dc',va='center',zorder=21)

box(W*0.46+0.28, 0.04, W*0.54-0.46, 1.46, fc='#060d1a', ec='#37474f', lw=1, z=20, a=0.92)
SPECS=[
    ('PV Array',  f'{NUM_MODULES}×585W={PV_KWP:.1f}kWp  {NUM_STRINGS}str×{MODS_PER_STR}mod  '
                  f'Vmpp={STR_VMPP:.0f}V  Voc={STR_VOC:.0f}V  Impp={ARR_IMPP:.1f}A'),
    ('Battery',   f'LFP {BAT_V}V/{BAT_AH}Ah={BAT_KWH:.0f}kWh  '
                  f'Usable={BAT_USABLE:.0f}kWh  DoD={BAT_DOD*100:.0f}%  Buffer:06-08h & 17-20h'),
    ('MPPT',      f'{MPPT_KW}kW  5-Channel  Eff={MPPT_EFF*100:.1f}%  '
                  f'Max 600V/60A  Out:{BAT_V}V DC  IEC 62109'),
    ('Inverter',  f'{INV_KW}kW Off-Grid 3-Phase  Eff={INV_EFF*100:.0f}%  '
                  f'{AC_V3}V/{AC_HZ}Hz  Iout={INV_IOUT:.1f}A  IEC 62109'),
    ('DB Panel',  f'MCCB {MCCB_A}A + {N_MOTOS}×MCB {MCB_A}A  IEC 60947  36kA Breaking'),
    ('Operation', f'10× Moto Chargers  {KW_PER_MOTO}kW each  =  {TOTAL_LOAD:.0f}kW Total  '
                  f'·  100% Off-Grid  ·  Solar + Battery'),
]
sx0 = W*0.46+0.48
for si,(sl,sv) in enumerate(SPECS):
    row_=si//2; col_=si%2
    sx=sx0+col_*11.8; sy=1.20-row_*0.42
    ax.text(sx,sy,sl+':',fontsize=6.2,color='#ffd600',
            fontweight='bold',va='center',zorder=21)
    ax.text(sx+1.52,sy,sv,fontsize=5.8,color='#b0bec5',va='center',zorder=21)

# ══════════════════════════════════════════════════════════════
#  13.  ANIMATION
# ══════════════════════════════════════════════════════════════
def animate(frame):
    tg    = frame * 0.018
    noise = np.sin(tg * 0.70)
    n2    = np.sin(tg * 1.40 + 0.80)
    blink = 0.5 + 0.5*np.sin(tg*5.0)

    # ── Particles ──────────────────────────────────
    for scat, pst in zip(particles, particle_state):
        pi = pst['path']
        x0,y0,x1,y1,col,spd,sz = FLOW_PATHS[pi]
        pst['t'] = (pst['t'] + spd) % 1.0
        t = pst['t']
        wob = 0.036*np.sin(t*6*np.pi)
        dx = x1-x0; dy = y1-y0
        dn = max(abs(dx)+0.001, 0.001)
        px = x0 + t*dx + wob*(-dy/dn)
        py = y0 + t*dy + wob*(dx/dn)
        scat.set_offsets([[px, py]])
        scat.set_alpha(float(0.5+0.5*np.sin(t*np.pi))*0.92)

    # ── Sun glow ────────────────────────────────────
    sun_glow.set_radius(0.90+0.18*np.sin(tg*2.5))
    sun_glow.set_alpha (0.14+0.09*np.sin(tg*2.5))

    # ── PV shimmer ──────────────────────────────────
    for i, pp in enumerate(pv_patches):
        sh = 0.90+0.10*np.sin(tg*1.8+i*0.28)
        pp.set_facecolor((26/255*sh, 35/255*sh, 126/255*sh))

    # ── Battery fills ───────────────────────────────
    soc_now = BAT_SOC + int(noise*3)
    for bf in bat_fills:
        bf.set_width((BKW-0.06)*soc_now/100)
        bf.set_facecolor('#43a047' if soc_now>30 else '#f44336')

    # ── Inverter LCD ────────────────────────────────
    pv_live = ARR_KW + noise*0.6
    if inv_lcd:
        inv_lcd[1].set_text(f'P_in  : {pv_live:.1f} kW')
        inv_lcd[3].set_text(f'P_out : {TOTAL_LOAD+noise*0.5:.0f} kW')
        inv_lcd[4].set_text(f'I_out : {INV_IOUT+noise*0.8:.1f} A')

    # ── MPPT LCD ────────────────────────────────────
    if mppt_lcd:
        mppt_lcd[1].set_text(f'Iin : {ARR_IMPP+noise*0.3:.1f} A')
        mppt_lcd[2].set_text(f'Pin : {pv_live:.1f} kW')

    # ── Motorcycle bays ─────────────────────────────
    for mi, moto in enumerate(MOTO_STATES):
        on = moto["status"] == "CHARGING"
        col = {'CHARGING':'#29b6f6','CHARGED':'#66bb6a','READY':'#ffd600'}.get(moto["status"],'#546e7a')
        if on and moto["soc"] < 100:
            moto["soc"] = min(100, moto["soc"] + 0.004)
        sc2 = moto["soc"]
        soc_fc = '#00e676' if sc2<80 else ('#ffeb3b' if sc2<95 else '#f44336')
        scr,s_stat,s_pwr,s_soc,s_slbl,mled,msoc_f = ch_patches_all[mi]
        scr.set_facecolor('#0a2a0a' if on else '#1a1a00')
        s_stat.set_text(moto["status"])
        s_stat.set_color('#00ff88' if on else col)
        s_pwr.set_text(f'P={KW_PER_MOTO}kW' if on else 'P=0kW')
        s_pwr.set_color('#69f0ae' if on else '#ff8a80')
        s_soc.set_width((BAY_W-0.20)*sc2/100)
        s_soc.set_facecolor(soc_fc)
        s_slbl.set_text(f'{sc2:.0f}%')
        msoc_f.set_width((BAY_W-0.08)*sc2/100)
        msoc_f.set_facecolor(soc_fc)
        if on:
            mled.set_color('#00e5ff')
            mled.set_alpha(0.50+0.50*np.sin(tg*4.0+mi*0.4))
        else:
            mled.set_color('#ffeb3b')
            mled.set_alpha(0.80)
        # MCB toggle
        tog, ton = mcb_toggles[mi]
        tog.set_facecolor('#1b5e20' if on else '#b71c1c')
        tog.set_edgecolor('#4caf50' if on else '#f44336')
        ton.set_text('ON' if on else 'OFF')
        # Wheel spin
        bounce = 0.0
        for out_c,inn_c,spokes,wx_,wy_ in moto_wheel_all[mi]:
            out_c.center=(wx_,wy_+bounce)
            inn_c.center=(wx_,wy_+bounce)
            if on:
                for si2,sp in enumerate(spokes):
                    ang2=tg*2.2+si2*2.094+mi*0.3
                    sp.set_xdata([wx_,wx_+0.14*np.cos(ang2)])
                    sp.set_ydata([wy_+bounce,wy_+bounce+0.14*np.sin(ang2)])

    # ── NOW needle ─────────────────────────────────
    _update_needle()

    return (particles + [sun_glow] + pv_patches + bat_fills +
            [inv_lcd[1] if inv_lcd else sun_glow] + _NOW)

anim = FuncAnimation(fig, animate, frames=None, interval=40, blit=False)
plt.tight_layout(pad=0)

# ══════════════════════════════════════════════════════════════
#  CONSOLE SUMMARY
# ══════════════════════════════════════════════════════════════
print("╔══════════════════════════════════════════════════════════════════╗")
print("║  AMPERSAND SOLAR MOTORCYCLE CHARGING STATION                    ║")
print("║  Engineer  : Hermes MUGISHA  ·  Energy Engineer                 ║")
print("║  Client    : Ampersand E-Mobility  ·  Kigali, Rwanda            ║")
print("╠══════════════════════════════════════════════════════════════════╣")
print(f"║  PV Array  : {NUM_MODULES}× Jinko Tiger Neo 585W = {PV_KWP:.1f} kWp          ║")
print(f"║  Strings   : {NUM_STRINGS} strings × {MODS_PER_STR} modules  Vmpp={STR_VMPP:.0f}V  Voc={STR_VOC:.0f}V      ║")
print(f"║  Array     : Impp={ARR_IMPP:.1f}A  Power={ARR_KW:.1f}kW                     ║")
print(f"║  MPPT      : {MPPT_KW}kW  5-ch  Eff={MPPT_EFF*100:.1f}%  Max 600V/60A        ║")
print(f"║  Battery   : LFP {BAT_V}V/{BAT_AH}Ah = {BAT_KWH:.0f}kWh  Usable={BAT_USABLE:.0f}kWh     ║")
print(f"║              Buffer: 06:00-08:00h  &  17:00-20:00h (5h total)  ║")
print(f"║  Inverter  : Off-Grid 3Ph {INV_KW}kW  Eff={INV_EFF*100:.0f}%  {AC_V3}V/{AC_HZ}Hz      ║")
print(f"║  DB Panel  : MCCB {MCCB_A}A + {N_MOTOS}×MCB {MCB_A}A  IEC 60947  36kA          ║")
print(f"║  Motos     : {N_MOTOS}× {KW_PER_MOTO}kW = {TOTAL_LOAD:.0f}kW Active Load                  ║")
print(f"║  Operation : 100% Off-Grid  ·  Solar + Battery Buffer           ║")
print(f"║  Schedule  : 08-17h Solar  ·  06-08h+17-20h Battery  ·  Grid   ║")
print("╠══════════════════════════════════════════════════════════════════╣")
print("║  ► Close window to exit.                                        ║")
print("╚══════════════════════════════════════════════════════════════════╝")

plt.savefig('ampersand_solar_moto_station.png', dpi=160,
            bbox_inches='tight', facecolor='#060d1a')
print("  ✔  Preview saved: ampersand_solar_moto_station.png")

plt.show()
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  SOLAR-POWERED EV CHARGING STATION  ·  5-CHARGER UPGRADED SYSTEM           ║
║  Engineer : Hermes MUGISHA  ·  Energy Engineer                               ║
║  Project  : Solar Powered EVs Charging Station — Rwanda E-Mobility 2026     ║
║─────────────────────────────────────────────────────────────────────────────║
║  ENERGY FLOW (LEFT → RIGHT):                                                 ║
║  SUN → PV ARRAY (182×720W=120.9kWp) → COMBINER → MPPT → INVERTER (100kW)    ║
║                         ↕ BATTERY (LFP 800V/300Ah = 680-820kWh)                ║
║  INVERTER → SMART METER → DISTRIBUTION BOARD → 5 CHARGERS → 5 EVs          ║
║─────────────────────────────────────────────────────────────────────────────║
║  PV Array  : 168× Jinko Tiger Neo 720W = 120.1 kWp                          ║
║              16 strings × 16 modules  Vmpp=684.2V  Impp=180.2A             ║
║  Battery   : LFP 800V/300Ah=640kWh  Buffer: 08-11h & 16-20h                ║
║  MPPT      : 132 kW  ·  3-channel  ·  Eff=98.5%                             ║
║  Inverter  : On-Grid 3-Phase 150kW  400V/50Hz  Eff=97.5%                   ║
║  DB Panel  : MCCB 350A + MCB 40A×2 + MCB 63A×2 + MCB 120A×1               ║
║  CH-1 & 2  : 1-Phase  7kW   32A  230V  IEC 62196 Type 1                  ║
║  CH-3 & 4  : 3-Phase  22kW  63A  400V  IEC 62196 Type 2                    ║
║  CH-5      : 3-Phase  40kW  100A 400V  IEC 62196 Type 3                    ║
║  Peak Load : 98 kW  (all 5 chargers active)                                  ║
║─────────────────────────────────────────────────────────────────────────────║
║  HOW TO RUN:                                                                 ║
║    pip install matplotlib numpy                                               ║
║    python solar_ev_5charger_system.py                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ── Backend selection: TkAgg for interactive; fall back to Agg if no display ──
import matplotlib
try:
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    plt.figure()
    plt.close()
except Exception:
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

import matplotlib.patches   as mpatches
import matplotlib.patheffects as pe
import numpy                as np
from matplotlib.patches    import FancyBboxPatch, Arc
from matplotlib.animation  import FuncAnimation
from datetime import datetime

# ══════════════════════════════════════════════════════════════
#  SYSTEM CONSTANTS
# ══════════════════════════════════════════════════════════════
NUM_MODULES   = 168
MOD_POWER_W   = 720
PV_KWP        = NUM_MODULES * MOD_POWER_W / 1000    # 120.1 kWp
PV_VMPP_MOD   = 41.45                               # V per module
PV_IMPP_MOD   = 13.27                               # A per string
MODS_PER_STR  = 16
NUM_STRINGS   = 10
STR_VMPP      = PV_VMPP_MOD * MODS_PER_STR          # 684.2 V
STR_IMPP      = PV_IMPP_MOD                         # 13.27 A per string
ARR_VMPP      = STR_VMPP                             # 684.2 V
ARR_IMPP      = STR_IMPP * NUM_STRINGS               # 180.2 A
ARR_KW        = PV_KWP                               # 120.1 kW

BAT_V         = 800
BAT_AH        = 300
BAT_KWH       = BAT_V * BAT_AH / 1000               # 840 kWh
BAT_SOC       = 78

MPPT_EFF      = 0.985
INV_KW        = 150
INV_EFF       = 0.975
AC_V3         = 400
AC_V1         = 230
AC_HZ         = 50
INV_IOUT      = INV_KW * 1000 / (np.sqrt(3) * AC_V3)  # 144.3 A

MCCB_A        = 350
MCB_A         = [40, 40, 63, 63, 120]

# 5 Chargers
CHARGERS = [
    {"id":1,"phase":"1-Phase","kw": 7,"V":230,"A": 32,"mcb": 40,
     "status":"Charging","soc":72.0,"ev":"EV-A","col":"#0d3b7a"},
    {"id":2,"phase":"1-Phase","kw": 7,"V":230,"A": 32,"mcb": 40,
     "status":"Charging","soc":75.0,"ev":"EV-B","col":"#4a1080"},
    {"id":3,"phase":"3-Phase","kw":22,"V":400,"A": 63,"mcb": 63,
     "status":"Charging","soc":88.0,"ev":"EV-C","col":"#14451a"},
    {"id":4,"phase":"3-Phase","kw":22,"V":400,"A": 63,"mcb": 63,
     "status":"Charging","soc":88.0,"ev":"EV-D","col":"#7a1a05"},
    {"id":5,"phase":"3-Phase","kw":40,"V":400,"A":100,"mcb":120,
     "status":"Charging","soc":92.0,"ev":"EV-E","col":"#5a0a3a"},
]

TOTAL_LOAD = sum(c["kw"] for c in CHARGERS if c["status"] == "Charging")
PEAK_LOAD  = max(c["kw"] for c in CHARGERS)

# ══════════════════════════════════════════════════════════════
#  CANVAS
# ══════════════════════════════════════════════════════════════
W, H = 46, 18
fig  = plt.figure(figsize=(W, H), facecolor='#060d1a')
fig.patch.set_facecolor('#060d1a')
ax   = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_facecolor('#060d1a')
ax.axis('off')
try:
    fig.canvas.manager.set_window_title(
        "Solar EV Station — 5 Chargers — 100.1kWp — Rwanda E-Mobility 2026 — Eng. Hermes MUGISHA")
except Exception:
    pass

# Sky gradient
for i in range(180):
    t = i / 180
    r = int(6  + t * 16)
    g = int(13 + t * 22)
    b = int(26 + t * 50)
    ax.axhspan(i * H / 180, (i + 1) * H / 180,
               color=(r/255, g/255, b/255), zorder=0, alpha=0.72)

# Ground strip
ax.add_patch(mpatches.Rectangle((0, 0),   W, 1.55, color='#0d1f0d', zorder=1))
ax.add_patch(mpatches.Rectangle((0, 1.4), W, 0.40, color='#1a3a1a', zorder=1))

# Subtle grid
for gx in np.arange(0, W, 1.4):
    ax.plot([gx, gx], [0, H], color='#0e2040', lw=0.16, alpha=0.18, zorder=1)
for gy in np.arange(0, H, 1.4):
    ax.plot([0, W], [gy, gy], color='#0e2040', lw=0.16, alpha=0.18, zorder=1)

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════
def box(x, y, w, h, fc='#0d1f33', ec='#29b6f6', lw=2.0,
        r=0.15, z=8, a=1.0):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f'round,pad={r}',
                       facecolor=fc, edgecolor=ec,
                       linewidth=lw, zorder=z, alpha=a)
    ax.add_patch(p)
    return p

def txt(x, y, s, sz=7.0, c='#cfd8dc', ha='center', va='center',
        bold=False, mono=False, z=11, a=1.0):
    ax.text(x, y, s, ha=ha, va=va, fontsize=sz, color=c, alpha=a,
            fontweight='bold' if bold else 'normal', zorder=z,
            fontfamily='monospace' if mono else 'sans-serif')

def sbar(x, y, w, h, pct, z=12):
    ax.add_patch(mpatches.Rectangle((x, y), w, h, color='#1a1a2a', zorder=z))
    fc = '#00e676' if pct < 80 else ('#ffeb3b' if pct < 95 else '#f44336')
    ax.add_patch(mpatches.Rectangle((x, y), w * pct / 100, h, color=fc, zorder=z+1))
    ax.text(x + w/2, y + h/2, f'{pct:.0f}%', ha='center', va='center',
            fontsize=6.2, color='white', fontweight='bold',
            fontfamily='monospace', zorder=z+2)

def arrow(x0, y0, x1, y1, c='#ff9800', lw=2.5, z=8):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=c, lw=lw), zorder=z)

def biarrow(x0, y0, x1, y1, c='#4caf50', lw=2.5, z=8):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='<->', color=c, lw=lw), zorder=z)

def tag(x, y, s, fc='#1a0d00', c='#ffb74d', sz=6.2, z=9):
    ax.text(x, y, s, ha='center', va='center', fontsize=sz, color=c,
            fontweight='bold', zorder=z,
            bbox=dict(boxstyle='round,pad=0.18', facecolor=fc,
                      alpha=0.90, edgecolor='none'))

# ══════════════════════════════════════════════════════════════
#  1.  SUN
# ══════════════════════════════════════════════════════════════
SX, SY = 1.20, 12.80
ax.add_patch(plt.Circle((SX, SY), 0.70, color='#FFD700', zorder=6))
ax.add_patch(plt.Circle((SX, SY), 0.92, color='#FFD700', alpha=0.20, zorder=5))
ax.add_patch(plt.Circle((SX, SY), 1.15, color='#FFD700', alpha=0.07, zorder=4))
sun_glow = plt.Circle((SX, SY), 0.92, color='#FFD700', alpha=0.18, zorder=5)
ax.add_patch(sun_glow)
for ang in np.linspace(0, 360, 18, endpoint=False):
    r = np.radians(ang)
    ax.plot([SX + 1.00*np.cos(r), SX + 1.42*np.cos(r)],
            [SY + 1.00*np.sin(r), SY + 1.42*np.sin(r)],
            color='#FFD700', lw=2.2, zorder=6, alpha=0.82)
ax.text(SX, SY, '☀', ha='center', va='center',
        fontsize=14, color='#FF6F00', fontweight='bold', zorder=7)
for dy, s, c, bold in [
    (-1.55, 'SOLAR IRRADIANCE',       '#FFD700', True ),
    (-1.88, '1000 W/m²  |  AM1.5',   '#FFA000', False),
    (-2.16, 'Temp: 25°C (STC)',       '#FFB300', False),
    (-2.44, f'Peak: {PV_KWP:.1f} kWp','#ffcc02', True ),
]:
    ax.text(SX, SY + dy, s, ha='center',
            fontsize=6.8 if bold else 6.0, color=c,
            fontweight='bold' if bold else 'normal', zorder=7)

# ══════════════════════════════════════════════════════════════
#  2.  PV ARRAY
# ══════════════════════════════════════════════════════════════
PV_X, PV_Y  = 2.60, 5.60
PMW, PMH    = 0.84, 0.58
GAPC, GAPR  = 0.06, 0.06
COLS, ROWS  = 8, 11

pv_patches = []
for row in range(ROWS):
    for col in range(COLS):
        px = PV_X + col * (PMW + GAPC)
        py = PV_Y + row * (PMH + GAPR)
        p  = ax.add_patch(mpatches.Rectangle(
               (px, py), PMW, PMH,
               facecolor='#1a237e', edgecolor='#42a5f5',
               linewidth=1.0, zorder=8))
        pv_patches.append(p)
        for ci in range(3):
            for ri in range(2):
                ax.add_patch(mpatches.Rectangle(
                    (px + 0.04 + ci*0.255, py + 0.05 + ri*0.22),
                    0.21, 0.17,
                    facecolor='#283593', edgecolor='#5c6bc0',
                    linewidth=0.22, zorder=9))
        ax.text(px + PMW/2, py + PMH - 0.10, 'JINKO',
                ha='center', fontsize=3.8, color='#90caf9',
                fontweight='bold', zorder=10)
        ax.text(px + PMW/2, py + 0.08, '720W',
                ha='center', fontsize=3.6, color='#64b5f6', zorder=10)
    py_r = PV_Y + row * (PMH + GAPR)
    ax.text(PV_X - 0.32, py_r + PMH/2, f'S{row+1}',
            ha='center', va='center', fontsize=6.0,
            color='#ff9800', fontweight='bold', zorder=11)

# Mounting poles
for col in range(COLS):
    px = PV_X + col * (PMW + GAPC) + PMW/2
    ax.plot([px, px - 0.10], [PV_Y, PV_Y - 0.50], color='#757575', lw=1.8, zorder=7)
    ax.plot([px - 0.10, px - 0.10], [PV_Y - 0.50, 1.65], color='#616161', lw=1.4, zorder=7)

# Irradiance arrows
for col in [1, 4, 6]:
    for row in [2, 6, 9]:
        if row < ROWS:
            sx = PV_X + col * (PMW + GAPC) + PMW/2
            sy = PV_Y + row * (PMH + GAPR) + PMH
            ax.annotate('', xy=(sx - 0.05, sy + 0.10),
                        xytext=(sx - 0.52, sy + 0.72),
                        arrowprops=dict(arrowstyle='->', color='#FFD700',
                                        lw=1.4, alpha=0.68), zorder=8)

# PV title box
PV_RIGHT  = PV_X + COLS * (PMW + GAPC)
PV_TOP_Y  = PV_Y + ROWS * (PMH + GAPR) + 0.10
PV_TITLE_W = COLS * (PMW + GAPC) + 0.28
box(PV_X - 0.38, PV_TOP_Y, PV_TITLE_W, 1.00,
    fc='#0d1f33', ec='#42a5f5', lw=1.5, z=10)
txt(PV_X + COLS*(PMW+GAPC)/2 - 0.05, PV_TOP_Y + 0.68,
    f'JINKO TIGER NEO  ·  {PV_KWP:.1f} kWp  SOLAR PV ARRAY',
    sz=9.5, c='#42a5f5', bold=True, z=11)
txt(PV_X + COLS*(PMW+GAPC)/2 - 0.05, PV_TOP_Y + 0.30,
    f'{NUM_MODULES} Mods  ·  {NUM_STRINGS} Strings×{MODS_PER_STR}  ·  '
    f'Vmpp={ARR_VMPP:.1f}V  ·  Impp={ARR_IMPP:.1f}A  ·  Pmpp={ARR_KW:.1f}kW',
    sz=7.0, c='#90caf9', mono=True, z=11)

# ══════════════════════════════════════════════════════════════
#  3.  STRING COMBINER / DC DISCONNECT
# ══════════════════════════════════════════════════════════════
CB_X, CB_Y = PV_RIGHT + 1.20, 6.10
CB_W, CB_H = 2.10, 5.60

box(CB_X, CB_Y, CB_W, CB_H, fc='#111f11', ec='#4caf50', lw=2.2, z=9)
txt(CB_X + CB_W/2, CB_Y + CB_H + 0.22, 'STRING COMBINER',
    sz=8.5, c='#4caf50', bold=True, z=10)
txt(CB_X + CB_W/2, CB_Y + CB_H - 0.20, '+ DC DISCONNECT',
    sz=7.2, c='#81c784', z=10)

FSTEP = (CB_H - 0.50) / NUM_STRINGS
for si in range(NUM_STRINGS):
    fy = CB_Y + 0.26 + si * FSTEP
    ax.add_patch(mpatches.Rectangle((CB_X + 0.14, fy), 0.54, 0.24,
                 facecolor='#1b5e20', edgecolor='#4caf50', lw=0.7, zorder=11))
    ax.text(CB_X + 0.41, fy + 0.12, f'F{si+1}  15A',
            ha='center', va='center', fontsize=4.6,
            color='#a5d6a7', fontfamily='monospace', zorder=12)
    ax.add_patch(plt.Circle((CB_X + 1.84, fy + 0.12), 0.066,
                 color='#00e676', zorder=12))
txt(CB_X + CB_W/2, CB_Y + 0.14,
    f'DC  {ARR_VMPP:.1f}V  /  {ARR_IMPP:.1f}A',
    sz=6.5, c='#c8e6c9', mono=True, z=11)

arrow(PV_RIGHT, PV_Y + ROWS*(PMH+GAPR)/2, CB_X, CB_Y + CB_H*0.55,
      c='#ff9800', lw=2.8)
tag((PV_RIGHT + CB_X)/2, PV_Y + ROWS*(PMH+GAPR)/2 + 0.30,
    f'DC  {ARR_VMPP:.0f}V / {ARR_IMPP:.0f}A  =  {ARR_KW:.0f}kW')

# ══════════════════════════════════════════════════════════════
#  4.  MPPT CHARGE CONTROLLER  132kW · 4-channel
# ══════════════════════════════════════════════════════════════
MX, MY = CB_X + CB_W + 1.10, 6.10
MW, MH = 2.20, 5.60

box(MX, MY, MW, MH, fc='#0d2233', ec='#29b6f6', lw=2.2, z=9)
txt(MX + MW/2, MY + MH + 0.22, 'MPPT SOLAR',
    sz=8.5, c='#29b6f6', bold=True, z=10)
txt(MX + MW/2, MY + MH - 0.20, 'CHARGE CONTROLLER  132 kW',
    sz=7.0, c='#81d4fa', z=10)

# LCD screen
ax.add_patch(mpatches.Rectangle((MX + 0.12, MY + 3.10), MW - 0.24, 2.18,
             facecolor='#001400', edgecolor='#2e7d32', lw=0.9, zorder=11))
mppt_lcd = []
for li, ln in enumerate([
    f'Vin : {ARR_VMPP:.1f} V',
    f'Iin : {ARR_IMPP:.1f} A',
    f'Pin : {ARR_KW:.1f} kW',
    f'Vout: {BAT_V} V  DC',
    f'Eff : {MPPT_EFF*100:.1f} %',
    f'IEC 62109 Cert.',
]):
    t = ax.text(MX + MW/2, MY + 5.02 - li*0.32, ln,
                ha='center', va='center', fontsize=5.8,
                color='#00ff41', fontfamily='monospace', zorder=12)
    mppt_lcd.append(t)

# 3 channel LEDs
for chi, (mc, ml) in enumerate([('#00e676','CH-1'),
                                  ('#00bcd4','CH-2'),
                                  ('#ffea00','CH-3')]):
    ax.add_patch(plt.Circle((MX + 0.34 + chi*0.66, MY + 2.80), 0.10,
                 color=mc, zorder=12))
    ax.text(MX + 0.34 + chi*0.66, MY + 2.62, ml,
            ha='center', fontsize=5.0, color=mc, zorder=12)

for li, ln in enumerate([
    f'4 MPPT × 33 kW  each',
    f'Max Input: 800V / 80A',
    f'Output: {BAT_V}V DC → Inverter',
    f'Eff: {MPPT_EFF*100:.1f}%  |  IEC 62109',
]):
    txt(MX + MW/2, MY + 2.26 - li*0.36, ln, sz=5.8, c='#80deea', mono=True, z=11)

arrow(CB_X + CB_W, CB_Y + CB_H/2, MX, MY + MH/2, c='#ff9800', lw=2.8)
tag((CB_X + CB_W + MX)/2, CB_Y + CB_H/2 + 0.28,
    f'DC  {ARR_VMPP:.0f}V / {ARR_IMPP:.0f}A')

# ══════════════════════════════════════════════════════════════
#  5.  BATTERY  LFP 800V/300Ah = 620kWh
# ══════════════════════════════════════════════════════════════
BX, BY = MX - 0.10, 1.82
BW, BH = MW + 0.20, 3.72

box(BX, BY, BW, BH, fc='#091a09', ec='#66bb6a', lw=2.2, z=9)
txt(BX + BW/2, BY + BH + 0.22, 'BATTERY ENERGY STORAGE',
    sz=8.5, c='#66bb6a', bold=True, z=10)
txt(BX + BW/2, BY + BH - 0.20,
    f'LFP  {BAT_V}V / {BAT_AH}Ah  =  {BAT_KWH:.0f} kWh',
    sz=7.0, c='#a5d6a7', z=10)

# 8 battery modules (2×4 grid)
BKW, BKH = 0.88, 0.58
bat_fills = []
for bi in range(8):
    bkc = bi % 2
    bkr = bi // 2
    bkx = BX + 0.18 + bkc * (BKW + 0.14)
    bky = BY + 0.24 + bkr * (BKH + 0.12)
    ax.add_patch(mpatches.Rectangle((bkx, bky), BKW, BKH,
                 facecolor='#1b5e20', edgecolor='#4caf50', lw=0.8, zorder=11))
    fill = ax.add_patch(mpatches.Rectangle((bkx + 0.03, bky + 0.03),
                        (BKW - 0.06) * BAT_SOC / 100, BKH - 0.06,
                        color='#43a047', zorder=12))
    bat_fills.append(fill)
    ax.text(bkx + BKW/2, bky + BKH/2, f'M{bi+1}  {BAT_V//8}V',
            ha='center', va='center', fontsize=5.0,
            color='white', fontweight='bold', zorder=13)
    ax.add_patch(mpatches.Rectangle((bkx + BKW - 0.09, bky + 0.16),
                 0.07, 0.27, color='#9e9e9e', zorder=13))

sbar(BX + 0.16, BY + BH - 0.52, BW - 0.32, 0.30, BAT_SOC, z=12)
bat_src_txt = ax.text(BX + BW/2, BY + 0.14,
                      '⏱  Buffer: 08:00–11:00h  &  16:00–20:00h',
                      ha='center', fontsize=6.5, color='#fff176',
                      fontweight='bold', zorder=11)

biarrow(MX + MW/2, MY, BX + BW/2, BY + BH, c='#66bb6a', lw=2.5)
tag(MX + MW/2 - 0.88, (MY + BY + BH)/2,
    f'{BAT_V}V DC\nCharge / Discharge',
    fc='#0a1f0a', c='#a5d6a7', sz=6.0)

# ══════════════════════════════════════════════════════════════
#  6.  ON-GRID 3-PHASE 150kW INVERTER
# ══════════════════════════════════════════════════════════════
IX, IY = MX + MW + 1.10, 3.90
IW, IH = 2.90, 7.60

box(IX, IY, IW, IH, fc='#150a2e', ec='#ce93d8', lw=2.5, z=9)
txt(IX + IW/2, IY + IH + 0.22, 'ON-GRID  INVERTER',
    sz=9.0, c='#ce93d8', bold=True, z=10)
txt(IX + IW/2, IY + IH - 0.20, '3-PHASE  ·  150 kW',
    sz=8.0, c='#e1bee7', bold=True, z=10)

# Display screen
ax.add_patch(mpatches.Rectangle((IX + 0.12, IY + 5.25), IW - 0.24, 2.10,
             facecolor='#0a0018', edgecolor='#7b1fa2', lw=1.0, zorder=11))
inv_lcd = []
for li, ln in enumerate([
    f'DC IN : {ARR_VMPP:.0f}V / {ARR_IMPP:.0f}A',
    f'P_in  : {ARR_KW:.1f} kW',
    f'AC OUT: {AC_V3}V / {AC_HZ}Hz',
    f'P_out : {ARR_KW*INV_EFF:.1f} kW',
    f'I_out : {INV_IOUT:.1f} A (3-Ph)',
    f'Eff   : {INV_EFF*100:.1f}%  THD<3%',
]):
    t = ax.text(IX + IW/2, IY + 7.08 - li*0.30, ln,
                ha='center', va='center', fontsize=5.8,
                color='#ce93d8', fontfamily='monospace', zorder=12)
    inv_lcd.append(t)

# 3-phase sine waves
t_s = np.linspace(0, 4*np.pi, 120)
xs  = IX + 0.18 + (IW - 0.36) * t_s / (4*np.pi)
for ph, clr in [(0, '#f44336'), (2*np.pi/3, '#ffeb3b'), (4*np.pi/3, '#2196f3')]:
    ax.plot(xs, IY + 4.88 + 0.36*np.sin(t_s + ph),
            color=clr, lw=1.3, zorder=12, alpha=0.92)
txt(IX + IW/2, IY + 4.38, '3-Phase AC  L1 / L2 / L3',
    sz=6.0, c='#b39ddb', z=12)

for si, ss in enumerate([
    f'Rated: {INV_KW}kW / {INV_KW/0.8:.0f}kVA',
    f'Input: DC 200–900 V',
    f'Output: 3Ph {AC_V3}V + 1Ph {AC_V1}V',
    f'MPPT: 3-ch  800V/80A',
    f'Prot.: IP65  |  IEC 62109',
    f'Cert.: CE / IEC 61727',
]):
    txt(IX + IW/2, IY + 3.90 - si*0.32, ss,
        sz=5.8, c='#d1c4e9', mono=True, z=11)

# Cooling fins
for fi in range(11):
    ax.add_patch(mpatches.Rectangle((IX - 0.26, IY + 0.28 + fi*0.62),
                 0.20, 0.50,
                 facecolor='#37474f', edgecolor='#546e7a', lw=0.4, zorder=10))

arrow(MX + MW, MY + MH/2, IX, IY + IH*0.60, c='#ff9800', lw=2.8)
tag((MX + MW + IX)/2, MY + MH/2 + 0.28,
    f'DC  {ARR_VMPP:.0f}V / {ARR_IMPP:.0f}A  =  {ARR_KW:.0f}kW')

biarrow(BX + BW, BY + BH*0.65, IX, IY + 0.88, c='#66bb6a', lw=2.5)
tag((BX + BW + IX)/2, BY + BH*0.65 + 0.28,
    f'{BAT_V}V  Backup / Grid-Charge',
    fc='#0a1f0a', c='#a5d6a7', sz=6.2)

# ══════════════════════════════════════════════════════════════
#  7.  SMART METER
# ══════════════════════════════════════════════════════════════
SMX, SMY = IX + IW + 1.00, 5.30
SMW, SMH = 2.50, 5.92

box(SMX, SMY, SMW, SMH, fc='#070f20', ec='#00e5ff', lw=2.5, r=0.18, z=12)

ax.add_patch(FancyBboxPatch((SMX, SMY + SMH - 0.82), SMW, 0.82,
             boxstyle='round,pad=0.12',
             facecolor='#005f6e', edgecolor='none', zorder=13))
txt(SMX + SMW/2, SMY + SMH - 0.40,
    '⚡  SMART METER  3Ph 100A',
    sz=8.5, c='white', bold=True, z=14)

SM_ROWS = [
    ('Solar PV',   '#FFD700', f'{ARR_KW:.1f} kW'),
    ('Batt. SoC',  '#00e676', f'{BAT_SOC} %'),
    ('Load',       '#ff7043', f'{TOTAL_LOAD} kW'),
    ('Volt 3Ph',   '#4fc3f7', f'{AC_V3} V'),
    ('Current',    '#80cbc4', f'{INV_IOUT:.1f} A'),
    ('Frequency',  '#ce93d8', '50.00 Hz'),
    ('Energy/Day', '#ffeb3b', '—— kWh'),
    ('Grid Status','#69f0ae', 'ON-GRID ✓'),
]
sm_texts = []
RH = 0.50
for ri, (lbl, lc, val) in enumerate(SM_ROWS):
    ry = SMY + SMH - 0.92 - (ri + 1) * RH
    if ry < SMY + 0.95:
        break
    rc = '#0d1a30' if ri % 2 == 0 else '#0a1424'
    ax.add_patch(mpatches.Rectangle((SMX + 0.08, ry + 0.04),
                 SMW - 0.16, RH - 0.07, facecolor=rc, zorder=13))
    ax.add_patch(mpatches.Rectangle((SMX + 0.08, ry + 0.04),
                 0.12, RH - 0.07, facecolor=lc, zorder=14))
    txt(SMX + 0.26, ry + RH/2, lbl, sz=6.8, c='#cfd8dc', ha='left', mono=True, z=14)
    t = ax.text(SMX + SMW - 0.14, ry + RH/2, val,
                ha='right', va='center', fontsize=7.8,
                color=lc, fontweight='bold',
                fontfamily='monospace', zorder=14)
    sm_texts.append(t)

# IoT strip
box(SMX + 0.10, SMY + 0.10, SMW - 0.20, 0.80,
    fc='#040c1e', ec='#29b6f6', lw=1.2, r=0.10, z=13)
wc2, wy2 = SMX + 0.96, SMY + 0.52
for ri2, r2 in enumerate([0.13, 0.23, 0.34]):
    ax.add_patch(Arc((wc2, wy2 - 0.04), r2*2, r2*2,
                 angle=0, theta1=22, theta2=158,
                 color='#29b6f6', lw=1.4 - ri2*0.3, zorder=14))
ax.add_patch(plt.Circle((wc2, wy2 - 0.04), 0.050, color='#29b6f6', zorder=15))
txt(SMX + 1.40, SMY + 0.52, 'IoT Connected', sz=7.0,
    c='#29b6f6', bold=True, ha='left', z=14)
txt(SMX + 2.16, SMY + 0.70, '☁ MQTT',
    sz=5.8, c='#80deea', bold=True, z=14)
txt(SMX + 2.16, SMY + 0.34, 'Modbus TCP',
    sz=5.6, c='#80deea', z=14)
iot_led = ax.add_patch(plt.Circle((SMX + SMW - 0.20, SMY + 0.52), 0.090,
                        color='#00e676', zorder=15))

arrow(IX + IW, IY + IH*0.58, SMX, SMY + SMH*0.54, c='#ce93d8', lw=3.0)
tag((IX + IW + SMX)/2, IY + IH*0.58 + 0.30,
    f'3Ph {AC_V3}V/{AC_HZ}Hz  ·  {ARR_KW*INV_EFF:.0f}kW',
    fc='#1a0033', c='#ce93d8', sz=6.5)

# ══════════════════════════════════════════════════════════════
#  8.  DISTRIBUTION BOARD
# ══════════════════════════════════════════════════════════════
MCB_ROW_H = 1.02
DBX, DBY  = SMX + SMW + 1.00, 4.50
DBW       = 2.64
DBH       = 1.30 + 5 * MCB_ROW_H + 0.32   # ≈ 6.72

box(DBX, DBY, DBW, DBH, fc='#141208', ec='#ffd600', lw=2.5, z=9)
txt(DBX + DBW/2, DBY + DBH + 0.22, 'DISTRIBUTION  BOARD',
    sz=9.0, c='#ffd600', bold=True, z=10)
txt(DBX + DBW/2, DBY + DBH - 0.20, 'AC BUS  ·  MCCB + MCB Breakers',
    sz=7.2, c='#fff176', z=10)

# MCCB main breaker
box(DBX + 0.14, DBY + DBH - 1.22, DBW - 0.28, 0.92,
    fc='#1a0000', ec='#f44336', lw=1.6, r=0.07, z=11)
txt(DBX + DBW/2, DBY + DBH - 0.80,
    f'MCCB  {MCCB_A}A  —  MAIN  (3Ph)',
    sz=7.5, c='#ef9a9a', bold=True, z=12)
txt(DBX + DBW/2, DBY + DBH - 1.06,
    'IEC 60947  |  Breaking Cap.: 36 kA',
    sz=5.8, c='#ef9a9a', mono=True, z=12)
ax.add_patch(FancyBboxPatch((DBX + DBW - 0.62, DBY + DBH - 1.06),
             0.42, 0.38, boxstyle='round,pad=0.03',
             facecolor='#1b5e20', edgecolor='#4caf50', lw=1.0, zorder=13))
txt(DBX + DBW - 0.41, DBY + DBH - 0.88, 'ON',
    sz=6.5, c='white', bold=True, z=14)

# AC Bus bar strip
ax.add_patch(mpatches.Rectangle((DBX + 0.12, DBY + 0.10), DBW - 0.24, 0.28,
             facecolor='#1a1a00', edgecolor='#ffd600', lw=0.8, zorder=11))
for bi, (bc, bl) in enumerate([('#f44336','L1'), ('#ffeb3b','L2'),
                                ('#2196f3','L3'), ('#78909c','N')]):
    bx2 = DBX + 0.18 + bi * 0.58
    ax.add_patch(mpatches.Rectangle((bx2, DBY + 0.12), 0.48, 0.18,
                 facecolor=bc, edgecolor='none', zorder=12, alpha=0.7))
    txt(bx2 + 0.24, DBY + 0.21, bl, sz=5.0, c='white', bold=True, z=13)

# 5 MCB rows
MCB_INFO = [
    ('MCB-1','CH-1  1Ph   7kW', '40A', '#4fc3f7', True,  '230V · 32A'),
    ('MCB-2','CH-2  1Ph   7kW', '40A', '#4fc3f7', True,  '230V · 32A'),
    ('MCB-3','CH-3  3Ph  22kW', '63A', '#ff7043', True,  '400V · 58A'),
    ('MCB-4','CH-4  3Ph  22kW', '63A', '#ff7043', True,  '400V · 58A'),
    ('MCB-5','CH-5  3Ph  40kW','120A', '#e040fb', True,  '400V · 100A'),
]
mcb_toggles = []
for mi, (mnm, mds, ma, mc, mon, mvl) in enumerate(MCB_INFO):
    my2 = DBY + DBH - 2.28 - mi * MCB_ROW_H
    box(DBX + 0.14, my2, DBW - 0.28, MCB_ROW_H - 0.08,
        fc='#141414', ec=mc, lw=1.2, r=0.07, z=11)
    txt(DBX + 0.32, my2 + MCB_ROW_H*0.72, mnm,
        sz=8.0, c=mc, bold=True, ha='left', z=12)
    txt(DBX + 0.32, my2 + MCB_ROW_H*0.46, mds,
        sz=6.2, c='#cfd8dc', ha='left', mono=True, z=12)
    txt(DBX + 0.32, my2 + MCB_ROW_H*0.20, mvl,
        sz=5.8, c='#90a4ae', ha='left', mono=True, z=12)
    txt(DBX + DBW - 0.42, my2 + MCB_ROW_H*0.46, ma,
        sz=6.5, c='white', bold=True, z=12)
    tog = ax.add_patch(FancyBboxPatch((DBX + DBW - 0.62, my2 + 0.26),
                       0.42, 0.42, boxstyle='round,pad=0.03',
                       facecolor='#1b5e20', edgecolor='#4caf50', lw=0.9, zorder=13))
    ton = ax.text(DBX + DBW - 0.41, my2 + 0.47, 'ON',
                  ha='center', va='center', fontsize=5.8,
                  color='white', fontweight='bold', zorder=14)
    mcb_toggles.append((tog, ton))

arrow(SMX + SMW, SMY + SMH*0.52, DBX, DBY + DBH*0.52, c='#ce93d8', lw=3.0)
tag((SMX + SMW + DBX)/2, SMY + SMH*0.52 + 0.30,
    f'AC  {AC_V3}V / {AC_HZ}Hz',
    fc='#1a0033', c='#ce93d8', sz=6.5)

# ══════════════════════════════════════════════════════════════
#  9.  FIVE EV CHARGERS + CONNECTED EVs
# ══════════════════════════════════════════════════════════════
CH_X0  = DBX + DBW + 0.58
CH_GAP = 2.07
CH_Y   = 4.72
CH_W   = 1.79
CH_H   = 6.37
EV_Y   = 1.63
EV_H   = 0.99

CH_XS = [CH_X0 + ci * CH_GAP for ci in range(5)]

WIRE_COLS = ['#4fc3f7','#4fc3f7','#ff7043','#ff7043','#e040fb']
EV_COLS   = ['#0d3b7a','#4a1080','#14451a','#7a1a05','#5a0a3a']

ch_patches = []
ev_patches = []
ev_wheels  = []

for ci, ch in enumerate(CHARGERS):
    cx     = CH_XS[ci]
    is3ph  = ch["phase"] == "3-Phase"
    ec_col = '#e040fb' if ch["kw"] == 40 else ('#ff7043' if is3ph else '#29b6f6')
    on     = ch["status"] == "Charging"
    scr_c  = '#00ff88' if on else '#ff5252'

    # Charger body
    box(cx, CH_Y, CH_W, CH_H, fc='#080e1c', ec=ec_col, lw=2.2, z=9)

    # Phase / power badge
    ax.add_patch(FancyBboxPatch((cx + 0.06, CH_Y + CH_H - 0.58),
                 CH_W - 0.12, 0.46, boxstyle='round,pad=0.03',
                 facecolor='#bf360c' if is3ph else '#1a237e',
                 edgecolor=ec_col, lw=0.9, zorder=11))
    txt(cx + CH_W/2, CH_Y + CH_H - 0.36, ch["phase"],
        sz=7.0, c=ec_col, bold=True, z=12)

    # Screen
    scr = ax.add_patch(mpatches.Rectangle(
            (cx + 0.08, CH_Y + 3.48), CH_W - 0.16, 2.44,
            facecolor='#0a2a0a' if on else '#1a0000',
            edgecolor='#2e7d32' if on else '#7f0000',
            lw=0.9, zorder=11))
    s_stat = ax.text(cx + CH_W/2, CH_Y + 5.54,
                     'CHARGING' if on else 'STANDBY',
                     ha='center', fontsize=6.2, color=scr_c,
                     fontweight='bold', fontfamily='monospace', zorder=12)
    s_pwr = ax.text(cx + CH_W/2, CH_Y + 5.12,
                    f'P = {ch["kw"]:>2d} kW',
                    ha='center', fontsize=9.0,
                    color='#69f0ae' if on else '#ff8a80',
                    fontweight='bold', zorder=12)
    ax.text(cx + CH_W/2, CH_Y + 4.74, f'V = {ch["V"]} V',
            ha='center', fontsize=7.0, color=scr_c,
            fontfamily='monospace', zorder=12)
    ax.text(cx + CH_W/2, CH_Y + 4.42, f'I = {ch["A"]} A',
            ha='center', fontsize=7.0, color=scr_c,
            fontfamily='monospace', zorder=12)
    ax.text(cx + CH_W/2, CH_Y + 4.12, f'f = {AC_HZ} Hz',
            ha='center', fontsize=6.2, color=scr_c,
            fontfamily='monospace', zorder=12)
    ax.text(cx + CH_W/2, CH_Y + 3.78, ch["ev"],
            ha='center', fontsize=6.2, color='#b2dfdb',
            fontfamily='monospace', zorder=12)

    # SoC bar
    ax.add_patch(mpatches.Rectangle((cx + 0.10, CH_Y + 3.20),
                 CH_W - 0.20, 0.26, color='#1a1a2a', zorder=12))
    s_soc = ax.add_patch(mpatches.Rectangle(
                (cx + 0.10, CH_Y + 3.20),
                (CH_W - 0.20) * ch["soc"] / 100, 0.26,
                color='#00e676', zorder=13))
    s_slbl = ax.text(cx + CH_W/2, CH_Y + 3.33, f'{ch["soc"]:.0f}%  SoC',
                     ha='center', va='center', fontsize=5.8,
                     color='white', fontweight='bold', zorder=14)

    # IEC 62196 Type 1 connector
    ax.add_patch(plt.Circle((cx + CH_W/2, CH_Y + 2.66), 0.36,
                 facecolor='#1a1a1a', edgecolor=ec_col, lw=1.8, zorder=11))
    ax.add_patch(plt.Circle((cx + CH_W/2, CH_Y + 2.66), 0.24,
                 facecolor='#212121', zorder=12))
    for pox, poy in [(-0.11, 0.09),(0.11, 0.09),(0, -0.10),
                     (-0.15,-0.02),(0.15,-0.02),(0, 0.00)]:
        ax.add_patch(plt.Circle((cx + CH_W/2 + pox, CH_Y + 2.66 + poy),
                     0.038, color='#bdbdbd', zorder=13))
    txt(cx + CH_W/2, CH_Y + 2.18, 'IEC 62196', sz=5.2, c='#78909c', z=12)
    txt(cx + CH_W/2, CH_Y + 1.94, 'Type  1',   sz=5.2, c='#78909c', z=12)

    # RFID / NFC pad
    ax.add_patch(FancyBboxPatch((cx + 0.10, CH_Y + 0.38),
                 CH_W - 0.20, 0.86, boxstyle='round,pad=0.04',
                 facecolor='#1a237e', edgecolor='#5c6bc0', lw=0.8, zorder=11))
    txt(cx + CH_W/2, CH_Y + 0.90, 'RFID / NFC',    sz=5.8, c='#9fa8da', z=12)
    txt(cx + CH_W/2, CH_Y + 0.62, 'TAP  TO  START', sz=5.0, c='#7986cb', z=12)

    # Labels below/above charger
    txt(cx + CH_W/2, CH_Y - 0.28,
        f'CH-{ch["id"]}  ·  {ch["kw"]} kW',
        sz=8.5, c=ec_col, bold=True, z=10)
    txt(cx + CH_W/2, CH_Y - 0.54,
        f'{ch["phase"]}  ·  {ch["V"]}V  ·  {ch["A"]}A',
        sz=6.5, c='#b0bec5', z=10)
    txt(cx + CH_W/2, CH_Y + CH_H + 0.16,
        f'{ch["V"]}V · {ch["A"]}A · MCB {ch["mcb"]}A',
        sz=6.0, c=WIRE_COLS[ci], z=9)

    # EV Car body
    ecol  = EV_COLS[ci]
    ev_b  = ax.add_patch(FancyBboxPatch(
              (cx - 0.06, EV_Y + 0.42), CH_W + 0.12, EV_H,
              boxstyle='round,pad=0.08',
              facecolor=ecol, edgecolor='#b0bec5', lw=1.2, zorder=9))
    ev_r  = ax.add_patch(FancyBboxPatch(
              (cx + 0.14, EV_Y + 0.84), CH_W - 0.28, 0.52,
              boxstyle='round,pad=0.06',
              facecolor=ecol, edgecolor='#b0bec5', lw=0.9, zorder=10))
    ev_patches.append((ev_b, ev_r))

    # Windshields
    for wx_off in [0.16, 0.82]:
        ax.add_patch(FancyBboxPatch((cx + wx_off, EV_Y + 0.88),
                     0.44, 0.36, boxstyle='round,pad=0.03',
                     facecolor='#b3e5fc', edgecolor='#0288d1',
                     lw=0.5, zorder=11))

    # Headlights
    for hx_off in [-0.04, 1.46]:
        ax.add_patch(FancyBboxPatch((cx + hx_off, EV_Y + 0.62),
                     0.12, 0.30, boxstyle='round,pad=0.02',
                     facecolor='#fff9c4', edgecolor='#fdd835', lw=0.5, zorder=11))

    # Wheels (animated)
    whl_row = []
    for wx_off in [0.20, 1.26]:
        out_c = ax.add_patch(plt.Circle((cx + wx_off, EV_Y + 0.38), 0.24,
                             facecolor='#212121', edgecolor='#616161',
                             lw=0.9, zorder=11))
        inn_c = ax.add_patch(plt.Circle((cx + wx_off, EV_Y + 0.38), 0.10,
                             facecolor='#424242', zorder=12))
        spokes = []
        for sang in [0, 60, 120]:
            sr = np.radians(sang)
            sp = ax.plot([cx + wx_off, cx + wx_off + 0.10*np.cos(sr)],
                         [EV_Y + 0.38,  EV_Y + 0.38 + 0.10*np.sin(sr)],
                         color='#757575', lw=0.7, zorder=12)[0]
            spokes.append(sp)
        whl_row.append((out_c, inn_c, spokes, cx + wx_off, EV_Y + 0.38))
    ev_wheels.append(whl_row)

    # Charge port LED
    led = ax.add_patch(plt.Circle((cx + CH_W/2, EV_Y + 0.66), 0.11,
                       color='#00e5ff' if on else '#37474f', zorder=12))
    ax.text(cx + CH_W/2, EV_Y + 0.66, ch["ev"],
            ha='center', va='center', fontsize=4.8,
            color='white', fontweight='bold', zorder=13)

    # EV SoC bar
    ax.add_patch(mpatches.Rectangle((cx + 0.02, EV_Y + 0.04),
                 CH_W - 0.04, 0.20, color='#1a1a2a', zorder=9))
    ev_soc_f = ax.add_patch(mpatches.Rectangle(
                   (cx + 0.02, EV_Y + 0.04),
                   (CH_W - 0.04) * ch["soc"] / 100, 0.20,
                   color='#22c55e', zorder=10))

    # Charging cable
    ax.plot([cx + CH_W/2, cx + CH_W/2], [CH_Y, EV_Y + EV_H + 0.44],
            color=ec_col, lw=1.6, ls='--', zorder=8, alpha=0.75)

    ch_patches.append((scr, s_stat, s_pwr, s_soc, s_slbl, led, ev_soc_f))

# DB → Charger wiring
for ci, ch in enumerate(CHARGERS):
    cx = CH_XS[ci]
    wc = WIRE_COLS[ci]
    db_y = DBY + DBH
    ax.plot([DBX + DBW*0.35 + (5 - ci)*0.26,
             DBX + DBW*0.35 + (5 - ci)*0.26,
             cx + CH_W/2,
             cx + CH_W/2],
            [db_y,
             db_y + (ci + 3)*0.26,
             db_y + (ci + 3)*0.26,
             db_y + 0.02],
            color=wc, lw=2.4, zorder=8,
            path_effects=[pe.Stroke(linewidth=3.8,
                          foreground='#000000', alpha=0.38),
                          pe.Normal()])

# ══════════════════════════════════════════════════════════════
#  10.  ENERGY FLOW PARTICLES
# ══════════════════════════════════════════════════════════════
FLOW_PATHS = [
    (PV_RIGHT,   PV_Y + ROWS*(PMH+GAPR)/2,
     CB_X,        CB_Y + CB_H*0.55,          '#ff9800', 0.013, 22),
    (CB_X + CB_W, CB_Y + CB_H/2,
     MX,           MY + MH/2,                '#e43232', 0.013, 12),
    (MX + MW,     MY + MH/2,
     IX,           IY + IH*0.58,             '#2f00ff', 0.016, 30),
    (BX + BW,     BY + BH*0.65,
     IX,           IY + 0.85,                '#d7d011', 0.011, 15),
    (MX + MW/2,   MY,
     BX + BW/2,   BY + BH,                   '#66bb6a', 0.012, 12),
    (IX + IW,     IY + IH*0.58,
     SMX,          SMY + SMH*0.54,           '#ce93d8', 0.017, 40),
    (SMX + SMW,   SMY + SMH*0.52,
     DBX,          DBY + DBH*0.52,           '#ffd600', 0.016, 35),
    (DBX + DBW,   DBY + DBH - 2.28 - 0*MCB_ROW_H + (MCB_ROW_H-0.08)/2,
     CH_XS[0] + CH_W/2, CH_Y + CH_H,        '#4fc3f7', 0.016, 16),
    (DBX + DBW,   DBY + DBH - 2.28 - 1*MCB_ROW_H + (MCB_ROW_H-0.08)/2,
     CH_XS[1] + CH_W/2, CH_Y + CH_H,        '#4fc3f7', 0.016, 16),
    (DBX + DBW,   DBY + DBH - 2.28 - 2*MCB_ROW_H + (MCB_ROW_H-0.08)/2,
     CH_XS[2] + CH_W/2, CH_Y + CH_H,        '#ff7043', 0.016, 30),
    (DBX + DBW,   DBY + DBH - 2.28 - 3*MCB_ROW_H + (MCB_ROW_H-0.08)/2,
     CH_XS[3] + CH_W/2, CH_Y + CH_H,        '#ff7043', 0.016, 15),
    (DBX + DBW,   DBY + DBH - 2.28 - 4*MCB_ROW_H + (MCB_ROW_H-0.08)/2,
     CH_XS[4] + CH_W/2, CH_Y + CH_H,        '#e040fb', 0.018, 40),
    (SMX + SMW*0.5, SMY + SMH,
     SMX + SMW*0.5, SMY + SMH + 0.90,        '#00e5ff', 0.020, 20),
]

N_PART         = 9
particles      = []
particle_state = []
for pi, (x0, y0, x1, y1, col, spd, sz) in enumerate(FLOW_PATHS):
    for ni in range(N_PART):
        sc = ax.scatter([], [], s=sz, color=col, zorder=20,
                        alpha=0.92, edgecolors='white', linewidths=0.26)
        particles.append(sc)
        particle_state.append({'t': ni / N_PART, 'path': pi})

# ══════════════════════════════════════════════════════════════
#  REAL-TIME ENERGY MANAGEMENT SYSTEM MODE
# ══════════════════════════════════════════════════════════════
def get_system_mode():
    now  = datetime.now()
    hour = now.hour + now.minute / 60
    t    = (hour - 8) % 24
    if   0  <= t < 2:  return "BATTERY_DISCHARGE"
    elif 2  <= t < 9:  return "SOLAR_DIRECT"
    elif 9  <= t < 12: return "BATTERY_DISCHARGE"
    elif 12 <= t < 15: return "GRID_STANDBY"
    elif 15 <= t < 20: return "GRID_CHARGING"
    else:              return "PRESTART"

# ══════════════════════════════════════════════════════════════
#  TIME INDICATOR  — persistent animated artists
# ══════════════════════════════════════════════════════════════
#  These are created once (as mutable objects) and updated every
#  animation frame so the NOW line sweeps smoothly in real time.
# ══════════════════════════════════════════════════════════════

# Placeholder position — will be set correctly on first animate() call
_SCHED_Y      = None   # populated inside draw_daily_operational_schedule()
_SCHED_X0     = None
_SCHED_TOTALW = None

# The vertical NOW line (a Line2D)
_now_line, = ax.plot([], [], color='#00e5ff', lw=2.8, zorder=50,
                     solid_capstyle='round')

# Glow copy (thicker, semi-transparent) for a neon effect
_now_glow, = ax.plot([], [], color='#00e5ff', lw=7.0, zorder=49,
                     alpha=0.22, solid_capstyle='round')

# "NOW: HH:MM:SS" label — background pill + foreground text
_now_bg = ax.add_patch(FancyBboxPatch(
    (0, 0), 1.80, 0.42,
    boxstyle='round,pad=0.10',
    facecolor='#002a33', edgecolor='#00e5ff',
    linewidth=1.4, zorder=52, alpha=0.93))

_now_label = ax.text(
    0, 0, '',
    ha='center', va='center',
    fontsize=7.2, color='#00e5ff',
    fontweight='bold', fontfamily='monospace',
    zorder=53)

# Small downward-pointing triangle marker on top of the bar
_now_marker, = ax.plot([], [], marker='v', color='#00e5ff',
                       markersize=7, zorder=54, linestyle='none',
                       markeredgecolor='white', markeredgewidth=0.5)

# Collect all NOW artists so animate() can return them
_NOW_ARTISTS = [_now_line, _now_glow, _now_bg, _now_label, _now_marker]


def _update_now_indicator():
    """Reposition every NOW artist to match the current wall-clock time."""
    if _SCHED_Y is None:
        return
    now   = datetime.now()
    hour  = now.hour + now.minute / 60 + now.second / 3600
    t     = (hour - 8) % 24          # offset from 08:00
    xt    = _SCHED_X0 + (t / 24) * _SCHED_TOTALW
    y     = _SCHED_Y
    label = f'NOW: {now.strftime("%H:%M:%S")}'

    # Vertical line from tick-row down through the bar + a little above
    _now_line.set_data([xt, xt], [y - 0.22, y + 1.10])
    _now_glow.set_data([xt, xt], [y - 0.22, y + 1.10])

    # Triangle marker just above the bar
    _now_marker.set_data([xt], [y + 1.10])

    # Background pill (width centred on xt)
    pill_w, pill_h = 2.10, 0.46
    _now_bg.set_x(xt - pill_w / 2)
    _now_bg.set_y(y + 1.18)
    _now_bg.set_width(pill_w)
    _now_bg.set_height(pill_h)

    # Text centred in the pill
    _now_label.set_position((xt, y + 1.18 + pill_h / 2))
    _now_label.set_text(label)

# ══════════════════════════════════════════════════════════════
#  DAILY OPERATIONAL SCHEDULE
# ══════════════════════════════════════════════════════════════
def draw_daily_operational_schedule():
    global _SCHED_Y, _SCHED_X0, _SCHED_TOTALW

    y       = H - 3.8
    h       = 0.8
    x0      = 4.0
    total_w = W - 10.0

    # Store layout so the animator can reposition the NOW artists
    _SCHED_Y      = y
    _SCHED_X0     = x0
    _SCHED_TOTALW = total_w

    txt(W/2, y + 1.78,
        'DAILY OPERATIONAL SCHEDULE — REAL-TIME CONTROL',
        sz=8, c='#ffd600', bold=False, z=40)

    def tx(t):
        return x0 + (t / 24.0) * total_w

    segments = [
        (0,   1.2,    "#103661", 'BTTRY'),
        (1.2,   8.2,  '#1b5e20', 'PV'),
        (8.2,  11.2,  '#311b92', 'BTTRY'),
        (11.2, 14.2,  '#263238', 'GRID'),
        (14.2, 19.2,  '#263238', 'GRID CHG BTTRY'),
        (19.2, 24,    '#263238', 'GRID'),
    ]
    for s, e, col, label in segments:
        xs = tx(s)
        xe = tx(e)
        box(xs, y, xe - xs, h,
            fc=col, ec='#90a4ae', lw=1.5, r=0.12, z=35)
        txt((xs + xe) / 2, y + h/2, label,
            sz=7, c='white', bold=True, z=36)

    # Timeline ticks (static — drawn once)
    times  = [0,  1.2,  8.2,  11.2, 14.2, 19.2, 24]
    labels = ['08:00','11:00','16:00','20:00','23:00','04:00','08:00']
    for t_val, lab in zip(times, labels):
        xt = tx(t_val)
        ax.plot([xt, xt], [y - 0.15, y],
                color='#ffd600', lw=1.2, zorder=36)
        txt(xt, y - 0.40, lab, sz=6.5, c='#ffd600', z=36)

    # Position NOW artists for the very first frame
    _update_now_indicator()

draw_daily_operational_schedule()

# ══════════════════════════════════════════════════════════════
#  11.  TITLE BANNER
# ══════════════════════════════════════════════════════════════
box(0.18, H - 1.88, W - 0.36, 1.72, fc='#060d1a', ec='#f59e0b', lw=2.4, z=20, a=0.97)
ax.plot([0.18, W - 0.18], [H - 0.18, H - 0.18],
        color='#f59e0b', lw=3.2, alpha=0.85, zorder=21)
for xi, ci in zip(np.linspace(0.18, W - 0.18, 300),
                  [plt.cm.plasma(x) for x in np.linspace(0, 1, 300)]):
    ax.plot([xi, xi + (W - 0.36)/300], [H - 0.20, H - 0.20],
            color=ci, lw=2.5, alpha=0.7, zorder=22)

ax.text(W/2, H - 0.68,
        'SOLAR-POWERED EVs CHARGING STATION  ·  120.9 kWp  ·  150 kW ON-GRID  ·  '
        'IoT SMART METER  ·  5 CHARGERS  ·  ANIMATED ENERGY FLOW',
        ha='center', fontsize=13.5, color='white',
        fontweight='bold', zorder=21)
ax.text(W/2, H - 1.14,
        f'Jinko Tiger Neo 720W · {NUM_MODULES}Mod / {PV_KWP:.0f}kWp  ·  '
        f'LFP {BAT_KWH:.0f}kWh  ·  150kW On-Grid Inverter  ·  '
        f'2×7kW(1Ph) + 2×22kW(3Ph) + 1×40kW(3Ph)  ·  '
        f'Peak={PEAK_LOAD}kW  ·  Rwanda E-Mobility 2026',
        ha='center', fontsize=9.0, color='#4fc3f7', zorder=21)
ax.text(W/2, H - 1.55,
        f'📍 Kigali, Rwanda  ·  GHI=1752kWh/m²/yr  ·  PSH=4.8h/day  '
        f'·  Engineer: Hermes MUGISHA  ·  Energy Engineer',
        ha='center', fontsize=7.8, color='#ffd600', zorder=21)

# ══════════════════════════════════════════════════════════════
#  12.  LIVE DATA PANEL
# ══════════════════════════════════════════════════════════════
box(0.20, H - 4.40, 3.40, 2.28, fc='#060d1a', ec='#4caf50', lw=1.8, z=20, a=0.95)
txt(1.90, H - 2.32, 'LIVE  DATA', sz=8.5, c='#4caf50', bold=True, z=21)
LD_LABELS = ['Irrad.','PV Out','Battery','Load','Efficiency']
LD_VALS   = ['1000W/m²', f'{ARR_KW:.1f}kW', f'{BAT_SOC}%',
             f'{TOTAL_LOAD}kW', '97.5%']
LD_COLS   = ['#FFD700','#ff9800','#66bb6a','#ce93d8','#80deea']
live_texts = []
for li, (ll, lv, lc) in enumerate(zip(LD_LABELS, LD_VALS, LD_COLS)):
    row  = li % 3
    col_ = li // 3
    lx   = 0.32 + col_*1.70
    ly   = H - 2.90 - row*0.48
    ax.text(lx, ly, ll + ':', fontsize=6.0, color='#90a4ae', va='center', zorder=21)
    t = ax.text(lx + 1.60, ly, lv, fontsize=7.0, color=lc,
                fontweight='bold', va='center', ha='right',
                fontfamily='monospace', zorder=21)
    live_texts.append(t)

# ══════════════════════════════════════════════════════════════
#  13.  LEGEND + SPECS FOOTER
# ══════════════════════════════════════════════════════════════
box(0.18, 0.04, W*0.54, 1.46, fc='#060d1a', ec='#37474f', lw=1, z=20, a=0.92)
LEG = [
    ('#ff9800','DC Flow  (PV → Combiner → MPPT → Inverter)'),
    ('#66bb6a','Battery  Charge / Discharge  (LFP 620 kWh)'),
    ('#ce93d8','AC Bus  (Inverter → Smart Meter → DB)'),
    ('#4fc3f7','1-Phase  230V / 32A / 7 kW  Charger (×2)'),
    ('#ff7043','3-Phase  400V / 63A / 22 kW  Charger (×2)'),
    ('#e040fb','3-Phase  400V / 100A / 40 kW  Charger (×1)'),
    ('#00e5ff','IoT  MQTT / Modbus TCP  Data Link'),
]
for li, (lc, lt) in enumerate(LEG):
    col_ = li % 4
    row  = li // 4
    lx   = 0.36 + col_*6.20
    ly   = 1.12 - row*0.56
    ax.plot([lx, lx + 0.50], [ly, ly], color=lc, lw=3.2, zorder=21)
    ax.add_patch(plt.Circle((lx + 0.25, ly), 0.08, color=lc, zorder=22))
    ax.text(lx + 0.68, ly, lt, fontsize=7.0, color='#cfd8dc', va='center', zorder=21)

box(W*0.54 + 0.28, 0.04, W*0.46 - 0.46, 1.46, fc='#060d1a', ec='#37474f', lw=1, z=20, a=0.92)
SPECS = [
    ('PV Array', f'{NUM_MODULES}×720W={PV_KWP:.0f}kWp  {NUM_STRINGS}str×{MODS_PER_STR}mod  '
                 f'Vmpp={ARR_VMPP:.0f}V  Impp={ARR_IMPP:.0f}A'),
    ('Battery',  f'LFP {BAT_V}V/{BAT_AH}Ah={BAT_KWH:.0f}kWh  SoC={BAT_SOC}%  '
                 f'Buffer: 08–11h & 16–20h'),
    ('MPPT',     f'150kW  4-ch×33kW  Eff={MPPT_EFF*100:.1f}%  Max 800V/80A  Out:{BAT_V}V DC'),
    ('Inverter', f'{INV_KW}kW On-Grid 3Ph  Eff={INV_EFF*100:.1f}%  '
                 f'{AC_V3}V/{AC_HZ}Hz  Iout={INV_IOUT:.0f}A'),
    ('DB Panel', f'MCCB {MCCB_A}A + MCB 40A×2 + 63A×2 + 120A×1  IEC 60947  36kA'),
    ('IoT/Meter',f'3Ph 150A  Modbus TCP+MQTT  IEC 62056  IEC 61851/62196'),
]
sx0 = W*0.54 + 0.48
for si, (sl, sv) in enumerate(SPECS):
    row  = si // 2
    col_ = si % 2
    sx   = sx0 + col_*9.8
    sy   = 1.18 - row*0.42
    ax.text(sx, sy, sl + ':', fontsize=6.2, color='#ffd600',
            fontweight='bold', va='center', zorder=21)
    ax.text(sx + 1.62, sy, sv, fontsize=5.8, color='#b0bec5',
            va='center', zorder=21)

# ══════════════════════════════════════════════════════════════
#  14.  ANIMATION
# ══════════════════════════════════════════════════════════════
def animate(frame):
    tg    = frame * 0.018
    noise = np.sin(tg * 0.70)
    n2    = np.sin(tg * 1.40 + 0.80)
    blink = 0.5 + 0.5 * np.sin(tg * 5.0)

    # Energy particles
    for scat, pst in zip(particles, particle_state):
        pi             = pst['path']
        x0,y0,x1,y1,col,spd,sz = FLOW_PATHS[pi]
        pst['t']       = (pst['t'] + spd) % 1.0
        t              = pst['t']
        wob            = 0.038 * np.sin(t * 6 * np.pi)
        dx             = x1 - x0
        dy             = y1 - y0
        dn             = max(abs(dx) + 0.001, 0.001)
        px             = x0 + t*dx + wob*(-dy/dn)
        py             = y0 + t*dy + wob*( dx/dn)
        scat.set_offsets([[px, py]])
        scat.set_alpha(float(0.5 + 0.5*np.sin(t*np.pi)) * 0.92)

    # Sun glow
    sun_glow.set_radius(0.90 + 0.18 * np.sin(tg * 2.5))
    sun_glow.set_alpha (0.14 + 0.09 * np.sin(tg * 2.5))

    # PV shimmer
    for i, pp in enumerate(pv_patches):
        sh = 0.90 + 0.10 * np.sin(tg*1.8 + i*0.28)
        pp.set_facecolor((26/255*sh, 35/255*sh, 126/255*sh))

    # Battery module fill
    soc_now = BAT_SOC + int(noise * 3)
    for bf in bat_fills:
        bf.set_width((BKW - 0.06) * soc_now / 100)
        bf.set_facecolor('#43a047' if soc_now > 30 else '#f44336')

    # Live data panel
    irr_live = int(1000 + noise * 18)
    pv_live  = ARR_KW  + noise * 0.8
    bat_live = BAT_SOC + int(noise * 3)
    ld_live  = TOTAL_LOAD + noise * 1.2
    live_texts[0].set_text(f'{irr_live} W/m²')
    live_texts[1].set_text(f'{pv_live:.1f} kW')
    live_texts[2].set_text(f'{bat_live} %')
    live_texts[3].set_text(f'{ld_live:.1f} kW')
    live_texts[4].set_text(f'{INV_EFF*100:.1f} %')

    # Smart Meter rows
    v_l  = AC_V3    + noise * 1.8
    i_l  = INV_IOUT + noise * 1.2
    f_l  = 50.0     + noise * 0.04
    e_l  = 520.0    + n2 * 5.0
    upd  = [f'{pv_live:.1f} kW',  f'{bat_live} %',
            f'{ld_live:.1f} kW',  f'{v_l:.0f} V',
            f'{i_l:.1f} A',        f'{f_l:.2f} Hz',
            f'{e_l:.0f} kWh',      'ON-GRID ✓']
    for ti, txt_ in enumerate(upd):
        if ti < len(sm_texts):
            sm_texts[ti].set_text(txt_)

    # MPPT LCD
    if mppt_lcd:
        mppt_lcd[1].set_text(f'Iin : {ARR_IMPP + noise*0.5:.1f} A')
        mppt_lcd[2].set_text(f'Pin : {pv_live:.1f} kW')

    # Inverter LCD
    if inv_lcd:
        inv_lcd[1].set_text(f'P_in  : {pv_live:.1f} kW')
        inv_lcd[3].set_text(f'P_out : {pv_live*INV_EFF:.1f} kW')
        inv_lcd[4].set_text(f'I_out : {i_l:.1f} A (3-Ph)')

    # IoT LED blink
    iot_led.set_alpha(0.35 + 0.65 * blink)

    # EV chargers + cars
    for ci, ch in enumerate(CHARGERS):
        cx     = CH_XS[ci]
        on     = ch["status"] == "Charging"
        scr_c  = '#00ff88' if on else '#ff5252'
        scr, s_stat, s_pwr, s_soc, s_slbl, led, ev_soc_f = ch_patches[ci]

        scr.set_facecolor('#0a2a0a' if on else '#1a0000')
        s_stat.set_text('CHARGING' if on else 'STANDBY')
        s_stat.set_color(scr_c)
        s_pwr.set_text(f'P = {ch["kw"]:>2d} kW' if on else 'P =  0 kW')
        s_pwr.set_color('#69f0ae' if on else '#ff8a80')

        if on and ch["soc"] < 100:
            ch["soc"] = min(100, ch["soc"] + 0.004)
        sc     = ch["soc"]
        soc_fc = '#00e676' if sc < 80 else ('#ffeb3b' if sc < 95 else '#f44336')
        s_soc.set_width((CH_W - 0.20) * sc / 100)
        s_soc.set_facecolor(soc_fc)
        s_slbl.set_text(f'{sc:.0f}%  SoC')
        ev_soc_f.set_width((CH_W - 0.04) * sc / 100)
        ev_soc_f.set_facecolor(soc_fc)

        tog, ton = mcb_toggles[ci]
        tog.set_facecolor('#1b5e20' if on else '#b71c1c')
        tog.set_edgecolor('#4caf50' if on else '#f44336')
        ton.set_text('ON' if on else 'OFF')

        if on:
            led.set_color('#00e5ff')
            led.set_alpha(0.50 + 0.50 * np.sin(tg*4.0 + ci*1.0))
        else:
            led.set_color('#37474f')
            led.set_alpha(0.50)

        bounce = 0.016 * np.sin(tg*3.0 + ci*0.9) if on else 0.0
        ev_b, ev_r = ev_patches[ci]
        ev_b.set_y(EV_Y + 0.42 + bounce)
        ev_r.set_y(EV_Y + 0.84 + bounce)

        for out_c, inn_c, spokes, wx_, wy_ in ev_wheels[ci]:
            if on:
                out_c.center = (wx_, wy_ + bounce)
                inn_c.center = (wx_, wy_ + bounce)
                for si2, sp in enumerate(spokes):
                    ang2 = tg*2.2 + si2*2.094 + ci*0.5
                    sp.set_xdata([wx_, wx_ + 0.10*np.cos(ang2)])
                    sp.set_ydata([wy_ + bounce, wy_ + bounce + 0.10*np.sin(ang2)])
            else:
                out_c.center = (wx_, wy_)
                inn_c.center = (wx_, wy_)

    # ── Real-time NOW indicator (line + glow + pill label + triangle) ──
    _update_now_indicator()

    return (particles + [sun_glow] + pv_patches + bat_fills +
            live_texts + sm_texts + [iot_led] + _NOW_ARTISTS)

# Keep reference to prevent garbage collection
anim = FuncAnimation(fig, animate, frames=None, interval=40, blit=False)

plt.tight_layout(pad=0)

# ══════════════════════════════════════════════════════════════
#  CONSOLE SUMMARY
# ══════════════════════════════════════════════════════════════
print("╔══════════════════════════════════════════════════════════════════╗")
print("║  SOLAR-POWERED EV CHARGING STATION  —  5-CHARGER SYSTEM         ║")
print("║  Engineer  : Hermes MUGISHA  ·  Energy Engineer                 ║")
print("║  Project   : Rwanda E-Mobility 2026  ·  Kigali      ║")
print("╠══════════════════════════════════════════════════════════════════╣")
print(f"║  PV Array  : {NUM_MODULES}× Jinko Tiger Neo 720W = {PV_KWP:.1f} kWp           ║")
print(f"║  Strings   : {NUM_STRINGS} strings × {MODS_PER_STR} modules/string              ║")
print(f"║  DC Bus    : Vmpp={ARR_VMPP:.1f}V  Impp={ARR_IMPP:.1f}A  P={ARR_KW:.1f}kW        ║")
print(f"║  MPPT      : 132kW  3-channel  Eff=98.5%  Out:{BAT_V}V DC         ║")
print(f"║  Battery   : LFP {BAT_V}V/{BAT_AH}Ah = {BAT_KWH:.0f}kWh  SoC={BAT_SOC}%          ║")
print(f"║              Buffer: 08:00–11:00h  &  16:00–20:00h             ║")
print(f"║  Inverter  : On-Grid 3Ph {INV_KW}kW  Eff={INV_EFF*100:.1f}%  {AC_V3}V/{AC_HZ}Hz    ║")
print(f"║  Sm.Meter  : 3Ph 100A  Modbus TCP / MQTT IoT                   ║")
print(f"║  DB Panel  : MCCB {MCCB_A}A + MCB 40A×2 + 63A×2 + 120A×1          ║")
print(f"║  CH-1 & 2  : 1-Phase   7kW  32A  230V  IEC 62196 Type 2       ║")
print(f"║  CH-3 & 4  : 3-Phase  22kW  63A  400V  IEC 62196 Type 2       ║")
print(f"║  CH-5      : 3-Phase  40kW 120A  400V  IEC 62196 Type 1       ║")
print(f"║  Load      : Active={TOTAL_LOAD}kW  |  Peak={PEAK_LOAD}kW                  ║")
print("╠══════════════════════════════════════════════════════════════════╣")
print("║  ► Close window to exit.                                        ║")
print("╚══════════════════════════════════════════════════════════════════╝")

# Save static preview
plt.savefig('solar_ev_5charger_system.png', dpi=160,
            bbox_inches='tight', facecolor='#060d1a')
print("  ✔  Preview saved: solar_ev_5charger_system.png")

plt.show()
