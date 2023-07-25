import os
import sys
import logging
import argparse
import yaml

def read_param(config_path):
    with open(config_path) as  yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


def main(config_path, datasource):
    config= read_param(config_path)
    print(config)

if __name__=='__main__':
    args= argparse.ArgumentParser()
    default_config= os.path.join('config','param.yaml')
    args.add_argument('--config',default=default_config)
    args.add_argument("--datasource",default=None)


    parsed_arg= args.parse_args()
    main(config_path=parsed_arg.config,datasource= parsed_arg.datasource)