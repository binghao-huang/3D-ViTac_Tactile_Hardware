# 1mm FPC Pitch Variant ｜ 1mm 间距 FPC 变体

3D-ViTac / FlexiTac 触觉传感器硬件的 1mm 间距 FPC 变体。
原版 reading board 与 connector 使用 0.5mm 间距 FFC 座，手工焊接困难；
本变体将 FFC 座及焊盘改为 1mm 间距，电路原理与引脚定义保持不变，
焊接难度明显降低。基于嘉立创EDA专业版绘制，可直接配合嘉立创下单
打样与 SMT 贴片（免费额度以嘉立创当期活动规则为准）。

## 中文说明

### 背景

- 原版 0.5mm 间距 FFC 座手工焊接困难、成功率低，是复刻过程中的主要痛点。
- 本变体将间距扩大到 1mm：焊盘间距翻倍，手工焊接的容错率与成功率显著提升。

### 改动内容

- FFC 座及焊盘：0.5mm → 1mm 间距
- Reading Board：2× `HC-FPC-1.0-16P-CXH25`（1.0mm，16P，LCSC C49166851）
- Connector Board：1× `AFA07-S16FCC-00`（1.0mm，16P，LCSC C13744）
- 电路原理与引脚定义保持不变；设计工具：嘉立创EDA专业版（EasyEDA Pro）

### 兼容性与注意事项

- 与原版两块板 pin 脚兼容
- **注意：必须更换为 1mm 间距 FFC 排线**（原 0.5mm 排线无法插入）
- Arduino 安装方式与现有固件（`arduino_code`）不变
- 连接板沿用原版做法：排针无需焊接，导电线用胶带贴合

### 文件

| 路径 | 说明 |
| --- | --- |
| `reading_board/` | 读数板：源工程、Gerber、BOM、贴片坐标 |
| `connector/` | 连接板：源工程、Gerber、BOM、贴片坐标 |

### 验证状态

[已打样]

---

## English

### Background

- The original 0.5 mm-pitch FFC connectors are difficult to hand-solder,
  which is the main pain point when reproducing the sensor.
- This variant widens the pitch to 1 mm: pad spacing doubles, and the
  hand-soldering success rate improves significantly.

### What changed

- FFC connectors & footprints: 0.5 mm → 1 mm pitch
- Reading board: 2× `HC-FPC-1.0-16P-CXH25` (1.0 mm, 16P, LCSC C49166851)
- Connector board: 1× `AFA07-S16FCC-00` (1.0 mm, 16P, LCSC C13744)
- Circuit and pin definitions unchanged; designed in EasyEDA Pro (嘉立创EDA)

### Compatibility & notes

- Pin-to-pin compatible with the original boards
- **Note: requires 1 mm-pitch FFC cables** (the original 0.5 mm cables will not fit)
- Arduino mounting and the existing firmware (`arduino_code`) are unchanged
- Connector board follows the original guide: pin header not soldered,
  conductive thread attached with tape

### Files

| Path | Description |
| --- | --- |
| `reading_board/` | source, Gerber, BOM, Pick & Place |
| `connector/` | source, Gerber, BOM, Pick & Place |

### Validation

[Fabricated]

