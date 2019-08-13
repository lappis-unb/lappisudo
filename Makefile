train:
	docker-compose rm -s -f coach
	docker-compose build coach

console:
	docker-compose run bot make run-console
