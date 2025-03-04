while :
do
  if [ -f refresh.trigger ]
  then
    rm -f refresh.trigger
    bash ./scripts/refresh.sh
  fi
  sleep 1
done
