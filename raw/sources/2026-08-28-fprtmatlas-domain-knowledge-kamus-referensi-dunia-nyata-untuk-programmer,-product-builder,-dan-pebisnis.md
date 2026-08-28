---
title: "2026-08-28-fprtm/atlas-domain-knowledge:-kamus-referensi-dunia-nyata-untuk-programmer,-product-builder,-dan-pebisnis"
source: "https://github.com/fprtm/atlas-domain-knowledge/blob/main/atlas-domain-knowledge.md"
author:
published:
created: 2026-08-28
description: "Kamus referensi dunia nyata untuk programmer, product builder, dan pebisnis - fprtm/atlas-domain-knowledge"
tags:
  - "clippings"
---
## Atlas Domain Knowledge

## Kamus Referensi Dunia Nyata untuk Programmer, Product Builder, dan Pebisnis

**Versi:** 1.0  
**Tanggal:** 22 Agustus 2026  
**Status:** Living reference / extensible ontology

---

## 0\. Tujuan Dokumen

Dokumen ini adalah kerangka referensi untuk memetakan **pengetahuan dunia nyata** menjadi struktur yang dapat dipakai untuk:

- memahami domain knowledge;
- merancang software, aplikasi, platform, dan AI system;
- menemukan kebutuhan bisnis;
- menerjemahkan pekerjaan manusia menjadi workflow dan system requirements;
- menentukan data yang diperlukan;
- menemukan peluang automation dan AI;
- membuat product discovery dan business model;
- membangun knowledge base, ontology, RAG, agent, atau decision-support system;
- menghubungkan industri, organisasi, pekerjaan, proses, sistem, data, aturan, dan teknologi.

Dokumen ini **bukan klaim sebagai daftar seluruh pengetahuan manusia**. Dunia nyata terlalu luas dan terus berubah. Sasaran dokumen ini adalah menyediakan **struktur yang cukup lengkap untuk dijadikan fondasi**, lalu dapat diperluas per industri atau per sistem.

Struktur utamanya:

```
WORLD
 ├── Domain Knowledge
 │    ├── Discipline
 │    ├── Subject
 │    ├── Concept
 │    └── Terminology
 │
 ├── Industry
 │    ├── Sector
 │    ├── Sub-industry
 │    └── Value Chain
 │
 ├── Organization
 │    ├── Company
 │    ├── Department
 │    └── Business Unit
 │
 ├── People
 │    ├── Role
 │    ├── Occupation
 │    ├── Skill
 │    └── Responsibility
 │
 ├── Work
 │    ├── Task
 │    ├── Process
 │    ├── Workflow
 │    └── Decision
 │
 ├── System
 │    ├── Application
 │    ├── Platform
 │    ├── Infrastructure
 │    └── Human + Machine System
 │
 ├── Information
 │    ├── Entity
 │    ├── Data
 │    ├── Document
 │    ├── Event
 │    └── Metric
 │
 ├── Rules
 │    ├── Law
 │    ├── Policy
 │    ├── Standard
 │    ├── Procedure
 │    └── Constraint
 │
 └── Technology
      ├── Software
      ├── Hardware
      ├── Network
      ├── AI
      └── Automation
```

---

## 1\. Prinsip Dasar

## 1.1 Domain knowledge bukan hanya "ilmu"

Domain knowledge adalah pengetahuan khusus yang dibutuhkan untuk memahami dan melakukan pekerjaan atau aktivitas dalam suatu domain.

Domain dapat berupa:

- ilmu;
- industri;
- profesi;
- organisasi;
- proses bisnis;
- sistem;
- produk;
- regulasi;
- komunitas;
- aktivitas sehari-hari;
- kombinasi beberapa domain.

Contoh:

```
Healthcare
→ Rumah sakit
→ Dokter
→ Diagnosis
→ Rekam medis
→ Data pasien
→ Clinical decision support
```

Di sini "healthcare" bukan sekadar ilmu kedokteran. Ia merupakan gabungan:

```
Medical knowledge
+ Hospital operations
+ Regulation
+ Administration
+ Finance
+ Information systems
+ Human behavior
```

## 1.2 Domain knowledge bersifat multidimensi

Satu objek dunia nyata dapat memiliki banyak perspektif.

Contoh: **rumah sakit**

Dari perspektif ilmu:

- kedokteran;
- biologi;
- farmakologi;
- psikologi.

Dari perspektif bisnis:

- revenue;
- cost;
- insurance;
- procurement;
- staffing.

Dari perspektif pekerjaan:

- dokter;
- perawat;
- apoteker;
- kasir;
- administrator.

Dari perspektif sistem:

- EMR;
- laboratory information system;
- pharmacy system;
- billing;
- scheduling.

Dari perspektif data:

- patient;
- encounter;
- diagnosis;
- medication;
- laboratory result;
- invoice.

Dari perspektif hukum:

- consent;
- privacy;
- medical record;
- licensing.

**Kesimpulan:** jangan memaksa satu domain menjadi satu pohon. Dunia nyata lebih tepat dimodelkan sebagai **graph**.

---

## 2\. Model Utama: Domain Knowledge Graph

Gunakan objek berikut sebagai vocabulary inti.

Entitas Arti

---

Domain wilayah pengetahuan/aktivitas Discipline cabang ilmu atau keahlian Industry aktivitas ekonomi/sektor Organization pelaku/organisasi Role peran dalam organisasi Occupation jenis pekerjaan Skill kemampuan melakukan pekerjaan Task pekerjaan/aktivitas spesifik Process rangkaian aktivitas Workflow urutan proses yang operasional Decision titik pengambilan keputusan System sistem manusia/teknologi Application software untuk fungsi tertentu Data Entity objek informasi Event kejadian yang mengubah keadaan Document artefak informasi Rule aturan Policy kebijakan Regulation regulasi Standard standar Metric ukuran KPI indikator performa Product sesuatu yang dijual/disediakan Service layanan Resource sumber daya Asset aset Risk risiko Control mekanisme pengendalian Stakeholder pihak berkepentingan Customer penerima nilai Supplier penyedia Technology teknologi yang memungkinkan sistem

---

## 3\. Hubungan Antarentitas

Hubungan yang sebaiknya tersedia:

```
Domain CONTAINS Discipline
Domain APPLIES_TO Industry
Industry CONTAINS SubIndustry
Industry HAS Organization
Organization HAS Department
Organization HAS Role
Role PERFORMS Task
Occupation REQUIRES Skill
Task BELONGS_TO Process
Process CONTAINS Workflow
Workflow PRODUCES Data
Workflow USES System
System STORES Data
System IMPLEMENTS Process
Decision USES Rule
Rule CONSTRAINS Process
Process PRODUCES Outcome
Outcome MEASURED_BY Metric
Product SERVES Customer
Customer GENERATES Demand
Supplier PROVIDES Resource
Resource SUPPORTS Process
Risk AFFECTS Process
Control MITIGATES Risk
Technology ENABLES System
```

Model seperti ini membuat dokumen dapat berkembang menjadi knowledge graph.

---

## 4\. Lapisan Pengetahuan

## Layer 1 --- Fundamental Knowledge

Pengetahuan yang relatif lintas domain:

- matematika;
- logika;
- statistik;
- bahasa;
- komunikasi;
- fisika;
- kimia;
- biologi;
- ilmu komputer;
- psikologi;
- ekonomi;
- hukum;
- filsafat;
- etika.

## Layer 2 --- Applied Knowledge

Penerapan ilmu:

- medicine;
- engineering;
- accounting;
- architecture;
- computer science;
- agriculture;
- finance;
- education.

## Layer 3 --- Industry Knowledge

Bagaimana pengetahuan dipakai dalam industri:

- banking;
- healthcare;
- manufacturing;
- retail;
- logistics;
- energy;
- telecommunications;
- construction.

## Layer 4 --- Organizational Knowledge

Bagaimana organisasi bekerja:

- strategy;
- finance;
- HR;
- operations;
- sales;
- marketing;
- procurement;
- legal;
- IT.

