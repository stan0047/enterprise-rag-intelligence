def has_access(user_role, document_metadata):

    department = document_metadata.get("department")

    source_type = document_metadata.get("source_type")

    if user_role == "Admin":
        return True

    if source_type == "pdf":
        return True

    if department is None:
        return True

    if department == user_role:
        return True

    return False