### Serverless notes
- API gateway needs lambda to have this format in the response to not throw malformed exception:
```
    {
        'statusCode': 200,
        'headers': {
        },
        'body': json.dumps(response_list),
        'isBase64Encoded': 'false'
    }
```

### Lambda
- needs to deploy before testing
- throttle request set to 1 for singleton

### Api gateway
stages - relative path, needs to deploy first before it goes live
- throttle request set to 1 for singleton
