# 저장소 소개
백준, 프로그래머스 등 다양한 코딩 테스트 문제를 해결 하고 관련 내용을 기록하기 위한 저장소입니다.

# 유틸리티

## new_problem

새로운 문제를 추가하기 위한 스크립트

```
python -m new_problem <problem_owner> <problem_id>
```

|Problem owner|Template|
|---|---|
|백준|baekjoon|
|기타|default|

* 백준은 stdin, stdout를 Mock 해야 하기 때문에 따로 템플릿이 제공됩니다.