## Layer 5 --- Operational Knowledge

Bagaimana pekerjaan benar-benar dilakukan:

- task;
- SOP;
- workflow;
- decision;
- exception;
- escalation.

## Layer 6 --- System Knowledge

Bagaimana pekerjaan diwujudkan dalam sistem:

- application;
- database;
- API;
- workflow engine;
- integration;
- authentication;
- reporting;
- automation.

## Layer 7 --- Data & Decision Knowledge

Apa yang diketahui dan bagaimana keputusan dibuat:

- entity;
- event;
- state;
- metric;
- rule;
- model;
- prediction;
- decision.

---

## 5\. Peta Ilmu / Discipline Knowledge

## 5.1 Mathematics

### Cabang

- arithmetic;
- algebra;
- geometry;
- trigonometry;
- calculus;
- differential equations;
- linear algebra;
- discrete mathematics;
- probability;
- statistics;
- optimization;
- numerical methods;
- graph theory;
- game theory;
- mathematical logic.

### Digunakan oleh

- engineering;
- finance;
- economics;
- computer science;
- physics;
- AI;
- operations research;
- cryptography.

---

## 5.2 Computer Science

### Foundations

- algorithms;
- data structures;
- computational theory;
- programming languages;
- operating systems;
- computer architecture;
- databases;
- networking;
- distributed systems.

### Software Engineering

- requirements;
- architecture;
- design patterns;
- testing;
- CI/CD;
- observability;
- version control;
- reliability;
- security;
- maintenance.

### AI

- machine learning;
- deep learning;
- NLP;
- computer vision;
- speech;
- recommendation;
- reinforcement learning;
- generative AI;
- agents;
- knowledge representation;
- information retrieval.

---

## 5.3 Natural Sciences

### Physics

- mechanics;
- thermodynamics;
- electromagnetism;
- optics;
- quantum physics;
- relativity;
- materials physics;
- astrophysics.

### Chemistry

- organic;
- inorganic;
- physical chemistry;
- analytical chemistry;
- biochemistry;
- materials chemistry.

### Biology

- molecular biology;
- genetics;
- microbiology;
- ecology;
- evolution;
- zoology;
- botany;
- neuroscience.

### Earth Science

- geology;
- geophysics;
- meteorology;
- climatology;
- oceanography;
- hydrology;
- volcanology;
- seismology.

---

## 5.4 Engineering

### Cabang

- mechanical engineering;
- electrical engineering;
- civil engineering;
- chemical engineering;
- industrial engineering;
- software engineering;
- systems engineering;
- aerospace engineering;
- environmental engineering.

### Digunakan oleh

- manufacturing;
- construction;
- energy;
- automotive;
- aerospace & defense.

---

## 5.5 Medicine & Health Sciences

### Cabang

- clinical medicine;
- surgery;
- pharmacology;
- pathology;
- radiology;
- public health;
- epidemiology;
- nursing;
- nutrition;
- dentistry.

### Digunakan oleh

- hospital;
- clinic;
- pharmaceutical;
- insurance;
- public health agency.

---

## 5.6 Business & Management

### Cabang

- management;
- strategy;
- marketing;
- finance;
- accounting;
- operations management;
- organizational behavior;
- entrepreneurship;
- supply chain management.

### Digunakan oleh

- hampir semua industri;
- startup;
- corporate;
- consulting.

---

## Psychology

- cognitive;
- developmental;
- clinical;
- social;
- organizational;
- behavioral;
- educational.

## Sociology

- social structure;
- institutions;
- family;
- organizations;
- communities;
- inequality;
- social networks.

## Economics

- microeconomics;
- macroeconomics;
- econometrics;
- development;
- labor;
- international;
- behavioral economics.

## Political Science

- government;
- public policy;
- political institutions;
- international relations;
- geopolitics;
- public administration.

## Anthropology

- cultural;
- biological;
- linguistic;
- archaeology.

---

## 7\. Law, Regulation & Governance

## Major areas

- constitutional law;
- civil law;
- criminal law;
- commercial law;
- corporate law;
- tax;
- labor;
- intellectual property;
- environmental law;
- health law;
- financial regulation;
- data protection;
- technology law;
- international law.

## Operational artifacts

```
Law
→ Regulation
→ Policy
→ Standard
→ Procedure
→ SOP
→ Control
→ Audit
→ Evidence
```

Untuk software, aturan harus dapat diterjemahkan menjadi:

```
IF condition
THEN action
UNLESS exception
REQUIRE evidence
ESCALATE when violation
```

---

## 8\. Major Industry Map

Berikut peta industri tingkat tinggi yang dapat dijadikan root taxonomy.

## A. Agriculture & Food

### Subdomain

- agriculture;
- plantation;
- livestock;
- fisheries;
- aquaculture;
- food processing;
- food distribution;
- restaurants;
- food retail.

### Sistem

- farm management;
- inventory;
- traceability;
- cold chain;
- POS;
- procurement;
- food safety;
- production planning.

### AI opportunities

- yield prediction;
- disease detection;
- demand forecasting;
- route optimization;
- quality inspection.

---

## B. Healthcare & Life Sciences

### Subindustry

- hospitals;
- clinics;
- pharmacies;
- laboratories;
- medical devices;
- biotechnology;
- pharmaceuticals;
- insurance;
- telemedicine.

### Roles

- physician;
- nurse;
- pharmacist;
- laboratory analyst;
- radiologist;
- medical coder;
- administrator;
- researcher.

### Processes

- registration;
- triage;
- consultation;
- diagnosis;
- treatment;
- prescription;
- laboratory testing;
- imaging;
- billing;
- insurance claim;
- discharge;
- follow-up.

### Systems

- EMR/EHR;
- hospital information system;
- laboratory system;
- pharmacy system;
- radiology system;
- scheduling;
- billing;
- claims;
- telemedicine.

### Data

- patient;
- encounter;
- diagnosis;
- medication;
- allergy;
- procedure;
- laboratory result;
- imaging;
- invoice;
- claim.

### AI

- clinical decision support;
- medical imaging;
- triage;
- documentation;
- coding;
- drug discovery;
- patient risk prediction.

---

## C. Banking & Financial Services

### Subindustry

- retail banking;
- corporate banking;
- investment banking;
- asset management;
- insurance;
- fintech;
- payments;
- lending;
- securities.

### Processes

- onboarding;
- KYC;
- account opening;
- deposit;
- withdrawal;
- payment;
- transfer;
- lending;
- underwriting;
- collections;
- trading;
- settlement;
- reconciliation;
- fraud investigation.

### Systems

- core banking;
- payment gateway;
- ledger;
- CRM;
- loan management;
- credit scoring;
- fraud detection;
- trading platform;
- risk engine;
- treasury.

### Data

- customer;
- account;
- transaction;
- payment;
- loan;
- collateral;
- credit history;
- market data;
- risk exposure.

### AI

- fraud detection;
- credit scoring;
- AML monitoring;
- customer service;
- forecasting;
- portfolio optimization.

---

## D. Insurance

### Processes

- quotation;
- underwriting;
- policy issuance;
- premium collection;
- claim;
- assessment;
- settlement;
- renewal.

### Systems

- policy administration;
- claims;
- underwriting;
- actuarial;
- CRM;
- payment.

### Data

- policy;
- insured;
- premium;
- coverage;
- claim;
- incident;
- beneficiary.

---

## E. Manufacturing

### Industries

- automotive;
- electronics;
- chemicals;
- pharmaceuticals;
- textiles;
- food;
- machinery;
- consumer goods.

### Value chain

```
Supplier
→ Procurement
→ Receiving
→ Raw Material
→ Production
→ Quality Control
→ Packaging
→ Warehouse
→ Distribution
→ Customer
```

### Systems

- ERP;
- MES;
- WMS;
- QMS;
- PLM;
- SCM;
- maintenance;
- industrial IoT;
- SCADA.

### AI

