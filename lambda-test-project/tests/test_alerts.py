from pages.alerts_page import AlertsPage

def test_handle_all_alerts(driver):
    alerts = AlertsPage(driver)
    alerts.handle_js_alert()
    alerts.handle_js_confirm_accept()
    alerts.handle_js_confirm_dismiss()
    alerts.handle_js_prompt("Hello This is Prakhar Tiwari!")
    driver.execute_script("lambda-status=passed")
