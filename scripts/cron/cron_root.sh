# Edit this file to introduce tasks to be run by cron with root access right.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any')
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command

MAILTO=""
LOGS_FILE='/home/dilshod070/src/mlmltool/log-cron'

0 15 * * * /home/dilshod070/src/mlmltool/scripts/cron/cleanup >> $LOGS_FILE 2>&1

# To update cron script, please use `mlmltool update_cron -t=root`