- predictive maintenance;
- visual inspection;
- demand forecasting;
- process optimization;
- anomaly detection;
- production scheduling.

---

## F. Logistics & Supply Chain

### Processes

- procurement;
- sourcing;
- warehousing;
- inventory;
- order fulfillment;
- transportation;
- delivery;
- returns.

### Systems

- ERP;
- WMS;
- TMS;
- OMS;
- fleet management;
- route optimization;
- tracking.

### Data

- SKU;
- order;
- shipment;
- package;
- vehicle;
- driver;
- warehouse;
- location;
- inventory;
- delivery event.

---

## G. Retail & E-commerce

### Business areas

- merchandising;
- pricing;
- promotion;
- sales;
- customer service;
- inventory;
- fulfillment;
- loyalty.

### Systems

- POS;
- e-commerce;
- OMS;
- CRM;
- recommendation engine;
- inventory;
- payment.

### AI

- recommendation;
- personalization;
- demand forecasting;
- dynamic pricing;
- customer segmentation;
- fraud detection.

---

## H. Construction & Real Estate

### Subdomains

- architecture;
- civil engineering;
- construction;
- property development;
- property management;
- brokerage.

### Systems

- CAD;
- BIM;
- project management;
- construction management;
- property management;
- facility management.

### Data

- project;
- building;
- unit;
- floor;
- room;
- material;
- contractor;
- work order;
- lease;
- tenant.

---

## I. Energy & Utilities

### Subindustries

- electricity;
- oil & gas;
- solar;
- wind;
- geothermal;
- water;
- waste.

### Systems

- SCADA;
- grid management;
- asset management;
- energy management;
- billing;
- metering.

### AI

- load forecasting;
- predictive maintenance;
- anomaly detection;
- energy optimization.

---

## J. Mining & Natural Resources

### Processes

- exploration;
- surveying;
- extraction;
- processing;
- transport;
- environmental monitoring;
- rehabilitation.

### Systems

- fleet management;
- mine planning;
- geological modeling;
- equipment monitoring;
- safety management.

---

## K. Transportation

### Modes

- road;
- rail;
- aviation;
- maritime;
- public transit;
- ride-hailing.

### Systems

- booking;
- ticketing;
- dispatch;
- fleet;
- route planning;
- navigation;
- traffic management.

---

## L. Telecommunications

### Areas

- mobile;
- fixed broadband;
- fiber;
- enterprise connectivity;
- data center;
- IoT.

### Systems

- OSS;
- BSS;
- network management;
- provisioning;
- billing;
- customer management.

---

## M. Media & Entertainment

- publishing;
- television;
- film;
- music;
- gaming;
- streaming;
- advertising.

### Systems

- content management;
- recommendation;
- ad serving;
- streaming;
- digital rights;
- analytics.

---

## N. Education

### Organizations

- schools;
- universities;
- vocational institutions;
- tutoring;
- EdTech;
- corporate training.

### Processes

- admission;
- enrollment;
- teaching;
- assessment;
- grading;
- attendance;
- graduation;
- alumni.

### Systems

- LMS;
- SIS;
- exam;
- attendance;
- library;
- student analytics.

---

## O. Government & Public Sector

### Domains

- civil registration;
- taxation;
- licensing;
- public health;
- education;
- social assistance;
- transportation;
- public safety;
- urban planning.

### Systems

- identity;
- tax;
- licensing;
- public service portal;
- case management;
- benefits management;
- open data.

---

## P. Legal Services

### Processes

- intake;
- research;
- drafting;
- review;
- negotiation;
- litigation;
- compliance;
- contract management.

### Systems

- document management;
- matter management;
- contract lifecycle management;
- legal research;
- billing.

---

## Q. Hospitality & Tourism

- hotels;
- restaurants;
- travel agencies;
- attractions;
- events;
- airlines.

### Systems

- PMS;
- booking;
- POS;
- revenue management;
- CRM;
- channel management.

---

## R. Automotive

### Value chain

```
Design
→ Engineering
→ Supplier
→ Manufacturing
→ Distribution
→ Dealer
→ Sales
→ Financing
→ Service
→ Used Vehicle
→ Recycling
```

### Systems

- dealer management;
- service management;
- vehicle diagnostics;
- supply chain;
- manufacturing;
- connected vehicle.

---

## S. Aerospace & Defense

- aircraft;
- satellites;
- space;
- avionics;
- maintenance;
- mission systems;
- security.

Domain ini memiliki regulasi, safety, reliability, dan security requirements yang sangat tinggi.

---

## T. Professional Services

- consulting;
- accounting;
- auditing;
- law;
- engineering;
- architecture;
- recruitment;
- marketing agencies.

### Common systems

- CRM;
- project management;
- timesheet;
- billing;
- document management;
- knowledge management.

---

### Subdomain

- NGO;
- foundation;
- social enterprise;
- advocacy;
- humanitarian aid;
- community development.

### Processes

- program design;
- fundraising;
- grant management;
- volunteer management;
- beneficiary intake;
- impact reporting;
- compliance.

### Systems

- donor CRM;
- grant management system;
- volunteer management;
- fundraising platform;
- impact measurement.

### Data

- donor;
- donation;
- grant;
- program;
- beneficiary;
- volunteer;
- impact metric.

### AI

- donor segmentation;
- fraud detection (donation);
- impact prediction;
- grant matching.

---

## V. Sports, Fitness & Wellness

### Subdomain

- professional sports;
- fitness center;
- wellness/spa;
- sports league;
- sports media;
- personal training.

### Systems

- membership management;
- booking;
- wearable/fitness tracking;
- league management;
- ticketing.

### Data

- member;
- session;
- performance metric;
- team;
- match;
- ticket.

### AI

- performance analysis;
- injury prediction;
- personalized training plan;
- demand forecasting (class booking).

---

## W. Fashion & Apparel

### Value chain

```
Design
→ Sourcing
→ Manufacturing
→ Wholesale/Retail
→ E-commerce
→ Customer
→ Returns
```

### Systems

- PLM;
- ERP;
- POS;
- e-commerce;
- inventory;
- size/fit recommendation.

### AI

- trend forecasting;
- size recommendation;
- visual search;
- virtual try-on;
- demand forecasting.

---

## X. Cybersecurity

### Subdomain

- application security;
- network security;
- identity & access management;
- threat intelligence;
- incident response;
- managed security services.

### Systems

- SIEM;
- SOAR;
- EDR/XDR;
- vulnerability management;
- IAM;
- firewall/IDS-IPS.

### Data

- asset;
- vulnerability;
- threat;
- incident;
- log event;
- identity.

### AI

- anomaly detection;
- threat detection;
- phishing detection;
- automated triage.

---

## Y. Sustainability & ESG

### Subdomain

- carbon accounting;
- renewable energy;
- circular economy;
- ESG reporting;
- environmental compliance.

### Systems

- ESG reporting platform;
- carbon tracking;
- supply chain traceability.

### Data

- emission;
- energy usage;
- waste;
- supplier ESG score;
- compliance report.

### AI

- emission forecasting;
- anomaly detection (energy usage);
- supply chain risk scoring.

---

## 9\. Cross-Industry Corporate Functions

Hampir semua perusahaan memiliki fungsi berikut.

## Strategy

- vision;
- mission;
- objectives;
- OKR;
- competitive analysis;
- market analysis;
- business model.

## Finance

- accounting;
- budgeting;
- forecasting;
- treasury;
- tax;
- accounts payable;
- accounts receivable;
- financial reporting.

## Human Resources

- recruitment;
- onboarding;
- payroll;
- performance;
- learning;
- compensation;
- benefits;
- offboarding.

## Sales

- lead;
- qualification;
- opportunity;
- proposal;
- negotiation;
- contract;
- closing;
- account management.

## Marketing

- research;
- segmentation;
- positioning;
- campaign;
- content;
- advertising;
- SEO;
- CRM;
- analytics.

## Operations

- planning;
- execution;
- quality;
- capacity;
- scheduling;
- incident;
- continuous improvement.

## Procurement

