#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'voicerss_tts_plug = ' \
                     'jarbas_tts_plugin_voicerss:VoiceRSSTTSPlugin'
setup(
    name='jarbas-tts-plugin-voicerss',
    version='0.1',
    description='A voiceRSS tts plugin for mycroft',
    url='https://github.com/JarbasLingua/jarbas-tts-plugin-voicerss',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['jarbas_tts_plugin_voicerss'],
    install_requires=["requests"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
