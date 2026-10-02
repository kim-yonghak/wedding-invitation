# 모바일 청첩장 프로젝트 인수인계 · 새 AI 계정용

작성일: 2026-10-02 · 기준 소스 버전: **1.0.2**

이 문서는 이전 대화 없이 같은 청첩장을 이어서 수정하기 위한 작업 지침이다. 실제 소스는 함께 전달하는 `olive-wedding-project.zip`에 있다. 문서만으로 기존 사진과 코드를 완전히 복원할 수는 없으므로, 새 계정에 **이 MD와 소스 ZIP을 함께 첨부**한다.

## 1. 이 문서를 받은 AI가 먼저 할 일

당신은 사용자가 제작 중인 한국어 모바일 청첩장의 유지보수를 맡는다. 아래 내용을 읽고 첨부 소스를 확인한 뒤, 사용자가 말하는 수정 사항을 기존 프로젝트에 직접 반영한다.

1. 소스 ZIP을 풀고 `olive-wedding/package.json`의 버전을 확인한다. 이 문서의 기준은 1.0.2이며, 더 최신 파일이 첨부되었다면 최신 파일과 그 변경 내역을 우선한다.
2. `README.md`, `CHANGELOG.md`, `TEST_REPORT.md`, `src/config.ts`를 먼저 읽고 요청과 관련된 구현 파일을 확인한다.
3. 기존 디자인과 기능을 유지하면서 요청한 부분을 수정한다. 처음부터 비슷한 사이트를 새로 만들지 않는다.
4. 수정 가능한 환경이라면 설명만 하지 말고 실제 파일 수정, 필요한 검증, 다운로드 가능한 결과물 제작까지 진행한다.
5. 사소한 구현 선택은 기존 코드와 이 문서를 기준으로 판단한다. 이름·날짜·실제 사진 등 정확한 사용자 정보가 없으면 임의의 실제 값으로 바꾸지 않는다.
6. 수정 후 새 소스 ZIP과 GitHub 업로드용 파일을 제공한다. 버전과 `CHANGELOG.md`를 함께 갱신하고, 실제로 확인한 검증 결과만 기록한다.
7. 한국어로 간단히 설명한다. 사용자는 GitHub 웹 화면에서 파일을 올리는 방식을 사용했으므로 업로드 경로와 파일명을 구체적으로 안내한다.
8. 파일 제작 완료와 원격 배포 완료를 구분한다. 계정·저장소 접근 권한이 없는 상태에서 GitHub에 반영했다고 말하지 않는다.

### 소스가 없을 때

- 먼저 첨부 파일과 접근 가능한 저장소에 원본 소스가 있는지 확인한다.
- GitHub 저장소에 배포용 `index.html`만 있을 수 있다. 이 파일은 JavaScript·CSS·사진이 포함된 빌드 결과물이므로, 원본 React 소스가 있다고 가정하면 안 된다.
- 원본이 없으면 사용자에게 `olive-wedding-project.zip`을 요청한다. 기존 계정의 파일 링크나 임시 작업 경로는 새 계정에서 접근된다고 가정하지 않는다.
- 배포된 사이트를 보기만 한 상태에서 전체 프로젝트를 확보했다고 말하지 않는다.

## 2. 프로젝트와 전달 파일

| 항목 | 현재 정보 |
| --- | --- |
| 프로젝트 | 우리의 다음, 함께 — 올리브·라임 모바일 청첩장 |
| 사용자 | 김용학 / GitHub `kim-yonghak` |
| 공개 사이트 | https://kim-yonghak.github.io/wedding-invitation/ |
| GitHub 저장소 주소 | https://github.com/kim-yonghak/wedding-invitation |
| 현재 소스 버전 | 1.0.2 |
| 원본 프로젝트 | `olive-wedding-project.zip` 안의 `olive-wedding/` |
| 로컬 실행용 단독 파일 | `wedding-invitation.html` |
| 마지막 업로드 패키지 | `kakao-preview-update.zip` — 최상위에 `index.html`, `og-preview-v1.jpg` 두 파일 |
| 미리보기 이미지 URL | https://kim-yonghak.github.io/wedding-invitation/og-preview-v1.jpg |
| 커스텀 도메인 | 별도 도메인이 확정되었다는 기록 없음. 현재는 위 GitHub Pages 주소 사용 |

