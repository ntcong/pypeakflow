from conftest import have_auth
import pytest


@pytest.mark.skipif(have_auth(), reason="ARBOR environment required")
def test_system_version(pf):
    output = pf.cliRun("system version")
    assert "results" in output
    assert "Version: Peakflow" in output['results']


@pytest.mark.skipif(have_auth(), reason="ARBOR environment required")
def test_alert_summary_blank(pf):
    assert "<alert_count>0" in pf.getDosAlertSummariesXML("alert_id:")


@pytest.mark.skipif(have_auth(), reason="ARBOR environment required")
def test_alert_summary_all(pf):
    assert "<alert_count>10" in pf.getDosAlertSummariesXML("")
