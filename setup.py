from distutils.core import setup
setup(
  name = 'famous-quotes',
  packages = ['famous-quotes'],
  version = '0.2.7',
  license='MIT',
  description = "With the assistance of this programme, you can not only display a random quote of a celebrity you admire, but you can also add your own famous quotes. After you added it, is's automatically saved. Then, you can call the programme and you'll have a random quote displayed to you.",   # Give a short description about your library
  author = 'moonwake769',
  #author_email = '',
  url = 'https://github.com/moonwake769/famous-quotes',
  download_url = 'https://github.com/moonwake769/famous-quotes/archive/refs/tags/v0.2.7-alpha.tar.gz',
  keywords = ['quotes', 'python', 'cli', 'famous people'],   # Keywords that define your package best
  package_data = {"famous-quotes" : ["*"]},
  install_requires=[],
  include_package_data = True,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
