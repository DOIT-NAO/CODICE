@echo off
set IP=192.168.178.214
set KEY=C:\Users\nao\.ssh\key_ed25519
echo %IP%
ssh  -i %KEY% nao@%IP% "rm -rf /home/nao/4ci/src > /dev/null 2>&1 ; mkdir /home/nao/4ci/src > /dev/null 2>&1"
scp  -i %KEY%  -r ./src  nao@%IP%:/home/nao/4ci 
@REM -i %KEY% nao@%IP% "bash start_4ci.sh"
