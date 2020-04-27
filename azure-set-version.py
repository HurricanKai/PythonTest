from version import get_version

if __name__ == "__main__":
    print("##vso[build.updatebuildnumber]" + get_version())