**제작한 소스와 실제 서버 상태는 구분한다.** 사용자는 GitHub Pages 배포 성공을 확인했다. 1.0.2는 카카오톡 미리보기 설정을 추가하고 업로드 파일까지 전달한 버전이다. 제작 측에서는 수정 파일의 원격 업로드 및 실제 카카오톡 카드 표시를 직접 검증하지 않았다. 이후 사용자가 정상 동작을 확인했다면 그 정보를 이어서 기록한다.

## 3. 지금까지의 진행 과정과 확정된 결정

| 순서 | 요청·진행 내용 | 결과 |
| --- | --- | --- |
| 1 | 한국어 모바일 청첩장 제작, 테스트 사진도 임시 생성 | 11개 섹션과 임시 사진 7장, 로컬 입력 저장, 클라우드 연결 코드 제작 |
| 2 | 첫 진입 때 휴대폰 번호 등이 보이는 입력창 제거 요청 | 자동으로 열리던 RSVP 바텀시트 제거. 사용자가 버튼을 눌렀을 때만 열리도록 변경 |
| 3 | 카카오톡에서 링크로 열 수 있는지, Git으로 배포 가능한지 문의 | 정적 웹 배포 및 GitHub Pages 방식 안내 |
| 4 | Custom domain과 Visit site 위치 문의 | GitHub Pages 배포 과정을 안내했고 사용자가 접속 성공 확인 |
| 5 | 카카오톡 링크 미리보기에 사진 표시 요청 | 공개 주소를 받아 정적 OG 태그와 별도 공개 JPG 추가, 업로드용 ZIP 제공 |
| 6 | 다른 AI 계정에서 이어서 작업할 인수인계 요청 | 이 문서와 최신 소스 ZIP 제공 |

### 반드시 유지할 최신 결정

- **처음 접속할 때 RSVP나 연락처 입력창을 자동으로 띄우지 않는다.** 최초 요청의 ‘2초 후 자동 팝업, 하루 한 번’은 이후 사용자 요청으로 폐기되었다.
- ‘오늘 하루 보지 않기’ 체크박스도 제거된 상태다. 사용자가 다시 요청하지 않는 한 복원하지 않는다.
- RSVP 기능 자체는 남아 있다. **‘참석 의사 전달하기’ 버튼을 누르면 열린다.**
- 현재 수동 RSVP 폼의 연락처 입력은 **선택 항목**으로 남아 있다. 자동 팝업 제거와 전화번호 필드 전체 삭제를 혼동하지 않는다. 추후 사용자가 필드도 없애 달라고 하면 별도 변경한다.
- 별도 로그인이나 전화번호 인증 없이 링크로 청첩장을 보는 구조를 유지한다.
- 사진과 이름은 테스트 값이다. 사용자 이름 김용학을 신랑 이름으로 임의 적용하지 않는다.

## 4. 디자인과 섹션 구성

- 한국어, 세로 스크롤 원페이지, 중앙 정렬.
- 청첩장 본문은 `width: 480px; max-width: 100%`. 작은 휴대폰에서는 화면 너비에 맞춰 줄어들어 가로 스크롤이 생기지 않도록 구현했다.
- 배경 `#474a37`, 포인트 `#d8e592`, 은은한 라임 도트 패턴, 작은 별 구분 장식.
- 폰트는 Noto Sans KR + Gowun Batang. 로컬 WOFF2 파일을 사용하며 라이선스를 포함한다.
- 따뜻한 다크톤, 미니멀하고 모던한 스타일. 부드러운 등장 효과, 바텀시트 슬라이드, 모바일 터치 영역, 모션 감소 설정을 지원한다.
- Radix 기반 shadcn/ui 스타일 Button/Dialog/Accordion을 사용한다. **현재 스타일은 일반 CSS이며 Tailwind 빌드가 아니다.**

