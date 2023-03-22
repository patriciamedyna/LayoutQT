import setuptools

setuptools.setup(name='LayoutQT',
                 version='0.1.0',
                 description='Document aesthetics and text extractor',
                 long_description=open('README.md').read().strip(),
                 authors='Patricia Drumond and Fabrício Braz',
                 authors_email='patriciamedyna@gmail.com, fabricio.braz@gmail.com',
                 url='https://github.com/patriciamedyna/LayoutQT',
                 py_modules=['LayoutQT'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='document OCR visual features',
                 classifiers=['Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
                              'Intended Audience :: Developers',      # Define that your audience are developers
                             'Topic :: Text Processing',
                             'License :: OSI Approved :: MIT License',   # Again, pick a license
                 ])
