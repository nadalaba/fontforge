import sys
import sysconfig as sc

install_dir_full = sys.argv[1]
is_apple = len(sys.argv) > 2 and sys.argv[2] == "APPLE"

if is_apple: scheme = "posix_prefix"
# sc.get_default_scheme() exists only in Python >= 3.10.
# Previously, it was called _get_default_scheme().
elif hasattr(sc, "get_default_scheme"): scheme = sc.get_default_scheme()
else: scheme = sc._get_default_scheme()

p = sc.get_path("platlib", scheme, vars={"platbase": "."})

# "posix_local" prepends "local/", causing double "local/" if installing to
# /usr/local. Remove it unless installing directly to platbase (e.g., /usr).
if (
    scheme == "posix_local" and
    install_dir_full != sc.get_config_var("platbase") and
    p.startswith("local/")
):
    p = p[6:]

print(p)
