# ServerlessDemo

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI using PyCharm.

For detailed instructions, follow the tutorial : 
 - [Developing Django Application using AWS in PyCharm Guide](https://www.jetbrains.com/pycharm/guide/tutorials/intro-aws/)
 - [PyCharm and AWS Toolkit Webinar by Jetbrains](https://www.youtube.com/watch?v=4Uoc3aLQjNI)


The provided execution role does not have permissions to call CreateNetworkInterface on EC2 (when trying to configure a VPC for the lambda function)
    https://stackoverflow.com/questions/41177965/the-provided-execution-role-does-not-have-permissions-to-call-describenetworkint


## Build
To package the zip file for the Lambda Layer run

```
make
```

or

```
make layer-requirements.zip
```


