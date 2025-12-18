import hou, os

def upversion_auto(filepath):
    directory, filename = os.path.split(filepath)
    base, ext = os.path.splitext(filename)
    final_path = "" 

    tag = "_v"
    idx = filename.rfind(tag)

    # If no "_v" found create _v000
    if idx == -1:
        # If filename ends with "_", remove it to avoid "__v000"
        if base.endswith("_"):
            base = base[:-1]

        version_number = 0
        padding = 3

        # Find first available version (_v000, _v001, _v002...)
        while True:
            new_filename = f"{base}{tag}{str(version_number).zfill(padding)}{ext}"
            new_path = os.path.join(directory, new_filename)
            if not os.path.exists(new_path):
                final_path = new_path
                break
            version_number += 1

    else:
        # If "_v" exists, need to check numbers
        version_start = idx + len(tag)

        # Extract digits after "_v"
        version_str = ""
        for c in filename[version_start:]:
            if c.isdigit():
                version_str += c
            else:
                break

        # If "_v" exists but no digits after, treat as no version
        if version_str == "":
            base = filename[:idx]
            if base.endswith("_"):
                base = base[:-1]

            version_number = 0
            padding = 3

            while True:
                new_filename = f"{base}{tag}{str(version_number).zfill(padding)}{ext}"
                new_path = os.path.join(directory, new_filename)
                if not os.path.exists(new_path):
                    final_path = new_path
                    break
                version_number += 1

        # If digits exist, normalize padding + auto-increment
        else:
            original_padding = len(version_str)
            if original_padding < 3:
                version_str = version_str.zfill(3)
                padding = 3
            else:
                padding = original_padding

            version_number = int(version_str)

            # Find next available version (no overwrite)
            while True:
                version_str_padded = str(version_number).zfill(padding)
                new_filename = (
                    filename[:version_start] +
                    version_str_padded +
                    filename[version_start + original_padding:]
                )
                new_path = os.path.join(directory, new_filename)
                if not os.path.exists(new_path):
                    final_path = new_path
                    break
                version_number += 1

    # Save the .hip file
    if final_path:
        try:
            hou.hipFile.save(final_path)
        except Exception as e:
            hou.ui.displayMessage(f"Error while saving:\n{e}")