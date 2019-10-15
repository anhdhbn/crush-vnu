web: sh -c 'cd ./crawl-data/ && celery flower -A tasks.app --port=$PORT'
worker: sh -c 'cd ./crawl-data/ && celery worker -A tasks.app -l INFO --hostname=worker@%h'