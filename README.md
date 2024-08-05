# simple-python-project
Basic Flask app

# requirements:
1) Docker version 26.1.3
2) Docker Compose version v2.27.0

# installation
1) make docker-build
2) go on http://localhost:80

# makefile commands:
+ make docker-build - run project
+ make docker-stop - stop project
+ make docker-exec - exec container with app
+ make build-develop - run project in develope mode
+ make run-test - run tests
+ make run-linter - run linter

# workflows:
branches: [main, develop]
+ linter.yaml - check code with linter (push, pull requests)
+ linter.yaml - run pytest (push, pull requests)

