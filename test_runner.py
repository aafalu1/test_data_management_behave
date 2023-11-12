import subprocess


def run_pytest_with_html_report(tag):
    # Construct the pytest command
    command = f"behave -f html-pretty -o behave-report.html --tags={tag}"

    # Execute the pytest command
    subprocess.run(command, shell=True)


# Example usage: Call the function to execute the pytest command with the @smoketest tag
run_pytest_with_html_report("@input")