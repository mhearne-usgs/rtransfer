from distutils.core import setup

setup(name='rtransfer',
      version='0.1dev',
      description='Retrieve/send files from remote systems with service accounts',
      author='Mike Hearne',
      author_email='mhearne@usgs.gov',
      url='',
      scripts = ['rget','rput','rcfg'],
)
