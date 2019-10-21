worker: cd ./crawl-data/ && python -c "from crawler.init.downloadchilkat import install_chilkat; install_chilkat()" && celery worker -A jobqueue.tasks.app -c 35 -B -l INFO --hostname=worker@heroku -E
beat: cd ./crawl-data/ && python -c "from crawler.init.downloadchilkat import install_chilkat; install_chilkat()" && celery beat -A jobqueue.tasks.app -l INFO 
