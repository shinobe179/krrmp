# krrmp

Tool for AWS session impersonation assistance.

## How to use

1. Get AWS session data.
2. Save it in a file or clipboard.
3. Pass it to krrmp.

Then krrmp outputs session data as some formats: 

- simple enumerations(e.g. for `aws configure`)
- `export` command
- `~/.aws/credential`
- aws_enum_services.py
  - cf: https://github.com/NotSoSecure/cloud-service-enum/tree/master/aws_service_enum

from file

```
$ ./krrmp.py f FILE_NAME
```

from clipboard

```
$ ./krrmp.py i
[*]Please input session data as JSON.
[*]If it is finished, send a blank line.
...
```

