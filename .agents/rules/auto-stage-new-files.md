# 새 파일 자동 Stage 규칙

이 워크스페이스에서 새로 생성한 파일은 Git `stage` 상태(`git add`)로 만든다.

1. `write_file` 도구로 새로 생성한 파일은 `.agents/hooks.json`의 `PostToolUse` 훅이 자동으로 `git add` 처리하므로 별도로 다시 `git add`할 필요 없다.
2. 셸 명령(`run_command` 등)으로 워크스페이스 안에 새 파일을 생성한 경우에는 `.gitignore`에 해당하지 않는 파일에 한해 `git add <파일>`을 실행해 stage 상태로 만든다.
3. 이미 Git이 추적 중인 기존 파일의 수정 사항은 요청이 없는 한 자동으로 stage하지 않는다.