- sourcing;
- vendor evaluation;
- quotation;
- purchase order;
- receiving;
- invoice matching.

## Legal

- contracts;
- compliance;
- intellectual property;
- disputes;
- regulatory affairs.

## IT

- infrastructure;
- software;
- security;
- support;
- data;
- architecture;
- governance.

## Customer Success

- onboarding;
- adoption;
- health score;
- renewal;
- upsell;
- churn prevention;
- advocacy.

## Data & Analytics

- data collection;
- data governance;
- data pipeline;
- reporting;
- business intelligence;
- data science;
- data quality.

## Risk & Compliance

- risk assessment;
- policy enforcement;
- regulatory compliance;
- audit;
- control testing;
- incident management.

---

## 10\. Occupation & Job Knowledge

Pekerjaan sebaiknya dimodelkan sebagai:

```
Occupation
→ Role
→ Responsibility
→ Task
→ Skill
→ Knowledge
→ Tool
→ Output
→ KPI
```

Contoh:

## Software Engineer

**Responsibilities**

- build software;
- maintain software;
- troubleshoot;
- review code;
- design architecture.

**Tasks**

- implement feature;
- write test;
- review pull request;
- debug incident;
- deploy service.

**Skills**

- programming;
- system design;
- testing;
- debugging;
- Git;
- cloud.

**Outputs**

- source code;
- API;
- deployment;
- documentation.

**KPI**

- reliability;
- delivery;
- defect rate;
- lead time;
- maintainability.

---

## Accountant

**Knowledge**

- accounting;
- tax;
- financial reporting;
- audit.

**Tasks**

- record transaction;
- reconcile account;
- prepare report;
- close period;
- calculate tax.

**Systems**

- accounting;
- ERP;
- spreadsheet;
- banking.

**Outputs**

- journal;
- ledger;
- financial statements;
- tax reports.

---

## Sales Representative

**Tasks**

- prospect;
- qualify;
- contact;
- demo;
- negotiate;
- close;
- follow up.

**Systems**

- CRM;
- email;
- communication;
- quotation;
- contract.

**Data**

- lead;
- contact;
- company;
- opportunity;
- activity;
- deal.

---

## Product Manager

**Responsibilities**

- define product vision;
- prioritize roadmap;
- gather requirements;
- coordinate stakeholders;
- validate solutions.

**Tasks**

- write PRD;
- run discovery interview;
- prioritize backlog;
- analyze metrics;
- run experiment.

**Skills**

- product strategy;
- user research;
- data analysis;
- communication;
- prioritization.

**Systems**

- roadmap tool;
- analytics;
- A/B testing;
- project management;
- CRM.

**Outputs**

- roadmap;
- PRD;
- feature spec;
- experiment result.

**KPI**

- adoption;
- retention;
- NPS;
- feature usage;
- time-to-market.

---

## Data Analyst

**Responsibilities**

- extract insight;
- build report;
- maintain dashboard;
- validate data quality.

**Tasks**

- write query;
- build dashboard;
- analyze trend;
- present finding;
- clean data.

**Skills**

- SQL;
- statistics;
- visualization;
- business acumen;
- storytelling.

**Systems**

- data warehouse;
- BI tool;
- spreadsheet;
- notebook.

**Outputs**

- dashboard;
- report;
- analysis;
- recommendation.

**KPI**

- decision impact;
- report accuracy;
- turnaround time.

---

## HR Business Partner

**Responsibilities**

- align HR strategy with business;
- support workforce planning;
- manage employee relations.

**Tasks**

- recruitment support;
- performance calibration;
- conflict resolution;
- policy advisory.

**Skills**

- employment law;
- negotiation;
- coaching;
- organizational design.

**Systems**

- HRIS;
- ATS;
- performance management.

**Outputs**

- workforce plan;
- policy;
- performance review.

**KPI**

- retention;
- time-to-hire;
- employee engagement.

---

## Customer Support Agent

**Responsibilities**

- resolve customer issue;
- document interaction;
- escalate complex case.

**Tasks**

- answer ticket;
- troubleshoot;
- process refund;
- update knowledge base.

**Skills**

- communication;
- product knowledge;
- empathy;
- troubleshooting.

**Systems**

- helpdesk/ticketing;
- CRM;
- knowledge base;
- chat.

**Data**

- ticket;
- customer;
- interaction;
- resolution.

**KPI**

- first response time;
- resolution time;
- CSAT;
- ticket backlog.

---

## 11\. Process Knowledge

Setiap proses dapat dimodelkan:

```
Trigger
→ Input
→ Actor
→ Task
→ Decision
→ Output
→ State Change
→ Exception
→ Escalation
→ Audit Trail
```

Contoh: **Purchase Order**

```
Purchase Request
→ Approval
→ Vendor Selection
→ Purchase Order
→ Supplier Confirmation
→ Delivery
→ Receiving
→ Invoice
→ 3-Way Match
→ Payment
```

### Process metadata

Setiap proses idealnya mempunyai:

- process\_id;
- name;
- owner;
- purpose;
- trigger;
- input;
- output;
- actors;
- systems;
- rules;
- SLA;
- KPI;
- risks;
- exceptions;
- audit requirements.

---

## 12\. Business System Knowledge

## 12.1 ERP

Mengintegrasikan:

- finance;
- procurement;
- inventory;
- sales;
- manufacturing;
- HR.

## 12.2 CRM

Mengelola:

- customer;
- lead;
- opportunity;
- interaction;
- campaign;
- account.

## 12.3 HRIS

Mengelola:

- employee;
- position;
- attendance;
- payroll;
- performance;
- leave.

## 12.4 SCM

Mengelola:

- supplier;
- sourcing;
- inventory;
- demand;
- supply;
- logistics.

## 12.5 WMS

Mengelola:

- warehouse;
- location;
- stock;
- receiving;
- picking;
- packing;
- shipping.

## 12.6 TMS

Mengelola:

- shipment;
- carrier;
- route;
- vehicle;
- delivery.

## 12.7 CMS

Mengelola:

- content;
- author;
- publication;
- media;
- version.

## 12.8 LMS

Mengelola:

- learner;
- course;
- lesson;
- assessment;
- grade;
- completion.

## 12.9 ITSM

Mengelola:

- incident;
- problem;
- change;
- service request;
- asset;
- configuration item.

## 12.10 BI / Data Platform

Mengelola:

- data source;
- pipeline;
- warehouse;
- dashboard;
- report;
- data quality.

## 12.11 Marketing Automation

Mengelola:

- campaign;
- audience segment;
- email;
- lead scoring;
- journey;
- attribution.

---

## 13\. Information System Knowledge

Sistem software dapat dilihat sebagai:

```
User
→ Interface
→ Application
→ Business Logic
→ Workflow
→ Database
→ Integration
→ Infrastructure
```

### Komponen

- frontend;
- backend;
- database;
- cache;
- queue;
- API;
- authentication;
- authorization;
- file storage;
- search;
- analytics;
- logging;
- monitoring;
- notification.

---

## 14\. Data Knowledge

## Core data types

### Master Data

Relatif stabil:

- customer;
- product;
- supplier;
- employee;
- location;
- account.

### Transaction Data

Terjadi karena aktivitas:

- order;
- payment;
- invoice;
- shipment;
- claim;
- booking.

### Event Data

Kejadian:

- login;
- click;
- delivery;
- machine failure;
- payment received.

### Reference Data

Nilai referensi:

- country;
- currency;
- category;
- status;
- unit.

### Document Data

- contract;
- invoice;
- receipt;
- report;
- medical record;
- policy.

### Sensor Data

- temperature;
- GPS;
- pressure;
- vibration;
- energy usage.

---

## 15\. Decision Knowledge

Banyak sistem sebenarnya adalah **decision system**.

Model:

```
Context
→ Evidence
→ Rules
→ Model
→ Decision
→ Action
→ Outcome
```

Contoh:

### Credit

```
Customer
→ Financial Data
→ Credit Rules
→ Risk Model
→ Credit Decision
→ Approve / Reject
```

