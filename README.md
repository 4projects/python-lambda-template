## Python Lambda

See this blog post here about usage. Currently scrapes a json feed and sends it to dynamodb.

### TO UPDATE CODE
```
zip -g App.zip *.py
aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://App.zip
```
