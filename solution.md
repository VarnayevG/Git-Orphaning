Решение:

Итак, у нас есть ветка master с последним рабочим состоянием, 
а также 3 коммита после этого, которые должны были быть
в develop. 

1. Создаем ветку develop с момента последнего рабочего состояния master:

git checkout <latests-working-commit>

git checkout -b develop

2. Переносим коммиты из master в develop

git cherry-pick <commit1> <commit2> <commit3>

3. Удаляем коммиты из master

git checkout master

git reset -hard <latests-working-commit>

git push origin HEAD --force

4. Делаем PR из develop в master и merge-им

5. Добавляем файл с решением (тут уже можно сразу в master)


Solution:

So, we have master branch with the latest working state
as well as 3 commits after it, which should have been commited into develop branch. 

1. Create develop branch from the master latest working state:

git checkout <latests-working-commit>

git checkout -b develop

2. Transfer commits from master to develop

git cherry-pick <commit1> <commit2> <commit3>

3. Remove commits from master

git checkout master

git reset -hard <latests-working-commit>

git push origin HEAD --force

4. Create PR from develop to master and merge

5. Add solution file (straight to master this time)