### Healthcare

```
Patient
→ Symptoms + History + Tests
→ Clinical Rules
→ Clinical Model
→ Recommendation
→ Treatment decision
```

### E-commerce

```
User
→ Behavior
→ Recommendation Model
→ Ranked Products
→ Display
→ Purchase
```

---

## 16\. Rules & Constraints

Sistem nyata selalu mempunyai constraint.

## Jenis

- legal;
- financial;
- operational;
- safety;
- security;
- technical;
- ethical;
- organizational;
- contractual.

Contoh:

```
IF customer_age < minimum_age
THEN reject transaction
```

Tetapi sistem production-grade membutuhkan:

```
Rule
+ Effective Date
+ Jurisdiction
+ Version
+ Exception
+ Authority
+ Evidence
```

---

## 17\. Business Model Knowledge

Dari perspektif pebisnis, sistem harus menjawab:

```
Who?
→ Has what problem?
→ Why does it matter?
→ What value is created?
→ Who pays?
→ How much?
→ How often?
→ What are the costs?
→ What are the risks?
```

### Business model components

- customer segment;
- value proposition;
- channel;
- revenue;
- cost;
- key resources;
- key activities;
- partners;
- competitive advantage.

---

## 18\. Product Knowledge

Produk sebaiknya dipetakan:

```
Customer
→ Need
→ Problem
→ Job-to-be-Done
→ Solution
→ Feature
→ Workflow
→ Outcome
```

Contoh:

```
Warehouse Manager
→ Sulit mengetahui stok real-time
→ Stock discrepancy
→ Need inventory visibility
→ Inventory system
→ Stock dashboard
→ Receiving/Picking workflow
→ Accurate inventory
```

---

## 19\. System Discovery Framework untuk Programmer

Sebelum coding, tanyakan:

## A. Domain

- Industri apa?
- Apa istilah khususnya?
- Apa konsep utamanya?
- Apa aturan domain?

## B. Actor

- Siapa pengguna?
- Siapa decision maker?
- Siapa operator?
- Siapa admin?
- Siapa customer?
- Siapa pihak eksternal?

## C. Process

- Apa trigger?
- Apa input?
- Apa langkahnya?
- Apa keputusan?
- Apa output?
- Apa exception?

## D. Data

- Apa entity?
- Apa attribute?
- Apa relationship?
- Apa event?
- Apa historical data?

## E. Rules

- Apa yang wajib?
- Apa yang dilarang?
- Apa approval?
- Apa batasan?
- Apa SLA?

## F. System

- Apa yang harus otomatis?
- Apa yang harus manual?
- Apa integrasinya?
- Apa source of truth?

## G. Quality

- Apa KPI?
- Apa failure mode?
- Apa audit requirement?
- Apa security requirement?

---

## 20\. System Discovery Framework untuk Pebisnis

Pebisnis dapat memakai urutan:

```
Market
→ Customer
→ Problem
→ Workflow
→ Cost
→ Revenue
→ Risk
→ Data
→ Technology
```

Pertanyaan utama:

### Market

- siapa targetnya?
- seberapa besar?
- siapa kompetitor?

### Customer

- siapa pengguna?
- siapa pembayar?
- siapa decision maker?

### Problem

- masalah apa?
- seberapa sering?
- berapa mahal dampaknya?

### Workflow

- bagaimana proses sekarang?
- bagian mana yang lambat?
- bagian mana yang manual?

### Economics

- berapa cost?
- berapa revenue?
- berapa potential saving?
- berapa willingness to pay?

### Technology

- apa yang dapat diotomatisasi?
- apa yang harus tetap human-in-the-loop?
- apa data yang tersedia?

---

## 21\. AI System Mapping

Untuk menemukan use case AI:

```
Industry
→ Role
→ Task
→ Decision
→ Data
→ Pattern
→ AI Capability
→ Action
→ Business Outcome
```

## Capability map

### Prediction

- demand forecasting;
- risk prediction;
- failure prediction.

### Classification

- fraud;
- spam;
- diagnosis support;
- document classification.

### Ranking

- recommendations;
- search;
- lead prioritization.

### Generation

- document;
- email;
- report;
- code;
- content.

### Extraction

- invoice;
- contract;
- medical document;
- CV.

### Optimization

- route;
- schedule;
- pricing;
- inventory.

### Agents

- research;
- customer support;
- operations;
- workflow execution.

---

## 22\. Human-in-the-Loop

Tidak semua sistem harus full automation.

Model:

```
AI
→ Recommendation
→ Human Review
→ Decision
→ Execution
```

Cocok untuk:

- healthcare;
- legal;
- finance;
- safety;
- compliance;
- high-value transactions.

---

## 23\. Knowledge Base untuk AI

Jika domain knowledge akan digunakan oleh AI, struktur minimal:

```
domain:
  id:
  name:
  description:

concepts:
  - id:
    name:
    definition:
    synonyms:
    parent:
    related:

roles:
  - id:
    name:
    responsibilities:
    skills:

processes:
  - id:
    name:
    trigger:
    inputs:
    steps:
    outputs:
    exceptions:

rules:
  - id:
    condition:
    action:
    exceptions:
    authority:

entities:
  - id:
    name:
    attributes:
    relationships:

systems:
  - id:
    name:
    purpose:
    users:
    inputs:
    outputs:

metrics:
  - id:
    name:
    formula:
    target:
```

---

## 24\. Domain Ontology Template

Untuk setiap domain, buat folder:

```
domain/
├── README.md
├── concepts.md
├── terminology.md
├── industries.md
├── organizations.md
├── occupations.md
├── roles.md
├── skills.md
├── processes.md
├── workflows.md
├── systems.md
├── entities.md
├── data.md
├── events.md
├── rules.md
├── regulations.md
├── metrics.md
├── risks.md
├── products.md
├── services.md
├── use-cases.md
├── ai-use-cases.md
└── glossary.md
```

---

## 25\. Standard Entry untuk Setiap Konsep

Gunakan format:

```
id: healthcare.patient
name: Patient
type: entity
domain: healthcare

definition: >
  A person receiving or seeking healthcare services.

synonyms:
  - patient
  - care recipient

related:
  - healthcare.encounter
  - healthcare.provider
  - healthcare.diagnosis

used_by:
  - physician
  - nurse
  - administrator

systems:
  - EMR
  - hospital_information_system

data:
  - patient_id
  - name
  - date_of_birth
  - contact

rules:
  - privacy
  - consent

lifecycle:
  - registered
  - active
  - discharged
```

---

## 26\. Glossary Design

Setiap istilah idealnya memiliki:

- preferred term;
- alternative term;
- definition;
- domain;
- language;
- abbreviation;
- examples;
- related terms;
- broader term;
- narrower term;
- source;
- version;
- effective date.

Terminology sebaiknya dibedakan dari sekadar daftar kata. ISO 704:2022 memandang terminology work sebagai pekerjaan sistematis untuk mengumpulkan, mendeskripsikan, memproses, dan menyajikan konsep beserta designation/istilahnya; pendekatan tersebut berlaku lintas bidang seperti ilmiah, teknologi, industri, hukum, dan administrasi. citeturn0search0turn0search13

### Contoh entry

```
term: Purchase Order
domain: procurement
language: en
abbreviation: PO
definition: >
  A commercial document issued by a buyer to a seller, indicating type,
  quantity, and agreed price for products or services.
alternative_terms:
  - Order Pembelian
  - Surat Pesanan
broader_term: procurement document
narrower_term: blanket purchase order
related_terms:
  - invoice
  - goods_receipt_note
  - supplier
examples:
  - "PO #2026-0453 dikirim ke supplier untuk 500 unit raw material."
source: internal glossary
version: 1.0
effective_date: 2026-08-22
```
```
term: Service Level Agreement
domain: operations
language: en
abbreviation: SLA
definition: >
  A commitment between a service provider and a client that defines
  the expected level of service, including metrics and remedies.
alternative_terms:
  - Perjanjian Tingkat Layanan
broader_term: contract
narrower_term: operational level agreement
related_terms:
  - KPI
  - incident
  - escalation
source: umumnya diacu dari standar IT service management (mis. ISO/IEC 20000)
version: 1.0
effective_date: 2026-08-22
```

