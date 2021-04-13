import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


include_wagtail = "{{cookiecutter.include_wagtail}}" == "y"


def main():
    project_path = os.getcwd()

    if not include_wagtail:
        cms_app_dir = os.path.join(
            project_path, "src", "{{cookiecutter.project_slug}}", "apps", "cms"
        )
        remove(cms_app_dir)


if __name__ == "__main__":
    main()
