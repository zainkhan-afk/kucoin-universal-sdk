# Contributing to kucoin-universal-sdk

Thank you for contributing to **kucoin-universal-sdk**! We welcome bug reports, feature suggestions, and code contributions to improve this SDK.

## Reporting Issues

- Clearly describe the problem with steps to reproduce.
- Include logs or screenshots if applicable.

Submit issues here: [Issue Tracker](https://github.com/Kucoin/kucoin-universal-sdk/issues).

## Suggesting Features

- Explain the feature and its use case.
- Provide relevant examples or references.

Open a feature request here: [Feature Requests](https://github.com/Kucoin/kucoin-universal-sdk/issues).

## Steps to Contribute:
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/your-feature`).  
3. Commit your changes (`git commit -m 'Add your feature'`).  
4. Push the branch (`git push origin feature/your-feature`).  
5. Open a pull request.  

## Commit Message Guidelines

We follow the **Conventional Commits** format for commit messages to maintain a clean and structured history:

```
<type>(<scope>): <subject>
```

### Common Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no functional changes)
- `refactor`: Code restructuring without changing behavior
- `test`: Adding or updating tests
- `chore`: Miscellaneous tasks (e.g., build or tooling changes)

**Example**:

```
feat(api): add support for custom headers

Added the ability to set custom HTTP headers for API requests. Closes #123.
```

## **Version Updates**

When making changes to the version of the SDK, ensure the following files are updated consistently:

1. **VERSION File**
   - Update the version string to reflect the new version (e.g., `1.0.1` or `1.0.0-alpha`).
   
2. **Python's `setup.py`**
   - Modify the `version` field in `setup.py` to match the updated version:
     ```python
     version="1.0.1",
     ```

3. **README File**
   - Update any references to the version number in installation instructions or examples, such as:
     ```bash
     pip install kucoin-universal-sdk==1.0.1
     ```
     
4. **CHANGELOG File**
   - Add release notes to the CHANGELOG

Ensure all version updates are consistent across these files before committing changes.
