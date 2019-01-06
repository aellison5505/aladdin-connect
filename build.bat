cp lambda_func.py ./package
cp lamda_bridge.py ./package
aws s3 sync ./package s3://lambda-aladdin-con --delete
aws codebuild start-build --project-name agc-backend --region us-east-1



