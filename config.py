import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://webapidbcosmo.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'bWyGFJmB7GESpyYR5pwwlCmpISQdq5fYJpeHey1oAr5PToX4LFtuIex4zWGH4ri2CJ3lgzcgNnFZACDbNPqlMA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'usercontainer'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'userItem'),
}