| 순서 | 섹션 | 현재 구현 |
| --- | --- | --- |
| 1 | 히어로 | 전체 화면 커버 사진, 아래로 이동하는 스크롤 표시 |
| 2 | 초대장 | 부모님·신랑신부 이름, 초대 글, 별 장식 |
| 3 | 연락처 | 신랑측/신부측 2열 모달, 총 6명, `tel:`·`sms:` 링크 |
| 4 | 포토 갤러리 | 사진 3장 가로 스와이프, 이동 버튼, 확대 모달, 키보드 좌우 이동 |
| 5 | 날짜·카운트다운 | 달력 날짜 강조, D-day, 실시간 남은 시간 |
| 6 | 오시는 길 | 테스트 약도, 주소, 네이버·카카오 지도 검색 링크, 교통·주차 안내 |
| 7 | 예식장 안내 | 사진과 설명 카드 3개 |
| 8 | 축의금 계좌 | 양측 아코디언, 계좌 복사 |
| 9 | 참석 여부 | 버튼으로만 여는 RSVP 바텀시트, 입력 검증 |
| 10 | 방명록 | 이름·메시지 작성 모달, 랜덤 6색 포스트잇, 2열 메이슨리 |
| 11 | 푸터 | 공유, 링크 복사 |

원래 초대 글의 ‘오랜 시간 걸음 지키며’는 제작 과정에서 ‘오랜 시간 곁을 지키며’로 정리했다. 원문 폼 명세의 혼동되는 항목도 성함 입력과 참석 여부 선택으로 분리했다.

## 5. 현재 테스트 정보

| 항목 | 값 |
| --- | --- |
| 신랑 / 신부 | 김도윤 / 이서연 |
| 신랑 부모님 | 김정호 / 박미영 |
| 신부 부모님 | 이상훈 / 최은정 |
| 예식 일시 | 2027년 5월 22일 오후 2시, 한국 시간 |
| 코드의 날짜 | `2027-05-22T14:00:00+09:00` |
| 예식장 | 올리브 가든 · 2층 가든홀 — 임시 정보 |
| 주소 | 서울특별시 성동구 · 상세 주소 입력 예정 |
| 지도 검색어 | 서울숲 — 테스트용 |
| 전화·계좌·교통·주차 | 모두 테스트 값 |
| 사진 | AI 생성 커버 1장, 갤러리 3장, 안내 사진 3장 |

실제 이름·날짜를 바꿀 때는 화면 설정과 정적 미리보기 문구를 함께 수정한다. `demo: false`만 지정해도 테스트 값이 실제 정보로 바뀌는 것은 아니다.

## 6. 소스 파일 구조와 수정 위치

아래 경로는 별도 표시가 없으면 `olive-wedding/` 기준이다. 이전 계정의 절대 작업 경로에 의존하지 않는다.

