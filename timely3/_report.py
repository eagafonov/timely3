import logging
import json
import sys

# from pprint import pformat

log = logging.getLogger(__name__)

log_report = logging.getLogger('timely3.report')

stat = dict()

LOG_JOURNAL = False


def log_reporter(journal):
    global stat

    for j in journal:
        scopes, duraion = j
        global LOG_JOURNAL

        duraion *= 1000

        if LOG_JOURNAL:
            log_report.info("[%s] %s", ']['.join(scopes), duraion)

        stat2update = stat

        for scope in scopes:
            stat2update = stat2update.setdefault(scope, dict())

        stat2update['_duration_total'] = stat2update.setdefault('_duration_total', 0) + duraion
        stat2update['_duration_count'] = stat2update.setdefault('_duration_count', 0) + 1

        stat2update['_duration_min'] = min(stat2update.setdefault('_duration_min', sys.float_info.max), duraion)
        stat2update['_duration_max'] = max(stat2update.setdefault('_duration_max', 0), duraion)

    log.info("[STAT]%s", json.dumps(stat, indent=2))

    # reset statistics
    stat = dict()


def report():
    return stat
