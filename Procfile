web: cd ./crawl-data/ && ls && celery flower -A jobqueue.tasks.app --port=$PORT
worker: cd ./crawl-data/ && celery worker -A jobqueue.tasks.app -l INFO --hostname=worker@%h
