def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('gifti_c', parent_package, top_path)

    config.add_data_dir('linux2')
    config.add_data_files('linux2/libgifti.so')
    config.add_data_files('linux2/libgifti-1.0.0.so')
    config.add_data_files('linux2/libgifti64.so')
    config.add_data_files('linux2/libgifti64-dyn.so')
    config.add_data_dir('win32')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())