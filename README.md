
# IMPERIUM SERVER 웹 v2 | IMPERIUM SERVER Website v2

⚡ **IMPERIUM SERVER v2**는 마인크래프트 유저들을 위한 최신 공식 커뮤니티 및 서버 소개 웹사이트입니다.  
This is the **v2 version** of the official community and server introduction website for Minecraft players.

v2에서는 기존 웹사이트 기능을 모두 포함하면서, **향상된 UI/UX, 반응형 디자인, 관리자 기능 강화, 프로젝트 & 팀원 소개 페이지**를 새롭게 제공합니다.  
Version 2 includes all previous features plus **enhanced UI/UX, responsive design, improved admin functionalities, and new project & crew introduction pages**.

---

## 🚀 프로젝트 개요 | Project Overview

**IMPERIUM SERVER v2**는 Django 기반으로 구축된 최신 서버 웹입니다.  
서버 콘텐츠와 커뮤니티 정보를 효율적으로 관리하고 전달하는 것을 목표로 합니다.  
IMPERIUM SERVER v2 is a Django-powered web project, designed to efficiently manage and deliver server content and community information.

---

## 🔧 주요 기능 | Key Features

- 📢 **서버 소개 및 공지사항 게시**  
  Server introduction and announcements

- 🛠️ **관리자 전용 CRUD 시스템 (공지/프로젝트/팀원)**  
  Admin-only CRUD system for notices, projects, and crew members

- 📱 **완전 반응형 디자인 (모바일/PC 대응)**  
  Fully responsive design for mobile and desktop

- 🔐 **reCAPTCHA v3 기반 스팸 방지 기능 (테스트되지 않음)**  
  Spam protection using Google reCAPTCHA v3 (Not tested)

---

## ⚙️ 기술 스택 | Tech Stack

| 항목 | 내용 |
|------|------|
| 백엔드 / Backend | Django (Python) |
| 프론트엔드 / Frontend | HTML (Jinja2), Tailwind CSS |
| 서버 / Server | Hypercorn (ASGI) |
| 데이터베이스 / Database | SQLite |
| 배포 / Deployment | Linux 서버 (Self-hosted) |
| 보안 / Security | Google reCAPTCHA v3 |

---

## 📂 프로젝트 구조 | Project Structure

```

wltp_website_v2/
├─ venv/                             # 가상 환경 설정 폴더
├─ about_crew/                       # 크루 소개 앱
├─ about_crewones/                   # 팀원 소개 앱
├─ about_crewones_settings           # 팀원의 컴퓨터 사양이나 게임 설정 소개 앱
├─ account/                          # 사용자 계정 관리 서비스
├─ notice/                           # 공지사항 앱
├─ projects/                         # 프로젝트 앱
├─ config/                           # Django 프로젝트 설정
├─ main/                             # 메인 앱 (홈, 네비게이션 등)
├─ blog/                             # 블로그 앱
├─ projects/                         # 프로젝트 소개 앱
├─ about_crewones/                   # 팀원 소개 앱
├─ media/                            # 이미지 등 미디어 정적 파일
├─ static/                           # 정적 파일 (CSS, JS)
├─ templates/                        # HTML 템플릿
├─ .gitignore
├─ README.md
├─ secrets.json
├─ start.sh
├─ testmode.sh
└─ manage.py

```

---

## 📫 문의 및 기여 | Contact & Contribution

오류 제보, 제안, 또는 기여는 GitHub 이슈 또는 Pull Request로 환영합니다.  
Bug reports, suggestions, or contributions are welcome via GitHub Issues or Pull Requests.

- GitHub: [https://github.com/wltp0321/wltp_website_v2](https://github.com/wltp0321/wltp_website_v2)

---

## 📌 참고 | Notes

- 이 프로젝트는 **v2 버전** 기준으로 Django 5.2.3 이상에서 개발되었습니다.
- Tailwind CSS를 사용하여 **현대적이고 반응형 UI**를 구현했습니다.
- 관리자(staff) 권한을 통해 **프로젝트/공지/팀원 CRUD 기능**을 사용할 수 있습니다.


2026-06-21 : 웹훅을 추가하였습니다
