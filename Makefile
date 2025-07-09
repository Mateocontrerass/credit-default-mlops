
# Lint the code using black
lint:
	black app test

# Run all tests
test:
	pytest -v --disable-warnings

# Run API container
run-api:
	docker build -t credit-api -f Dockerfile .
	docker run -p 8000:8000 -p 7860:7860 credit-api

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