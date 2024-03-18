echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/SadKidBGMZ/fwdbot SadKidBGMZ/fwdbot 
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/SadKidBGMZ/fwdbot -b $BRANCH /fwdbot
fi
cd SadKidBGMZ/fwdbot 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
