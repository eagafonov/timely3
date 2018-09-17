import logging

# log = logging.getLogger(__name__)

log_report = logging.getLogger('timely3.report')


def log_reporter(journal):
    for j in journal:
        scopes, duraion = j
        log_report.info("[%s] %s", ']['.join(scopes), duraion)


def report():
    return dict(message="Report is not implemented")
