-----------------------------------
            git command
-----------------------------------
'''''''''基本command'''''''''
mkdir test
cd test
vi README.txt
git add README.txt //把README.txt从提交到暂存区
git commit -m "version 1.0" //从暂存区提交到版本库 "version 1.0"是这个版本的描述
git status //查看文件状态，在哪个区
git reset --hard HEAD^ //回退到上一个版本
git reset --hard 版本ID //回退到这个ID的版本,比如:acc2149
git log //查看版本信息
git log --oneline //查看简易版本信息
git reflog //查看所有版本信息，包括删除回退过的版本
cat README.txt //查看文件的里面的内容
git diff HEAD -- README.txt //命令可以查看工作区和版本库里面最新版本的区别：
git checkout -- README.txt //命令git checkout -- readme.txt意思就是，把README.txt文件在工作区的修改全部撤销
git reset HEAD readme.txt //命令git reset HEAD <file>可以把暂存区的修改撤销掉（unstage），重新放回工作区：
rm README.txt //rm命令,通常直接在文件管理器中把没用的文件删了
git rm README.txt //要从版本库中删除该文件，那就用命令git rm 删掉

'''''''''''GitHub远程仓库'''''''''''''''
'''
首先，登陆GitHub，然后，在右上角找到“Create a new repo”按钮，创建一个新的仓库：
在Repository name填入test，其他保持默认设置，点击“Create repository”按钮，就成功地创建了一个新的Git仓库：
'''
由于你的本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，所以，需要一点设置：
第1步：创建SSH Key: 
ssh-keygen -t rsa -C "youremail@example.com"
//在本地的learngit仓库下(git bash here)运行命令：
git remote add origin git@github.com:15626106696/test.git //15626106696(GitHub账户名)把本地库的所有内容推送到远程库上：
//下一步，就可以把本地库的所有内容推送到远程库上：
git push -u origin master
//从现在起，只要本地作了提交，就可以通过命令：
git push origin master

//从远程仓库克隆git项目到本地仓库
git clone git@github.com:15626106696/test.git  //15626106696/test.git 可以是任意账号的项目，但是最好还是先在GitHub上Fork别人的项目

'''''''''''分支管理'''''''''''''''
'''
Git鼓励大量使用分支：
查看分支：git branch
创建分支：git branch <name>
切换分支：git checkout <name>
创建+切换分支：git checkout -b <name>
合并某分支到当前分支：git merge <name>
删除分支：git branch -d <name>
'''
git checkout -b dev //创建并切换到分支dev
git branch //查看当前分支
git checkout master //切换回master分支
git merge dev //切换到master分支后，执行此命令，则把dev分支的成果合并到master分支
git branch -d dev //合并完成后，此命令用于删除dev分支
