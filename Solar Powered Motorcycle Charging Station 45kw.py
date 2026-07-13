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