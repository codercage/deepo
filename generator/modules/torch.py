# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .tools import Tools


@dependency(Tools)
@source('git')
class Torch(Module):

    def build(self):
        return r'''
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
                sudo \
                && \

            $GIT_CLONE https://github.com/torch/distro.git ~/torch --recursive && \
            cd ~/torch && \
            sed -i.bak 's/python-software-properties/software-properties-common/g' install-deps && \
            bash install-deps && \
            ./install.sh && \
        '''
