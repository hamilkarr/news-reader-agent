# AI 에이전트 설계 패턴: 범용적인 역할 분할 방법론

## 🎯 핵심 질문

> 개발자가 신문사 업무를 모르는데, 어떻게 뉴스 리더 에이전트를 3단계로 나눴을까?
> 분야에 상관없이 적용할 수 있는 궁극의 설계법이 있을까?

---

## 🧠 궁극의 설계법: ETL 패턴 + 전문가 분업 패턴

### 핵심 원리: 입력 → 처리 → 출력

어떤 분야든 복잡한 작업은 이 3단계로 나눌 수 있다:

| 단계               | 역할               | 뉴스 예시   | 쇼핑몰 예시 | 연구 예시   |
| ------------------ | ------------------ | ----------- | ----------- | ----------- |
| **수집 (Gather)**  | 원재료 모으기      | 뉴스 검색   | 상품 크롤링 | 논문 검색   |
| **처리 (Process)** | 가공/분석하기      | 요약/분석   | 비교/평가   | 분석/정리   |
| **생성 (Produce)** | 최종 결과물 만들기 | 리포트 작성 | 추천 리스트 | 연구 보고서 |

---

## 📐 이 패턴의 정체: Crew AI의 권장 패턴

이것은 **Crew AI 프레임워크**가 권장하는 설계 방식이다.

```
🔍 Researcher/Hunter/Gatherer  →  원재료 수집
       ↓
📝 Analyst/Processor/Summarizer  →  분석/처리
       ↓
🎯 Writer/Creator/Curator  →  최종 결과물 생성
```

Crew AI 공식 문서와 예제들을 보면 거의 대부분 이 구조를 따른다.

---

## 🔑 왜 이 패턴이 효과적인가?

### 1. Single Responsibility Principle (단일 책임 원칙)

소프트웨어 설계의 기본 원칙. 각 에이전트가 **딱 하나의 책임**만 가지면:

- 프롬프트가 명확해짐
- LLM이 덜 혼란스러워함
- 디버깅이 쉬워짐

### 2. Chain of Thought (사고의 연쇄)

LLM은 복잡한 작업을 **단계별로 나누면** 더 잘 수행한다.

```
"뉴스 찾아서 요약하고 리포트 써줘" ❌ (한번에)
"뉴스 찾아줘" → "요약해줘" → "리포트 써줘" ✅ (단계별)
```

### 3. Information Bottleneck (정보 병목)

```
무한한 원데이터 → 핵심만 추출 → 압축된 결과물
```

각 단계에서 정보가 **정제되고 압축**되어 다음 단계로 전달된다.

---

## 🛠️ 범용 에이전트 설계 공식

**어떤 분야**든 이 템플릿을 적용할 수 있다:

```yaml
# 1단계: 수집자 (Gatherer)
agent_1:
  role: "[분야] 정보 수집 전문가"
  goal: "관련 정보를 찾아서 모으기"

# 2단계: 처리자 (Processor)
agent_2:
  role: "[분야] 분석 전문가"
  goal: "수집된 정보를 분석하고 가공하기"

# 3단계: 생성자 (Producer)
agent_3:
  role: "[분야] 결과물 제작 전문가"
  goal: "최종 결과물 만들기"
```

---

## 💡 실제 적용 예시

| 프로젝트    | Agent 1 (수집)         | Agent 2 (처리)      | Agent 3 (생성)        |
| ----------- | ---------------------- | ------------------- | --------------------- |
| 뉴스 리더   | News Hunter            | Summarizer          | Curator               |
| 주식 분석   | Data Collector         | Analyst             | Report Writer         |
| 여행 플래너 | Destination Researcher | Itinerary Planner   | Travel Guide Writer   |
| 코드 리뷰   | Code Scanner           | Bug Analyzer        | Review Reporter       |
| 채용 시스템 | Resume Collector       | Candidate Evaluator | Recommendation Writer |

---

## 🎓 핵심 요약

개발자가 특정 도메인을 몰라도 이런 구조가 나오는 이유:

1. **Crew AI 프레임워크의 권장 패턴**을 따름
2. **소프트웨어 설계 원칙** (단일 책임)을 AI 에이전트에 적용
3. **ETL 패턴** (Extract-Transform-Load)의 변형
4. **LLM 특성** (단계별 수행이 더 정확함)을 활용

> 💡 **결론**: 도메인 지식이 아니라 **에이전트 설계 패턴**을 알면 된다!

---

## 관련 링크

- [[agents]] - 에이전트 설정 파일
- [[tasks]] - 태스크 설정 파일
- [Crew AI 공식 문서](https://docs.crewai.com/)

---

#AI #에이전트 #설계패턴 #CrewAI #멀티에이전트
