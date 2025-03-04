@echo off
set IP=172.32.44.92
set KEY=C:\Users\nao\.ssh\key_ed25519
echo %IP%
ssh -i %KEY% nao@%IP% "rm -rf /home/nao/4ci/src > /dev/null 2>&1 ; mkdir /home/nao/4ci/src > /dev/null 2>&1"
scp -i %KEY%  -r ./src  nao@%IP%:/home/nao/4ci 
ssh -i %KEY% nao@%IP% "touch /home/nao/4ci/devScript/refresh.trigger"