def format_name(full_name):
    parts = full_name.split()
    if len(parts) >= 2:
        first_initial = parts[0][0]
        # Check for suffixes
        suffixes = ['Jr', 'Jr.', 'Sr', 'Sr.', 'III', 'II', 'IV']
        if parts[-1] in suffixes:
            last_name = f"{parts[-2]} {parts[-1]}"
        else:
            last_name = parts[-1]
        return f"{first_initial}. {last_name}"
    return full_name

def sort_dict_with_prioritized_keys(d, priority_keys):
    # Start with prioritized keys first
    sorted_items = {key: d[key] for key in priority_keys if key in d}
    # Add remaining keys sorted alphabetically
    sorted_items.update({k: d[k] for k in sorted(d) if k not in priority_keys})
    return sorted_items

