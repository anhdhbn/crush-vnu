worker: cd ./crawl-data/ && python -c "from crawler.init.downloadchilkat import install_chilkat; install_chilkat()" && celery worker -A jobqueue.proxies.tasks.app -B -l INFO --hostname=worker@heroku -E
beat: cd ./crawl-data/ && python -c "from crawler.init.downloadchilkat import install_chilkat; install_chilkat()" && celery beat -A jobqueue.tasks.app -l INFO 
