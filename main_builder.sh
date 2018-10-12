mkdir lambda_package
pip-3.6 install synapseclient -t lambda_package
cp main.py .synapseConfig lambda_package
cd lambda_package
zip -r ../lambda_package.zip .
cd ..
aws lambda update-function-code --function-name test_single_thread --zip-file fileb://lambda_package.zip
rm -r lambda_package.zip lambda_package/
