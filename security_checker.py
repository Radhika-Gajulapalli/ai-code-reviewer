def check_security(code):
    warnings = []

    if "eval(" in code:
        warnings.append("Use of eval() detected")

    if "exec(" in code:
        warnings.append("Use of exec() detected")

    if "password =" in code:
        warnings.append("Hardcoded password detected")

    return warnings