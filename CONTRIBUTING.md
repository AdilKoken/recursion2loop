# Contributing guidelines

## Pull Request Checklist

Before sending your pull requests, make sure you do the following:

- Read the [contributing guidelines](CONTRIBUTING.md)
- Read the [Code of Conduct](CODE_OF_CONDUCT.md)
- Check if your changes are consistent with the [guidelines](#general-guidelines-and-philosophy-for-contribution)
- Changes are consistent with the [Coding Style](#python-coding-style)
- Run the [unit tests](#running-unit-tests)

## How to become a contributor and submit your own code

### Typical Pull Request Workflow

**1. New PR**

- As a contributor, you submit a New PR on GitHub
- We inspect every incoming PR and add certain labels to the PR
- At this stage we check if the PR is valid and meets quality requirements
- We check if the PR has sufficient description, if applicable unit tests are added, and if it is a reasonable contribution

**2. Valid?**

- If the PR passes all the quality checks then we go ahead and assign a reviewer
- If the PR didn't meet the validation criteria, we request additional changes

**3. Review**

- For a valid PR, a reviewer checks if the PR looks good or needs additional changes
- If all looks good, the reviewer will approve the PR
- If changes are needed, you'll be requested to make the suggested changes
- You make the change and submit it for review again
- This cycle repeats until the PR gets approved
- Note: We may reach out if the PR is awaiting your response for more than 2 weeks

**4. Approved**

- Once approved, your changes will be merged into the main branch

### Contributing code

If you have improvements to our library, send us your pull requests! For those just getting started, GitHub has a [how-to](https://help.github.com/articles/using-pull-requests/).

If you want to contribute, start by looking through the [GitHub "issues" tab](https://github.com/yourusername/yourrepo/issues). Start with issues labeled "good first issue" if you're new.

### Contribution guidelines and standards

Before sending your pull request for review, make sure your changes are consistent with these guidelines:

#### General guidelines and philosophy for contribution

- Include unit tests when you contribute new features, as they help to a)
  prove that your code works correctly, and b) guard against future breaking
  changes to lower the maintenance cost.
- Bug fixes also generally require unit tests, because the presence of bugs
  usually indicates insufficient test coverage.

* Keep API compatibility in mind when you change code

- When you contribute a new feature to Recursion2Loop, the maintenance burden is
  (by default) transferred to the Recursion2Loop team. This means that the benefit
  of the contribution must be compared against the cost of maintaining the
  feature.

#### License

Include a license at the top of new files. Use the MIT License format since this project is MIT licensed.

#### Python coding style

Changes to the Python code should conform to [Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

Use `pylint` to check your Python changes:

```bash
pip install pylint
pylint your_file.py
```

#### Running unit tests

To run the unit tests:

1. Set up your development environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

2. Run the tests:
   ```bash
   python setup.py pytest
   ```

For a single test:

```bash
python -m pytest tests/test_specific.py -k test_name
```

Remember to run all tests before submitting a PR to ensure your changes don't break existing functionality.

---

These contributing guidelines are adapted from the [TensorFlow Contributing Guidelines](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md)