---

## 27\. Occupation Taxonomy

Untuk pekerjaan, jangan membuat taxonomy sepenuhnya dari nol.

ISCO-08 dari ILO menyediakan klasifikasi pekerjaan empat tingkat dengan 10 major groups, 43 sub-major groups, 130 minor groups, dan 436 unit groups. citeturn0search5turn0search9

Gunakan sebagai salah satu backbone:

```
Occupation
→ ISCO group
→ Local occupation
→ Role
→ Tasks
→ Skills
→ Knowledge
→ Tools
→ Outputs
```

Untuk pemetaan yang lebih kaya, ESCO menghubungkan occupation dengan knowledge, skills, competences, dan mapping ke ISCO-08. citeturn0search11

---

## 28\. Skill Taxonomy

Skill dapat dibagi:

## Technical

- programming;
- accounting;
- welding;
- diagnosis;
- CAD;
- data analysis.

## Cognitive

- analysis;
- problem solving;
- reasoning;
- decision making.

## Social

- communication;
- negotiation;
- leadership;
- collaboration.

## Operational

- equipment operation;
- inspection;
- maintenance;
- scheduling.

## Domain-specific

- clinical diagnosis;
- tax calculation;
- credit underwriting;
- geological interpretation.

---

## 29\. Value Chain

Untuk setiap industri, buat:

```
Raw Material
→ Supplier
→ Production
→ Distribution
→ Sales
→ Customer
→ After-sales
→ Recycling / Disposal
```

Kemudian petakan:

```
Value Chain
→ Business Process
→ Job
→ System
→ Data
→ KPI
→ Risk
→ Opportunity
```

Contoh manufaktur:

```
Procurement
→ Production
→ QC
→ Warehouse
→ Distribution
→ Dealer
→ Customer
```

Peluang sistem dapat muncul pada setiap node.

---

## 30\. Business Capability Map

Pisahkan **apa yang bisnis harus mampu lakukan** dari bagaimana software melakukannya.

Contoh:

```
Customer Management
├── Customer Acquisition
├── Customer Onboarding
├── Customer Support
└── Customer Retention

Financial Management
├── Billing
├── Payment
├── Accounting
├── Budgeting
└── Reporting
```

Capability bukan sama dengan feature.

Contoh:

```
Capability:
Inventory Management

Possible features:
- stock dashboard
- receiving
- picking
- stock adjustment
- stock transfer
- inventory report
```

---

## 31\. Enterprise Architecture View

Gunakan empat lapisan:

```
Business Architecture
        ↓
Application Architecture
        ↓
Data Architecture
        ↓
Technology Architecture
```

### Business

- strategy;
- capability;
- process;
- organization.

### Application

- application;
- service;
- API;
- integration.

### Data

- entity;
- database;
- data warehouse;
- data lake.

### Technology

- cloud;
- server;
- network;
- compute;
- storage;
- security.

---

## 32\. Requirement Mapping

Requirement sebaiknya ditelusuri:

```
Business Goal
→ Business Problem
→ User
→ Job
→ Process
→ Requirement
→ Feature
→ System Component
→ Data
→ Test
→ KPI
```

Contoh:

```
Goal:
Reduce warehouse stock discrepancy

Problem:
Inventory data tidak akurat

Actor:
Warehouse manager

Process:
Stock receiving

Requirement:
Setiap penerimaan harus tercatat

Feature:
Receiving module

Data:
Purchase Order
GRN
SKU
Quantity

KPI:
Inventory accuracy
```

---

## 33\. Event-Driven View

Banyak sistem lebih mudah dipahami sebagai event.

Contoh:

```
OrderCreated
→ PaymentReceived
→ OrderConfirmed
→ ItemPicked
→ ItemPacked
→ ShipmentCreated
→ ItemDelivered
```

Event harus dapat memiliki:

- timestamp;
- actor;
- source;
- entity;
- previous state;
- new state;
- metadata.

---

## 34\. State Machine View

Entity sering memiliki lifecycle.

Contoh Order:

```
Draft
 ↓
Submitted
 ↓
Confirmed
 ↓
Paid
 ↓
Processing
 ↓
Shipped
 ↓
Delivered
 ↓
Completed
```

Dengan exception:

```
Cancelled
Refunded
Failed
Returned
```

State machine sangat berguna untuk programmer karena mengubah domain knowledge menjadi behavior sistem.

---

## 35\. Risk Knowledge

Setiap domain memiliki risk taxonomy.

## Risk types

- financial;
- operational;
- legal;
- compliance;
- security;
- privacy;
- safety;
- reputational;
- strategic;
- technical.

Model:

```
Risk
→ Cause
→ Event
→ Impact
→ Likelihood
→ Control
→ Mitigation
→ Owner
```

---

## 36\. Metrics & KPI

Setiap sistem sebaiknya memiliki:

### Input metrics

- volume;
- capacity;
- resources.

### Process metrics

- time;
- throughput;
- error;
- utilization.

### Output metrics

- quantity;
- quality;
- completion.

### Business metrics

- revenue;
- cost;
- margin;
- retention;
- conversion.

### Risk metrics

- incident;
- loss;
- fraud;
- failure.

---

## 37\. Reference Architecture untuk Sistem Bisnis

Template generik:

```
┌──────────────┐
       │   Customer   │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │   Channel    │
       │ Web/Mobile   │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │ Application  │
       └──────┬───────┘
              ↓
    ┌────────────────────┐
    │ Domain / Workflow  │
    └─────────┬──────────┘
              ↓
    ┌────────────────────┐
    │      Data         │
    └─────────┬──────────┘
              ↓
┌────────────────────────────┐
│ Integration / External API │
└────────────────────────────┘
```

---

## 38\. Product Discovery Template

Sebelum membangun:

```
1. Industry
2. Customer
3. Role
4. Job
5. Problem
6. Current workflow
7. Pain point
8. Cost of problem
9. Desired outcome
10. Existing solution
11. Data available
12. Rules
13. Technology
14. MVP
15. Business model
16. KPI
17. Risk
```

---

## 39\. System Design Template

Setelah domain dipahami:

```
Domain
→ Actors
→ Use Cases
→ Processes
→ Entities
→ State
→ Rules
→ Events
→ APIs
→ Storage
→ Integrations
→ Security
→ Observability
```

---

## 40\. Example End-to-End: Warehouse Management

## Domain

Logistics / Supply Chain

## Industry

Retail / Manufacturing / 3PL

## Organization

Warehouse operator

## Roles

- warehouse manager;
- receiving clerk;
- picker;
- packer;
- dispatcher.

## Processes

```
Receiving
Putaway
Picking
Packing
Shipping
Stock Count
Return
```

## Core entities

```
Warehouse
Location
SKU
Inventory
Lot
SerialNumber
PurchaseOrder
SalesOrder
Shipment
Package
Employee
```

## Systems

```
WMS
ERP
OMS
TMS
Scanner
Printer
```

## Events

```
GoodsReceived
StockMoved
OrderReleased
ItemPicked
PackagePacked
ShipmentDispatched
ShipmentDelivered
```

## Business metrics

```
Inventory Accuracy
Order Accuracy
Pick Rate
Dock-to-Stock Time
Order Cycle Time
On-Time Shipment
```

## AI

```
Demand Forecasting
Slotting Optimization
Picking Route Optimization
Anomaly Detection
Labor Forecasting
```

---

## 41\. Example End-to-End: Restaurant System

## Domain

Hospitality / Food Service

## Roles

- owner;
- manager;
- cashier;
- waiter;
- kitchen staff;
- purchasing staff.

## Processes

```
Reservation
Seating
Order
Kitchen Preparation
Serving
Payment
Inventory
Procurement
Closing
```

