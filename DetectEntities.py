# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


import boto3
import json

comprehend = boto3.client(service_name='comprehendmedical', region_name='us-east-2')
text = 'Patient is a 56 years old man, name Jonathan Schwarz,  and he arrived at the emergency room complaining of a headache. He is currently taking 500mg of Acetaminophin which he took at 10:00 am this morning.'

print('Calling DetectEntitiesV2')
print(json.dumps(comprehend.detect_entities(Text=text)))
print('End of DetectEntities\n')