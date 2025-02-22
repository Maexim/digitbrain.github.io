import pandas, json, ast, sys

# Add more substructures here, with their parent. Case-sensitive
STRUCTURES = {
    "Microservice": "",
    "Deployment": "DMA Tuple",
    "DataAssetsMapping": "DMA Tuple",
}


def is_not_empty(value):
    return all([value, value == value])


def to_list_or_dict(value):
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value if is_not_empty(value) else None


def get_subkey_at_index(column, row):
    try:
        subkey = column[row]
    except KeyError:
        subkey = None
    return subkey if is_not_empty(subkey) else None


def is_type(value, *args):
    checks = []
    for val_type in args:
        checks.append(val_type in value.lower())
    return any(checks)


def is_optional_and_empty(value, required):
    return not value and "mandatory" not in required.lower()


def validate_sheet(sheet):
    if not all(
        key in sheet for key in ("Key", "Subkey", "Values", "Type", "Condition")
    ):
        raise ValueError


def handle_lists(sheet_name, the_json):
    for name, parent in STRUCTURES.items():

        if not sheet_name.startswith(name):
            continue

        # If the substructure has a parent (i.e anything other than a MS)
        if parent:
            the_json.setdefault(parent, {}).setdefault(name, []).append({})
            return the_json[parent][name][len(the_json[parent][name]) - 1]

        # Microservices
        else:
            the_json.setdefault(name, []).append({})
            return the_json[name][len(the_json[name]) - 1]


def to_json(file_name):
    workbook = pandas.read_excel(file_name, sheet_name=None)

    my_dict = {}

    for sheet_name in workbook:
        # Load each sheet
        sheet = pandas.read_excel(
            file_name, sheet_name=sheet_name, skiprows=[0], usecols="B,C,D,G,H"
        )
        try:
            validate_sheet(sheet)
        except ValueError:
            print(f"WARNING: Invalid sheet: {sheet_name}")
            continue

        # Most assets are dictionaries
        if not sheet_name.startswith(tuple(STRUCTURES.keys())):
            sheet_key = my_dict.setdefault(sheet_name, {})

        # MS is a list, as are all substructures
        else:
            try:
                sheet_key = handle_lists(sheet_name, my_dict)
            except AttributeError:
                print(
                    f"WARNING: Skipping {sheet_name} because value filled in parent sheet"
                )
                continue

        # Parent key for nested subkeys
        parent_key = ""

        # Iterate over rows in required columns
        for i, (key, subkey, value, field_type, required) in enumerate(
            zip(
                sheet["Key"],
                sheet["Subkey"],
                sheet["Values"],
                sheet["Type"],
                sheet["Condition"],
            )
        ):

            # skip row if type cell is empty (assume rest of row is too)
            if isinstance(field_type, float):
                continue

            # Eval / clean value
            value = to_list_or_dict(value)

            # Clean/re-assign fields
            subkey = subkey if is_not_empty(subkey) else None
            key = key if is_not_empty(key) and not subkey else parent_key
            required = required if is_not_empty(required) else ""

            # Get the next subkey along
            next_subkey = get_subkey_at_index(sheet["Subkey"], i + 1)

            # Creating objects/lists of objects
            if not subkey and next_subkey is not None:
                parent_key = key
                if is_type(field_type, "list", "array"):
                    sheet_key.setdefault(key, []).append({})
                elif is_type(field_type, "map"):
                    sheet_key.setdefault(key, {})

            # Skip optional fields without provided values
            elif is_optional_and_empty(value, required):
                continue

            # Normal behaviour - keys
            elif not subkey:
                sheet_key[key] = value

            # Nesting subkeys in objects/lists of objects
            else:
                # Objects
                try:
                    sheet_key[key].setdefault(subkey, value)

                # Lists
                except AttributeError:
                    sheet_key[key][0][subkey] = value

    return my_dict


if __name__ == "__main__":
    # Quick filename as arg
    if len(sys.argv) == 1:
        file = "metadata.xlsx"
        path = "tools/output/output.json"
    else:
        if not sys.argv[1].endswith(".xlsx"):
            print("Not a .xlsx file!")
            sys.exit(1)
        file = sys.argv[1]
        path = f"{file[:-5]}.json"

    metadata = to_json(file)

    # dump the JSON
    app_json = json.dumps(metadata, indent=4)
    with open(path, "w") as f:
        f.write(app_json)
