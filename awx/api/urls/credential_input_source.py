# Copyright (c) 2017 Ansible, Inc.
# All Rights Reserved.

from django.conf.urls import url

from awx.api.views import (
    CredentialInputSourceList,
)


urls = [
    url(r'^$', CredentialInputSourceList.as_view(), name='credential_input_source_list'),
]

__all__ = ['urls']
