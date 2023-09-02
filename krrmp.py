#!/usr/bin/env python3

import json
import sys

help_text = '''
krrmp - AWS session impersonation tool.
usage: krrmp [ -f <file_name> | -i ]
-f file_name : File name recorded session data as JSON.
               alias: --file, f, file
-i : Paste session data as JSON and push enter.
     alias: --input, i, input
'''

def main():
    try:
        subcmd = sys.argv[1]
    except IndexError:
        print(help_text)
        sys.exit(1)

    data = ''
    if subcmd in ['-h', '--help', 'h', 'help']:
        print(help_text)
        sys.exit(0)
    elif subcmd in ['-f', '--file', 'f', 'file']:
        data = json.loads(open(sys.argv[2]).read())
    elif subcmd in ['-i', '--input', 'i', 'input']:
        print('[*]Please input session data as JSON.')
        print('[*]If it is finished, send a blank line.')
        while True:
            buf = input()
            if buf:
                data += buf
            else:
                break
        data = json.loads(data)
    else:
        print('[x]Unexpected subcommand. Bye.')
        sys.exit(100)

    access_key    = data['AccessKeyId']
    secret_key    = data['SecretAccessKey']
    session_token = data['Token']

    print('# for "aws configure", set_keys in pacu, etc')
    print(access_key)
    print(secret_key)
    print(session_token)
    print('')

    print('# for environments')
    print(f'export AWS_ACCESS_KEY_ID={access_key}')
    print(f'export AWS_SECRET_ACCESS_KEY={secret_key}')
    print(f'export AWS_SESSION_TOKEN={session_token}')
    print('')

    print('# for ~/.aws/credential')
    print(f'aws_access_key_id={access_key}')
    print(f'aws_secret_access_key={secret_key}')
    print(f'aws_session_token={session_token}')
    print('')

    print('# for aws_enum_services.py')
    print('# cf: https://github.com/NotSoSecure/cloud-service-enum/tree/master/aws_service_enum')
    print('aws_service_enum.py\\')
    print(f'  --access-key={access_key}\\')
    print(f'  --secret-key={secret_key}\\')
    print(f'  --session-token={session_token}')


if __name__ == '__main__':
    main()

