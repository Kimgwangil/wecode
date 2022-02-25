# Git 중간시험

~~2022.02.25(금) git 중간시험~~

## Git 명령어

### 1. git init
- 내가 프로젝트를 만들고자 하는 폴더 안에서 `git init`을 입력한다.
 이는 __'이제부터 내가 git을 사용하겠다.'__, __'변경사항을 받을 준비를 하거라.'__ 라는 의미로 볼 수 있다.
---
### 2. git branch
- 현재 내가 생성한 브랜치를 보여준다. `git init`으로 초기화를 하자마자 `git branch`를 입력하면 `Master` 브랜치만 있다.
---
### 3. git branch -M main
- `Master` 브랜치의 이름을 `main`으로 바꿔준다.
그냥 사용해도 될텐데 왜? 라고 생각할 수 있지만, `Master`라는 단어에는 상하, 수직관계라는 의미가 내포되어 있기에 세계적으로 `main`이라는 이름으로 많이 변경하는 추세라고 한다.
---
### 4. git stauts
- 현재 수정사항이 있는지, `add` 해야할 파일이 있는가, `commit` 해야하는 파일이 있는가 확인할 수 있다.
---
### 5. git add .
- 현재 폴더 내에서 수정사항이 있는 파일들을 모두 담아준다. 이는 `commit`을 하기 위해 미리 준비시키는 것이다.
---
### 6. git commit -m "msg"
- `add` 시켰던 파일들을 `commit`, 중간 저장해주는 것이다.
한 브랜치에서 작업을 하다가 저장을 하고나서 커밋을 하지 않으면 `main` 외의 다른 브랜치로는 넘어갈 수 없다.
-  `"msg"` 부분에는 변경된 내용을 간략하지만 자세하게 적어주면 되는데, 혹 적을 내용이 너무 많다면 `git commit` 만 입력을 하고, 자유롭게 상세하게 적을 수 있다. (줄바꿈도 가능)
    - "msg" 부분에는 보통 `"Add : ~"`, `"Modify : ~"`, `"Fix : ~"`, `"Revise : ~"`, `"Delete : ~"`를 사용하여 무엇을 하였는지 직관적으로 알 수 있게 해주는 것이 좋다.
---
### 7. git remote add oringin 'github 주소'
- 뒤에 github 주소가 있는 부분은 `''`를 빼고  적어주면 된다.
이는 repository를 만들고 나면 맨 위에 떠있는 주소를 복사해도 되고, 
아예 명령어 자체도 복사할 수도 있으니 편한 방법을 사용하면 된다.
---
### 8. git remote -v
- 
---
### 9. git push oringin main
- 내 `origin` 안에 있는 `main` 브랜치의 `commit` 내용을 github 레파지토리 안으로 보낸다. 최종 저장이라고 보면 좋을 것 같다.
- 혹시 다른 브랜치를 생성하고 그 브랜치를 올리는 경우엔 마지막의 main 대신 해당 브랜치 이름을 적어주면 된다.
    ex) git push origin feature/README
---
### 10. git checkout -b feature/README
- 원래대로라면 `git branch feature/README`(브랜치생성) -> `git checkout feature/README`(브랜치이동) 의 순서로 작업해야 하지만, 이 명령어를 사용하면 __브랜치를 생성하고 바로 그 브랜치로 이동__을 시켜준다. 
- `-b`는 __branch__의 약자이고, 이 `-b` 뒷부분에는 내가 원하는 브랜치 이름을 작성해주면 된다.
