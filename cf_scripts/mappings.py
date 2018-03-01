#!/usr/bin/python
# -*- coding: utf-8 -*-


from troposphere import constants

logicalName = 'logicalName'
mapping = 'mapping'

PV64 = 'PV64'
HVM64 = 'HVM64'
HVMG2 = 'HVMG2' # GPU Instance

PV64_MAP =  {'Arch': PV64}
HVM64_MAP = {'Arch': HVM64}
HVMG2_MAP = {'Arch': HVMG2} # GPU Instance

AWSInstanceType2Arch = {
    logicalName :'AWSInstanceType2Arch',
    mapping : {
        't1.micro':  PV64_MAP,

        't2.micro':  HVM64_MAP,
        't2.small':  HVM64_MAP,
        't2.medium': HVM64_MAP,
    }}


centos_7_AWSRegionArch2AMI = {
    logicalName: 'centos7AWSRegionArch2AMI',
    mapping: {
        constants.US_EAST_1: {HVM64: "ami-96a818fe"},
        constants.US_WEST_1: {HVM64: "ami-6bcfc42e"},
        constants.US_WEST_2: {HVM64: "ami-c7d092f7"}

    }}


centos_65_AWSRegionArch2AMI = {
    logicalName: 'centos65AWSRegionArch2AMI',
    mapping : {
        constants.US_EAST_1: {HVM64: 'ami-c2a818aa'},    # market place image
        constants.US_WEST_1: {HVM64: 'ami-57cfc412'},    # market place image
        constants.US_WEST_2: {HVM64: 'ami-81d092b1'}     # market place image
    }}


ubuntu_14_AWSRegionArch2AMI = {
    logicalName: 'ubuntu14AWSRegionArch2AMI',
    mapping : {
        constants.US_EAST_1: {HVM64: 'ami-d05e75b8'},
        constants.US_WEST_1: {HVM64: 'ami-df6a8b9b'},
        constants.US_WEST_2: {HVM64: 'ami-5189a661'},
        constants.AP_NORTHEAST_1: {HVM64: 'ami-936d9d93'},
        constants.AP_SOUTHEAST_1: {HVM64: 'ami-96f1c1c4'},
        constants.AP_SOUTHEAST_2: {HVM64: 'ami-69631053'},
        constants.EU_CENTRAL_1: {HVM64: 'ami-accff2b1'},
        constants.EU_WEST_1: {HVM64:'ami-47a23a30' },
        constants.SA_EAST_1: {HVM64: 'ami-4d883350'}
    }}


ubuntu_12_AWSRegionArch2AMI = {
    logicalName: 'ubuntu12AWSRegionArch2AMI',
    mapping : {
        constants.US_EAST_1: {HVM64: 'ami-427a392a'},
        constants.US_WEST_1: {HVM64: 'ami-82bba3c7'},
        constants.US_WEST_2: {HVM64: 'ami-2b471c1b'}
    }}



ami_nat_instanceAWSRegionArch2AMI = {
    logicalName: 'amazonNATInstance',
    mapping :{
            constants.US_EAST_1: {HVM64: 'ami-b0210ed8'},
            constants.US_WEST_1: {HVM64: 'ami-ada746e9'},
            constants.US_WEST_2: {HVM64: 'ami-75ae8245'}
    }}

