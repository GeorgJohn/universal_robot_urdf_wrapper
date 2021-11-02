import os
import sys
import shutil
import argparse

from config import config

import utils


def main():
    """ Main function to be run. """

    # parse input arguments
    parser = argparse.ArgumentParser(description='Convert the universal robot xacro description files to urdf files.')
    parser.add_argument('-p', '--path',
                        type=str,
                        help='Path where the new description files were saved.',
                        default='../UniversalRobotModelDescription/')
    args = parser.parse_args()

    # build up new directory structure
    if os.path.exists(args.path):
        print(f'Directory {args.path} already exist.')
        print(f'Would you like to overwrite the existing directory? \n [Y] / N')
        choice = input()
        choice = choice.upper()
        if choice == 'N':
            sys.exit(f'Finish process. Nothing is happened.')
        else:
            # remove full directory with all files
            shutil.rmtree(args.path)

    # create directory structure
    for dir_ in config.dir_struct_urx + config.dir_struct_urx_e:
        os.makedirs(os.path.join(args.path, dir_))

    # copy meshes to the new data directory
    shutil.copytree('../universal_robot/ur_description/meshes', os.path.join(args.path, 'ur_description/meshes'))
    shutil.copytree('../universal_robot/ur_e_description/meshes', os.path.join(args.path, 'ur_e_description/meshes'))

    # convert urx robots
    x_files = os.listdir(config.xacro_path_urx)
    for f in x_files:
        if config.wrapper_key in f:
            ur_type = f[:3]
            src_path = os.path.join(config.xacro_path_urx, f)
            des_path = ''
            for p in config.dir_struct_urx:
                if ur_type in p:
                    des_path = os.path.join(args.path, p)
            if len(des_path) == 0:
                sys.exit('EXIT. Process finished with error. Models might be incomplete!')
            else:
                output = f.replace('.xacro', '')
                out_path = os.path.join(des_path, output)
                os.system(config.xacro_cmd + src_path + ' > ' + out_path)
                utils.replace_txt(out_path, 'ur_description', '..')

    # convert urx_e robots
    x_files = os.listdir(config.xacro_path_urx_e)
    for f in x_files:
        if config.wrapper_key in f:
            ur_type = f[:3]
            src_path = os.path.join(config.xacro_path_urx_e, f)
            des_path = ''
            for p in config.dir_struct_urx_e:
                if ur_type in p:
                    des_path = os.path.join(args.path, p)
            if len(des_path) == 0:
                sys.exit('EXIT. Process finished with error. Models might be incomplete!')
            else:
                output = f.replace('.xacro', '')
                out_path = os.path.join(des_path, output)
                os.system(config.xacro_cmd + src_path + ' > ' + out_path)
                utils.replace_txt(out_path, 'ur_e_description', '..')


if __name__ == '__main__':
    main()
