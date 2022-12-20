import boto3


class SESService:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            aws_access_key_id='AKIA57WCLYEK2YRS67RD',
            aws_secret_access_key='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',
            region_name='eu-central-1')

    def send_email(self, email, username):
        response = self.client.send_email(
            Source='csgo.skins.info1@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': f'Welcome {username}!',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': f'Hi {username},\n'
                                f'thank you very much for signing up for our News!\n'
                                f'SOME GREAT STUFF COMMING SOON... \n\n'
                                f'STAY TUNED!\n\n'
                                f'Best Regards\n'
                                f'Your CSGO-SKINS Team',
                        'Charset': 'UTF-8'
                    }
                }
            },
        )
