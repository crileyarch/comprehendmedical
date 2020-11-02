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

comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
text = 'SEATTLE—(BUSINESS WIRE) October 29, 2020—Amazon.com, Inc. (NASDAQ: AMZN) today announced financial results for its third quarter ended September 30, 2020.\
     Operating cash flow increased 56% to $55.3 billion for the trailing twelve months, compared with $35.3 billion for the trailing twelve months ended September 30, 2019.\
     Free cash flow increased to $29.5 billion for the trailing twelve months, compared with $23.5 billion for the trailing twelve months ended September 30, 2019.'

print('Calling DetectEntitiesV2')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en')))
print('End of DetectEntities\n')

#SEATTLE—(BUSINESS WIRE) October 29, 2020—Amazon.com, Inc. (NASDAQ: AMZN) today announced financial
#results for its third quarter ended September 30, 2020.
#• Operating cash flow increased 56% to $55.3 billion for the trailing twelve months, compared with $35.3 billion for
#the trailing twelve months ended September 30, 2019.
#• Free cash flow increased to $29.5 billion for the trailing twelve months, compared with $23.5 billion for the trailing
#twelve months ended September 30, 2019.
#• Free cash flow less principal repayments of finance leases and financing obligations increased to $18.4 billion for
#the trailing twelve months, compared with $14.6 billion for the trailing twelve months ended September 30, 2019.
#• Free cash flow less equipment finance leases and principal repayments of all other finance leases and financing
#obligations increased to $17.9 billion for the trailing twelve months, compared with $10.5 billion for the trailing
#twelve months ended September 30, 2019.
#• Common shares outstanding plus shares underlying stock-based awards totaled 518 million on September 30,
#2020, compared with 511 million one year ago.
#• Net sales increased 37% to $96.1 billion in the third quarter, compared with $70.0 billion in third quarter 2019.
#Excluding the $691 million favorable impact from year-over-year changes in foreign exchange rates throughout the
#quarter, net sales increased 36% compared with third quarter 2019.
#• Operating income increased to $6.2 billion in the third quarter, compared with operating income of $3.2 billion in
#third quarter 2019.
#• Net income increased to $6.3 billion in the third quarter, or $12.37 per diluted share, compared with net income of
#$2.1 billion, or $4.23 per diluted share, in third quarter 2019. 