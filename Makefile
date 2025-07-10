install:
	@if [ "$$VIRTUAL_ENV" = "" ]; then \
		echo "❌ Virtual environment not activated. Please create a virtual environment"; \
		exit 1; \
	fi
	@echo " Installing Python dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt

	@echo " Installing development dependencies..."
	pip install -r requirements-dev.txt

	@echo " Installing pre-commit hooks..."
	pre-commit install

	@echo "✅ Environment is ready!"


# Lint the code using black
lint:
	black app test src

# Run all tests
test:
	pytest -v --disable-warnings

# Run API container locally
run-api:
	docker build -t credit-api -f Dockerfile .
	docker run -p 8000:8000  credit-api

# Clean up .pyc and __pycache__
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Format code and show diffs
check-format:
	black --diff --color app test

# Run Prefect flow locally
run-flow:
	python flow.py

# Deploy to cloud
deploy:
	gcloud run deploy credit-predictor \
		--source . \
		--region us-central1 \
		--allow-unauthenticated \
		--port 8000 \
		--project credit-default-mlops

