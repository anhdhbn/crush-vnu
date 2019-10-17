worker: cd ./crawl-data/ && python -c "from crawler.init.downloadchilkat import install_chilkat; install_chilkat()" && celery worker -A jobqueue.tasks.app -l INFO --hostname=worker@%h -E
