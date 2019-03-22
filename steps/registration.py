from behave import *


use_step_matcher('re')


@given('Page (?P<url>.*) is loaded')
def step_impl(context, url):
    context.browser.get(url)