## Systems

- POS;
- reservation;
- kitchen display;
- inventory;
- accounting;
- CRM.

## Entities

- customer;
- table;
- menu item;
- order;
- order item;
- payment;
- ingredient;
- supplier;
- purchase order.

## AI

- demand forecasting;
- menu recommendation;
- staffing prediction;
- inventory forecasting;
- review analysis.

---

## 42\. Example End-to-End: SaaS B2B

## Industry

Software

## Customer

Business

## Roles

```
Buyer
Admin
Manager
Operator
End User
```

## Funnel

```
Lead
→ Demo
→ Trial
→ Activation
→ Subscription
→ Renewal
```

## Systems

- website;
- CRM;
- product;
- billing;
- support;
- analytics.

## Data

- account;
- user;
- subscription;
- invoice;
- usage;
- feature event;
- support ticket.

## KPI

- acquisition;
- activation;
- conversion;
- MRR;
- ARR;
- churn;
- retention;
- LTV;
- CAC.

---

## 43\. How to Turn This Atlas into a Real Knowledge Repository

Gunakan struktur:

```
atlas/
├── README.md
├── ontology/
│   ├── entities.md
│   ├── relations.md
│   ├── taxonomy.md
│   └── schema.yaml
│
├── disciplines/
│   ├── mathematics/
│   ├── computer-science/
│   ├── biology/
│   ├── economics/
│   └── law/
│
├── industries/
│   ├── healthcare/
│   ├── finance/
│   ├── manufacturing/
│   ├── logistics/
│   ├── retail/
│   ├── education/
│   └── ...
│
├── occupations/
│   ├── software-engineer/
│   ├── doctor/
│   ├── accountant/
│   └── ...
│
├── systems/
│   ├── erp/
│   ├── crm/
│   ├── wms/
│   ├── lms/
│   └── ...
│
├── processes/
│   ├── procurement/
│   ├── sales/
│   ├── onboarding/
│   └── ...
│
├── data/
│   ├── entities/
│   ├── events/
│   ├── documents/
│   └── metrics/
│
└── glossary/
    ├── id.md
    ├── en.md
    └── ...
```

---

Gunakan ID stabil.

```
discipline.computer-science
industry.healthcare
industry.banking
occupation.software-engineer
role.warehouse-manager
process.order-fulfillment
system.wms
entity.customer
entity.product
event.order-created
metric.inventory-accuracy
rule.credit.minimum-age
```

Jangan menggunakan nama display sebagai primary key.

---

## 45\. Versioning

Domain knowledge berubah.

Setiap entry sebaiknya memiliki:

```
version: 1.0
status: active
created_at:
updated_at:
effective_from:
effective_until:
source:
authority:
confidence:
```

Untuk regulasi, policy, dan terminology, versioning sangat penting.

---

## 46\. Source & Authority

Tidak semua knowledge mempunyai tingkat otoritas yang sama.

Gunakan:

```
Tier 1
Official law / regulation / standard

Tier 2
Government / professional body

Tier 3
Academic / research institution

Tier 4
Industry documentation

Tier 5
Expert practice

Tier 6
Community / anecdotal knowledge
```

Untuk AI, simpan provenance:

```
Claim
→ Source
→ Author
→ Date
→ Authority
→ Evidence
```

---

## 47\. Confidence

Pengetahuan dapat diberi confidence:

```
verified
high
medium
low
uncertain
deprecated
```

Jangan mencampur fakta resmi dengan opini tanpa metadata.

---

## 48\. Multilingual Domain Knowledge

Karena istilah dunia nyata memiliki sinonim:

```
concept: purchase_order

preferred:
  en: Purchase Order
  id: Pesanan Pembelian

synonyms:
  en:
    - PO
  id:
    - Surat Pesanan
    - Order Pembelian

related:
  - procurement
  - supplier
  - invoice
```

Ini sangat penting untuk:

- search;
- RAG;
- chatbot;
- translation;
- multilingual software.

---

## 49\. Domain Knowledge → Database

Contoh:

```
Customer
Product
Order
OrderItem
Payment
Shipment
```

Relationship:

```
Customer 1 ─── N Order
Order 1 ─── N OrderItem
Product 1 ─── N OrderItem
Order 1 ─── N Payment
Order 1 ─── 1 Shipment
```

Domain knowledge menentukan entity dan relationship.

---

## 50\. Domain Knowledge → API

Contoh:

```
POST /orders
GET /orders/{id}
POST /orders/{id}/confirm
POST /orders/{id}/cancel
POST /orders/{id}/pay
POST /orders/{id}/ship
```

Endpoint bukan sekadar keputusan teknis.

Ia merepresentasikan **domain action**.

---

## 51\. Domain Knowledge → UI

UI juga berasal dari domain.

Warehouse manager membutuhkan:

- stock;
- location;
- receiving;
- picking;
- shipment.

Sales membutuhkan:

- lead;
- opportunity;
- pipeline;
- customer.

Dokter membutuhkan:

- patient;
- encounter;
- diagnosis;
- medication.

Jangan mulai dari:

> "Halaman apa yang mau dibuat?"

Mulai dari:

> "Pekerjaan apa yang harus dilakukan user?"

---

## 52\. Domain Knowledge → AI Agent

Agent yang baik harus mengetahui:

```
Role
→ Goal
→ Context
→ Available Tools
→ Rules
→ Permissions
→ Workflow
→ Data
→ Escalation
```

Contoh warehouse agent:

```
Goal:
Reduce delayed shipments

Tools:
- WMS
- TMS
- inventory API

Knowledge:
- warehouse SOP
- shipment SLA
- carrier rules

Actions:
- check inventory
- check shipment
- recommend priority

Restrictions:
- cannot modify shipment without approval
```

---

## 53\. Business + Programmer Shared Language

Masalah besar dalam pembangunan software adalah:

```
Business language ≠ Technical language
```

Atlas ini menjadi **translation layer**.

Contoh:

```
Business:
"Order sudah dibayar."

Domain:
Payment received.

System:
Payment.status = succeeded.

Event:
PaymentReceived.

Database:
payment.status = 'PAID'.

API:
POST /payments/{id}/confirm.

Analytics:
GMV += order.total.
```

Satu konsep dunia nyata diterjemahkan ke berbagai layer.

---

## 54\. Anti-Pattern

## Jangan:

### 1\. Membuat taxonomy hanya berdasarkan software

Karena software mengikuti domain, bukan sebaliknya.

### 2\. Menganggap satu industri = satu domain

Healthcare memiliki banyak subdomain.

### 3\. Menganggap role = occupation

Doctor adalah occupation.

Clinical Director adalah role.

### 4\. Menganggap process = feature

"Order fulfillment" adalah process.

"Order tracking screen" adalah feature.

### 5\. Mengabaikan exception

Dunia nyata penuh dengan:

- cancel;
- refund;
- failure;
- dispute;
- retry;
- approval;
- escalation.

### 6\. Mengabaikan manusia

Sistem production biasanya adalah:

```
Human
+
Process
+
Software
+
Data
+
Rules
```

---

## 55\. Master Meta-Model

Model paling penting dalam Atlas:

```
┌──────────────┐
                │   DOMAIN     │
                └──────┬───────┘
                       │
     ┌─────────────────┼──────────────────┐
     ↓                 ↓                  ↓
DISCIPLINE          INDUSTRY          REGULATION
     │                 │                  │
     ↓                 ↓                  ↓
 KNOWLEDGE        ORGANIZATION           RULE
                       │
                       ↓
                     ROLE
                       │
                       ↓
                    TASK
                       │
                       ↓
                    PROCESS
                       │
            ┌──────────┼──────────┐
            ↓          ↓          ↓
         SYSTEM      DATA       DECISION
            │          │          │
            └──────────┼──────────┘
                       ↓
                    OUTCOME
                       │
                       ↓
                      KPI
                       │
                       ↓
                BUSINESS VALUE
```

Ini adalah inti dari keseluruhan dokumen.

---

## 56\. The 12 Questions

