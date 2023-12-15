# ADS PowerMeter Poller
This circumvents EPICS stack to directly utilize the ads system to poll analog values from the power PowerMeter

# To Run
* User must ssh onto `ctl-tst-dev-01`
* User must source pcds_conda environment
	* `/cds/home/j/joshc/dotfiles/try_me.sh && source pcds_conda`
	* 'cd /cds/home/j/joshc && python3 sample.py -t [time in seconds] -f [file name to save]'