| 파일·폴더 | 역할 |
| --- | --- |
| `src/config.ts` | 인물·날짜·사진·예식장·교통·연락처·계좌 및 서비스 연결 설정 |
| `src/App.tsx` | 섹션, 모달, 지도, 공유, 폼 검증, 방명록 Realtime 구독 |
| `src/data.ts` | Supabase 클라이언트, 타입, localStorage, 방명록·RSVP 저장, 샘플 방명록 |
| `src/styles.css` | 색상·폰트 적용·레이아웃·반응형·애니메이션 |
| `src/fonts.css` | 폰트 로딩 규칙, 설치 후 스크립트로 생성 |
| `src/main.tsx` | React 진입점 |
| `src/components/ui/` | Button, Dialog, Accordion 및 유틸리티 |
| `src/assets/hero.jpg` | 화면의 커버 사진 |
| `src/assets/gallery-1.jpg` ~ `gallery-3.jpg` | 갤러리 사진 |
| `src/assets/guide-1.jpg` ~ `guide-3.jpg` | 예식장 안내 사진 |
| `src/assets/ASSET_PROMPTS.json` | 임시 이미지 생성 프롬프트 기록 |
| `public/og-preview-v1.jpg` | 카카오톡 등 외부 크롤러가 읽을 공개 미리보기 사진 |
| `index.html` | 소스 HTML, 정적 title·description·OG·Twitter·canonical 설정 |
| `vite.config.ts` | 상대 경로 배포, 5175 포트, 일반·단독 빌드 설정 |
| `scripts/fonts.mjs` | 설치된 폰트 패키지에서 WOFF2용 CSS 생성 |
| `scripts/standalone.mjs` | CSS·JS 등을 포함한 단독 HTML 및 업로드 폴더 생성 |
| `.env.example` | 서비스 연결 환경변수 예시. 값은 비어 있음 |
| `supabase/migrations/202610020001_wedding.sql` | 테이블, 제약, RLS, 방명록 Realtime 설정 |
| `licenses/` | 폰트 라이선스 |
| `preview/` | 과거 화면 캡처와 일부 브라우저 검증 기록 |
| `README.md`, `CHANGELOG.md`, `TEST_REPORT.md` | 사용법, 변경 이력, 검증 결과 |

### 사용자의 요청을 코드에 연결하는 표

| 사용자가 바꾸려는 내용 | 먼저 수정할 곳 | 함께 확인할 곳 |
| --- | --- | --- |
| 이름·부모님 | `src/config.ts`의 `groom`, `bride` | `contacts`, `accounts`, 영문 이름·이니셜, `index.html`, 샘플 방명록 |
| 결혼 날짜·시간 | `src/config.ts`의 `date` | `index.html`의 설명·공유 문구. 시간대 `+09:00` 유지 |
| 초대 문구 | `src/App.tsx`의 `invitation-copy` | 모바일 줄바꿈 |
| 배경·포인트 색 | `src/styles.css`의 CSS 변수 | 도트·버튼·활성 상태, `index.html`의 theme-color |
| 커버 사진 | `src/assets/hero.jpg` | 화면 비율·잘림. 카톡 사진도 바꾸려면 공개 JPG 별도 수정 |
| 갤러리 사진·개수·설명 | `src/assets/`, `src/config.ts`의 `gallery` | 확대 모달, 이동 버튼, alt 문구 |
| 예식장·주소·지도 | `src/config.ts`의 venue/hall/address/mapQuery/map | 실제 좌표, 교통·주차, 지도 연결 설정 |
| 안내 사진·글 | `src/assets/guide-*.jpg`, `src/config.ts`의 `guides` | 카드 높이·줄바꿈 |
| 연락처 | `src/config.ts`의 `contacts` | 표시 이름과 `tel:`·`sms:` 대상 |
| 계좌 | `src/config.ts`의 `accounts` | 표시 값과 복사 값 |
| 참석 폼 항목 | `src/App.tsx` | `src/data.ts`의 `Submission`, 저장 로직, SQL 스키마·제약 |
| 방명록 색·모양 | `src/styles.css` | `color_index` 0~5와 스타일 대응 |
| 샘플 방명록 | `src/data.ts`의 `seedNotes` | 기존 localStorage가 있으면 샘플 변경이 바로 안 보일 수 있음 |
| 카카오톡 제목·설명 | `index.html`의 OG/Twitter/title/description | 정적 HTML에 반영되는지 |
| 카카오톡 사진 | `public/og-preview-v1.jpg`, `index.html` | 아래 미리보기 수정 절차 |
| 사이트 주소 | `src/config.ts`의 `connections.siteUrl` | OG URL·canonical·이미지 URL, 환경변수, 등록된 서비스 도메인 |

