web: cd ./crawl-data/ && celery flower -A tasks.app --port=$PORT
worker: cd ./crawl-data/ && celery worker -A tasks.app -l INFO --hostname=worker@%h
