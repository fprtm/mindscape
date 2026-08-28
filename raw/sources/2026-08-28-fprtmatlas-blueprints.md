---
title: "2026-08-28-fprtm/atlas-blueprints"
source: "https://github.com/fprtm/atlas-blueprints/tree/main"
author:
published:
created: 2026-08-28
description: "Contribute to fprtm/atlas-blueprints development by creating an account on GitHub."
tags:
  - "clippings"
---
## Atlas Blueprints

Katalog ide MVP software, dikelompokkan per industri, disusun dari kerangka referensi [`atlas-domain-knowledge`](https://github.com/fprtm/atlas-domain-knowledge) (role, process, system, data per industri).

Tujuan: punya perpustakaan ide MVP yang lengkap lintas industri dan lintas kategori sistem (ERP/CRM/WMS/dst) sebagai bank ide siap divalidasi/dibangun, bukan sekadar brainstorm lepas.

## Cara pakai

1. Buka folder industri yang relevan (lihat daftar di bawah).
2. Tiap folder industri punya `README.md` — ringkasan subdomain, role, dan sistem existing yang relevan (rujukan ke Atlas).
3. Tiap ide MVP ada di `mvp-<slug>/README.md`, formatnya standar — lihat [`_template/mvp-template.md`](https://github.com/fprtm/atlas-blueprints/blob/main/_template/mvp-template.md).
4. Kalau satu ide mau dilanjut jadi build beneran, jalankan `/sdd-pipeline:orchestrator` dari dalam folder `mvp-<slug>/` itu — nanti dokumen discovery/build/prove-nya nambah sebagai subfolder `docs/` di situ juga.

## Status tracking

Setiap `mvp-*/README.md` punya field `Status`: `idea` → `validated` → `building` → `shipped`. Belum ada dashboard otomatis — scan manual / `grep -r "Status:" atlas-blueprints/` dulu.

## Daftar Industri

| # | Folder | Industri |
| --- | --- | --- |
| 01 | [agriculture-food](https://github.com/fprtm/atlas-blueprints/blob/main/01-agriculture-food) | Agriculture & Food |
| 02 | [healthcare](https://github.com/fprtm/atlas-blueprints/blob/main/02-healthcare) | Healthcare & Life Sciences |
| 03 | [banking-financial-services](https://github.com/fprtm/atlas-blueprints/blob/main/03-banking-financial-services) | Banking & Financial Services |
| 04 | [insurance](https://github.com/fprtm/atlas-blueprints/blob/main/04-insurance) | Insurance |
| 05 | [manufacturing](https://github.com/fprtm/atlas-blueprints/blob/main/05-manufacturing) | Manufacturing |
| 06 | [logistics-supply-chain](https://github.com/fprtm/atlas-blueprints/blob/main/06-logistics-supply-chain) | Logistics & Supply Chain |
| 07 | [retail-ecommerce](https://github.com/fprtm/atlas-blueprints/blob/main/07-retail-ecommerce) | Retail & E-commerce |
| 08 | [construction-real-estate](https://github.com/fprtm/atlas-blueprints/blob/main/08-construction-real-estate) | Construction & Real Estate |
| 09 | [energy-utilities](https://github.com/fprtm/atlas-blueprints/blob/main/09-energy-utilities) | Energy & Utilities |
| 10 | [mining-natural-resources](https://github.com/fprtm/atlas-blueprints/blob/main/10-mining-natural-resources) | Mining & Natural Resources |
| 11 | [transportation](https://github.com/fprtm/atlas-blueprints/blob/main/11-transportation) | Transportation |
| 12 | [telecommunications](https://github.com/fprtm/atlas-blueprints/blob/main/12-telecommunications) | Telecommunications |
| 13 | [media-entertainment](https://github.com/fprtm/atlas-blueprints/blob/main/13-media-entertainment) | Media & Entertainment |
| 14 | [education](https://github.com/fprtm/atlas-blueprints/blob/main/14-education) | Education |
| 15 | [government-public-sector](https://github.com/fprtm/atlas-blueprints/blob/main/15-government-public-sector) | Government & Public Sector |
| 16 | [legal-services](https://github.com/fprtm/atlas-blueprints/blob/main/16-legal-services) | Legal Services |
| 17 | [hospitality-tourism](https://github.com/fprtm/atlas-blueprints/blob/main/17-hospitality-tourism) | Hospitality & Tourism |
| 18 | [automotive](https://github.com/fprtm/atlas-blueprints/blob/main/18-automotive) | Automotive |
| 19 | [aerospace-defense](https://github.com/fprtm/atlas-blueprints/blob/main/19-aerospace-defense) | Aerospace & Defense |
| 20 | [professional-services](https://github.com/fprtm/atlas-blueprints/blob/main/20-professional-services) | Professional Services |
| 21 | [non-profit-social-sector](https://github.com/fprtm/atlas-blueprints/blob/main/21-non-profit-social-sector) | Non-Profit & Social Sector |
| 22 | [sports-fitness-wellness](https://github.com/fprtm/atlas-blueprints/blob/main/22-sports-fitness-wellness) | Sports, Fitness & Wellness |
| 23 | [fashion-apparel](https://github.com/fprtm/atlas-blueprints/blob/main/23-fashion-apparel) | Fashion & Apparel |
| 24 | [cybersecurity](https://github.com/fprtm/atlas-blueprints/blob/main/24-cybersecurity) | Cybersecurity |
| 25 | [sustainability-esg](https://github.com/fprtm/atlas-blueprints/blob/main/25-sustainability-esg) | Sustainability & ESG |

Daftar ini mengikuti urutan A–Y di `atlas-domain-knowledge.md` §8.