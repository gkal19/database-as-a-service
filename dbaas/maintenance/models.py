# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
import simple_audit
from django.db import models
from django.utils.translation import ugettext_lazy as _
from physical.models import Host
from util.models import BaseModel


LOG = logging.getLogger(__name__)


class Maintenance(BaseModel):
    description = models.TextField(verbose_name=_("Description"),
        null=False, blank=False)
    scheduled_for = models.DateTimeField(verbose_name=_("Schedule for"),)
    main_script = models.TextField(verbose_name=_("Main Script"),
        null=False, blank=False)
    rollback_script = models.TextField(verbose_name=_("Rollback Script"),
        null=True, blank=True)
    check_script = models.TextField(verbose_name=_("Check Script"),
        null=True, blank=True)
    host_query = models.TextField(verbose_name=_("Query Hosts"),
        null=False, blank=False)



class HostMaintenance(BaseModel):
    ERROR = 0
    SUCCESS = 1
    RUNNING = 2
    ROLLBACK = 3
    WAITING = 4

    MAINTENANCE_STATUS = (
        (ERROR, 'Error'),
        (SUCCESS, 'Success'),
        (RUNNING, 'Running'),
        (ROLLBACK, 'Rollback'),
        (WAITING, 'Waiting'),
    )

    started_at = models.DateTimeField(verbose_name=_("Started at"),)
    finished_at = models.DateTimeField(verbose_name=_("Finished at"),)
    main_log = models.TextField(verbose_name=_("Main Script"),
        null=False, blank=False)
    rollback_log = models.TextField(verbose_name=_("Rollback Script"),
        null=True, blank=True)
    check_log = models.TextField(verbose_name=_("Check Script"),
        null=True, blank=True)
    status = models.IntegerField(choices=MAINTENANCE_STATUS, default=WAITING)
    host = models.ForeignKey(Host, related_name="host_maintenance",)
    maintenance = models.ForeignKey(Maintenance, related_name="maintenance",)


simple_audit.register(Maintenance)
simple_audit.register(HostMaintenance)