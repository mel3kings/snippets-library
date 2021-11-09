# Setting up your local sonar
### Prerequisites
1. Make sure your VM on Docker has at least 4gb of memory (Server and runner takes a lot of memory)
   1. this can be checked under docker preference > resources

## Run a sonar server:
```docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest```

- default user/pw is admin/admin

## Create token and sonar.properties
1. this is found under Account (Icon from upper right) > Security > Generate Token ( you need this in running sonar scanner)
2. Under your project that you want to scan, create `sonar-project.properties`, file name is crucial
```
# must be unique in a given SonarQube instance
sonar.projectKey=my:project

# --- optional properties ---

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0

# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.

# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```
3. Run Scanner:
Remember to update token (from step 1) and source folder as the volume. After running it will appear in the dashboard
```
docker run \
--rm \
--network=host \
-e SONAR_HOST_URL="http://127.0.0.1:9000" \
-e SONAR_LOGIN="{SONAR_SECURITY_TOKEN}" \
-v "/Users/melchor_tatlonghari/workspace/${LOCAL_DIRECTORY}:/usr/src" \
sonarsource/sonar-scanner-cli
```

4. it should appear in sonarqube dashboard after its done.

### Connectivity issues
We use --network=host to allow docker to hit sonar server via 127.0.0.1 ie simulating the host's network
```
--network:host for 127.0.0.1
```

##TLDR
```
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest

docker run \
--rm \
--network=host \
-e SONAR_HOST_URL="http://127.0.0.1:9000" \
-e SONAR_LOGIN="{SONAR_SECURITY_TOKEN}" \
-v "/Users/melchor_tatlonghari/workspace/<local_directory>:/usr/src" \
sonarsource/sonar-scanner-cli```