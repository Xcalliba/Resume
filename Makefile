.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec my-user --no-session -- sam deploy

deploy-site:
	aws-vault exec my-user --no-session -- aws s3 sync ./website_files s3://my-fantastic-website-kojo-hagan

invoke-get:
	sam build && aws-vault exec my-user --no-session -- sam local invoke MyLambdaFunction

