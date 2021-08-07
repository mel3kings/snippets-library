import boto3, json

dynamodb = boto3.resource('dynamodb')
retroTable = dynamodb.Table('retro');


def lambda_handler(event, context):
    print("Event to request by Lambda function to get all from dynamo..v2")
    try:
        print("scanning..")
        response = retroTable.scan()
        response_list = []
        for item in response['Items']:
            data = {
                'date_entry': item['date_entry'],
                'workout': item['workout'],
                'adventure': item['adventure'],
                'family': item['family'],
                'goal': item['goal'],
                'hobby': item['hobby'],
                'money': item['money']
            }
            response_list.append(data)
        print(response_list)
    except Exception as e:
        print(e)
        print("error getting from dynamo db".format(e))
    return {
        'statusCode': 200,
        'headers': {
        },
        'body': json.dumps(response_list),
        'isBase64Encoded': 'false'
    }
