#!/bin/sh

set -ex

(cd `git rev-parse --show-toplevel` && poetry run isort app && poetry run black app)
