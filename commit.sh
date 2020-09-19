#!/bin/sh
cd D:/CSE450
git add --all
timestamp() {
  date +"at %H:%M on %m/%d/%Y"
}
git commit -am "Update $(timestamp)"
git pull
git push origin master

# Log the commit

repo="Machine Learning"

## Declare file
cd C:/RunFiles
log=commit_log.txt
 
## append commit to log file
printf "Commit ${repo} $(timestamp)" >> $log
printf "\n" >> $log