#!/usr/bin/env bash

if [ "$PLATFORM_ENVIRONMENT_TYPE" != production ]; then

    # Pull credentials from PLATFORM_RELATIONSHIPS environment variable.
    DB_USER=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r '.database[0].username')
    DB_HOST=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r '.database[0].host')
    DB_PORT=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r '.database[0].port')
    DB_PASS=$(echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq -r '.database[0].password')

    # Sanitize data
    PGPASSWORD=$DB_PASS psql -c "UPDATE bigfoot_user SET username=substring(md5(username||'$PLATFORM_PROJECT_ENTROPY') for 8);" -U $DB_USER -h $DB_HOST -p $DB_PORT
    PGPASSWORD=$DB_PASS psql -c "UPDATE bigfoot_user SET email=substring(md5(email||'$PLATFORM_PROJECT_ENTROPY') for 8);" -U $DB_USER -h $DB_HOST -p $DB_PORT

fi   
