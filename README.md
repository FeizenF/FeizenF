<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=230&section=header&text=Feizen&fontSize=76&fontColor=E5B80B&fontAlignY=34&desc=Cyber%20Security%20%C2%B7%20Digital%20Forensics%20%C2%B7%20Developer&descSize=15&descAlign=center&descAlignY=58&textBg=false&stroke=E5B80B&strokeWidth=1&color=0:05070A,50:0D1117,100:2A2410" alt="Feizen" width="100%" />

<a href="https://github.com/FeizenF">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&pause=1100&color=E5B80B&center=true&vCenter=true&width=760&lines=Cyber+Security+Student;Digital+Forensics+%7C+Security+Fundamentals;Flutter+%2B+Web+Developer;Build+things.+Understand+systems." alt="Typing SVG" />
</a>

<br />

<a href="https://github.com/FeizenF">
  <img src="https://img.shields.io/badge/GitHub-FeizenF-0D1117?style=flat-square&logo=github&logoColor=E5B80B" alt="GitHub" />
</a>
<a href="mailto:Fernandabrian46@gmail.com">
  <img src="https://img.shields.io/badge/EMAIL-Contact-0D1117?style=flat-square&logo=gmail&logoColor=E5B80B" alt="Email" />
</a>
<img src="https://komarev.com/ghpvc/?username=FeizenF&style=flat-square&color=1C1C1C&label=PROFILE+VIEWS" alt="Profile views" />
<a href="https://github.com/FeizenF/FeizenF/actions/workflows/activity.yml">
  <img src="https://img.shields.io/github/actions/workflow/status/FeizenF/FeizenF/activity.yml?style=flat-square&label=ACTIVITY&logo=github&logoColor=E5B80B&color=1C1C1C" alt="Activity workflow status" />
</a>

</div>

<br />

## `01` // ABOUT

I'm an Informatics student working across **Cyber Security, Digital Forensics, and Software Development**.

Most of my work starts from the same question: how does this system actually work? I build the application to find out, then look at it from the other side: the data model, the storage, and what an attacker or an investigator would see.

```console
$ whoami
feizen · informatics student

$ pwd
informatics · cyber security · app development

$ cat focus.txt
security  forensics  web  mobile

$ status
online · open to collaboration

$ date -u
2026-11-24 · last sync 00:57 UTC
```

## `02` // FOCUS

`CYBER SECURITY` · `DIGITAL FORENSICS` · `WEB DEVELOPMENT` · `MOBILE DEVELOPMENT`

## `03` // STACK

**Languages**

<p align="left">
  <img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=E5B80B" alt="Python" />
  <img src="https://img.shields.io/badge/Dart-0D1117?style=flat-square&logo=dart&logoColor=E5B80B" alt="Dart" />
  <img src="https://img.shields.io/badge/PHP-0D1117?style=flat-square&logo=php&logoColor=E5B80B" alt="PHP" />
  <img src="https://img.shields.io/badge/JavaScript-0D1117?style=flat-square&logo=javascript&logoColor=E5B80B" alt="JavaScript" />
</p>

**Frameworks & Tools**

<p align="left">
  <img src="https://img.shields.io/badge/Flutter-0D1117?style=flat-square&logo=flutter&logoColor=E5B80B" alt="Flutter" />
  <img src="https://img.shields.io/badge/Flask-0D1117?style=flat-square&logo=flask&logoColor=E5B80B" alt="Flask" />
  <img src="https://img.shields.io/badge/Laravel-0D1117?style=flat-square&logo=laravel&logoColor=E5B80B" alt="Laravel" />
  <img src="https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=E5B80B" alt="React" />
  <img src="https://img.shields.io/badge/SQLite-0D1117?style=flat-square&logo=sqlite&logoColor=E5B80B" alt="SQLite" />
  <img src="https://img.shields.io/badge/MySQL-0D1117?style=flat-square&logo=mysql&logoColor=E5B80B" alt="MySQL" />
  <img src="https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=E5B80B" alt="Git" />
  <img src="https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=E5B80B" alt="Linux" />
</p>

## `04` // SELECTED WORK

<table>
<tr>
<td width="33%" valign="top">

### [fintrack](https://github.com/FeizenF/fintrack)

Offline personal finance manager for Android.

Multi-account ledger, budgets, savings goals, reports with charts, encrypted JSON backup.

`Flutter` `Dart` `Drift` `SQLite` `Riverpod`

</td>
<td width="33%" valign="top">

### [Student-App](https://github.com/FeizenF/Student-App)

Academic app for courses, grades, and GPA tracking.

Course and grade CRUD, automatic letter grades, live GPA calculation, local persistence.

`Flutter` `Dart` `Material 3`

</td>
<td width="33%" valign="top">

### [feizen-haven-hotel](https://github.com/FeizenF/feizen-haven-hotel)

Hotel booking system with room management and payments.

Public site, user dashboard, and admin panel behind Flask blueprints and SQL sessions.

`Flask` `Python` `MySQL` `Tailwind CSS`

</td>
</tr>
</table>

**Project notes**

- **fintrack** - the transaction ledger is the only source of truth; account balances are never stored as a column, always derived. Backup is AES-256-GCM with PBKDF2-derived keys, and restore validates the schema before swapping every table inside one Drift transaction. Local only: no server, no analytics.
- **Student-App** - GPA is computed from grade points weighted by credits, so the number moves the moment a grade changes. State survives restart through `SharedPreferences`.
- **feizen-haven-hotel** - routes split by concern (auth, booking, admin, API), admin views gated by role, booking state flows public listing to payment to confirmation.

## `05` // CURRENTLY

- **fintrack** - hardening the finished Android build: validation, backup edge cases, release packaging.
- **Web systems** - small applications focused on backend logic, database design, and practical CRUD flows.
- **Security and forensics** - studying file analysis, metadata, and the fundamentals behind defensive work.

## `06` // GITHUB ACTIVITY

<p align="center">
  <img height="180em" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=FeizenF&theme=github_dark" alt="GitHub stats" />
  <img height="180em" src="https://streak-stats.demolab.com/?user=FeizenF&hide_border=true&background=0D1117&ring=E5B80B&fire=FF8C00&currStreakLabel=E5B80B&sideLabels=C9D1D9&currStreakNum=C9D1D9&sideNums=C9D1D9&dates=6E7681" alt="GitHub streak" />
</p>

<p align="center">
  <img height="180em" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=FeizenF&theme=github_dark" alt="Top languages" />
  <img height="180em" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=FeizenF&theme=github_dark" alt="Most committed languages" />
</p>

## `07` // LEARNING

`Cyber Security` · `Network Security` · `Laravel` · `React`

<br />

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:2A2410,50:0D1117,100:05070A" alt="Footer" width="100%" />

<sub>Build things. Understand systems. Keep learning.</sub>

</div>