Jika hanya boleh mengingat satu framework, gunakan 12 pertanyaan:

1. **Domain apa?**
2. **Siapa yang terlibat?**
3. **Apa pekerjaan mereka?**
4. **Apa tujuan mereka?**
5. **Apa prosesnya?**
6. **Apa keputusan yang dibuat?**
7. **Apa aturan yang berlaku?**
8. **Apa data yang dibutuhkan?**
9. **Sistem apa yang digunakan?**
10. **Apa output-nya?**
11. **Bagaimana keberhasilan diukur?**
12. **Bagaimana teknologi dapat memperbaikinya?**

Jika 12 pertanyaan ini terjawab, biasanya kita sudah memiliki fondasi kuat untuk merancang sebuah sistem.

---

## 57\. Master Workflow: Dari Ide ke Sistem

```
IDEA
 ↓
INDUSTRY
 ↓
CUSTOMER
 ↓
ROLE
 ↓
JOB
 ↓
PROBLEM
 ↓
PROCESS
 ↓
DECISION
 ↓
RULE
 ↓
DATA
 ↓
SYSTEM
 ↓
FEATURE
 ↓
ARCHITECTURE
 ↓
IMPLEMENTATION
 ↓
METRIC
 ↓
BUSINESS OUTCOME
```

---

## 58\. Master Checklist untuk Programmer

- Pahami domain.
- Kumpulkan terminology.
- Identifikasi actor.
- Identifikasi occupation dan role.
- Petakan task.
- Petakan workflow.
- Identifikasi business rules.
- Identifikasi entity.
- Identifikasi state.
- Identifikasi event.
- Identifikasi integration.
- Identifikasi permission.
- Identifikasi audit requirement.
- Identifikasi KPI.
- Buat domain model.
- Buat API model.
- Buat data model.
- Buat UI berdasarkan workflow.
- Uji dengan scenario nyata.
- Uji exception.

---

## 59\. Master Checklist untuk Pebisnis

- Siapa customer?
- Siapa user?
- Siapa payer?
- Apa problem?
- Berapa cost problem?
- Bagaimana proses saat ini?
- Bagian mana yang paling mahal?
- Bagian mana yang paling lambat?
- Bagian mana yang rawan error?
- Apa existing solution?
- Apa competitive advantage?
- Apa data yang tersedia?
- Apa constraint?
- Apa regulatory risk?
- Apa ROI?
- Apa MVP?
- Apa metric sukses?
- Apa peluang automation?
- Apa peluang AI?
- Apa yang tetap harus dilakukan manusia?

---

## 60\. Roadmap Pengembangan Atlas

Dokumen ini sebaiknya tidak dianggap selesai.

## Phase 1 --- Core Ontology

Bangun:

- entities;
- relationships;
- taxonomy;
- terminology.

## Phase 2 --- Major Domains

Bangun:

- 20--30 industri utama;
- discipline map;
- occupation map.

## Phase 3 --- Process Library

Bangun:

- business process;
- workflow;
- decision;
- state machine.

## Phase 4 --- System Library

Bangun:

- ERP;
- CRM;
- WMS;
- TMS;
- HRIS;
- LMS;
- POS;
- CMS;
- BI;
- data platform.

## Phase 5 --- Data Ontology

Bangun:

- entities;
- events;
- documents;
- metrics;
- relationships.

## Phase 6 --- AI Use Case Library

Untuk setiap task:

```
Task
→ Data
→ AI capability
→ Human involvement
→ Risk
→ Expected outcome
```

## Phase 7 --- Industry Deep Dive

Pilih satu industri.

Contoh:

```
Healthcare
→ Hospital
→ Emergency Department
→ Triage
→ Patient flow
→ Clinical decision
→ EMR
→ AI
```

Kemudian ulangi untuk industri lain.

---

## 61\. Prinsip Akhir

Atlas ini sebaiknya diperlakukan sebagai **knowledge graph yang hidup**, bukan buku yang sekali dibuat lalu selesai.

Dunia nyata:

```
berubah
→ melahirkan konsep baru
→ melahirkan pekerjaan baru
→ melahirkan proses baru
→ melahirkan software baru
→ menghasilkan data baru
→ menghasilkan aturan baru
```

Karena itu struktur yang paling tahan lama bukan daftar statis, melainkan hubungan:

```
KNOWLEDGE
   ↕
INDUSTRY
   ↕
ORGANIZATION
   ↕
ROLE
   ↕
TASK
   ↕
PROCESS
   ↕
SYSTEM
   ↕
DATA
   ↕
DECISION
   ↕
OUTCOME
   ↕
BUSINESS VALUE
```

**Inilah mental model utama untuk membangun sistem dunia nyata.**

---

## Appendix A --- Quick Domain Template

```
domain:
  id:
  name:
  definition:

disciplines:
  - id:
    name:

industries:
  - id:
    name:

organizations:
  - id:
    name:

occupations:
  - id:
    name:

roles:
  - id:
    name:

skills:
  - id:
    name:

processes:
  - id:
    name:
    trigger:
    inputs:
    outputs:

workflows:
  - id:
    process:
    steps:

entities:
  - id:
    name:
    attributes:

events:
  - id:
    name:

rules:
  - id:
    name:
    condition:
    action:

systems:
  - id:
    name:
    purpose:

metrics:
  - id:
    name:
    formula:

risks:
  - id:
    name:
    mitigation:

ai_use_cases:
  - id:
    task:
    capability:
    human_review:
    expected_outcome:
```

---

## Appendix B --- Minimal Graph Schema

```
Node:
  id
  type
  name
  definition
  domain
  source
  version
  status

Edge:
  from
  relation
  to
  source
  confidence
  valid_from
  valid_until
```

Contoh:

```
industry.healthcare
  HAS
occupation.doctor

occupation.doctor
  PERFORMS
task.diagnose-patient

task.diagnose-patient
  USES
entity.patient-data

task.diagnose-patient
  SUPPORTED_BY
system.emr

task.diagnose-patient
  PRODUCES
entity.diagnosis

entity.diagnosis
  MEASURED_BY
metric.diagnostic-accuracy
```

---

Jika Atlas ini nantinya dikembangkan menjadi proyek serius, tambahkan:

1. **Taxonomy**
2. **Ontology**
3. **Knowledge graph**
4. **Terminology/glossary**
5. **Occupation graph**
6. **Skill graph**
7. **Industry graph**
8. **Business process library**
9. **System catalog**
10. **Data ontology**
11. **Regulatory knowledge**
12. **Decision models**
13. **AI capability map**
14. **Use-case library**
15. **Reference architectures**
16. **API patterns**
17. **Security patterns**
18. **KPI library**
19. **Risk library**
20. **Source/provenance layer**

Dengan begitu, Atlas bukan hanya menjadi "kamus", tetapi dapat menjadi **referensi untuk discovery, product design, system architecture, software engineering, business analysis, dan AI engineering**.

---

## Appendix D --- Referensi Kerangka Klasifikasi

Atlas ini sebaiknya tidak menggantikan taxonomy resmi. Gunakan taxonomy resmi sebagai sumber/anchor ketika relevan.

- **ISO 704:2022** --- prinsip dan metode terminology work; berguna sebagai dasar untuk memodelkan konsep, istilah, definisi, dan hubungan terminologis. ISO menyatakan standar ini berlaku pada bidang ilmiah, teknologi, industri, hukum, administrasi, dan bidang pengetahuan lainnya.
- **ILO ISCO-08** --- klasifikasi pekerjaan internasional dengan struktur hierarkis empat tingkat dan 436 unit groups.
- **ESCO** --- model occupation dan skills yang menghubungkan occupation dengan knowledge, skills, competences, serta mapping ke ISCO-08.

Referensi tersebut dipakai sebagai **building blocks**, bukan sebagai satu-satunya taxonomy untuk seluruh Atlas. Dunia bisnis dan sistem software membutuhkan lapisan tambahan seperti proses, data, sistem, rules, events, dan KPI.