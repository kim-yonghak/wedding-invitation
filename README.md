# 윤호 ♥ 채연 모바일 청첩장 — 수정본

## 이번 수정

- 사용자가 제공한 확대 이미지의 초대 문구·가족 성함·예식 일시·장소·교통·주차 안내를 반영했습니다.
- 김윤호 · 김채연 / 2027년 2월 28일 일요일 오전 11시 / 영등포구 더베르G
- 신랑: 김기호 • 김정연의 장남 윤호 / 신부: 김순창 • 권희정의 차녀 채연
- 장소: 서울 영등포구 국회대로 612 2층
- 큰 영문 메인 제목과 폴라로이드 장식은 제거했습니다. 날짜를 상단 양쪽에, 이름을 하단 양쪽에 배치하고 사진을 왼쪽 2장–오른쪽 3장–왼쪽 2장으로 배치했습니다.
- 최초 요청의 올리브 #474a37 / 라임 #d8e592 / 도트 / 종이 질감 / 접힌 자국 / 최대 480px / Noto Sans KR + Gowun Batang은 유지했습니다.
- 약도는 제공받은 이미지의 약도 영역을 SVG viewBox로 그대로 표시합니다. 사용자 자료 원본을 assets/map-reference.png로 포함했습니다.
- 실제 커플 사진과 실제 계좌는 제공되지 않아 이전 샘플을 유지했습니다. 인물 사진은 AI 생성 이미지입니다. 계좌 팝업의 성함은 원문에 맞게 변경했습니다.

## 컴퓨터에서 확인

압축을 풀고 index.html을 브라우저로 열면 됩니다. assets 폴더를 함께 유지하세요. 인터넷 연결 시 Google Fonts를 읽습니다. 공유·복사 기능의 최종 확인은 공개 HTTPS 주소에서 해 주세요.

## 카카오톡 링크 미리보기

대표 이미지: `assets/share-preview.png`

- 올리브 도트 배경과 종이 질감 위에 “Wedding Invitation / 소중한 당신을 초대합니다”를 넣은 전용 이미지입니다.
- 제목: “윤호 ♥ 채연, 결혼합니다”
- 설명: “2027년 2월 28일 일요일 오전 11시 | 영등포구 더베르G”
- 정적인 `<head>`에 og:title, og:description, og:image, og:url, 이미지 크기·유형·대체 설명을 넣었습니다.
- 아래 **GitHub Actions 방식**으로 배포하면 실제 Pages 주소에 맞는 절대 이미지 URL이 자동으로 들어갑니다. 커스텀 도메인도 Pages에 등록한 뒤 다시 배포하면 반영됩니다.
- 서버의 HTML에 직접 반영되므로 카카오 스크랩 봇이 JavaScript를 실행할 필요가 없습니다.
- 카카오톡에서 실제 표시되는 미리보기는 공개 배포 후 확인해야 합니다. 현재는 아직 GitHub에 배포하지 않았습니다.

## 권장 배포: GitHub Actions

이전 버전의 “Deploy from a branch” 안내 대신 다음 설정을 사용하세요. 별도 앱 키나 유료 서버는 필요하지 않습니다.

1. GitHub 저장소를 만듭니다. 기본 브랜치는 `main`을 사용하세요.
2. 압축 안의 `index.html`, `assets/`, `scripts/`, `.github/`, `.nojekyll`을 저장소 최상위에 올립니다. ZIP 자체를 올리거나 폴더를 한 단계 더 감싸지 마세요. `.github/workflows/pages.yml`이 누락되지 않게 확인하세요.
3. Settings → Pages → Build and deployment → Source에서 **GitHub Actions**를 선택합니다.
4. Actions → Publish wedding invitation → Run workflow로 실행합니다. 이후 `main`에 변경을 올릴 때마다 자동 배포됩니다. 설정 전에 첫 실행이 실패했으면 설정 후 다시 실행하세요.
5. 성공한 배포의 주소 또는 Settings → Pages에 표시되는 주소를 카카오톡으로 보냅니다.

워크플로는 Pages의 `base_url`을 읽고 `scripts/prepare-pages.py`를 실행해 `_site/`를 생성합니다. 여기에 실제 주소가 입력된 HTML과 이미지가 들어갑니다. 생성한 `_site/`만 배포합니다.

브랜치가 main이 아니라면 `.github/workflows/pages.yml`의 branches를 실제 기본 브랜치명으로 변경하세요.

### 브랜치 배포를 계속 쓰려는 경우

`index.html`의 아래 세 개 태그를 실제 공개 HTTPS 주소로 직접 바꿔 주세요. 상대 주소로 둔 og:image의 플랫폼별 처리를 기대하기보다 절대 URL을 쓰는 것이 확실합니다.

```html
<meta property="og:url" content="https://YOUR-ID.github.io/YOUR-REPO/">
<meta property="og:image" content="https://YOUR-ID.github.io/YOUR-REPO/assets/share-preview.png">
<meta name="twitter:image" content="https://YOUR-ID.github.io/YOUR-REPO/assets/share-preview.png">
```