## 7. 실행·빌드·결과물 생성

프로젝트는 React + TypeScript + Vite 기반이다. 실제 의존성 버전은 `package.json`과 `package-lock.json`을 따른다. 인수인계를 이유로 프레임워크나 의존성을 일괄 업그레이드하지 않는다.

README 기준 Node.js 22.12 이상 환경에서 프로젝트 폴더로 이동한다.

```bash
cd olive-wedding
npm ci
npm run dev
```

기본 접속 주소는 `http://localhost:5175/`다. Vite 설정은 `port: 5175`, `strictPort: true`다. 포트가 점유되면 임의로 다른 포트로 바꾸기 전에 점유 프로세스와 실행 환경을 확인한다. `npm ci`의 postinstall에서 폰트 CSS가 생성된다.

소스 수정 후 빌드:

```bash
npm run build
npm run standalone
```

두 명령 모두 TypeScript 검사를 먼저 수행한다. 결과물은 다음과 같다.

| 결과 | 용도 |
| --- | --- |
| `olive-wedding/dist/` | 이미지·폰트 등을 별도 파일로 출력하는 일반 정적 배포본 |
| `olive-wedding/dist-standalone/` | 단독 HTML을 만들기 위한 중간 빌드 결과 |
| 프로젝트 상위의 `wedding-invitation.html` | 사진·폰트·JS·CSS를 포함하는 로컬 테스트용 단독 HTML |
| 프로젝트 상위의 `github-pages/index.html` | GitHub 웹에서 교체 업로드할 완성 HTML |
| 프로젝트 상위의 `github-pages/og-preview-v1.jpg` | 같은 위치에 함께 업로드할 미리보기 사진 |

**소스 루트의 `olive-wedding/index.html`을 그대로 서버에 올리지 않는다.** 이 파일은 `/src/main.tsx`를 참조하는 빌드 전 템플릿이다. 사용자가 웹 업로드로 배포할 때는 `npm run standalone`이 만든 `github-pages/index.html`을 전달한다.

### 다음 수정 시 전달할 파일

1. 업로드용 ZIP: `github-pages/` 안의 파일들을 ZIP 최상위에 넣는다. 현재는 `index.html`, `og-preview-v1.jpg` 두 파일이다. ZIP 자체를 GitHub에 올리는 방식이 아니다.
2. 최신 소스 ZIP: `olive-wedding/`의 소스, 공개 이미지, package/lock, 설정, 스크립트, 문서, 라이선스를 포함한다. `node_modules`, `.git`, 개인 `.env.local`, 로그는 제외한다. 기존 전달본처럼 일반 `dist/`와 단독 HTML을 함께 포함해도 된다.
3. `package.json`과 lockfile 버전을 맞추고 `CHANGELOG.md`에 요청·변경 결과를 기록한다. 기능 수정을 시작하면 현재 1.0.2 다음 버전부터 이어간다.

단독 HTML 생성 스크립트에서 긴 JS/CSS를 `String.replace`에 끼워 넣을 때는 현재의 **함수 콜백 방식**을 유지한다. 이전 제작 과정에서 문자열 치환의 `$&` 같은 패턴이 빌드 코드와 충돌해 결과물이 과도하게 커지는 문제를 피하기 위해 적용한 방식이다. 스크립트는 React root 뒤에서 실행되도록 body 끝에 배치한다.

## 8. GitHub Pages 배포 흐름

사용자는 GitHub 웹 화면에서 배포 파일을 업로드했다. 기존 안내 기준은 `main` 브랜치의 `/(root)`이며, 실제 저장소 설정이 바뀌었을 수 있으므로 재배포 시 확인한다. 원본 React 프로젝트 전체가 GitHub에도 올라가 있다고 가정하지 않는다.

