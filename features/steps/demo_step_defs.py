
from behave import *

@given(u'we have behave installed')
def test_example1(context):
    context.driver.get("https://www.google.com")


@when(u'we implement a test')
def test_example_2(context):
    context.title= context.driver.title
    assert context.title == 'Yahoo'


@step(u'behave will test it for us!')
def test_example_3(context):
    print(f"STEP: Then behave will test it for us!{context.title}")