그다음 Settings → Pages → Source: Deploy from a branch → main / (root)를 선택하면 됩니다. 이 방식을 쓰면 `.github/workflows/pages.yml`은 업로드에서 제외하세요.

## 원하는 공유 주소

- 무료 경로 커스텀: `https://깃허브아이디.github.io/원하는저장소이름/`
- 도메인 전체 커스텀: 소유한 도메인을 Settings → Pages → Custom domain에 연결합니다.
- 서브도메인의 DNS CNAME은 `깃허브아이디.github.io`로 설정합니다. DNS 값에 저장소 경로는 넣지 않습니다.
- 최상위 도메인은 GitHub 공식 문서의 A/AAAA 등 설정을 따릅니다.
- 도메인 확인 및 인증서 발급 후 Enforce HTTPS를 켭니다.
- 도메인을 바꾼 뒤 Actions를 다시 실행하면 OG 이미지 URL도 새 주소로 생성됩니다.
- `CONFIG.shareUrl`은 빈 문자열이면 현재 페이지 주소를 공유합니다. 특정 URL을 고정하고 싶을 때만 입력하세요. 여기에 URL을 쓰는 것만으로 도메인이 생성되지는 않습니다.

## 예전 미리보기가 남는 경우

카카오디벨로퍼스의 도구 → 카카오톡 URL 메타정보 관리에서 배포 주소를 검사하고 OG 캐시를 초기화한 뒤 링크를 다시 공유하세요. 이미 보낸 메시지의 카드가 즉시 바뀐다고 보장할 수는 없습니다.

공식 문서:
- https://developers.kakao.com/docs/ko/tool/common
- https://developers.kakao.com/docs/ko/message-template/faq
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## 남은 실제 정보

실제 사진과 계좌번호만 교체하면 됩니다.

계좌: index.html 하단 CONFIG.accounts에서 각 항목의 bank, number를 변경하고 demo를 false로 바꿉니다. role/name은 원문에 맞춰 두었습니다. 예시 계좌에는 송금할 수 없습니다.

사진: `assets/wedding-sheet.png`는 4열 × 2행의 가상 웨딩 화보입니다. 첫 장면은 메인, 다음 일곱 장면은 사진 1~7입니다. 같은 형식으로 교체하거나 개별 사진을 연결할 수 있습니다.

개별 사진을 쓰려면:
1. `assets/hero.jpg`, `assets/photo-1.jpg` ~ `assets/photo-7.jpg`를 올립니다.
2. CSS 마지막에 `.photo{background-size:cover;background-position:center}.hero .photo{background-image:url('assets/hero.jpg')}.seal .mini{background-image:url('assets/photo-7.jpg');background-position:center}`를 추가합니다.
3. 사진 버튼 생성 코드의 `pic.style.backgroundPosition=position(n+1)`을 `pic.style.backgroundImage='url(assets/photo-'+(n+1)+'.jpg)'`로 바꿉니다.
4. setPhoto 안의 `$('largePhoto').style.backgroundPosition=position(activePhoto+1)`을 `$('largePhoto').style.backgroundImage='url(assets/photo-'+(activePhoto+1)+'.jpg)'`로 바꿉니다.
5. descriptions의 사진 설명도 사진에 맞게 수정합니다.
6. 실제 사진·계좌 교체가 완료되면 하단 `.demo-note`를 제거합니다.

## 기능 및 확인 범위

사진 확대·이전/다음·키보드 이동·닫기, 양측 계좌 팝업과 복사, 공유 및 주소 복사 기능을 유지했습니다. 달력은 2027년 2월 28일 일요일을 표시하고, 남은 날짜 안내는 한국 달력 날짜 기준, 일·시·분·초 타이머는 실제 예식 시각까지 남은 시간 기준입니다.

지도 아이콘은 더베르G 장소 검색으로 연결됩니다. 모바일에서는 해당 앱 스킴을 사용하며 앱을 열지 못할 때 웹 지도 경로를 제공합니다. 정확한 장소 상세 ID를 임의로 생성하지 않았습니다. 지도 앱 설치 여부 및 카카오톡 인앱 브라우저 제한에 따라 앱 실행 방식은 달라질 수 있습니다.

화면·원문·달력·약도·사진 팝업·신부측 계좌 성함을 브라우저에서 확인했습니다. 자바스크립트 구문과 배포용 OG 절대 URL 생성도 검사했습니다. 실제 GitHub Actions 실행과 카카오톡 미리보기, iOS/Android 지도 앱 실행은 배포 후 실제 환경에서 최종 확인해야 합니다.

## 이미지 제작 기록

가상 웨딩 화보와 미리보기 카드는 내장 이미지 생성 도구로 제작했습니다. 이번 미리보기 프롬프트: 올리브 #474a37 도트 배경, 라임 #d8e592 포인트, 중앙 아이보리 종이와 은은한 접힘 자국, 작은 하트, 정확한 텍스트 “Wedding Invitation” 및 “소중한 당신을 초대합니다”, 이름·날짜·장소 없이 가로형 메시지 미리보기 카드. 원본 파일은 assets/share-preview.png입니다.
