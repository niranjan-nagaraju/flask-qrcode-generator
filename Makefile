CONTAINER_NAME = pyqrcode

deploy:
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml down -v
	docker-compose -f docker-compose.yml up -d --force-recreate


start:
	docker start $(CONTAINER_NAME)

stop:
	docker stop $(CONTAINER_NAME)
