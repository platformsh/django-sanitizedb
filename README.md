
## First steps

1. [Open a free trial account on Platform.sh](https://auth.api.platform.sh/register)
1. Create an empty project
1. [Install the Platform.sh CLI](https://docs.platform.sh/administration/cli.html)

## Setup

1. Generate a repo from the template starting point at https://github.com/platformsh-examples/django
1. Clone the repo locally
1. `platform project:list`
1. `platform project:set-remote PROJECT_ID`
1. Create a GitHub API token
1. [Setup the integration using the token](https://docs.platform.sh/integrations/source/github.html)
1. View the failed build in console. 

## Platformify 

1. `cat steps/routes.yaml .platform`
1. `cat steps/services.yaml .platform`
1. `cat steps/app.yaml .platform.app.yaml`
1. `git add . && git commit -m "Platformify Django"`
1. `git push origin main`
1. View the production build
1. View reused build/build+deploy steps
1. `platform ssh`
1. `python manage.py generate_fake_data`

## Upgrade to 3.10

1. Create a branch on GitHub to view data inheritance called `test`
1. `git checkout -b bumppy`
1. s/`type: python:3.9`/`type: python: 3.10`
1. `git add . && git commit -m "Upgrade to Python 3.10"`
1. `git push origin bumpy`
1. Open a pull request to activate
1. Merge
1. `git merge bumppy`

## Sanitizing data

1. `git checkout main`
1. `git checkout -b sanitize`
1. `platform ssh -e main 'echo $PLATFORM_ENVIRONMENT_TYPE'`
1. `platform ssh -e test 'echo $PLATFORM_ENVIRONMENT_TYPE'`
1. `platform ssh`
1. `echo $PLATFORM_RELATIONSHIPS`
1. `echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq`
1. `DB_USER=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r '.database[0].username')`
1. Exit the session
1. `cp steps/sanitize.sh .`
1. `chmod +x sanitize.sh`
1. `git add . && git commit -m "Sanitize non-production environments"`
1. `git push origin sanitize`
1. Open a pull request to activate
1. View the now sanitized data
1. Merge
