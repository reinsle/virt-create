#
# Regular cron jobs for the virt-create package
#
0 4	* * *	root	[ -x /usr/bin/virt-create_maintenance ] && /usr/bin/virt-create_maintenance
