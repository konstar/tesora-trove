# Copyright 2015 Tesora Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from trove.extensions.common.service import DefaultRootController
from trove.extensions.mysql import models
from trove.guestagent.db import models as guest_models


class OracleRootController(DefaultRootController):

    def _find_root_user(self, context, instance_id):
        user = guest_models.OracleUser('sys')
        # TODO(mvandijk): This should be ultimately using Oracle model
        # extensions. MySQL extensions will work for now, but may lead to
        # future bugs as it makes use of the 'host' field which
        # does not exist/has different meaning in Postgres.
        return models.User.load(
            context, instance_id, user.name, user.host, root_user=True)