1. `wedding-invitation` 저장소의 파일 목록을 연다.
2. **Add file → Upload files**를 선택한다.
3. 업로드 ZIP을 풀고 그 안의 완성 `index.html`과 공개 미리보기 JPG를 저장소 최상위에 올린다. 기존 `index.html`은 교체한다.
4. **Commit changes**로 반영한다.
5. GitHub Pages 배포 완료 후 공개 사이트에서 변경 내용을 확인한다.
6. 카카오톡 링크 미리보기는 새 메시지로 링크를 보내 확인한다.

커스텀 도메인은 현재 사용의 필수 조건이 아니다. 나중에 도메인을 바꾸면 `connections.siteUrl`, `connections.shareImageUrl`, 정적 OG·Twitter·canonical URL, 필요한 Kakao 서비스 도메인 설정을 함께 점검한다. 구체적인 DNS 값은 새 도메인과 당시 공식 안내를 확인해 적용한다.

## 9. 카카오톡 미리보기와 공유 기능

### 링크를 채팅창에 붙여 넣을 때 나오는 미리보기

현재 소스 `index.html`의 head에 정적 OG 태그를 넣었다. React가 실행된 뒤에만 삽입하는 방식으로 바꾸지 않는다.

```html
<meta property="og:title" content="도윤과 서연의 결혼식에 초대합니다" />
<meta property="og:description" content="2027. 05. 22. 토요일 오후 2시" />
<meta property="og:url" content="https://kim-yonghak.github.io/wedding-invitation/" />
<meta property="og:image" content="https://kim-yonghak.github.io/wedding-invitation/og-preview-v1.jpg" />
```

이 외에 `og:type`, locale, site_name, secure_url, 이미지 타입·너비·높이·alt, Twitter 메타 태그, canonical도 있다. 현재 JPG는 기존 커버를 복사한 **1024×1536 JPEG**다.

- 일반 링크 미리보기용으로 카카오 JavaScript 앱 키를 새로 받을 필요는 없다.
- HTML 내부 화면 사진이 포함되어 있어도, OG 사진은 외부에서 직접 접근 가능한 HTTPS 파일로 따로 제공한다.
- `.env.local`의 `VITE_SITE_URL`, `VITE_SHARE_IMAGE_URL`은 런타임 공유 설정이다. 이것만 바꾸면 정적 `index.html`의 메타 태그까지 자동 변경되는 구조는 아니다.

미리보기 사진을 새 사진으로 바꿀 경우:

