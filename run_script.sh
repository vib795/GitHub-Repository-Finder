#!/bin/bash

docker build -t find-good-first-issues .
docker run -e GITHUB_TOKEN=<your-github-token> -v $(pwd):/app find-good-first-issues
