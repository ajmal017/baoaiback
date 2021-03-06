import os
from flask import current_app
import traceback

def file_name(file_dir):
    '''All subdirectories under the directory  #目录下所有的子目录

    Args:
        file_dir (str) : 目录绝对路径

    Returns:
        str : modules dirs # 模块目录

    '''
    modules_dirs = []
    for root, dirs, files in os.walk(file_dir):        
        dirs.remove('__pycache__')
        modules_dirs = dirs
        break
        # print('root_dir:', root)  # 当前目录路径
        # print('sub_dirs:', dirs)  # 当前路径下所有子目录
        # print('files:', files)  # 当前路径下所有非目录子文件
    return modules_dirs


def init_app(app, **kwargs):
    '''init app  # 初始化应用

    1. import_module动态导入所有模块
    2. 执行导入模块的init_app方法

    Args:
        app (obj) : flask app 

    Returns:
        void : void

    '''
    basedir = os.path.abspath(os.path.dirname(__file__))
    modules_dirs = file_name(basedir)
    from importlib import import_module
    # for module_name in app.config['ENABLED_MODULES']:   
    for module_name in modules_dirs:
        # import_module('.%s' % module_name, package=__name__).init_app(app, **kwargs)
        try:
            import_module('.%s' % module_name, package=__name__).init_app(app, **kwargs)
        except Exception as e:
            print('%s module exception, traceback:\n%s' % (module_name, traceback.format_exc()))