1. `public/`에 새 JPG를 둔다. 사진 캐시를 구분하기 위해 `og-preview-v2.jpg`처럼 새 파일명을 사용할 수 있다.
2. `index.html`의 `og:image`, `og:image:secure_url`, `twitter:image`와 이미지 크기·alt를 실제 파일에 맞게 바꾼다.
3. `src/config.ts`의 `connections.shareImageUrl`과 환경변수에 지정된 값이 있다면 함께 바꾼다.
4. `scripts/standalone.mjs`의 이미지 복사 원본·대상 파일명도 바꾼다. 현재 스크립트에는 `og-preview-v1.jpg`가 직접 지정되어 있다.
5. 빌드 후 완성 HTML과 새 이미지를 모두 업로드한다.
6. 이전 카드가 계속 나오면 [카카오톡 URL 메타정보 관리](https://developers.kakao.com/tool/debugger/sharing)에서 청첩장 URL의 메타정보를 조회하고 캐시를 초기화한 뒤 새 메시지로 다시 공유한다. 과거 채팅의 카드가 즉시 바뀐다고 보장하지 않는다.

공식 설명: https://developers.kakao.com/docs/ko/tool/common

### 페이지 아래 ‘카카오 공유’ 버튼

링크 자동 미리보기와 별개 기능이다. 현재 코드는 카카오 키와 SDK가 준비되어 있으면 카카오 공유를 호출하고, 그렇지 않으면 지원 브라우저의 시스템 공유 또는 링크 복사로 이어진다. 카카오 SDK 공유·지도는 실제 앱 키로 검증하지 않았다.

## 10. 데이터 저장과 백엔드의 실제 상태

**GitHub Pages 배포 성공과 방명록·RSVP의 서버 저장은 별개다. 현재 전달 소스에는 연결 값이 없으며 로컬 테스트 모드로 동작한다.**

- 원래 요청은 Lovable Cloud와 두 테이블 생성이었다. 제작 당시 Lovable/Supabase 연동이 비활성화되어 실제 프로젝트·DB는 생성하지 못했다.
- 대신 Supabase 연결 코드와 SQL 마이그레이션을 포함했다.
- 연결 전에는 RSVP와 방명록을 해당 브라우저의 localStorage에 저장한다. 다른 기기에서는 같은 내용을 볼 수 없으며, 신랑·신부에게 전송되지 않는다.
- 같은 출처의 브라우저 탭 사이에는 `storage` 이벤트로 방명록 변경을 반영한다.
- 저장 키는 `wedding:${wedding.id}:notes`, `wedding:${wedding.id}:rsvp`다. `wedding.id`를 변경하면 이전 로컬 데이터와 분리된다. 기존 데이터를 이어 써야 할 때는 함부로 변경하지 않는다.
- `demo: false`와 서버 연결 여부는 별개다. `localMode`는 Supabase 연결 값 유무로 결정된다.
- 연결 후에는 방명록 INSERT를 Realtime으로 구독한다. 구독 성공 시 재조회로 누락을 보완한다. 클라우드 저장 실패를 로컬 저장 성공으로 바꾸지 않는다.
- 기존 로컬 입력은 클라우드로 자동 이관되지 않는다.

| 테이블 | 현재 필드 |
| --- | --- |
| `rsvp_submissions` | id, created_at, name, phone, attendance, guest_count, meal_preference, message, side, companions |
| `guestbook_messages` | id, created_at, author, content, color_index |

원래 요구 필드에 `id`, `created_at`을 추가했고, RSVP의 신랑측/신부측과 동행인을 보존하기 위해 `side`, `companions`도 추가했다.

- `attendance`: boolean.
- `side`: `groom` / `bride`.
- `meal_preference`: `yes` / `no` / `undecided`.
- 참석 인원: 참석이면 1~30. 불참이면 `guest_count: 0`, 식사 `no`, 동행인 빈 문자열로 저장.
- 방명록 `color_index`: 0~5.
- SQL은 요청에 따라 두 테이블 모두 익명 INSERT/SELECT를 허용한다. 따라서 연결 시 RSVP 이름·연락처도 공개 조회가 가능한 구조다. 현재 폼에 이 사실을 안내하며 연락처는 선택 입력이다. 이 구조를 비공개 수집으로 오인하지 않는다.
- 익명 UPDATE/DELETE는 부여하지 않았고 Realtime에는 방명록만 추가한다.

연결 작업을 요청받으면 실제 접근 가능한 프로젝트를 확인한 뒤 SQL과 환경변수를 적용하고 서버 저장·다른 기기 조회·Realtime을 검증한다. 환경변수만 입력해 두고 연결 완료로 보고하지 않는다. 기존 DB가 있다면 현재 스키마와 데이터를 확인하고 변경 마이그레이션을 설계한다.

```dotenv
VITE_SUPABASE_URL=
VITE_SUPABASE_PUBLISHABLE_KEY=
VITE_KAKAO_JAVASCRIPT_KEY=
VITE_SITE_URL=https://kim-yonghak.github.io/wedding-invitation/
VITE_SHARE_IMAGE_URL=https://kim-yonghak.github.io/wedding-invitation/og-preview-v1.jpg
```

Supabase 키는 공개 클라이언트용 publishable/anon 키를 사용한다. `VITE_*` 값은 빌드에 포함되므로 서버 비밀 키나 service-role 키를 넣지 않는다. 환경변수 변경 후에는 다시 빌드한다.

## 11. 지도 구현 상태

- 기본은 자체 테스트 약도다. 지도 링크는 서울숲 검색으로 연결된다.
- 실제 카카오 지도 임베드는 `demo: false`, 카카오 JavaScript 키, 실제 좌표 등의 설정이 필요하다.
- 실제 지도나 약도 이미지로 바꾸라는 요청이 오면 `MapPanel`, `DemoMap`과 설정 값을 확인하고 기존 주소·교통·주차 정보도 함께 맞춘다.

## 12. 검증 기록과 다음 수정의 확인 범위

### 이미 확인한 내용

- TypeScript 검사, 일반 배포 빌드, 단독 HTML 생성.
- 320/390/480px 화면에서 가로 넘침 없음, 넓은 화면에서 청첩장 최대 480px 유지.
- 갤러리 이동·확대, 연락처 링크, 계좌 펼치기·복사, RSVP 검증·저장, 방명록 저장·새로고침 유지·탭 간 반영.
- 새 진입과 새로고침 후 2초 이상 기다려도 RSVP 자동 팝업 없음. 버튼 클릭 시 정상 열림.
- 단독 HTML의 로컬 실행, 포함된 사진·폰트 로딩, 오프라인 화면 표시.
- 1.0.2 정적 HTML head에 올바른 OG URL·이미지·크기가 존재함. 빌드 결과와 업로드 폴더에 JPG가 존재함.

### 확인하지 않은 범위

- 실제 Lovable/Supabase 프로젝트·DB·Realtime 서버 연결.
- 실제 카카오 키를 이용한 지도·공유 전송.
- iOS Safari 및 카카오톡 인앱 브라우저의 실제 기기 테스트.
- 제작 측에서 1.0.2를 원격 업로드하고 카카오톡 미리보기까지 확인하는 작업.

`TEST_REPORT.md`의 **v1.0.0 자동 팝업 테스트는 과거 기록**이다. 최신 기대 동작은 v1.0.1 이후의 ‘자동 팝업 없음’이다.

다음 수정에서는 요청과 관련된 부분을 확인하고, 공통으로 빌드 성공·모바일 너비·자동 팝업 미발생을 점검한다. 이름·날짜·사진·공유를 바꿨다면 화면과 OG 메타정보의 일치, 공개 이미지 경로까지 확인한다. 실제로 수행하지 않은 테스트를 통과로 적지 않는다.

## 13. 새 계정에서 보낼 첫 메시지 예시

아래 MD와 `olive-wedding-project.zip`을 첨부한 후 다음처럼 말하면 된다.

> 첨부한 WEDDING_INVITATION_HANDOFF.md를 읽고, olive-wedding-project.zip을 기준으로 기존 청첩장 작업을 이어서 해줘. 먼저 실제 소스와 현재 버전을 확인해줘. 디자인과 기존 기능은 유지하고 내가 요청하는 부분만 수정해줘. 첫 접속 때 입력창이 자동으로 뜨면 안 돼. 수정 후에는 빌드와 필요한 동작을 확인하고, 최신 소스 ZIP과 GitHub에 바로 올릴 배포 파일, 변경 내역을 제공해줘. 실제 서버에 업로드하지 않았다면 파일 준비 완료로 구분해서 알려줘.

이어서 원하는 내용을 자유롭게 덧붙인다. 예를 들어 ‘커버를 첨부 사진으로 바꾸고 카톡 미리보기에도 같은 사진을 써줘’, ‘신랑신부 이름과 날짜를 아래 정보로 변경해줘’, ‘방명록이 다른 휴대폰에서도 보이게 서버에 연결해줘’처럼 요청하면 된다.
