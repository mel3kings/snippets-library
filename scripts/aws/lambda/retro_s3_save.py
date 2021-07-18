import json, urllib, boto3, csv

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
retroTable = dynamodb.Table('retro');


def lambda_handler(event, context):
    print("Event received by Lambda function: " + json.dumps(event, indent=2))
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    localFilename = '/tmp/retro.txt'

    try:
        s3.meta.client.download_file(bucket, key, localFilename)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

    with open(localFilename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        rowCount = 0
        for row in reader:
            rowCount += 1
            entry = int(row['entry'])
            date_entry = row['date_entry']
            goal = row['goal']
            workout = row['workout']
            work = row['work']
            family = row['family']
            adventure = row['adventure']
            money = row['money']
            hobby = row['hobby']
            notes = row['notes']

            print(entry, date_entry, goal, workout, work, family, adventure, money, hobby, notes)
            try:
                retroTable.put_item(
                    Item={
                        'entry': entry,
                        'date_entry': date_entry,
                        'goal': goal,
                        'workout': workout,
                        'work': work,
                        'family': family,
                        'adventure': adventure,
                        'money': money,
                        'hobby': hobby,
                        'notes': notes
                    })

            except Exception as e:
                print(e)
                print("Unable to insert data into DynamoDB table".format(e))
        return "%d counts inserted" % rowCount
    s3.Object(bucket, key).delete()
